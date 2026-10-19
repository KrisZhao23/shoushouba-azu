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

When assigning work, agree on the recipient and check-in time, and actually schedule the reminder. Report early completion, blockers, or decision needs immediately. Once the sender has scheduled an acknowledgment check, they can leave instead of polling online. Claim background follow-up only after scheduling succeeds; if tooling is unavailable, state the limitation and arrange a workable continuation.

Root (the overall coordinator) first updates the existing pending item with a brief disposition: next action, owner, and time or triggering event. Then acknowledge with that arrangement or its link; "received" alone is insufficient. Deferral needs a reason and resumption condition. Without a valid acknowledgment, the sender checks current status when due, reminds the recipient, and reschedules until acknowledged or explicitly paused or canceled by the user. Persistent silence calls for investigating the cause and who can take over; mark an unknown cause as unknown. Notifying the user alone does not end follow-up, and already executed business actions must not be repeated.

After a valid acknowledgment, the sender closes its reminder; Root follows the work through. Reuse, update, or close the relevant reminder instead of stacking reminders. Apply this to deliverables needing receipt or handoff, not every message, and never require acknowledgment of an acknowledgment. Receipt does not replace review approval or operational authorization.

Keep pending items brief and current: replace outdated content, and remove finished items. Link original evidence. Keep useful facts and key reasoning turns that locate mistakes in the ledger; delete useless wrong directions, expired conditions, duplicate explanations, and routine logs. Non-repeatable actions and external effects with unknown outcomes must remain visible. See [reference 03](../skills/clear-engineering/references/03-ledger-and-timeline.md) for record selection.

## Know when to stop

Complete the checks belonging to each responsibility. Once the goal is met and sufficient direct evidence exists, deliver and stop; arrange any handoff under the section above. Without a new failure, changed object, or contradictory evidence, do not repeat verification.
