#!/usr/bin/env python3
"""Build disposable Markdown navigation, or recheck one indexed source. Stdlib only."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile
from urllib.parse import unquote, urlsplit, quote


TOOL = "clear-engineering-navigation"
MARKER = f"<!-- {TOOL}: generated -->"
LIMITS = [
    "Only the entry and explicit scopes are read; links are not crawled.",
    "Directory scopes scan immediate .md/.markdown files only; hidden and linked paths are skipped.",
    "ATX/Setext headings and ordinary inline/reference links are extracted outside code fences.",
    "This is not a full CommonMark parser: nested blocks and HTML syntax need source inspection.",
    "Discovery and current title matches do not establish semantic completeness or current authority.",
    "Document opening and ancestor ranges are candidate context, not proven global scope or every dependency.",
    "Heading links use Codex absolute-file:line targets; saved links require rebuilding after source changes.",
]


def local_path(value):
    value = str(value)
    if value.startswith("\\\\?\\") and re.match(r"[A-Za-z]:\\", value[4:]):
        value = value[4:]
    if value.startswith(("\\\\", "//")) or "://" in value:
        raise ValueError("Use a local filesystem path, not a network path or URL")
    return Path(os.path.abspath(value))


def linked_path(path):
    # Do not follow symlinks or Windows junctions into undeclared material.
    for part in (path, *path.parents):
        try:
            info = part.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
            return True
    return False


def key(path, base):
    try:
        return Path(os.path.relpath(path, base)).as_posix()
    except ValueError:  # Windows sources/outputs may be on different drives.
        return path.as_posix()


def prose_lines(lines):
    """Keep line numbers; mask fenced/indented code, frontmatter and HTML comments."""
    result = []
    fence = None
    frontmatter = bool(lines and lines[0].strip() == "---")
    comment = False
    for i, line in enumerate(lines):
        if frontmatter:
            result.append("")
            if i and line.strip() in ("---", "..."):
                frontmatter = False
            continue
        if fence:
            result.append("")
            if re.fullmatch(r" {0,3}" + re.escape(fence[0]) + "{" + str(fence[1]) + r",}\s*", line):
                fence = None
            continue
        visible = ""
        while line:
            if comment:
                _, end, line = line.partition("-->")
                if not end:
                    break
                comment = False
            else:
                before, start, line = line.partition("<!--")
                visible += before
                if not start:
                    break
                comment = True
        opening = re.match(r" {0,3}(`{3,}|~{3,})(.*)$", visible)
        if opening and not (opening[1][0] == "`" and "`" in opening[2]):
            fence = (opening[1][0], len(opening[1]))
            result.append("")
            continue
        result.append("" if visible.startswith(("    ", "\t")) else visible)
    return result


def destination(text):
    """Read a Markdown destination, including balanced parentheses and angle paths."""
    text = text.lstrip()
    if text.startswith("<"):
        end = text.find(">")
        return text[1:end] if end >= 0 else None
    depth = 0
    out = []
    escaped = False
    for ch in text:
        if escaped:
            out.append(ch)
            escaped = False
        elif ch == "\\":
            escaped = True
        elif ch.isspace() or (ch == ")" and depth == 0):
            break
        else:
            depth += (ch == "(") - (ch == ")")
            out.append(ch)
    return "".join(out) if depth == 0 else None


def extract_links(prose):
    definitions = {}
    def_lines = set()
    for i, line in enumerate(prose, 1):
        match = re.match(r" {0,3}\[([^]]+)\]:\s*(.*)", line)
        if match:
            definitions.setdefault(" ".join(match[1].lower().split()), destination(match[2]))
            def_lines.add(i)
    links = []
    for i, line in enumerate(prose, 1):
        if i in def_lines:
            continue
        line = re.sub(r"(`+).*?\1", "", line)
        for match in re.finditer(r"(?<![!\\])\[([^]\n]+)\](?:\[([^]\n]*)\])?", line):
            tail = line[match.end():]
            if tail.startswith("("):
                target = destination(tail[1:])
            else:
                label = match[2] or match[1]
                target = definitions.get(" ".join(label.lower().split()))
            if target is not None:
                links.append({"line": i, "label": match[1], "destination": target})
    return links


def parse_source(path):
    # ponytail: common Markdown only; use a full parser only for demonstrated syntax misses.
    if linked_path(path):
        raise ValueError("Linked filesystem paths are outside discovery")
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    if "\0" in text:
        raise ValueError("NUL bytes: source is not readable UTF-8 Markdown")
    lines = text.splitlines()
    prose = prose_lines(lines)
    headings = []
    for i, line in enumerate(prose):
        match = re.match(r" {0,3}(#{1,6})(?:[ \t]+(.*?)|[ \t]*)$", line)
        if match:
            title = re.sub(r"[ \t]+#+[ \t]*$", "", match[2] or "").strip()
            headings.append({"level": len(match[1]), "title": title, "line": i + 1})
        elif i and re.fullmatch(r" {0,3}(=+|-+)[ \t]*", line) and prose[i - 1].strip():
            previous = prose[i - 1]
            if not re.match(r"\s*(?:#|>|[-+*] |\d+[.)] )", previous) and not (headings and headings[-1]["line"] == i):
                headings.append({"level": 1 if line.strip()[0] == "=" else 2,
                                 "title": previous.strip(), "line": i})
    preamble = {"start": 1, "end": headings[0]["line"] - 1 if headings else len(lines)}
    stack = []
    for index, heading in enumerate(headings):
        while stack and stack[-1]["level"] >= heading["level"]:
            stack.pop()
        heading["path"] = [h["title"] for h in stack] + [heading["title"]]
        heading["context"] = ([preamble] if preamble["end"] else []) + [
            {"start": h["line"], "end": h["intro_end"]} for h in stack]
        heading["intro_end"] = headings[index + 1]["line"] - 1 if index + 1 < len(headings) else len(lines)
        heading["end"] = next((h["line"] - 1 for h in headings[index + 1:]
                               if h["level"] <= heading["level"]), len(lines))
        stack.append(heading)
    opening = dict(preamble)
    if not any(line.strip() for line in prose[:preamble["end"]]):
        level = 0
        for heading in headings:
            if heading["level"] <= level:
                break
            opening["end"] = heading["intro_end"]
            body = lines[heading["line"]:heading["intro_end"]]
            if body and re.fullmatch(r" {0,3}(=+|-+)[ \t]*", body[0]):
                body = body[1:]  # Setext underline belongs to the title, not its introduction.
            if any(line.strip() for line in body):
                break  # Lists, tables and code also count; do not drift into later sections.
            level = heading["level"]
    for heading in headings:
        heading["context"] = ([opening] if opening["end"] else []) + [
            span for span in heading["context"] if span["end"] > opening["end"]]
    return {"sha256": hashlib.sha256(raw).hexdigest(), "line_count": len(lines),
            "preamble": preamble, "document_opening": opening,
            "headings": headings, "links": extract_links(prose)}


def local_target(source, href):
    if re.match(r"^[A-Za-z]:[/\\]", href):
        return local_path(href)
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    return local_path(source.parent / unquote(parsed.path))


def discover(scopes, excludes, outputs, issues):
    found = set()
    def excluded(path):
        return path in outputs or any(path == p or p in path.parents for p in excludes)
    def error(path, exc):
        issues.append({"path": str(path), "error": type(exc).__name__, "detail": str(exc)})
    for scope in scopes:
        try:
            if excluded(scope):
                raise ValueError("An explicit scope is excluded")
            if linked_path(scope):
                raise ValueError("Linked scopes are not followed")
            if scope.is_file():
                if scope.suffix.lower() not in (".md", ".markdown"):
                    raise ValueError("File scopes must be Markdown")
                found.add(scope)
            elif scope.is_dir():
                for path in sorted(scope.iterdir()):
                    if (not path.name.startswith(".") and path.suffix.lower() in (".md", ".markdown")
                            and not excluded(path) and not linked_path(path) and path.is_file()):
                        found.add(path)
            else:
                raise FileNotFoundError("Scope does not exist")
        except (OSError, ValueError) as exc:
            error(scope, exc)
    return found


def build(entry, scopes, excludes, outputs):
    # ponytail: re-read explicit scopes on demand; add a cache only if measured cost warrants it.
    issues = []
    paths = discover(scopes, excludes, outputs, issues) | {entry}
    records = []
    for path in sorted(paths, key=lambda p: key(p, entry.parent)):
        record = {"path": key(path, entry.parent)}
        try:
            record.update(parse_source(path))
        except (OSError, ValueError) as exc:
            record["error"] = {"type": type(exc).__name__, "detail": str(exc)}
            issues.append({"path": record["path"], **record["error"]})
        records.append(record)
    entry_record = next(r for r in records if r["path"] == entry.name)
    referenced = set()
    for link in entry_record.get("links", []):
        try:
            target = local_target(entry, link["destination"])
            if target:
                referenced.add(key(target, entry.parent))
        except ValueError:
            pass  # Network or malformed destinations stay visible as links, never fetched.
    for record in records:
        record["relation"] = ("entry" if record is entry_record else
                              "unclassified" if "error" in entry_record else
                              "entry-linked" if record["path"] in referenced else "discovered")
    return {"generator": TOOL, "schema": 1, "base": str(entry.parent), "entry": entry.name,
            "scopes": [key(p, entry.parent) for p in scopes],
            "excludes": [key(p, entry.parent) for p in excludes],
            "status": "partial" if issues else "ok", "limits": LIMITS,
            "entry_links_outside_index": sorted(referenced - {r["path"] for r in records}),
            "issues": issues, "files": records}


def md_text(value):
    return re.sub(r"([\\`*{}\[\]()#+.!_<>|])", r"\\\1", str(value)).replace("\n", " ")


def source_link(title, path, line):
    return f"[{md_text(title)}](<{local_path(path).as_posix()}:{line}>)"


def render(data, output):
    lines = [MARKER, "# Source navigation", "", f"Status: **{data['status']}**. Generated; sources remain authoritative.",
             f"Base: `{data['base']}`", f"Entry: `{data['entry']}`", "",
             "Scopes: " + ", ".join(f"`{p}`" for p in data["scopes"]),
             "Excludes: " + ", ".join(f"`{p}`" for p in data["excludes"]), ""]
    lines += [f"- {text}" for text in data["limits"]]
    if data["issues"]:
        lines += ["", "## Discovery / read failures", ""]
        lines += ["- " + md_text(json.dumps(issue, ensure_ascii=False)) for issue in data["issues"]]
    if data["entry_links_outside_index"]:
        lines += ["", "## Entry links outside this index (not read or checked)", ""]
        lines += ["- " + md_text(p) for p in data["entry_links_outside_index"]]
    for record in data["files"]:
        path = Path(data["base"]) / record["path"]
        relative = key(path, output.parent)
        url = path.as_uri() if Path(relative).is_absolute() else quote(relative, safe="/:")
        lines += ["", f"## [{md_text(record['path'])}]({url}) — {record['relation']}", ""]
        if "error" in record:
            lines += ["Read failed: " + md_text(record["error"]["detail"])]
            continue
        lines += [f"Source SHA-256: `{record['sha256']}`; {record['line_count']} lines."]
        if record["preamble"]["end"]:
            lines += [f"File preamble: L1–L{record['preamble']['end']}."]
        if record["document_opening"]["end"]:
            lines += [f"Document opening (candidate context): L1–L{record['document_opening']['end']}."]
        lines += [""]
        for heading in record["headings"]:
            context = ", ".join(f"L{r['start']}–L{r['end']}" for r in heading["context"]) or "none"
            lines += ["  " * (len(heading["path"]) - 1) +
                      f"- {source_link(heading['title'], path, heading['line'])} — L{heading['line']}–L{heading['end']}; context: {context}"]
        if record["links"]:
            lines += ["", "Source links (not followed):", ""]
            lines += [f"- L{link['line']}: {md_text(link['label'])} → {md_text(link['destination'])}"
                      for link in record["links"]]
    return "\n".join(lines) + "\n"


def check_output(path, kind):
    if linked_path(path):
        raise ValueError("Output may not use a linked filesystem path")
    if path.exists():
        text = path.read_text(encoding="utf-8")
        if kind == "json":
            data = json.loads(text)
            generated = isinstance(data, dict) and data.get("generator") == TOOL
        else:
            generated = text.startswith(MARKER + "\n")
        if not generated:
            raise ValueError(f"Refusing to overwrite a non-generated file: {path}")


def write_changed(path, text):
    if path.exists() and path.read_bytes() == text.encode("utf-8"):
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    name = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
            name = stream.name
            stream.write(text.encode("utf-8"))
        os.replace(name, path)
    finally:
        if name and os.path.exists(name):
            os.unlink(name)


def locate(index, filename, headings):
    data = json.loads(index.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("generator") != TOOL or data.get("schema") != 1:
        raise ValueError("Unsupported navigation index")
    records = [r for r in data["files"] if r["path"] == filename]
    if len(records) != 1:
        return {"status": "not-indexed", "file": filename, "hint": "Rebuild the explicit discovery scopes."}, 1
    path = local_path(Path(data["base"]) / filename)
    try:
        current = parse_source(path)
    except (OSError, ValueError) as exc:
        return {"status": "unavailable", "file": str(path), "error": str(exc)}, 1
    changed = current["sha256"] != records[0].get("sha256")
    result = {"status": "changed" if changed else "unchanged", "file": str(path),
              "sha256": current["sha256"], "line_count": current["line_count"],
              "document_opening": current["document_opening"],
              "note": "Current source positions only; changes require reassessing meaning and applicability."}
    if not headings:
        result.update({"preamble": current["preamble"], "headings": current["headings"], "links": current["links"]})
        return result, 0
    matches = [h for h in current["headings"] if h["path"][-len(headings):] == headings]
    if len(matches) != 1:
        result.update({"match": "missing" if not matches else "ambiguous", "candidates": matches})
        return result, 1
    selected = matches[0]
    ranges = [{"start": selected["line"], "end": selected["end"]},
              current["document_opening"], *selected["context"]]
    result.update({"match": "current-title-match", "heading": selected,
                   "links": [link for link in current["links"]
                             if any(span["start"] <= link["line"] <= span["end"] for span in ranges)]})
    return result, 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    generate = commands.add_parser("build", help="Discover explicit scopes and write JSON plus sibling Markdown")
    generate.add_argument("--entry", required=True)
    generate.add_argument("--scope", action="append", required=True, help="Directory (immediate Markdown only) or Markdown file; repeatable")
    generate.add_argument("--exclude", action="append", default=[], help="Excluded file/directory; relative to entry's parent")
    generate.add_argument("--output", required=True, help="Generated .json path; sibling .md is also written")
    find = commands.add_parser("locate", help="Reparse one source; never trust saved line numbers")
    find.add_argument("--index", required=True)
    find.add_argument("--file", required=True, help="Exact file key from the index, relative to its recorded base")
    find.add_argument("--heading", action="append", default=[], help="Exact title; repeat ancestor-to-child to disambiguate")
    args = parser.parse_args(argv)
    try:
        if args.command == "locate":
            result, code = locate(local_path(args.index), args.file, args.heading)
        else:
            entry = local_path(args.entry)
            output = local_path(args.output)
            if output.suffix.lower() != ".json":
                raise ValueError("--output must end in .json")
            markdown = output.with_suffix(".md")
            scopes = sorted({local_path(entry.parent / p) for p in args.scope})
            excludes = sorted({local_path(entry.parent / p) for p in args.exclude})
            if entry in (output, markdown) or any(p in (output, markdown) for p in scopes):
                raise ValueError("Outputs must not replace the entry or an explicit source")
            check_output(output, "json")
            check_output(markdown, "markdown")
            data = build(entry, scopes, excludes, {output, markdown})
            json_text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
            markdown_text = render(data, markdown)
            write_changed(output, json_text)
            write_changed(markdown, markdown_text)
            result = {"status": data["status"], "files": len(data["files"]),
                      "json": str(output), "markdown": str(markdown), "issues": data["issues"]}
            code = 1 if data["issues"] else 0
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return code
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
