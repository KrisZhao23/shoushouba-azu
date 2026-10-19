# `<Project name>`: current engineering understanding

[English](project-ledger.md) | [简体中文](project-ledger.zh-CN.md)

> Optional starter; prompts are not project facts. Update the existing entry point when one exists. Merge or delete sections as needed without inventing unknown details. See [ledgers and timelines](../references/03-ledger-and-timeline.md) for maintenance.

## Project and goal

Project scope and workspace: `<Identity, actual scope, path base, and relationship to the platform>`.
Entry registration: `<Location in actual working instructions; state when unregistered or reading is unverified>`.
Goal and current state: `<Who needs what outcome; actual implementation or operation status; applicable snapshot>`.
Important constraints: `<Currently valid constraints affecting the work, their basis, and necessary unknowns>`.

## How the whole works together

`<How the main responsibilities produce the outcome, and who supplies and consumes which facts; expand only branches and failures that affect understanding.>`

| Responsibility and purpose summary | Implementation or existing explanation | Dependencies and connections | Impact and verification |
|---|---|---|---|
| `<What it owns; inputs and outputs>` | `<Files and symbols, with lines/snapshot when useful>` | `<Producers, consumers, shared state ownership, connecting contracts>` | `<Affected behavior and test/evidence links>` |

A small project may use a paragraph instead. Cover the [required implementation relationships](../references/03-ledger-and-timeline.md#implementation-map) for each responsibility here or in linked explanations, including hidden dependencies that actually exist. Use the [responsibility fragment](record-fragments.md) when detail is needed; state unknowns rather than substituting a file list for an explanation.

## Key behaviors and decisions

### `<Behavior, state, or decision>`

`<Current meaning, authority, and consumers; accepted agreement and its basis; keep unaccepted proposals distinct.>`

Rationale and limits: `<Tradeoffs difficult to reconstruct from code and their applicable conditions>`.
Implementation and verification: `<Actual location, results, supported scope, and unverified matters; an agreement is not proof of implementation>`.
Discrepancies to check: `<Incorrect records, implementation deviations, or accepted changes not yet reflected; delete if none>`.

## Current pending work

`<Link the existing Pending list. If there is no separate list, briefly state item, owner, next action, and check time or condition here. Keep only current values, remove finished items, and do not copy reports.>`

## Key turning points

`<Keep only what is worth revisiting: mistaken judgment or earlier choice → evidence that changed it → correction and impact, with necessary evidence references. Link existing records instead of copying them.>`

---

Use the [shared maintenance method](../references/03-ledger-and-timeline.md) for pruning and corrections. Do not retain content that helps neither continuation nor locating a key issue.
