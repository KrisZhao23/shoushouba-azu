# Coordination handbook

[English](coordination.md) | [简体中文](coordination.zh-CN.md)

Use this handbook when work requires coordinating multiple tasks, participants, or shared resources. One person may coordinate and execute; the [review handbook](review.md) and project agreements determine whether independent review is needed. For general judgment, see the [main Skill](../skills/clear-engineering/SKILL.md); for planning and continuation, see [reference 04](../skills/clear-engineering/references/04-planning-review-and-handoff.md).

## Organize work around the current outcome

First establish the current goal, the sequence the user has accepted, the authorized scope, and the stopping point. Distinguish completed work, work that can proceed independently, and work that depends on other results. Separate prerequisites for an operation from acceptance results produced afterward; do not require evidence that can only exist after execution.

When assigning work, provide the required outcome, scope, necessary evidence, available resources, and stopping boundaries. Reuse existing tasks and understanding when they still apply. Participants must be able to access the relevant basis for the work; do not assume other chats, tools, or services inherit the local context.

Choose roles and tools to meet actual needs. Projects may configure their own models, execution methods, and resource budgets. These choices do not change the responsibilities or become a universally required combination. Creating new chats, parallel tasks, or replacing participants remains subject to the current environment and user authorization.

## Assess dependencies and resources separately

Establish who is actually responsible for an outcome, then who may use the corresponding files, state, processes, or release resources. An available participant does not automatically own another task's resources. Assign a clear operator for a shared mutable resource at any given time; a change of role does not automatically release that resource.

Run work in parallel only when it is authorized, has independent resources, and can preserve its results. A critical unknown limits only the actions that depend on it; safe, independent investigation and preparation can continue. If supporting work keeps displacing the current goal, reassess whether it is necessary.

For external effects or service interruptions, verify the target, the actual writers, and the authorized scope. Complete preparation that does not require interruption in advance wherever possible. Consistency may require quiescing the actual writers, but a need to update something does not by itself authorize stopping all services.

## Monitor observable progress

Agree on feedback events or reasonable checkpoints around the next meaningful result. Short conversations do not need precise timing; specify the timezone when work crosses timezones or sequence matters. If event waiting or reminders are unavailable, state that limitation and do not promise background supervision that has not been arranged.

Intervene when work completes, fails, is blocked, drifts from the goal, or needs a decision. Elapsed time alone does not establish that a task is out of control. There is no need to repeatedly read unchanged status, full histories, or raw logs.

Identify the cause of a blockage, then make the smallest effective adjustment. After repeated failures, reassess the goal, dependencies, capabilities, and scope while retaining valid results. Renaming tasks or extending checks indefinitely does not constitute progress. The user's pauses, stops, and permission boundaries remain in force.

## Preserve the current facts

Use the project's existing entry point or coordination checkpoint to record the current goal, actual owners, relevant resources, valid authorization, results obtained, and next step. Refer to the original task evidence rather than copying every implementation detail. One paragraph can suffice for a simple project.

When handing over responsibility, establish what the recipient has actually accepted; sending a message alone does not complete a handoff. An ordinary progress report does not automatically introduce an approval wait. External actions with unknown outcomes and operations that must not be repeated should be visible at the current checkpoint.

When context is insufficient, first fill in the records and differences relevant to the next step. If a different participant or work context is truly needed, follow the environment's handoff rules. Do not replace participants mechanically after a fixed number of exchanges.

## Know when to stop

The executor verifies the actual execution result; the reviewer performs the relevant review; the overall coordinator uses those results to manage scope, resources, and next steps. Without a new failure, a changed object, or contradictory evidence, do not repeat verification at the same level. Once the goal is met and sufficient direct evidence exists, deliver the result and stop.
