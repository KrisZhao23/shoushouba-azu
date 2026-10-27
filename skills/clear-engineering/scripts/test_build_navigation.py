"""Run with Python; all sources and generated files live in one temporary directory."""

from contextlib import redirect_stdout, redirect_stderr
from io import StringIO
import json
from pathlib import Path
import re
import tempfile
from unittest.mock import patch

import build_navigation as nav


def invoke(*args):
    stdout, stderr = StringIO(), StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        code = nav.main(list(args))
    return code, stdout.getvalue(), stderr.getvalue()


def run():
    with tempfile.TemporaryDirectory(prefix="ce-navigation-") as folder:
        root = Path(folder)
        entry = root / "PROJECT-LEDGER.md"
        docs = root / "design"
        docs.mkdir()
        source = docs / "current.md"
        entry.write_text("# Project\nCurrent explanation.\n"
                         "[Design](design/current.md#choice) [Outside](archive/old.md)\n"
                         "[Extra][note]\n[note]: <extra note.md>\n", encoding="utf-8")
        source.write_text("\ufeff---\nkind: draft\n---\nScope: historical, not current acceptance.\n"
                          "# Design\nUnverified parent premise.\n## Choice\nFirst choice.\n"
                          "```markdown\n# Not a heading\n[Fake](fake.md)\n````\n"
                          "~~~\n## Also fake\n~~~\n"
                          "    # Indented code\n<!--\n# Comment\n```\n-->\n"
                          "## Choice\nSecond choice.\n# Other\nParent restriction.\n"
                          "## Choice\nUnique under Other.\n"
                          "[One](a(b).md) [Two](<a b.md>) [Ref][r]\n[r]: ref.md\n"
                          "Setext title\n------------\nFinal paragraph.\n", encoding="utf-8")
        (root / "extra note.md").write_text("# Extra\n", encoding="utf-8")
        (root / ".hidden.md").write_text("# Hidden\n", encoding="utf-8")
        archive = root / "archive"
        archive.mkdir()
        (archive / "old.md").write_text("# Old frozen evidence\n", encoding="utf-8")
        output = root / "navigation.json"
        args = ("build", "--entry", str(entry), "--scope", ".", "--scope", "design", "--output", str(output))
        originals = {p: p.read_bytes() for p in root.rglob("*.md")}
        code, _, error = invoke(*args)
        assert code == 0, error
        data = json.loads(output.read_text(encoding="utf-8"))
        records = {f["path"]: f for f in data["files"]}
        assert set(records) == {entry.name, "design/current.md", "extra note.md"}
        assert records["design/current.md"]["relation"] == "entry-linked"
        assert records["extra note.md"]["relation"] == "entry-linked"
        assert data["entry_links_outside_index"] == ["archive/old.md"]
        headings = records["design/current.md"]["headings"]
        assert [h["title"] for h in headings] == ["Design", "Choice", "Choice", "Other", "Choice", "Setext title"]
        assert [l["destination"] for l in records["design/current.md"]["links"]] == ["a(b).md", "a b.md", "ref.md"]
        original_lines = source.read_text(encoding="utf-8-sig").splitlines()
        for heading in headings:
            assert heading["title"] in original_lines[heading["line"] - 1]
            assert heading["end"] >= heading["line"]
        # Both renderings are disposable and unchanged runs do not rewrite them or index themselves.
        outputs = [output, output.with_suffix(".md")]
        before = [(p.read_bytes(), p.stat().st_mtime_ns) for p in outputs]
        assert invoke(*args)[0] == 0
        assert before == [(p.read_bytes(), p.stat().st_mtime_ns) for p in outputs]
        assert originals == {p: p.read_bytes() for p in originals}
        assert "Not a heading" not in outputs[1].read_text(encoding="utf-8")

        result, code = nav.locate(output, "design/current.md", ["Choice"])
        assert code == 1 and result["match"] == "ambiguous" and len(result["candidates"]) == 3
        result, code = nav.locate(output, "design/current.md", ["Other", "Choice"])
        assert code == 0 and result["status"] == "unchanged"
        context = "\n".join("\n".join(original_lines[r["start"] - 1:r["end"]])
                            for r in result["heading"]["context"])
        assert "historical" in context and "Parent restriction" in context
        # Unchanged section body cannot hide changed file/ancestor qualifications or shifted positions.
        source.write_text(source.read_text(encoding="utf-8-sig").replace("Parent restriction.",
                          "Parent now provisional.\nAdditional limitation."), encoding="utf-8")
        changed, code = nav.locate(output, "design/current.md", ["Other", "Choice"])
        assert code == 0 and changed["status"] == "changed"
        assert changed["heading"]["line"] == result["heading"]["line"] + 1
        new_lines = source.read_text(encoding="utf-8").splitlines()
        assert any("Parent now provisional." in new_lines[r["start"] - 1:r["end"]]
                   for r in changed["heading"]["context"])
        # Added files and chapters appear on a build without any hand-maintained file list.
        added = docs / "new.md"
        added.write_text("# Newly discovered\n", encoding="utf-8")
        source.write_text(source.read_text(encoding="utf-8") + "\n## Added chapter\n", encoding="utf-8")
        assert invoke(*args)[0] == 0
        data = json.loads(output.read_text(encoding="utf-8"))
        assert next(r for r in data["files"] if r["path"] == "design/new.md")["relation"] == "discovered"
        assert nav.locate(output, "design/current.md", ["Added chapter"])[1] == 0
        source.write_text(source.read_text(encoding="utf-8").replace("## Added chapter", "## Replacement"), encoding="utf-8")
        result, code = nav.locate(output, "design/current.md", ["Added chapter"])
        assert code == 1 and result["match"] == "missing" and result["status"] == "changed"
        moved = docs / "moved.md"
        source.rename(moved)
        assert nav.locate(output, "design/current.md", ["Choice"])[0]["status"] == "unavailable"
        added.unlink()
        assert invoke(*args)[0] == 0
        data = json.loads(output.read_text(encoding="utf-8"))
        assert {f["path"] for f in data["files"]} == {entry.name, "extra note.md", "design/moved.md"}
        assert "design/current.md" in data["entry_links_outside_index"]

        # Real invalid bytes, an unavailable scope, and simulated access denial must not look like an empty success.
        bad = docs / "unreadable.md"
        bad.write_bytes(b"\xff\xfe\x00")
        assert invoke(*args)[0] == 1
        data = json.loads(output.read_text(encoding="utf-8"))
        assert data["status"] == "partial" and next(r for r in data["files"] if r["path"].endswith("unreadable.md"))["error"]
        bad.unlink()
        read_bytes = Path.read_bytes
        def denied(path):
            if path == moved:
                raise PermissionError("simulated unreadable source")
            return read_bytes(path)
        with patch.object(Path, "read_bytes", denied):
            data = nav.build(entry, [docs], [], set(outputs))
            assert data["status"] == "partial" and data["issues"]
            assert nav.locate(output, "design/moved.md", ["Choice"])[1] == 1
        assert invoke(*args, "--scope", "missing-directory")[0] == 1
        # Existing authored files and the unique entry cannot be overwritten by output naming.
        assert invoke("build", "--entry", str(entry), "--scope", ".",
                      "--output", str(entry.with_suffix(".json")))[0] == 1
        authored = root / "authored.md"
        authored.write_text("# Keep this source\n", encoding="utf-8")
        assert invoke("build", "--entry", str(entry), "--scope", ".",
                      "--output", str(authored.with_suffix(".json")))[0] == 1
        assert authored.read_text(encoding="utf-8") == "# Keep this source\n"
        assert not authored.with_suffix(".json").exists()
        assert (archive / "old.md").read_bytes() == originals[archive / "old.md"]
        # The other-drive fallback is independent of whether a second physical drive is present.
        with patch.object(nav.os.path, "relpath", side_effect=ValueError("different drives")):
            assert nav.key(moved, output.parent) == moved.as_posix()
            assert moved.as_uri() in nav.render(data, output.with_suffix(".md"))
        code, stdout, stderr = invoke("locate", "--index", str(output), "--file", "design/moved.md", "--heading", "Other", "--heading", "Choice")
        assert code == 0 and json.loads(stdout)["match"] == "current-title-match", stderr
        # A subtitle's opening prose also matters to later sibling sections, not just descendants.
        opening_source = docs / "architecture notes (draft).md"
        opening_text = ("# System\n\n## Architecture subtitle\n\nVersion 1\n\nAccepted direction.\n\n"
                        "Capacity remains unverified.\n\nNo implementation is authorized.\n\n"
                        "### Reading map\n\nUse the relevant sections.\n\n## 5 Recovery\n\nRecovery design.\n")
        opening_source.write_text(opening_text, encoding="utf-8")
        assert invoke(*args)[0] == 0
        result, code = nav.locate(output, "design/architecture notes (draft).md", ["5 Recovery"])
        assert code == 0 and result["document_opening"] == {"start": 1, "end": 12}
        assert result["heading"]["line"] == 17
        assert result["heading"]["context"] == [{"start": 1, "end": 12}]
        opening_source.write_text(opening_text.replace("No implementation is authorized.",
                                  "Authorization still pending.\nNew opening qualification."), encoding="utf-8")
        result, code = nav.locate(output, "design/architecture notes (draft).md", ["5 Recovery"])
        assert code == 0 and result["status"] == "changed"
        assert result["document_opening"] == {"start": 1, "end": 13} and result["heading"]["line"] == 18
        # Rebuilding gives every heading a Codex file:line link; spaces/parentheses stay in one target.
        assert invoke(*args)[0] == 0
        markdown = output.with_suffix(".md").read_text(encoding="utf-8")
        targets = re.findall(r"- \[[^\n]+?\]\(<(.+):([0-9]+)>\)", markdown)
        generated = json.loads(output.read_text(encoding="utf-8"))
        expected = [(nav.local_path(Path(generated["base"]) / record["path"]), h["line"])
                    for record in generated["files"] for h in record.get("headings", [])]
        assert [(Path(path), int(line)) for path, line in targets] == expected
        assert (opening_source, 18) in expected
        for path, line in targets:
            assert Path(path).is_absolute() and Path(path).read_text(encoding="utf-8-sig").splitlines()[int(line) - 1].strip()
        # Empty title chains stop at a sibling; list/table/code introductions stop expansion too.
        opening_source.write_text("# Title\n\n## Empty\n\n## Sibling\nBody\n", encoding="utf-8")
        assert nav.parse_source(opening_source)["document_opening"] == {"start": 1, "end": 4}
        for body in ["- Pending validation", "| Pending | Validation |", "```\nPending validation\n```"]:
            opening_source.write_text(f"# Title\n{body}\n## Child\nLater body\n", encoding="utf-8")
            assert nav.parse_source(opening_source)["document_opening"]["end"] == 1 + len(body.splitlines())
        # Selected output retains opening/ancestor/descendant links, excluding unrelated siblings.
        opening_source.write_text("# Project\n[Opening](opening.md)\n"
                                  "## Before\n[Earlier](earlier.md)\n"
                                  "## Work\n[Parent](parent.md)\n"
                                  "### Target\n[Selected][selected]\n"
                                  "#### Detail\n[Child](child.md)\n"
                                  "### Other\n[Sibling](sibling.md)\n"
                                  "## After\n[Later](later.md)\n[selected]: selected.md\n", encoding="utf-8")
        assert invoke(*args)[0] == 0
        selected, code = nav.locate(output, "design/architecture notes (draft).md", ["Target"])
        assert code == 0
        assert [link["destination"] for link in selected["links"]] == ["opening.md", "parent.md", "selected.md", "child.md"]
        whole, code = nav.locate(output, "design/architecture notes (draft).md", [])
        assert code == 0
        assert [link["destination"] for link in whole["links"]] == ["opening.md", "earlier.md", "parent.md", "selected.md", "child.md", "sibling.md", "later.md"]
    print("PASS: discovery, current locations/context, ambiguity/failures, source protection and stable output")


if __name__ == "__main__":
    run()
