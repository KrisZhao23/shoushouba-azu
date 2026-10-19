# Record fragments to expand as questions arise

[English](record-fragments.md) | [简体中文](record-fragments.zh-CN.md)

Add fragments to existing explanations as needed; six new documents are not required. Formats may be combined, but [written implementation relationships](../references/03-ledger-and-timeline.md#implementation-map) are required. Replace prompts with facts, state unknowns, and use the shared maintenance method for pruning and corrections.

## Responsibility description

### `<Responsibility name>`

Purpose summary: `<Why it exists, what it owns, its inputs, outputs, and responsibility boundary.>`

Implementation location: `<Actual file and function/class/interface/registration symbol; add lines and snapshot when useful>`.
Producers and consumers: `<Who provides what; who calls or consumes it; links to collaborators' implementation or explanations>`.
State and coupling: `<Shared data ownership and readers/writers, shared constraints, and actual hidden inputs, initialization/call ordering, and lifecycle requirements>`.
Connecting contracts: `<Specific call/interface/event/table/adapter, data translation, contract ownership, and side-effect locations>`.
Change impact and verification: `<Affected consumers, behavior that must remain intact, and relevant test/evidence references>`.
Basis for the boundary: `<Actual changes, shared constraints, or resource differences>`.
Evidence / unknowns: `<Actual materials and scope supporting specific claims>`.

## End-to-end behavior description

### `<Behavior from trigger to observable outcome>`

`<The entry point; creation, transfer, reads, and writes of key facts; participants; and the final outcome. Use as much explanation as needed; there is no prescribed number of steps.>`

Must preserve: `<What may change and which relationships must remain intact>`.
Important interleavings / failures: `<Only those genuinely relevant to this behavior>`.
Consumers and relationships: `<Include relevant unchanged entry points, displays, background work, caches, or messages>`.
Implementation and verification: `<Key anchors, assertions, or runtime evidence; unverified scope>`.

## Shared state or contract description

### `<Shared fact name>`

Meaning and authority: `<What it represents, what it does not represent, and which system or responsibility has authority to interpret it>`.
Production / updates: `<Who changes it under which conditions; how multiple writers coordinate>`.
Use: `<Who uses it to display information, decide, or produce effects>`.
Semantic conditions: `<Applicable identity, units, null values, versions, freshness, and failure interpretations>`.
Change considerations: `<Which old objects or entry points depend on the old meaning; which boundaries can absorb changes>`.
Evidence: `<Actual locations and applicable scope>`.

## Important design decision

### `<Decision ID> · <Dispute to resolve>`

Current status: `<Proposed (not accepted) or accepted; include a date only when useful and known>`.
Acceptance basis and scope: `<Accepted content, scope, and basis; proposals do not become accepted by default>`.
Context: `<Facts, constraints, and unconfirmed conditions>`.
Choice and rationale: `<Why this choice is preferable to actual alternatives; do not merely list pattern names>`.
Costs and boundaries: `<What it commits to; when it does not apply; what evidence would refute it>`.
Implementation and verification: `<Implemented, unimplemented, or partly implemented; evidence references, distinct from approval>`.
Key turning point: `<If it has lasting value, briefly state the earlier judgment, evidence that changed it, and correction; delete redundant text of the superseded decision>`.

## Evidence description

### `<Evidence ID> · <Specific claim supported>`

Type: `<Author's explanation, source observation, test reading, actual execution, user confirmation, etc.>`.
Object and baseline: `<Actual version, snapshot, relevant configuration, and time>`.
Check method: `<Actual operations and assertions; do not present suggested commands as already executed>`.
Result: `<What was observed>`.
Limits: `<What it cannot establish and what gaps remain>`.
Location: `<Source, log, or result file; do not copy secret data>`.

## Unverified claim

### `<Unknown / disagreement ID> · <Specific question>`

Existing basis: `<Different accounts and their sources; clearly mark inferences>`.
Impact: `<Why it could change a decision; whether it restricts current actions>`.
Minimum check: `<What to observe at which actual location to make progress>`.
Once resolved, merge the conclusion into the relevant explanation and delete this item. Retain a brief turning point and evidence reference only when they have lasting value.
