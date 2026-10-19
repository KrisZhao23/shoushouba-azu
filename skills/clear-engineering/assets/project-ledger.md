# `<Project name>`: current engineering understanding

[English](project-ledger.md) | [简体中文](project-ledger.zh-CN.md)

> A starting template for a project ledger. The content below consists of writing prompts, not project facts or accepted agreements. When existing documentation serves the same purpose, reuse and supplement it instead of creating a parallel index. Choose what you need, merge or remove prompts, and do not invent unknown details for the sake of completeness.
>
> Purpose: help readers understand the whole, locate relevant responsibilities and implementations, verify the basis for claims, and continue from existing progress.

## 1. Reading guide and scope

Project and workspace: `<Project identity, scope, and actual workspace; explain its relationship to the platform or internal projects without treating a materials directory as the full implementation scope>`.
Designation and discovery of this entry point: `<Basis for its designation, the actual registered work entry point, and its location there; state when it has not been registered or reading has not been verified. The existence of this template does not establish adoption>`.
Base for resolving paths: `<Project root or another explicit base; reference an existing explanation rather than registering it again>`.
What the current materials correspond to: `<Verifiable code/configuration version, file snapshot, or explicit scope>`.
Division of responsibility between this entry point and existing materials: `<Which existing explanations remain authoritative for their purposes; avoid duplication>`.
Confirmed coverage and important gaps: `<What has been inspected; what is only secondhand, historical, or still unverified>`.

`<Explain in prose what the current reader can learn here and where to go deeper; do not label the entire record with a blanket "review passed".>`

## 2. Goal, boundaries, and current stage

`<Who needs what outcome, which behaviors must hold, which responsibilities are outside the project, and whether the work is currently research, a demonstration, implementation in progress, or actual operation. A business scope sketch is not a final module, sequence, or state model.>`

Important shared constraints: `<Requirements that actually apply, such as identity and authorization, state meanings, version correspondence, data integrity, actual effects, or operational constraints, with their basis for confirmation; do not copy a generic risk checklist>`.

## 3. How the whole works together

`<Explain how the main responsibilities cooperate to produce the outcome and who determines whether it holds. Beyond the normal path, identify branches, parallel work, joins, reversals, or failures that genuinely matter to understanding. A complete diagram is not required, but a list of module names is insufficient.>`

| Responsibility or collaborator | Commitment and boundary | Implementation / existing documentation entry point | Collaboration relationships that matter |
|---|---|---|---|
| `<Actual object>` | `<Why it owns this responsibility; what it does not own>` | `<Actual paths and symbols>` | `<What it depends on, from whom, and who uses its results>` |

The table is optional. A paragraph can suffice for a small project; a large project can retain the overall explanation here and expand internal details as questions arise.

## 4. Key behaviors, states, and contracts

### `<The behavior or shared fact most important to understand now>`

Goal and meaning of completion: `<User outcome, state, or external effect>`.
Accepted agreement: `<Specific content, applicable scope, and actual evidence of acceptance; state explicitly if unconfirmed>`.
Still proposed: `<Options or restrictions not yet accepted; do not treat them as settled premises; remove if inapplicable>`.
Actual observations: `<Key entry points, writers, interpreters, and consumers; applicable snapshot>`.
Collaboration premises: `<Versions, identity, timing, resources, and failure meanings that genuinely affect behavior>`.
Verification and unknowns: `<Evidence locations, actual execution scope, and unverified claims>`.
Where to go deeper: `<Link to existing explanations or behavior/contract records when expansion is needed; do not create empty files in advance>`.

When several behaviors refer to the same state, its interpretation can be maintained as a separate contract and referenced by those behaviors. Identical words do not automatically denote the same fact.

## 5. Important decisions and implementation differences

`<Preserve tradeoffs that are hard to reconstruct from code: which facts led to which choice, its costs and limits, and changes that would require reassessment. Small decisions can remain within the relevant behavior description.>`

Currently valid decisions: `<Accepted decisions, their scope and basis; make clear if not yet implemented>`.
Choices not yet accepted: `<Keep separate from currently valid decisions; explain whose judgment or what evidence is still needed; optional>`.
Differences between implementation and agreements: `<Distinguish stale documentation, implementation deviations, and accepted changes not yet reflected in the record>`.
Key history entry point: `<Actual location of important decisions or the timeline; do not copy the full history here>`.

## 6. Verification basis and matters to check

`<For each key claim, point to the corresponding source observation, test assertion, or actual result. Complete documentation is not evidence.>`

| Important claim | Evidence and baseline | Supported scope and limits | What remains to be verified |
|---|---|---|---|
| `<Specific claim>` | `<Actual source / snapshot / result>` | `<Static reading or executed check, environment, and coverage>` | `<Questions that could change the decision>` |

Connect important unknowns to concrete places to investigate. Continue within scope when they do not affect current work; restrict relevant actions when they affect high-risk decisions.

## 7. Current work and continuation entry points

| Active task or discussion | Current status | Continuation record | Effect on shared understanding |
|---|---|---|---|
| `<Actual task>` | `<Precise status: investigated, implemented, unverified, etc.>` | `<Actual file or section in this file>` | `<Relevant constraints or unresolved decisions>` |

A small project without parallel work can replace the table with a paragraph describing the current checkpoint. When a task ends, move stable knowledge back to the relevant responsibility or behavior and remove irrelevant process details from current navigation.

## 8. Key developments

`<Record them here or point to the actual timeline. Preserve the date, event type, changed judgment, impact, and evidence. Decision time is not implementation time or the time an effect became active.>`

### `<Event ID> · <Known time / unknown> · <Event title>`

`<Changes in facts and the basis for judgment; the respective implementation, verification, and activation status; recording time for retrospective entries; links to actual tasks, decisions, and evidence.>`

---

Maintenance principle: whoever discovers or changes a relevant shared fact makes the difference visible; whoever verifies a claim explains the basis and scope. Check the original text and baseline before saving parallel work. Five rounds of approval are not required, important history must not be overwritten without a trace, and every task need not reread the entire ledger.
