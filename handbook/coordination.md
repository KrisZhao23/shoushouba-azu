# Coordination handbook

[English](coordination.md) | [简体中文](coordination.zh-CN.md)

Use this handbook when work requires coordinating multiple tasks, participants, or shared resources. One person may coordinate and execute; the [review handbook](review.md) and project agreements determine whether independent review is needed. For general judgment, see the [main Skill](../skills/clear-engineering/SKILL.md); for planning and continuation, see [reference 04](../skills/clear-engineering/references/04-planning-review-and-handoff.md).

## Organize work around the current outcome

Establish the current goal, accepted sequence, authorization, and stopping point. Distinguish completed, independent, and dependent work. Establish prerequisites and verification methods before an operation; obtain its result evidence afterward.

When assigning work, provide the required outcome, scope, necessary evidence, available resources, and stopping boundaries. Reuse existing tasks and understanding when they still apply. Participants must be able to access the relevant basis for the work; do not assume other chats, tools, or services inherit the local context.

For changes across boundaries, link the relevant implementation explanations and identify who updates the affected relationships. Use [reference 03, section 3](../skills/clear-engineering/references/03-ledger-and-timeline.md#implementation-map) instead of copying them into each assignment.

Choose roles and tools for actual needs. Creating chats, parallel work, or replacing participants follows the environment's rules and user authorization.

## Assess dependencies and resources separately

Identify the outcome owner and available resources. Assign a clear operator for each shared mutable resource at any given time; availability or a role change does not automatically confer access.

Run work in parallel only when it is authorized, has independent resources, and can preserve its results. A critical unknown limits only the actions that depend on it; safe, independent investigation and preparation can continue. If supporting work keeps displacing the current goal, reassess whether it is necessary.

For external effects or interruption, verify the target, actual writers, and authorization; complete preparation that needs no interruption first. Consistency may require quiescing actual writers, but an update does not authorize stopping all services.

## Scheduled checks and handoff

When assigning work, agree on the recipient, follow-up owner, and check-in time. The sender is responsible for arranging receipt follow-up: confirm an existing reminder covers this delivery's valid acknowledgment and names its follow-up owner; otherwise create one. Claim background follow-up only after confirmation; if tooling is unavailable, state the limitation and arrange workable continuation. Report early completion, blockers, or decision needs immediately. Once arranged, leave instead of polling online.

Root (the overall coordinator) first updates the existing pending item with a brief disposition: next action, owner, and time or triggering event. Then acknowledge with that arrangement or its link; "received" alone is insufficient. Deferral needs a reason and resumption condition. Without a valid acknowledgment, the designated follow-up owner checks current status when due, reminds the recipient, and reschedules until acknowledged or explicitly paused or canceled by the user. Persistent silence calls for investigating the cause and who can take over; mark an unknown cause as unknown. Notifying the user alone does not end follow-up, and already executed business actions must not be repeated.

After a valid acknowledgment, end receipt tracking; retain a shared reminder if other follow-up remains, otherwise close it. Root follows the work through. Apply this to deliverables needing receipt or handoff, not every message, and never require acknowledgment of an acknowledgment. Receipt does not replace review approval or operational authorization.

Assignments and acknowledgments reference the [current report and evidence](../skills/clear-engineering/references/03-ledger-and-timeline.md#frozen-audit-records), adding only the actions, changes, and continuation arrangements for this step. Root's existing pending item holds only the current arrangement and references the current report. The coordination entry point holds current people, resources, authorizations, and record references, without copying results or evidence. Reminders reference the pending item; adjust them only when the recipient, follow-up owner, check time, or continuation state, such as completion or blockage, changes. See [maintenance triggers in reference 03](../skills/clear-engineering/references/03-ledger-and-timeline.md#record-updates).

## Know when to stop

Executors verify execution results, reviewers form independent judgments, and Root coordinates from them. Without a new failure, changed object, or contradiction, do not repeat checks at the same level or ask participants to copy facts into multiple records. Once the goal is met with sufficient direct evidence, deliver and stop; arrange handoff as above.
