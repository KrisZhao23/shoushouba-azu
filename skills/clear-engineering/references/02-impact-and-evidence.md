# Change impact, evidence across components, and reasons to stop

[English](02-impact-and-evidence.md) | [简体中文](02-impact-and-evidence.zh-CN.md)

Purpose: read this when adding behavior, fixing defects, changing shared state or contracts, reviewing work, or locating regressions. The goal is to investigate far enough to support the current decision, not to prove that nothing anywhere in the system has been missed.

## 1. Define the fact that is changing

Do not treat the edited file as the impact boundary. First explain the external result that needs to change, the behavior that may remain, and the key facts on which the commitment depends. A paragraph can be enough; a table is not mandatory.

For example, when a field gains a new allowed value, determine whether this expands its representation, adds a business state, or changes the meaning of an old value. A more permissive validator may let previously ignored input reach downstream consumers. Behavior can change even when parameter types remain identical. The Git case demonstrates such a chain in practice.

## 2. Trace relevant relationships from an anchor

Start at an actual entry point or shared fact and identify its producers, writers, interpreters, and consumers. Choose searches according to the evidence that triggers them: symbol references; reads and writes of fields and values; event and subscription registration; configuration reads; route and startup registration; cache updates and invalidation; background and batch work; exports and display; existing data and in-flight objects.

A search with no matches does not establish that a dependency is absent. Dynamic registration, template fields, constructed strings, plugins, cross-process protocols, and generated code need checks at the corresponding entry points. A purely local styling change does not require auditing all these relationships.

The project ledger first supplies relevant vocabulary, locations, and known cooperation paths; source code, configuration, and tests then establish the current facts. Prioritize claims most likely to change the decision or whose failure would be most costly, rather than traversing files in order.

If you find omissions caused by filtering or pagination, reassigned relationships, caches reused across principals, or a rebuild that triggers sending, use the relevant sections of [07·B/C](07-implementation-boundaries.md) to determine their actual semantics. Do not reduce them to "pay attention to state." The counterexamples in those sections support this task's impact and stopping judgments; they do not start a separate whole-system audit.

## 3. What to check when components work together

A value or state supplied by a producer must still satisfy the consumer's assumptions when used. Beyond the shape of the return value, this may require checking identity and scope, version binding, read/write order, concurrency races, failure interpretation, and whether resources remain valid.

An unchanged consumer may still be the most important verification target. When another consumer needs no change, explain whether its old contract is preserved, a compatibility entry point isolates the change, or the changed fact does not affect it at all.

For example, review may accept content version seven while publication reads version eight. Both functions can behave correctly by their local definitions and still fail to protect "publish only reviewed content." This requires checking the correspondence between the producer, the artifact carrying the content, and the consumer, rather than splitting more functions.

## 4. Stopping is a scope judgment, not an absolute proof

For one direction of outward investigation, these reasons can combine into a proportionate basis for stopping:

- The neighboring boundary's semantics, error meaning, and necessary assumptions remain intact, and actual consumers of that boundary have been checked.
- An existing conversion, version, or compatibility boundary absorbs the change, supported by relevant counterexample or contract checks.
- Build, static-constraint, or configuration evidence rules out the specific concern at hand, rather than merely showing that "type checking passed."
- The remaining unknown scope is explicit; the current action does not rely on guarantees from that scope; the residual risk is acceptable and there is a way to replace the approach.

These are not four conditions to fill out for every direction. The point is to explain why the investigation is sufficient using evidence relevant to this change. Not finding an important counterexample does not prove none exists. Unchanged parameters, working links, and reaching another directory are not sufficient reasons to stop on their own.

When a neighboring consumer involves high-risk state or effects that cannot be verified, first limit the affected action and propose a specific, minimal check. Do not pretend every dynamic dependency has been found, or turn a low-risk unknown into an endless investigation.

## 5. Distinguish what different evidence establishes

| Evidence | What it can support | What it does not automatically establish |
|---|---|---|
| Reading source, types, and configuration | Explicit logic and dependencies, and visible assumptions, in a given version | Successful execution or coverage of all dynamic paths |
| Build, type, and static checks | Definitions, interfaces, or rule constraints in the corresponding environment | Correct business meaning or correct external effects |
| Local rule or contract tests | Rules or boundaries for the specified inputs and assertions | Behavior across all entry points, concurrency, real resources, and consumers |
| Tests across components and through entry points | Behavior and state relationships on the paths exercised | Configurations not exercised, other versions, or other environments |
| Failure, concurrency, or recovery tests | Handling under the specified injected failure or interleaving | Every possible failure or an absolute exactly-once effect guarantee |
| Human observation and historical execution records | Observations at the time recorded, if the source is reliable | Continued validity in the current snapshot or details that were not recorded |

Use only the combination relevant to the current commitment. When a defect appears, first check whether the test would fail while the defect still exists. Do not change expected values just to make an incorrect result "green." If execution is unavailable, report precisely which assertions were read, what prevents execution, and what remains to be run.

Record actual commands or checking methods, the working snapshot, relevant environment, results, and limits; remove sensitive arguments. A suggested command must not be listed as "run." A successful exit code still requires checking what was actually verified.

## 6. Keep expected impact, actual changes, and behavioral results distinct

The expected impact before a change helps expose omissions. The actual changes may include necessary related edits, unrelated cleanup, or missing edits. Execution results may uncover issues neither anticipated. Do not replace the original expectation with the final changes and then claim the judgment was accurate.

Whether a new finding requires revisiting the design depends on whether it changes shared assumptions or important constraints, not on the size of the edit. Before-and-after expectations and key findings can remain in the task record; stable conclusions can then enter the project's current understanding.

## 7. Risk control and preserving evidence

Local snapshots, a relevant file list, and test results are enough to start; Git is not required. For irreversible data changes or external effects, a source-file backup is not equivalent to business recovery capability. Explain them separately. Do not call production services without authorization just to obtain evidence.

If an unknown does not affect the current decision, keep it as a clearly scoped item to verify and continue working. Important unknowns affecting authorization, data integrity, concurrency, or duplicate effects must not be hidden under "improve later."
