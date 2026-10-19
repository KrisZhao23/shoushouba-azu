# Execution handbook

[English](execution.md) | [简体中文](execution.zh-CN.md)

Use this handbook for design, coding, debugging, tool operations, and the project's existing delivery and recovery work. Follow the actual environment's authorization boundaries and project agreements first; see the [main Skill](../skills/clear-engineering/SKILL.md) for the general method. Use the [review handbook](review.md) when review is needed and the [coordination handbook](coordination.md) for work involving multiple participants.

## Trace the real entry point to the smallest complete change

Establish the current goal, the relevant overall understanding, and the task's current checkpoint. Then trace the entry point to the implementation, the source of state, and the actual consumers. Reuse known relationships that still apply and add only what this change requires. Identify the key facts, constraints, and places where changes belong; use existing capabilities when they are sufficient.

The executor may decide how to organize local, reversible implementation details that preserve shared meaning. When changing shared interfaces, state interpretation, authorization, resource lifecycles, or external effects, make the differences visible to the affected participants and adjust the relevant plans and verification.

If a new script, wrapper, or abstraction is needed, identify the specific gap in the existing mechanism. A need to preserve results in a record does not automatically require generating code to perform an ordinary operation.

## Separate prerequisites from results

Before an operation, verify the actual target, permissions, inputs, relevant versions, and failure boundaries, and establish how the result will be observed. Obtain health, page behavior, and runtime facts after startup. Even when code uses a shared loading entry point, check whether each input is genuinely a dependency of the current step.

When a prerequisite is missing, identify the specific error this step could cause and stop only the hazardous actions actually affected. Safe, independent local investigation or preparation may continue; an insufficient operational time window does not automatically suspend all work.

## Deliver through the project's actual mechanism

The project determines the delivery mechanism: build artifacts, a platform release, controlled file updates, or another existing method. Identify the exact target and applicable version, preserving the current environment's configuration, business data, and unrelated changes.

When review is required or an existing review conclusion is reused, ensure the actual deliverable matches the reviewed object. If the project requires prior review and it has not been obtained, do not activate that new change. Authorized, independent preparation that does not change the running instance can still proceed. See the [review handbook](review.md) for the full boundaries.

Order preparation, any necessary quiescence, release, startup, and acceptance checks according to actual dependencies. Whether a backup requires quiescence depends on consistency needs and the writers involved; service interruption must be within the authorized scope. Instructions sent to an external executor must be self-contained and cannot depend on local files or conversations that executor cannot see.

Verify instruction dispatch, receipt, actual execution, the effect taking place, and the result acknowledgment separately. A designated owner follows up with downstream executors; other participants avoid sending competing instructions. Use available feedback events or checkpoints instead of repeatedly polling unchanged state.

## Handle failure, uncertainty, and recovery

After a failure, first preserve the actual state, affected objects, and portions whose outcomes remain unknown, and stop extending the impact. A timeout does not prove an external action did not happen. Retry safety depends on the operation's semantics and the other system's guarantees; a local identifier alone does not establish it.

When the recovery goal is clear and an appropriate mechanism already exists, verify its actual version, parameters, and side effects, then reuse it. Do not automatically turn recovery into delivery of a new script. If a new hazardous change is still needed, address its risks and review under the project's rules.

Reverting code, restoring data, and undoing external effects are different actions. Clarify authorization for each, follow any additional project requirements for rollback or irreversible operations, and do not infer permission for every recovery method from an instruction to continue fixing the problem.

## Verify and enable continuation

Verify the behavior that should change and the behavior that must remain unchanged. Check actual consumers' formats, defaults, combined conditions, and state meanings. Tests need precise expectations; comparing two entry points with each other can pass when both are wrong.

Preserve necessary implementation locations, keywords, actual checks, and results in the task's existing documentation, and reference that record elsewhere. Distinguish proposals, implementation, verified results, effects in force, and unconfirmed matters. Do not create a separate document for every role or ordinary edit.

Once sufficient evidence supports the current commitment, deliver and stop. If work is incomplete, leave the next entry point, the actual owner, and actions that must not be repeated. Do not promise background continuation unless it has been arranged.
