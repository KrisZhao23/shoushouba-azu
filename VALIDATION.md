# Public draft validation record

[English](VALIDATION.md) | [简体中文](VALIDATION.zh-CN.md)

Scope: the public `0.1.3-candidate`. Maintain this record with the relevant files; published commits define the online version.

## Current revision and checks (2026-10-26)

- Added opt-in standard-library navigation in `scripts/build_navigation.py`, with one usage section in reference 03. `build` reads an entry and explicit immediate-directory/file scopes, emitting JSON and Markdown from the same extraction; `locate` rereads selected sources and reports changes, missing or ambiguous titles, and current context positions. A document-opening candidate covers introductory text under a subtitle even for later sibling sections; heading links target absolute source paths and line numbers in Codex. Sources remain untouched. Discovery does not determine current authority, and title matches do not prove historical identity. No dependency, service, model call, or mandatory refresh was added.
- `scripts/test_build_navigation.py` passed in both the public and installed locations, using isolated temporary sources: added files/chapters, changed ancestor context and positions, moved/deleted sources, duplicate titles, fenced/comment fake headings, ordinary links, read/discovery failures, source/output protection, cross-drive rendering fallback, and unchanged output bytes/modification times. Independent read-only review found two issues in cross-drive rendering and comment/fence ordering; both were corrected. Receiving-task feedback prompted regression cases for subtitle introductions and opening qualifications, sibling/list/table/code boundaries, and every generated heading's absolute file/line target (including spaces and parentheses). Public/installed Skill format, UTF-8 parity, bilingual usage, navigation links, diff formatting, and private-marker checks passed. A focused regression confirms 4 links from opening, ancestors and the selected section/descendants, excluding unrelated siblings; file-wide lookup retains all 7 links. The receiving task confirmed real-project opening-context and heading-link acceptance; the latest link filtering remains for it to check. Measured reduction in work is not established by script checks.

## Evidence that still applies

- Research attribution and license findings remain in the [source inventory](skills/clear-engineering/references/06-case-evidence.md#source-licenses). Project-owned content is MIT-licensed; third-party terms remain applicable. The video's music and sound effects are covered by the accompanying [audio notice](media/HUASHU-DESIGN-LICENSE.txt); no third-party implementation source was added.
- The existing self-check in the [single-file example](skills/clear-engineering/examples/single-file-tool.md) previously passed in an actual run. Its behavior was unchanged and was not retested. Licenses, source inventory, and publication identity were unchanged.

## Limits

These checks support file contents, format, and references, not task efficiency, automatic host loading, or cross-project effectiveness. The locally installed method now uses the same maintenance semantics; fixed-version evaluation copies remain unchanged, and no scheduled tasks were enabled. File updates do not establish that open conversations have reread them. Update this record when real use yields relevant evidence; do not accumulate a log of every editing round.
