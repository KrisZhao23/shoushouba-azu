# Public draft validation record

[English](VALIDATION.md) | [简体中文](VALIDATION.zh-CN.md)

Scope: `0.1.3-candidate`, including the method revision below. Maintain this record with the relevant files; published commits define the online version.

## Current evidence

- Method revision `CE-COMMITMENT-CHECK-20261031` (2026-10-31) updates the bilingual [entrypoint](skills/clear-engineering/SKILL.md), [scenario guidance](skills/clear-engineering/references/01-judgment.md), and [fictional publication example](skills/clear-engineering/examples/composed-publication.md). Keywords: original commitments, actual usage conditions, counterexamples, bounded stopping. The revision makes the original requirements the basis for judging an approach and removes the fixed scenario count.
- Independent bilingual review identified and resolved an ambiguity between reviewed and approved content. `quick_validate.py` passed for the public and installed Skill; six changed files match as UTF-8 text, with the installed entrypoint's existing bilingual description preserved. Relative links and added-text private-marker checks passed.
- Two independent fresh-context scenario checks used the updated entrypoint. A batch-renaming proposal was rejected because re-enumerating a changed directory would violate the confirmed preview; the proposed correction retained the preview mapping and handled target-name conflicts. A page-specific spacing change with sufficient Chrome evidence was accepted without expanding to unrelated testing. These were reasoning checks on fictional inputs, with no product execution or comparison against the previous Skill.
- Navigation behavior and limits are maintained in [reference 03](skills/clear-engineering/references/03-ledger-and-timeline.md#optional-local-navigation).
- The [navigation regression](skills/clear-engineering/scripts/test_build_navigation.py) passed in the public and installed locations on 2026-10-26, using isolated temporary sources. Coverage includes scoped discovery, changed/missing/ambiguous sources and context, Markdown parsing and section-scoped links, absolute heading destinations, read/discovery failures, source/output protection, cross-drive rendering, and stable output bytes/modification times. Exact cases and assertions remain in that script.
- Skill format, public/installed UTF-8 parity, bilingual usage, navigation links, diff formatting, and private-marker checks passed for that delivery. The receiving task subsequently confirmed real-project opening context, heading links, and section-scoped link acceptance. This is integration feedback, not measured workload reduction.

## Evidence that still applies

- Research attribution and license findings remain in the [source inventory](skills/clear-engineering/references/06-case-evidence.md#source-licenses). Project-owned content is MIT-licensed; third-party terms remain applicable. The video's music and sound effects are covered by the accompanying [audio notice](media/HUASHU-DESIGN-LICENSE.txt); no third-party implementation source was added.
- The existing self-check in the [single-file example](skills/clear-engineering/examples/single-file-tool.md) previously passed in an actual run. Its behavior was unchanged and was not retested.

## Limits

These checks support file contents, format, and references, not task efficiency, automatic host loading, or cross-project effectiveness. File updates do not establish that open conversations have reread them.
