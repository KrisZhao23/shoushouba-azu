# Review handbook

[English](review.md) | [简体中文](review.zh-CN.md)

See the [main Skill](../skills/clear-engineering/SKILL.md) for general judgment, [reference 04](../skills/clear-engineering/references/04-planning-review-and-handoff.md) for plan and code review, and [reference 02](../skills/clear-engineering/references/02-impact-and-evidence.md) for impact and evidence scope. This handbook explains when independent review is needed and how to use its conclusions. More specific existing project agreements continue to apply.

## Determine the review needed

First distinguish a new change, execution of an already reviewed operation, and restoration of an existing capability that is already authorized. Judge them by their actual effects and risks. A role perspective does not automatically require a separate chat. Where production behavior, permissions, persistent data, runtime dependencies, or irreversible effects are involved, use the project's governance and safety agreements to determine whether independent review is required and when it must be completed.

When the project requires independent review, a reviewer other than the executor and the relevant decision-maker performs it. The executor's own checks and tests do not replace it. Pure documentation changes or repeated operations on the same reviewed object with unchanged relevant premises can usually reuse an existing conclusion, subject to the project's requirements.

Before reusing a conclusion, verify the content, configuration, and side effects that will actually be executed. The same task name does not establish unchanged content or risk. Address new unreviewed changes and material risks within the relevant scope. A rule update does not automatically revoke existing authorization or silently reorder work in progress; unresolved conflicts limit only the affected actions.

## Start with the goal of this step

Assess whether the action is necessary, whether the current dependency order makes sense, and what business state a failure would leave behind before reviewing implementation details. Source code that follows the original design may reveal that the design itself needs correction.

When an existing capability must be interrupted, check the objects that genuinely need interruption, preparation that can be completed beforehand, and authorized recovery options if work is blocked. Health or acceptance results produced after an operation are subsequent evidence; what must be clear beforehand are the prerequisites and the method of verification.

When evidence is missing, explain the risk it creates for this step. Incomplete materials or record formatting alone do not justify blocking all work. If an existing operation is sufficient, do not create new code and an additional delivery chain merely to have something to review.

## Trace real relationships and precise assertions

Check the relevant producers, writers, and final consumers, including unchanged entry points, defaults, input formats, combined conditions, versions, and failure meanings. A shared input dependency in the code still needs a necessity check; it cannot be treated directly as a business prerequisite.

Look for counterexamples that discriminate between correct and incorrect behavior for the current risk, such as old objects, another entry point, repeated operations, mixed versions, or a lost acknowledgment. Every review does not need to audit every risk category. Distinguish static reading, simulated checks, and results from the actual environment; do not expand one type of evidence into a different guarantee.

## Produce one sufficient conclusion

In an existing record, identify the exact object, applicable baseline, coverage, conclusion, grounds for any block, and important unverified matters. Retain a way to identify the reviewer for independent reviews. Content identifiers or hashes identify an object; they do not by themselves establish correct behavior.

Separate blocking issues from non-blocking suggestions. Preferences for directories, patterns, or style do not make one of several reasonable implementations uniquely correct. After a correction, review the original issue and its necessary impact. Reuse valid results when the object has not changed and there is no new failure or contradictory evidence; a small change does not always need a new full review report.

## Respect deliverable and authorization boundaries

When prior review is required or an existing review is reused, verify before execution that the actual object corresponds to the reviewed object. Recheck only the affected portions when behavior or risk changes. Verifiable source-to-artifact correspondence can account for byte differences caused by packaging or signing.

If the project requires a prior pass and it has not been obtained, do not overwrite running content, migrate production data, or activate that new change. Authorized, independent preparation that does not change the running instance may continue. An explicitly agreed review after execution should retain the actual object and correction records; a template update must not introduce a new prior-review gate.

A review pass answers the corresponding review questions. It does not grant permission to deploy, interrupt services, recover, roll back, or perform other operations. Actions that do not need code review still follow authorization and prerequisite requirements without seeking a formal pass merely for its own sake.
