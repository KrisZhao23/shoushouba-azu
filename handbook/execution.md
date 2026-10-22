# Execution handbook

[English](execution.md) | [简体中文](execution.zh-CN.md)

Use this handbook for design, coding, debugging, tool operations, and the project's existing delivery and recovery work. Follow the actual environment's authorization boundaries and project agreements first; see the [main Skill](../skills/clear-engineering/SKILL.md) for the general method. Use the [review handbook](review.md) when review is needed.

## Trace the real entry point to the smallest complete change

Establish the current goal, relevant overall understanding, and task checkpoint. Trace the entry point to the implementation, source of state, and actual consumers. Reuse the plan's valid explanations of purpose, dependencies, and constraints; add only actual differences and implementation locations. Use sufficient existing capabilities.

The executor may decide how to organize local, reversible implementation details that preserve shared meaning. When changing shared interfaces, state interpretation, authorization, resource lifecycles, or external effects, make the differences visible to the affected participants and adjust the relevant plans and verification.

A new script, wrapper, or abstraction must fill a specific gap in existing capabilities; recordkeeping alone does not justify generating code.

## Separate prerequisites from results

Before an operation, verify the actual target, permissions, inputs, relevant versions, and failure boundaries, and establish how the result will be observed. Obtain health, page behavior, and runtime facts after startup. Even when code uses a shared loading entry point, check whether each input is genuinely a dependency of the current step.

When a prerequisite is missing, identify the specific error this step could cause and stop only the hazardous actions actually affected. Safe, independent local investigation or preparation may continue; an insufficient operational time window does not automatically suspend all work.

## Deliver through the project's actual mechanism

Use the project's existing delivery mechanism. Reference the original exact manifest for objects, versions, and content identifiers rather than copying full hash and size tables. If no manifest exists, identify the objects sufficiently in an existing record. Preserve the environment's configuration, business data, and unrelated changes.

When review is required or an existing review conclusion is reused, ensure the actual deliverable matches the reviewed object. If the project requires prior review and it has not been obtained, do not activate that new change. Authorized, independent preparation that does not change the running instance can still proceed. See the [review handbook](review.md) for the full boundaries.

Order preparation, necessary quiescence, release, startup, and acceptance checks by actual dependencies. Backup quiescence depends on consistency needs and active writers; service interruption requires authorization. External instructions must state this operation's actions and conditions, with references the recipient can read.

Verify dispatch, receipt, execution, and actual effect separately. A designated owner follows downstream work; avoid competing instructions. For reporting, valid acknowledgment, and scheduled follow-up, use only [Scheduled checks and handoff](coordination.md#scheduled-checks-and-handoff); no need to read the whole coordination handbook.

## Handle failure, uncertainty, and recovery

After a failure, first preserve the actual state, affected objects, and portions whose outcomes remain unknown, and stop extending the impact. A timeout does not prove an external action did not happen. Retry safety depends on the operation's semantics and the other system's guarantees; a local identifier alone does not establish it.

When the recovery goal is clear and an appropriate mechanism already exists, verify its actual version, parameters, and side effects, then reuse it. Do not automatically turn recovery into delivery of a new script. If a new hazardous change is still needed, address its risks and review under the project's rules.

Reverting code, restoring data, and undoing external effects are different actions. Clarify authorization for each, follow any additional project requirements for rollback or irreversible operations, and do not infer permission for every recovery method from an instruction to continue fixing the problem.

## Verify and enable continuation

Verify the behavior that should change and the behavior that must remain unchanged. Check actual consumers' formats, defaults, combined conditions, and state meanings. Tests need precise expectations; comparing two entry points with each other can pass when both are wrong.

Keep actual differences, valid conclusions, and important unknowns in the existing task record. Reference original test output; if the recipient has no stable readable source for it, first preserve enough original evidence to verify the result once in an existing record or evidence location. Correct missing, changed, or inaccurate implementation explanations at their source under [maintenance triggers in reference 03](../skills/clear-engineering/references/03-ledger-and-timeline.md#record-updates); reuse valid explanations and references instead of appending every round.

Once sufficient evidence supports the current commitment, deliver and stop. Link an existing pending item if available; do not wait for Root to update or create one before reporting. Root arranges continuation for unfinished work under the agreement above, identifying actions that must not be repeated.
