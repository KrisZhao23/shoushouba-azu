# Cases, Evidence, and Limits of Transfer

[English](06-case-evidence.md) | [简体中文](06-case-evidence.zh-CN.md)

Evidence baseline: the early v0.1.0 research draft. Candidate revision date: 2026-10-17. This revision rechecked the relevant definitions in `read-cache.c` at the pinned Git commit and the `c8ad9d0` diff. The other cases in sections 2–4 retain the v0.1.0 reading records; they are not presented as having all been reread for this revision. The official host entry points in section 5 were checked specifically; original sources for the added topics are in section 8.

Where retained historical case descriptions say "this round," they refer to the v0.1.0 research record. New checks for this candidate are explicitly called "this revision." Distinguish maintainers' reasons, source and test readings, practice reports, and inferences about transfer. No full-repository audit was performed, and no tests were run for Git, SQLite, Starlette, or users' actual projects.

The purpose is not to combine every open-source project's strengths into one architecture. Odoo, ERPNext, Temporal, Debezium, and other projects in the older report remain possible material for future topics, but their full evidence was not rechecked in this round and cannot endorse every item in this version by association. v0.1.0 mainly organized a concrete chain of Git changes and used projects of different kinds to constrain generalization. This revision corrects specific issues in that chain, such as the identification of actual consumers.

## 1. Detailed Case: A Change in Git's Shared Path Semantics and a stash Regression

### Reading anchors and the original goal

Pinned source anchor: `c8ad9d04c6a51cb5c73ebc9e42b627314eeafe2f`. This is a historical research subject, not a recommended Git version to install.

The maintainer's message for `6e773527b6` explains converting a full index by representing directories outside the sparse scope as directory entries. The conversion was limited by the modes and states supported at the time, and some commands still needed an expanded index. The source change also relaxed path validation to support directory entries with trailing separators. [G1]

There are two kinds of consumers here: index-entry construction and insertion sites that understand the special directory representation, and ordinary callers that still rely on the original meaning of shared path validation. Directory structure alone does not express this distinction.

### Actual changes and the failure record

The author of `fc5e90b` explains that `stash` previously ignored nested repositories and that the relaxation introduced a regression. This commit adds a test expected to fail. [G2]

Next, `2a1ae64` introduces internal result categories for ordinary valid paths, invalid paths, and directories with trailing separators. The commit states that no external behavior change is intended. [G3]

Finally, `c8ad9d0` restores the original meaning of public validation, accepts the special result at the relevant validation sites in entry construction and index insertion, and changes the regression test to expect success. [G4]

These three commits have a readable parent–child chain: `fc5e90b → 2a1ae64 → c8ad9d0`. Exact dates for every event were not reliably obtained from the pages, so this record does not invent them. Research-record dates differ from historical event times.

### Tracing the complete entry path to actual consumers

Static source at the pinned anchor confirms the following connections:

`stash` obtains names of untracked items and passes them to the logic that saves untracked content. That logic starts an `update-index` subprocess, passes the names through standard input, and selects a temporary index through `GIT_INDEX_FILE`. [G5]

The standard-input path in `update-index` reaches `update_one`, which obtains file status and calls the public `verify_path`. A rejected path is ignored; otherwise processing continues. Directory handling has its own branch as well. [G6]

This revision checked the pinned source and diff: public `verify_path` returns true only for `PATH_OK`; `make_cache_entry` and `add_index_entry_with_check` call `verify_path_internal` at the relevant validation sites and reject only `PATH_INVALID`, so they can accept paths classified as `PATH_DIR_WITH_SEP`. `make_transient_cache_entry` still calls public `verify_path`; it is not one of those two sites that accept the special result. [G4, G7]

This is a factual correction to v0.1.0's consumer identification. `make_transient_cache_entry` is only a comparison case for ordinary validation consumers. Its complete upstream uses were not traced in this revision, and the checks described above are not presented as the complete validation of every insertion or replacement path.

Consequently, inspecting only direct function calls from `stash`, or only the `read-cache.c` diff, misses cooperation through a subprocess, standard input, and an environment-selected index. This conclusion is an analysis of the source paths read. Not every filesystem branch of directory traversal was enumerated, and the actual error output was not reproduced by running it.

### What the tests actually support

The test added in `fc5e90b` initializes a repository inside a subdirectory, then runs `stash -u`. At the pinned anchor, `t/t3905-stash-include-untracked.sh` expects this scenario to succeed. [G2, G8]

The assertion text was read, but the test was not run. The added test mainly checks whether this command completes successfully. On its own, it does not establish the correctness of all untracked content, nested-repository data, or restoration behavior. A further local reproduction could also check retained content and index results; that is a verification recommendation, not an existing runtime result.

The original introducing commit also discusses comparisons between sparse and full representations. [G1] Those tests were not rerun in this round, and a publicly merged fix cannot be treated as validation on every platform.

### Judgment extracted for this version

A shared check becoming more permissive is not necessarily safe for existing consumers. When adding a local capability, distinguish an extension in capability from a change in public semantics. Preserving the old meaning for ordinary consumers while explicitly providing the special capability where it is understood was a suitable choice in this case.

The fix stayed in the original file; it did not require new modules or services. It does not imply that boundaries must be split into separate files, or that every shared function must remain compatible forever. Different choices may be appropriate when old consumers no longer exist, all consumers can migrate together, or the old semantics were wrong.

A project ledger for this behavior would usefully retain the two meanings of validity, their consumers, the cross-process connection, and regression evidence, rather than every call graph. Its timeline should preserve the changes in understanding: relaxation, discovery of the regression, preparation through classification, and restoration of the public meaning. Do not infer from the final implementation that all these tradeoffs were understood at the outset.

### Primary reading locations

- [G1: Introducing change 6e773527b6](https://github.com/git/git/commit/6e773527b6)
- [G2: Regression test fc5e90b](https://github.com/git/git/commit/fc5e90b)
- [G3: Internal classification 2a1ae64](https://github.com/git/git/commit/2a1ae64)
- [G4: Restoring public semantics c8ad9d0](https://github.com/git/git/commit/c8ad9d04c6a51cb5c73ebc9e42b627314eeafe2f)
- [G5: Pinned builtin/stash.c](https://raw.githubusercontent.com/git/git/c8ad9d04c6a51cb5c73ebc9e42b627314eeafe2f/builtin/stash.c), focusing on `get_untracked_files` and `save_untracked_files`.
- [G6: Pinned builtin/update-index.c](https://raw.githubusercontent.com/git/git/c8ad9d04c6a51cb5c73ebc9e42b627314eeafe2f/builtin/update-index.c), focusing on the standard-input branch, `update_one`, and `process_directory`.
- [G7: Pinned read-cache.c](https://raw.githubusercontent.com/git/git/c8ad9d04c6a51cb5c73ebc9e42b627314eeafe2f/read-cache.c), focusing on `verify_path`, `verify_path_internal`, `make_cache_entry`, and `add_index_entry_with_check`; compare `make_transient_cache_entry`, which still uses public validation.
- [G8: Pinned t3905 test](https://raw.githubusercontent.com/git/git/c8ad9d04c6a51cb5c73ebc9e42b627314eeafe2f/t/t3905-stash-include-untracked.sh).

## 2. SQLite: Expressing Overall Guarantees as Obligations with Defined Scope (Retained v0.1.0 Record)

The official architecture description separates responsibilities for compilation and execution, B-trees, the pager, and lower-level interfaces. The opening of `version-3.47.2/src/pager.c` expresses important relationships among writes, synchronization, locks, and recovery as invariants, and explicitly excludes journal modes such as WAL, MEMORY, and OFF from that set of constraints. [S1, S2]

The official testing description explains simulating crashes with a replacement VFS, then checking integrity and whether transactions complete or roll back, rather than checking only function return values. [S3] This round read the description and the source comments above; it did not execute those tests.

What this version borrows: record which responsibilities uphold important promises, their environmental assumptions, and the corresponding evidence. Do not extend a database's local guarantees to external-system effects, or transplant these layers and the scale of fault testing into every small tool.

- [S1: Official architecture](https://www.sqlite.org/arch.html)
- [S2: pager.c at a fixed tag](https://raw.githubusercontent.com/sqlite/sqlite/version-3.47.2/src/pager.c)
- [S3: Official testing description, Crash Testing](https://www.sqlite.org/testing.html)

## 3. Starlette: A Local Compatibility Fix That Constrains Overdesign (Retained v0.1.0 Record)

PR #2526, shown as merged on 2024-02-26 with diff commit `3031ee0`, removes the deprecated `app` argument passed to HTTPX from the `TestClient` constructor while preserving the existing transport. The diff is a one-line deletion in that file. [H1]

This is an observation from a source diff, not runtime verification in this round. It supports identifying a specific dependency contract and choosing a targeted fix. It does not establish a need for an added wrapper, or compatibility across every version combination.

- [H1: PR #2526 diff](https://github.com/Kludex/starlette/pull/2526/files)

## 4. Organizing Project Knowledge: Borrowing Strengths while Keeping Responsibilities Distinct (Retained v0.1.0 Record)

| Material | Practice actually observed in this round | What this version borrows | What is not adopted or established |
|---|---|---|---|
| rust-analyzer architecture description | Module source entry points, architecture constraints, deeper material, and testing directions | An entry point should explain intentionally absent dependencies as well as list locations | Documentation claims are not a source audit in this round; the same module structure is not required |
| GitLab's design-record workflow | An overview, decisions, on-demand subpages, and discoveries incorporated during implementation | Designs can start small; historical decisions can supersede one another | Team positions, merge requests, and organizational approvals do not become universal rules |
| Codified Context save-system record | Service responsibilities, runtime versus persistent state, and implementation anchors | Retain relationships that are difficult to reconstruct repeatedly | Main-branch records may change; the full application code was not checked |
| Codified Context drop-system excerpt | A knowledge gap leads to reading code, writing a record, and then using it in discussion | Grow knowledge during real tasks instead of creating a repository-wide ledger in advance | Selected interactions are not controlled evidence of long-term effectiveness |
| Nygard's ADR | Context, decision, consequences, and old decisions marked superseded | Retain the reasons for important judgments and their evolution | An ADR alone does not provide navigation to the current code |

The current rust-analyzer architecture page says that `base-db` does not know the specifics of Cargo or file paths and provides several implementation entry points. This round treats that as the authors' architecture description, not a claim that all current implementation satisfies those constraints. [R1]

GitLab explicitly permits a design to start with a short paragraph and evolve through exploration and implementation. Key decisions and technical details may live on subpages, and authors choose the sections needed. [L1] This version adopts the organization and evolution of information, not a fixed team process.

Codified Context's `save-system.md` contains `last-verified: 2026-02-15`. That is a status recorded by its author, not our verification date. The drop-system excerpt shows a task exposing a knowledge gap and prompting new documentation. [C1, C2]

The v1 paper reports stale documentation steering code back toward a deprecated path, and acknowledges a single-person, single-project observational study and unverified transfer across tools. [C3] This version therefore keeps on-demand records while rejecting the inferences that agents should trust documentation absolutely or that a ledger is automatically effective.

- [R1: rust-analyzer architecture page](https://rust-analyzer.github.io/book/contributing/architecture.html), a changing page, read on 2026-10-17; no commit was pinned for this round.
- [L1: GitLab Architecture Design Workflow](https://handbook.gitlab.com/handbook/engineering/architecture/workflow/), a changing page, read on 2026-10-17.
- [C1: Save-system record](https://github.com/arisvas4/codified-context-infrastructure/blob/main/case-study/context-docs/save-system.md), read on main in this round without a pinned commit.
- [C2: Drop-system interaction excerpt](https://github.com/arisvas4/codified-context-infrastructure/blob/main/data/case-study-excerpts/cs6-drop-system.md), read on main in this round without a pinned commit.
- [C3: Codified Context paper v1](https://arxiv.org/html/2602.20478v1), focusing on sections 5.2 and 5.3.
- [A1: Nygard, Documenting Architecture Decisions, 2011-11-15](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions).

## 5. Evidence for the Skill's Hosting Format Is Not Evidence of Method Effectiveness

This version uses a `SKILL.md` with `name` and `description`, and keeps on-demand references and templates in the same Skill directory. The optional `agents/openai.yaml` provides host display information and an implicit-invocation policy. Technical format and discovery mechanisms came from v0.1.0's official-documentation reading. This revision specifically reread the official Skills and AGENTS.md entry pages to confirm that the format, the fact that identical names do not automatically merge, and the scope descriptions still had documentation support. Host YAML was not changed. [O1, O2]

A brief working entry point can be placed in an existing `AGENTS.md`, but that file has a scope and loading time; it does not guarantee inheritance by every subagent, conversation, or environment. Detailed project facts do not belong in startup instructions. [O2]

- [O1: Official OpenAI Skills entry](https://developers.openai.com/codex/skills/), which redirected in this round to `learn.chatgpt.com/docs/build-skills`.
- [O2: Official OpenAI AGENTS.md entry](https://developers.openai.com/codex/guides/agents-md/), which redirected in this round to `learn.chatgpt.com/docs/agent-configuration/agents-md`.

These are public descriptions as of the reading date, not guarantees of support in a user's local version. Loading must be checked locally; file checks cannot substitute for that.

## 6. How Research Material Informed This Version

The research approach was inspired by [女娲.skill / Nuwa Skill](https://github.com/alchaincyf/nuwa-skill) by 花叔 Huashu: identify judgment methods in source material, organize them into a usable Skill, and observe their effect and limitations in actual tasks. This repository applies that approach to software engineering cases. It does not adopt persona simulation, fixed agent counts, or scoring conclusions, and does not include Nuwa's original Skill, templates, scripts, or images. Authors, licenses, and the specific extent of influence are recorded under [Sources and Licenses](#source-licenses).

The early research draft organized concerns including change, state, authorization, submission versus effect, existing work, and verification. The public draft retains material that explains the basis for judgments and identifies the nature of its sources. A historical material's mention of a project does not establish that all its mechanisms have been rechecked.

Public source cases, maintainer explanations, and practice reports identify their respective reading scopes and pinned-version conditions. Conclusions that were not rechecked retain their original evidence limits; preparing them for public use does not turn them into new verification results.

Different entry points can use implementations suited to their own boundaries; they need not mechanically call one shared location. Users must still check applicability along their own entry points, state, and consumers. Illustrative examples do not replace behavioral verification in a real project.

## 7. The Method's Status Where Evidence Is Limited

The existing real cases provide relatively strong support for shared-contract regressions, local compatibility fixes, and knowledge organization. They are not sufficient to claim adequate research or transfer validation for the formation and continuing evolution of an entire large-project architecture. This does not prevent use within explicit limits, or require completing a large case study in this round.

A code case supporting a judgment does not establish that this version's wording reliably prompts a model, or that it works over the long term across projects. These reasoning links form a usable, revisable first version. When they conflict with actual conditions, keep counterexamples, narrow their applicability, or remove items. Do not use more historical examples to rationalize every conclusion after the fact.

<a id="technical-sources"></a>

## 8. Targeted Sources for Technical Claims Added in This Revision

Reading date: 2026-10-17. The following are readings of official documentation and specifications, not complete source audits or runtime tests. Each supports a specific limitation; together they do not establish that the entire engineering method has been validated. The organization and tradeoffs proposed in the topic sections are this candidate's engineering recommendations and can be corrected by local counterexamples.

| ID and primary source | Fact directly supported | Applicability limit |
|---|---|---|
| [T1: Flask 3.1.x request context](https://flask.palletsprojects.com/en/stable/reqcontext/) | Request context is locally available; accessing its proxies outside the context raises an error | Framework behavior, not a claim about every language or framework; does not establish valid delegation to arbitrary background work |
| [T2: Python 3.11 asyncio, Task Cancellation](https://docs.python.org/3.11/library/asyncio-task.html#task-cancellation) | Cleanup is recommended on cancellation, and explicitly caught cancellation should generally propagate; swallowing it can interfere with related mechanisms | Does not guarantee cleanup after a process crash or reversal of remote effects |
| [T3: OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | Official security recommendations for least privilege and permission checks on each request | Guidance, not proof of a local policy's correctness; independent publication and business delegation still require actual policies |
| [T4: RFC 9111 §3.5](https://www.rfc-editor.org/rfc/rfc9111.html#section-3.5) | Restrictions and exceptions for reuse by shared HTTP caches after requests with Authorization | Not a complete design for permission isolation or immediate revocation in application caches |
| [T5: PostgreSQL 17 §47.2.2](https://www.postgresql.org/docs/17/logicaldecoding-explanation.html#LOGICALDECODING-REPLICATION-SLOTS) | Logical-decoding positions are persisted at checkpoints; recent changes can be resent after a crash, and consumers need to handle duplicates | A mechanism of one source, not evidence that every event has the same ordering guarantees |
| [T6: Stripe webhook, Event ordering](https://docs.stripe.com/webhooks#event-ordering) | Delivery is not guaranteed to follow generation order; timestamps alone are insufficient for deduplication or ordering | Changing interface documentation; no SDK/API version was pinned and no service was called in this round; illustrates why source capabilities need checking |
| [T7: RFC 9110 §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) and [§13.1.1](https://www.rfc-editor.org/rfc/rfc9110.html#section-13.1.1) | Conditions for automatically retrying non-idempotent requests and the conditional-request semantics of If-Match | An HTTP specification, not evidence that a remote system implements it or that a business operation has absolute exactly-once effects |

These links support specific technical claims in the new sections, not an expanded list of open-source projects to research. v0.1.0's limits on evidence about large architectures remain. Actual use, loading, and long-term benefits each require their own evidence.

<a id="source-licenses"></a>

## 9. Third-Party Sources, Attribution, and License Checks

Check date: 2026-10-18. The scope is the Skill, project ledger method and starter records, handbooks, examples, and research materials mentioned in this public draft—not the dependencies of a business project. Author entries use original attribution or public maintainers. Collaborative projects are not forcibly credited to one person; the original source remains authoritative for the attribution of individual commits, files, and documents.

### Sources Used in the Method, Cases, or Technical Explanations

| Project or material and URL | Author / public maintainer | What this repository uses and where | License checked and primary evidence |
|---|---|---|---|
| [女娲.skill / nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | 花叔 Huashu (alchaincyf) | Research-method inspiration in section 6; no upstream Skill, templates, or media are included | [MIT; copyright line 2026 Huashu (花叔)](https://raw.githubusercontent.com/alchaincyf/nuwa-skill/main/LICENSE) |
| [Git](https://github.com/git/git) | Git contributors; introducing commit by Derrick Stolee, regression test and fixes by René Scharfe, relevant commits integrated by Junio C Hamano | Commit chain, behavior analysis, and file/symbol locations in section 1; no Git implementation or test files bundled | [COPYING at the cited fixed version: GPL v2 unless explicitly stated otherwise](https://raw.githubusercontent.com/git/git/c8ad9d04c6a51cb5c73ebc9e42b627314eeafe2f/COPYING) |
| [SQLite](https://www.sqlite.org/) | Richard Hipp and SQLite authors and maintainers | Summary of architecture, invariants, and testing methods in section 2 | [Delivered code and documentation are in the public domain; build scripts and other materials may have separate licenses](https://www.sqlite.org/copyright.html) |
| [Starlette](https://github.com/Kludex/starlette) | Encode OSS Ltd and contributors; [the case PR's author is osoken](https://github.com/Kludex/starlette/pull/2526) | Local compatibility-fix analysis in section 3; no implementation snippets copied | [LICENSE.md at cited version 3031ee0: BSD-3-Clause](https://raw.githubusercontent.com/Kludex/starlette/3031ee0/LICENSE.md) |
| [rust-analyzer architecture documentation](https://rust-analyzer.github.io/book/contributing/architecture.html) | The rust-analyzer authors | Responsibility, entry-point, and dependency-organization ideas in section 4 | [Main repository states dual MIT / Apache-2.0 licensing](https://github.com/rust-lang/rust-analyzer#license); no separate license was found on the cited architecture page |
| [GitLab Architecture Design Workflow](https://handbook.gitlab.com/handbook/engineering/architecture/workflow/) | GitLab and Handbook contributors | Workflow summary and method inspiration in section 4; no original page or templates included | [The Handbook explicitly uses CC BY-SA 4.0](https://handbook.gitlab.com/handbook/about/handbook-usage/#external-use-of-the-handbook); the software-root MIT notice cannot substitute for it |
| [Codified Context companion repository](https://github.com/arisvas4/codified-context-infrastructure) | Aris Vasilopoulos; the license copyright line credits Aris | Analysis of the save-system record and interaction excerpts in section 4; on-demand knowledge accumulation is borrowed, but its records, agents, and MCP implementation are not included | [MIT](https://raw.githubusercontent.com/arisvas4/codified-context-infrastructure/main/LICENSE); [CITATION.cff](https://github.com/arisvas4/codified-context-infrastructure/blob/main/CITATION.cff) requests citation of the paper |
| [Codified Context paper v1, arXiv:2602.20478v1](https://arxiv.org/abs/2602.20478v1) | Aristidis Vasilopoulos (credited as Aris Vasilopoulos in the companion repository) | Section 4 summarizes the observational report and its limits, originally written in Chinese; no paper, figures, or original paragraphs included | The paper entry links to [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); recorded separately from the repository's MIT license |
| [Documenting Architecture Decisions, 2011-11-15](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | Michael Nygard; published by Cognitect | Context, decision, consequences, and supersession in section 4 and the project ledger method; this repository organizes its own record fragments | The original page explicitly waives copyright and related rights in this article to the extent permitted by law; that statement does not extend to the entire site |
| [Flask request-context documentation](https://flask.palletsprojects.com/en/stable/reqcontext/) | Pallets and Flask contributors | Specific framework-behavior summary in T1 and reference 07·A2 | [Flask documentation license page: BSD-3-Clause](https://flask.palletsprojects.com/en/stable/license/) |
| [Python 3.11 asyncio documentation](https://docs.python.org/3.11/library/asyncio-task.html#task-cancellation) | Python Software Foundation and Python contributors | Cancellation and cleanup guidance in T2 and reference 07·A3; this repository's single-file example uses standard-library APIs without bundling Python's implementation | [Software/documentation use the PSF License Agreement; documentation example code also has a 0BSD option](https://docs.python.org/3.11/license.html) |
| [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | OWASP Cheat Sheet Series contributors | Authorization guidance summary and further engineering analysis in T3 and reference 07·B; no original text, figures, or checklist included | [Cheat Sheet Series: CC BY-SA 4.0](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/master/LICENSE.md) |
| [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html) and [RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html) | Editors Roy T. Fielding, Mark Nottingham, and Julian Reschke; IETF Trust and the document authors | Summaries of specification semantics in T4/T7 and reference 07; no specification text or code components copied | Each RFC's copyright section specifies BCP 78 and the [IETF Trust legal provisions](https://trustee.ietf.org/license-info) in effect at publication; extracted code components also require the stated Revised BSD conditions |
| [PostgreSQL 17 logical-decoding documentation](https://www.postgresql.org/docs/17/logicaldecoding-explanation.html#LOGICALDECODING-REPLICATION-SLOTS) | PostgreSQL Global Development Group; the license page also retains portions of copyright held by the Regents of the University of California | Summary of duplicate-delivery conditions in T5 and reference 07·C2 | [PostgreSQL 17 documentation license notice](https://www.postgresql.org/docs/17/legalnotice.html): PostgreSQL License, covering software and documentation |
| [Stripe webhook documentation](https://docs.stripe.com/webhooks#event-ordering) | Stripe and its documentation authors / rights holders | Summary of delivery-ordering facts in T6 and reference 07·C2; no SDK or documentation paragraphs included | No general open-source license was confirmed for this webpage; [official terms](https://stripe.com/legal/ssa) reserve documentation rights and restrict copying/redistribution; an SDK license does not establish the webpage's license |
| [OpenAI Skills](https://learn.chatgpt.com/docs/build-skills) and [AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | OpenAI | Format and hosting-mechanism explanation in section 5; no client, generator, or webpage body bundled | No explicit general open-source license was found on the cited pages; distinguish services, documentation, output, and third-party content under the [official terms](https://openai.com/policies/terms-of-use/), rather than extending an open-source tool's license to all site text |

The summaries, originally written in Chinese, and engineering-transfer analyses were prepared for this repository; they are not the original authors' verbatim statements. The nature of each source remains distinguished in the preceding sections. Attribution and links do not imply the original authors' participation, endorsement, or guarantee.

### Projects Mentioned but Not Used as Implementations or Direct Research Evidence in This Version

The following appear above as historical material or case dependencies; their identities and license locations are also recorded. Only the current public main repository licenses were checked here. This does not establish the licenses of versions used in earlier research, every plugin, or commercial distributions.

| Project and URL | Author / public maintainer | Use in the current draft | License check |
|---|---|---|---|
| [Odoo Community](https://github.com/odoo/odoo) | Odoo and contributors | Mentioned in the opening historical context; no code or templates included | [19.0 main repository LGPL v3; individual third-party files may differ](https://raw.githubusercontent.com/odoo/odoo/19.0/LICENSE); does not cover Enterprise |
| [ERPNext](https://github.com/frappe/erpnext) | Frappe / ERPNext contributors | Mentioned in the opening historical context; no code or templates included | [Main repository GPL v3](https://raw.githubusercontent.com/frappe/erpnext/develop/license.txt) |
| [Temporal](https://github.com/temporalio/temporal) | Temporal Technologies Inc., Uber Technologies, Inc., and contributors | Mentioned in the opening historical context; no server, SDK, or workflow implementation included | [Main server repository MIT](https://raw.githubusercontent.com/temporalio/temporal/main/LICENSE); other components require separate checks |
| [Debezium](https://github.com/debezium/debezium) | Debezium community and contributors | Mentioned in the opening historical context; no connectors or other implementations included | [Main repository Apache-2.0](https://raw.githubusercontent.com/debezium/debezium/main/LICENSE.txt) |
| [HTTPX](https://github.com/encode/httpx) | Encode OSS Ltd and contributors | Dependency named in the section 3 Starlette case; its implementation was not separately distilled | [Main repository BSD-3-Clause](https://raw.githubusercontent.com/encode/httpx/master/LICENSE.md) |

### Current Finding and Limits on Future Reuse

This check found no implementations, images, original records, or substantial passages from the projects above distributed in this package, and no copied material clearly violating the verified licenses. A consolidated author/license description and attribution of Nuwa's methodological inspiration were previously missing; this section supplies verifiable sources. The finding applies to the current text and identifiable direct sources. It is not an exhaustive similarity assessment or a determination of ownership.

Studying software behavior, summarizing facts, and borrowing methods do not automatically subject this repository to the studied software's license. Conversely, translation, rewriting, or AI-assisted organization do not automatically rule out copying or adapting protected expression. See [WIPO's explanation of ideas and expression](https://www.wipo.int/en/web/copyright/protection) and [Creative Commons' explanation of adaptations](https://creativecommons.org/faq/#when-is-my-use-considered-an-adaptation).

If third-party code, original text, translations, figures, or templates are actually incorporated later, preserve the specific source, version, modification notice, and the copyright, license, and disclaimer notices required by the original license for those portions. A source link alone cannot replace notices required by MIT, BSD, or similar licenses. Copying or substantially adapting CC BY-SA material requires attribution, license information, modification notices, and compliance with ShareAlike for the corresponding adapted content. Do not describe all such content as this repository's own or relicense it wholesale under MIT. Webpages without a confirmed license are not freely copyable material.

This repository's own content that it is entitled to license uses [MIT](../LICENSE), with the public byline KZ. That choice does not replace the third-party licenses listed here or establish that publication has occurred. Add a row here when a new source is actually adopted. Merely using a production or checking tool does not mean distributing that tool; there is no need to list every tool in the environment as a source of the method.
