# Engineering judgment: let the conditions change the choice

[English](01-judgment.md) | [简体中文](01-judgment.zh-CN.md)

Purpose: read this when designing, refactoring, preparing a plan, or discovering a change in responsibilities or shared meaning. It explains reasoning relationships; it does not require the same form to be filled out for every task. Evidence sources and limits are in the [case notes](06-case-evidence.md).

## 1. Build the overall structure around observable commitments

First establish who needs what result, when that result counts as achieved, and what must not be broken. Distinguish the facts produced, decisions made, and external effects caused along the way, then find the existing places responsible for them. What matters is not just the number of modules: necessary obligations must be covered, without multiple uncoordinated interpretations.

A feature inventory describes what a system has; responsibilities explain why a part owns something; behavior paths explain how parts cooperate; runtime and failure relationships explain whether those arrangements hold in the real environment. These are different views and cannot substitute for one another. You do not need to draw them all, but should be able to explain the relevant relationships when a decision depends on them.

Start with two or three discriminating scenarios to challenge a proposed structure, such as normal completion, a change to one key assumption, and a real failure. This is not an attempt to enumerate the future. The purpose is to determine whether the proposed combination of responsibilities can deliver the behavior currently accepted. When something is missing, revisit responsibilities or contracts instead of merely appending exception conditions.

SQLite's architecture and pager invariants can help investigate how external guarantees become obligations across layers; they do not imply that every project should use the same layers. Git's sparse index can help investigate how a shared representation change affects existing consumers; it does not imply that every change needs a compatibility layer.

## 2. Distinguish the kind of change before choosing a boundary

When an external field name changes but its business meaning stays the same, absorb the change where the external representation is interpreted. Check that object identity, null values, units, time zones, defaults, and failure semantics really remain unchanged. One clear conversion function may be enough; this does not justify a family of factories and interfaces.

When business meaning changes, reassess the rules, state consumers, and interpretation of existing data. Field mapping alone cannot establish that adaptation is complete. The same number may now represent a different lifecycle.

When the runtime environment or a dependency version changes, check the actual combination. The issue may be a deprecated argument, a configuration change, or a startup path; it does not necessarily call for redesigning the architecture. Starlette's fix removing a deprecated argument is a useful counterexample to overdesign.

When resource or failure semantics change, moving from synchronous to asynchronous work, or from local calculation to a remote call, changes more than a function signature. Reassess cancellation, timeouts, retries, transactions, and lifecycles according to their actual semantics.

For identifying external representations, hidden inputs, import-time side effects, and lifecycles, see [07·A](07-implementation-boundaries.md#topic-a). This does not mean adding parameters to every function or a layer for every source.

## 3. When cohesion and independent change pull in different directions

Protecting a shared invariant does not automatically require all of its implementation to live in one file. Clear transactions, version correspondence, or cooperation contracts can preserve the relationship. Someone must still own the final decision, coordination, or conflict resolution; the invariant cannot be left without an owner.

Frequent changes together do not automatically establish a shared responsibility. Shared requirements, generated files, formatting, organizational divisions, and historical coupling can all cause files to change together. Investigate the reasons for change and the knowledge shared, rather than merely counting commits.

To decide whether a split is worthwhile, ask where the pressure for independent change comes from, which part would no longer need to understand the other, and how much the cost of combining them would grow. Passing the same hidden state through more functions does not deliver the intended benefit of a split.

To decide whether a merge is worthwhile, ask whether the separate parts merely forward calls to each other, require coordinated edits for every change, and have no independent contract or resource reason to remain separate. Abstractions that protect nothing may be removed. Merging must not conflate external representations, business policy, and authorization meaning again.

## 4. Consistent rules do not require one function; state ownership does not require one process

A policy needs an identifiable basis for interpretation and a way to maintain consistency. Different entry points may reuse a function, call the same service, be generated from the same rule, or use independent implementations whose consistency is checked. Repeated validation across trust boundaries may be necessary. The key questions are whether the policy is evolving independently, which changes require coordination, and who is responsible for resolving inconsistencies.

The same state may have multiple legitimate writers, provided their permissions, conditions, and conflict handling are explicit. Distinguish authoritative facts, requests, suggestions, confirmations, caches, and display projections. A single "complete" field must not be assumed to represent every lifecycle.

If a consumer uses a cache to decide a business action, establish the cache's freshness and authority boundaries. If the cache is only for display, still check whether it presents an incorrect commitment to the user. Calling something "just the frontend" does not remove the need to assess its meaning.

## 5. Resolve complexity tradeoffs with facts

| Tradeoff | Facts that change the choice | Avoid at either extreme |
|---|---|---|
| Merge or separate | Whether the parts protect the same invariant; whether independent change is real; coordination and navigation costs | Merging everything with the same name, or adding layers just because a file is long |
| Reuse or duplicate | Whether it is the same policy; whether a trust boundary is crossed; whether meaning can be kept in sync reliably | Extracting all similar code, or letting every entry point interpret policy independently |
| Preserve the old contract or migrate together | Whether old consumers and data exist; whether they can switch together; the duration and cost of compatibility | Keeping compatibility forever by default, or forcing everyone to upgrade after any change |
| Retry or check the outcome first | Whether the operation is repeatable; whether the other system recognizes a stable operation identity; whether its effect can be queried | Repeating immediately after a timeout, or stopping permanently after every timeout |
| Design more now or defer | Known constraints, near-term evidence, irreversible consequences, replacement and verification costs | Optimizing only for fewer changed lines, or building a platform for speculation |
| Investigate further or stop expanding | Whether neighboring contracts hold; whether key counterexamples have been addressed; what consequences the unknowns could have | Stopping because parameters are unchanged, or demanding proof that the entire system is unaffected |

This table is not a scoring system. A choice must rest on current facts and the differences between alternatives. When evidence is insufficient, reversible exploration may be appropriate, or explain why it is still insufficient for a costly decision.

## 6. External effects, authorization, and long-lived work are conditional topics

When real external effects are involved, distinguish the local decision, request initiation, delivery, the other system's effect, its response, and final confirmation. If that system supports neither deduplication nor querying the effect, a local operation ID helps correlation but cannot prevent duplicate effects. Compensation is another action and may fail. Cancelling a local wait does not cancel the remote operation.

When identity, caching, exports, push delivery, or background actions are involved, trace authorization through data outputs and actual effects. Reusing a trusted policy does not justify silently turning the current user into global state. Background actions need an explicit execution identity of their own. Source-system authorization or a simulated role must not be treated as a production guarantee without verification.

When existing data, old protocols, or in-flight tasks are affected, decide whether old objects retain their old meaning, are migrated, are recalculated, or are rejected, and explain how to establish their state after an interruption. Do not impose a migration platform on a small change with no such objects.

Expand as needed: [authorization across outputs and effects](07-implementation-boundaries.md#topic-b), [incremental changes, reversals, relationship corrections, and replay](07-implementation-boundaries.md#topic-c), and [confirmed content, external effects, and existing work](07-implementation-boundaries.md#topic-d). These are conditional engineering recommendations, not a claim that Git or any one project proves the whole method.

## 7. A plan does not precisely predict every implementation detail

First establish commitments that others can build on, while keeping internal implementation adjustable. The level of detail should vary with uncertainty and risk: investigate unknown resource capabilities, align on known shared contracts, and allow reversible internal organization to evolve during implementation.

Everyone proposing a plan should be able to explain how the task fits into the overall result, rather than copy a generic "impact assessment." A useful understanding of the whole shows up in identifying relevant producers and consumers, protecting shared invariants, and setting sensible limits on scope.

Discovering a new fact does not by itself mean the original plan failed. Equally, "plans can change" must not excuse ignoring an important constraint that was already known.

## 8. How a judgment can be overturned

Keep a checkable expectation for an important choice, such as "external representation changes should stay mainly in the conversion point," "ordinary consumers should retain the meaning of the old path," or "allowing edits should not change content already approved for publication." If later changes repeatedly break the expectation, revisit whether the original assessment of the conditions was wrong.

Do not infer reasons for the initial design from the final directory structure. Separate researchers' inferences from maintainers' own statements; retain uncertainty when several explanations are possible. A method can be revised, made more specific, or removed, rather than protected by continually adding exceptions.
