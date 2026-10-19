# Planning, design review, execution, code review, and continuity

[English](04-planning-review-and-handoff.md) | [简体中文](04-planning-review-and-handoff.zh-CN.md)

These are perspectives on responsibility, not five required agents, five reports, or a mandatory approval chain. The same person or agent may take several responsibilities, but restating the same assumption is not independent verification.

## 1. How everyone making a plan obtains the wider context

Establish the goals, main cooperation relationships, and important constraints relevant to the task. When the existing overall understanding still applies, read the current stopping point and relevant changes, then investigate implementation and verification through real questions. Understand who will use this output, what it changes, and which conditions others must provide; every small change does not require investigating the whole again.

Each subplan should remain connected to the overall goal, rather than merely receiving a file list. A delegation can provide the goal, boundaries, key contracts, relevant records, and permissions without copying the entire Skill or all repository documentation to every participant. Recipients check that they can access these sources; do not assume subagents automatically inherit files or context.

## 2. Plan when the implementation is not fully understood

Separate commitments that can be made now from local questions that need exploration before a decision. Do not invent a precise list of functions. Make a question to investigate as specific as possible, such as "Does the current approval action also check that the request is still pending?" rather than "Audit all concurrency."

Decisions affecting shared meaning, authorization, persistent data, external effects, or costly replacement need proportionate support first. Private, reversible implementation that does not change others' assumptions should retain room for judgment. When exploring resource capabilities, state the question to answer, the allowed actions, and what result would be enough; do not install tools or call production systems by default.

Distinguish conditions before an action from evidence after it. For example, before starting something, establish the target, permissions, parameters, and safety boundaries; startup success and actual runtime behavior are observed afterward. Establish how evidence will be obtained, rather than requiring results before they exist. Placing acceptance-check inputs in a shared loading function does not automatically make them legitimate startup prerequisites.

When support is missing, identify the specific risk in this step, limit only the dangerous actions that actually depend on it, and continue safe, independent work. Equally, do not complete a dangerous implementation that depends on an unknown key capability and only afterward supply the design rationale.

## 3. Design review checks whether claims can hold

First assess whether this step serves the current goal, whether it is needed now, and whether its conditions can be obtained in the proposed order. Then review ownership of constraints, the meaning participants assign to them, and the state left after failure. When an existing capability would be interrupted, check the necessary scope, preparation that can happen beforehand, and the authorized way to restore it if blocked. Testing cooperation with a discriminating scenario is more meaningful than checking the report format.

A direction may be accepted conditionally, but its conditions do not thereby become facts. Identify which supporting facts still need investigation in the implementation. If a fact turning out false would change the approach, make that visible to the executor. When several approaches are reasonable, a reviewer's preferences for directories, patterns, or code style must not become the only standard.

## 4. Execution turns responsibilities into actual behavior

Prefer existing capabilities that are sufficient. Trace from the commitment into implementation, attending to the source of state, call timing, external interactions, and actual consumers. Before adding a script or wrapper entry point, establish that existing operations really cannot meet the goal; a need to leave a record does not itself require generated code. When the plan missed something, preserve the new fact and its impact.

If only local implementation changes and shared meaning is preserved, proceed with the necessary verification. If the change affects shared interface semantics, state interpretation, write permissions, version applicability, failure behavior, or important resource constraints, adjust the relevant plans and shared understanding. Not every function edit returns to design review, and an internal function is not necessarily free of external impact.

## 5. Code review checks the combined result

Read beyond the changed lines. Trace the current commitment to relevant unchanged consumers, and check the actual producers and read locations, including defaults, combined conditions, and final input formats. Inspect actual test assertions, execution snapshots, and limits; a test file's existence is not a passing result.

Independently look for a scenario that could overturn the implementation's explanation, such as another entry point, an old object, interleaved old and new versions, repeated execution, or a lost response. Choose according to the current risk; do not audit every class of risk each time.

Review may reveal a problem in the design itself. If code follows a design that violates a business commitment, adjust both design and implementation. If the design has legitimately changed and the record is outdated, update the record. Keep the reason for the discrepancy visible.

## 6. Move from process records to current understanding

After verification, correct the original explanation. Delete useless wrong directions, expired conditions, duplicate explanations, and routine logs. For turns worth tracing, keep only the original basis, where judgment went wrong, the correction, and an evidence link; do not retain the full mistaken plan. Important unresolved claims remain unknown or disputed even after task closure. See [reference 03](03-ledger-and-timeline.md) for record selection.

## 7. Minimum continuity information for interruptions, transfers, and new conversations

The next person needs the current goal and scope; workspace/file snapshot; the distinction between investigated, implemented, and verified by execution; important agreements or changes; unresolved matters and blockers; where to inspect what next; and which actions must not be repeated.

This information can reference existing records, update the original stopping point, or be expressed in a paragraph. Changing roles does not require another full report. The next step should be ready to start, with the necessary reasons retained. State the safe boundaries when execution is not authorized or an external effect is unknown.

On resuming, first check differences between the current files and the recorded baseline, then continue. Reading the same record does not establish shared understanding. Observable signs include identifying who interprets the same state, what failure means, and where affected entry points are.

## 8. Separate changes to the method from changes to project facts

An individual business change may update the project ledger without changing the general Skill. If the method itself appears to encourage excessive splitting, missed checks, or useless records, preserve the counterexample and propose a method revision. A general change should state its scope and evidence, rather than extend one project's special decision to every project.
