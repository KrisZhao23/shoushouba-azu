# Implementation Judgment as Needed: Inputs, Authorization, State Changes, and External Effects

[English](07-implementation-boundaries.md) | [简体中文](07-implementation-boundaries.zh-CN.md)

Purpose: when an actual change involves one of the relationships below, read the relevant section directly. This is not a checklist to complete section by section for every task, nor a requirement to write four separate reports. General tradeoffs are covered in [01](01-judgment.md); impact tracing and stopping criteria are in [02](02-impact-and-evidence.md).

The following are conditional engineering recommendations proposed by this candidate. Where a source is cited, it supports the specific fact at issue; a framework's behavior is not generalized into a guarantee for every system. Sources and versions are listed under [Technical Sources](06-case-evidence.md#technical-sources). Important new facts may justify narrowing, changing, or abandoning a recommendation.

<a id="topic-a"></a>

## A. External Representations, Hidden Inputs, and Resource Lifecycles

### A1. First distinguish a change in encoding from a change in meaning

For an interface, file, message, or dependency upgrade, compare object identity, units, null values, dates versus instants, defaults, and failure meanings as well as field names and types. Do not interchange `0`, an empty string, a missing field, and "not yet obtained" without a basis. A string remaining parseable does not establish that it still represents the same fact. Dimensions with no evidence of change need not be examined one by one.

When only representation changes and meaning is demonstrably preserved, let existing parsing and validation absorb the change and give rules data whose meaning has already been established; a clear local function may be enough. Reject errors where they can be explained, or move to an explicit unknown state. Do not disguise invalid input as success with a default value.

If the identifier namespace, quantity unit, time convention, or failure meaning changes, trace rules, identity associations, relevant consumers, and existing data instead of merely adding a field alias. Use appropriate semantics for date-only facts and exact instants. Specify a timezone and conversion rule only when the business actually requires conversion; do not unconditionally turn every date into a UTC instant.

Business rules need not repeatedly validate a format already guaranteed by a trusted boundary, and external entry points may still need defensive validation. Judge whether the boundary is appropriate by whether a representation change forces unrelated rules to understand source details, not by whether a `parser` or `adapter` directory exists.

### A2. Put context that affects a decision where it can be identified

If the same explicit inputs yield different results because time, user, environment, randomness, or a global connection differs, locate those real inputs first. A rule that can be computed independently should not secretly choose "today," the current principal, or a configuration version, leaving its caller unable to explain the basis of the calculation.

An entry point can obtain the needed date, identity, or configuration once and provide explicit values to the relevant calculation. If execution genuinely needs changing time or another capability, provide a narrowly scoped capability rather than pretending it is a fixed value. Business meaning determines whether to use a snapshot or a live read: a historical report's comparison date is not the same kind of input as a request's remaining timeout. Do not mechanically put every global object in an unbounded `context`, or require every internal function to forward every parameter.

Framework-managed request context can support entry-point orchestration. Know when it is available, who manages it, and whether it will be used across requests or in background tasks. Flask 3.1.x documentation describes a locally scoped request context; accessing its proxies outside that scope fails [T1]. The engineering recommendation drawn from this is to avoid treating request proxies as lasting business facts or as authorization delegated to background work. Make the values, identity basis, and resources needed in the background explicit. Do not infer that every framework uses the same context mechanism.

If importing a module sends requests, writes files, starts tasks, or requires a hidden initialization call to work correctly, make that condition and its ownership recognizable. Prefer existing startup and shutdown entry points, or establish necessary capabilities where their composition can be inspected. Do not hide retries, business writes, or credential reads behind "just import it." Framework declaration registration and constant initialization without external effects are not automatically defects merely because they occur during import.

### A3. Creating, borrowing, handing over, and releasing are different responsibilities

A function that creates a resource, borrows a framework resource, or borrows from a shared pool may have different closing responsibilities. Make its lifetime, reuse conditions, and state after failure clear. A borrower should not close an entire shared pool on its own, and a creator must not release a resource immediately after handing it to an asynchronous consumer.

On exceptions, timeouts, cancellation, or partial initialization failure, check who cleans up resources already obtained, how still-running child tasks are observed or ended, and how cleanup failures are reported. Do not turn cancellation into success with broad exception handling, or claim that cleanup always restores everything after a process crash or at a remote system. Python 3.11's `asyncio` documentation recommends `try/finally` for cleanup and generally propagating cancellation after cleanup when explicitly caught [T2]. Other runtimes require checking their own lifecycle mechanisms.

Useful local checks might pass the same fact with two different dates, invoke a rule without request context, fail acquisition of a second resource after obtaining the first, or cancel a call while a consumer is still waiting. Select one or two relevant to this change. Once the relevant boundaries are explicitly preserved and unchanged consumers still receive valid inputs, apply the stopping criteria in [02](02-impact-and-evidence.md); do not expand into a repository-wide lifecycle audit.

Retain input conventions that affect behavior, initialization prerequisites, and resource ownership. There is no need to register every `with` statement or parameter. See the [single-file example](../examples/single-file-tool.md#code-example) for short code.

<a id="topic-b"></a>

## B. Authorization Follows Outputs and Actual Effects

### B1. Distinguish who requests, who executes, who interprets permissions, and what is affected

When a requirement involves switching principals, shared copies, exports, search, caching, pushes, or background actions, distinguish the current requesting principal, the actual executing principal, the trusted authority that interprets permissions, and the object, tenant, field, and action scope. These roles may overlap, but passing a `user_id` alone does not establish valid delegation.

Successful authentication confirms an identity; it does not automatically grant permission to act on every object. OWASP's authorization guidance calls for checking the relevant permissions on requests [T3]. This candidate therefore recommends tracing authorization along actual data-output and effect paths: permission to read does not automatically establish permission to aggregate, export, push to another person, or execute later.

Background tasks should rely on explicit service permissions or business delegation with a clear scope and validity. Do not conflate the two. A service account's technical ability to read everything is not a basis for returning everything to every requester. Principal and delegation information received across a boundary needs a trusted origin. Task records must not store tokens or secrets.

### B2. Check intermediate results and delivery paths that change visibility

Local copies, aggregates, search indexes, export files, notification bodies, error messages, and logs can all become new read entry points. Judge whether a result exposes previously invisible objects, details, or inferable information against the actual publication policy, rather than checking only the original page's query.

Caches need not always be duplicated per user ID; principals that genuinely share the same visibility scope can share results. Explain which scope constrains the cached content, how use obtains the correctly authorized view, and how changes to principal or object permissions stop reuse of results that are no longer permitted. An expiry duration alone does not establish immediate revocation. Conversely, a policy that explicitly permits delay does not require zero-delay invalidation.

RFC 9111 §3.5 specifies restrictions and exceptions for reusing shared HTTP-cache responses to requests with Authorization [T4]. It is not a complete permission design for application caches. Applications still need to check their own scope isolation, invalidation, queries, and delivery; copying an HTTP header does not settle those questions.

When tasks queue or results remain downloadable, make clear which policy establishes authorization at reading, execution, or delivery. Actions that require current permission should check current permission. If issued business delegation may continue, define its objects, content, duration, and revocation rules. Do not unconditionally repeat the same permission query at every stage, or assume that a single submission-time check remains valid forever. Exact guarantees under concurrent revocation depend on whether the executor can coordinate the decision with the effect. Checking at the entry point before writing does not automatically eliminate the race window.

### B3. Preserve exceptions without turning them into bypasses

An aggregate with an independent, accepted publication policy may have visibility rules different from its source details. Explain its intended audience and constraints against leakage; aggregation alone does not make data public. For an offline copy lawfully delivered outside the system's control, do not promise immediate retrieval through server-side revocation. Distinguish controls on future access from the fact that delivery has already happened.

Reuse existing trusted authorization mechanisms and close gaps in actual paths; this section does not require adding a new permission platform. A useful check might have two principals with different scopes hit the same query or cache, or change permission between queuing and delivery. Assertions should cover visible content and actual actions, not merely a hidden button or a 200 response.

Add the authorization authority, scope and check timing, necessary cache or delegation limits, and verified entry points to the project ledger. Link to the actual policy code and configuration rather than manually copying the entire permission matrix.

<a id="topic-c"></a>

## C. Incremental Updates, Revocation, Replay, and Relationship Corrections

### C1. Establish what the message or query actually claims

A complete snapshot of one object is not a complete snapshot of a collection; a page of query results is even less evidence of all objects. An update message may mean full replacement, a partial field patch, a quantity increment or decrement, or a business command. Their handling is not interchangeable. Whether a missing field preserves an old value or an explicit null clears it depends on the actual contract.

"Not seen this time" can support deletion or removal from a collection only when the authoritative source, scope, completeness, and consistency boundary are established. Unfinished pagination, changed filters, reduced permissions, partial failures, and time windows can all cause absence. Losing visibility permission may require hiding an object or removing a copy one is no longer authorized to retain; it must not fabricate deletion of the source object or unilaterally undo its business contribution.

### C2. Identity, deduplication, and ordering provide different evidence

Distinguish object identity, event or revision identity, and business-operation identity. The same object can change legitimately multiple times, while one event can be delivered more than once. Define the object, partition, or source within which versions are comparable. Receipt time, local time, and source time do not automatically establish a reliable total order. Do not arbitrarily convert opaque versions to integers for comparison.

A newer complete object snapshot may replace an older snapshot if the source guarantees that versions are comparable and the newer state supersedes the old. An incremental update may not allow skipping intermediate versions. Receiving "add another 2" first does not establish that an earlier "add 3" is included. Use the source's ordering, idempotency, or commutativity guarantees. Without them, possible responses include querying the object, reconciling the affected scope, buffering pending verification, or refusing unsafe progress; the largest timestamp alone does not solve the problem.

Duplicate and out-of-order deliveries are real interface conditions, but sources do not all require the same handling. PostgreSQL 17 documentation states that logical decoding may resend recent changes after crash recovery [T5]. Stripe webhook documentation does not guarantee delivery in event-generation order; event timestamps alone do not provide deduplication and ordering [T6]. Check each actual protocol rather than imposing PostgreSQL's position mechanism on ordinary HTTP messages.

If deduplication records and business contributions commit separately, a retry window may leave an event marked processed without its update, or updated without being marked processed. Use an existing transaction when it can coordinate them. Otherwise, provide a recoverable intermediate state or a way to verify the outcome. A set of processed IDs alone does not establish that the complete effect occurs exactly once.

### C3. Revocation and reassignment must account for existing contributions

Revocation, deletion, correction, and a new compensating business action are not synonyms. Identify which fact, relationship, or contribution is being withdrawn before choosing recalculation, replacement, subtraction, or a new action. A late old message must not "resurrect" an object whose revocation is confirmed. Comparable versions or deletion markers are one option, but only under a suitable protocol and retention scope.

Suppose a contribution moves from A to B. If a projection stores totals by owner, explain how A's old contribution is removed, how B's new contribution is added, and whether readers of the totals may see intermediate state. Changing an object's `owner` alone is not sufficient. Nor must every model perform two manual arithmetic updates: querying authoritative detail or recalculating a bounded scope may be more appropriate.

If the old ownership or contribution is unavailable, do not invent a delta. Use existing detail, query the source, or recalculate the relevant A/B scope. Relevant actual consumers may include filters, aggregates, caches, and search; do not overlook them because they are absent from the list of changed files.

### C4. Rebuilding derived results is not the same as repeating business actions

Rebuilding an index, cache, or projection requires interpreting existing facts again. It should not inadvertently resend email, charge money, create external documents, or start business tasks. Make derived computation and initiation of effects distinguishable responsibilities. When a notification really needs retrying or an action needs completing, handle that as a separate, authorized intent rather than an implicit side effect of replay.

Restoring historical facts under old rules and recalculating them under current rules serve different purposes; state which meaning the result has. Replay progress is only a processing position. It does not automatically establish data completeness, valid authorization, or consistent external effects.

Select short sequences relevant to this change, such as "repeat the same event," "receive the later version first," "a page is missing," "receive an old revision after reassignment," or "rebuild results without increasing the number of sends." State the expected final contribution and necessary visible states before checking the implementation. Projects without relevant incremental or replay behavior do not need event sourcing, a general replay platform, or full scans.

Retain the input contract, identity and ordering guarantees, meaning of absence, contribution updates, effect boundaries, evidence, and unknowns. Do not maintain a second event database.

<a id="topic-d"></a>

## D. External Effects and Existing Work: Binding Confirmation and Preserving Partial Outcomes

[01 §6](01-judgment.md) already distinguishes local records, requests, remote effects, and receipts; covers timeout and cancellation limits; and describes basic choices for compensation and existing objects. [02 §7](02-impact-and-evidence.md) already explains why a code snapshot is not business recovery. This section adds relationships that change implementation choices, not another migration process.

### D1. What executes must stay within the scope actually confirmed

When content can be edited after confirmation, executed later, or changed concurrently, identify what confirmation applies to: fixed content, an object version, a numeric range, or a policy that permits dynamic evaluation. Where content must be bound to confirmation, use an existing stable version, snapshot, or verifiable content identifier. Saving only an object ID and later reading its latest value may exceed the confirmed scope.

Changes within an accepted range may proceed under the agreement. If a change alters the confirmed target, amount, recipient, object scope, or other important meaning, obtain the relevant confirmation again or reject the stale action. Do not mechanically require new approval for unrelated presentation changes, or use "the user once clicked the button" to justify every later change.

A version or digest identifies confirmed content; it is not authorization, a lock, or atomicity. The actual updater needs to provide corresponding conditional checks or coordination. Reading a version and then writing unconditionally still leaves a race window. RFC 9110 §13.1.1 defines If-Match as one concrete HTTP conditional-request mechanism [T7]; not every system supports it, and it cannot protect every business constraint.

### D2. Preserve unknown, partial, and canceled outcomes at sufficient granularity

In a batch, items confirmed effective, items definitely not executed, and items with unknown outcomes must not all be collapsed into "failed." During recovery, use those facts and the remote system's capabilities to retry only the same intent where it is safe. Do not rerun an entire batch without a basis. Unknown items generally require querying or reconciliation. If the remote system is verified to support idempotent retries within the current scope and validity period, recovery can instead use the original intent and identifier. Do not mechanically require obtaining the original result before every retry. If neither capability is sufficient, retain pending verification rather than blindly repeating the action. The remote side may complete after local waiting is canceled; a successor should be able to find the original operation and its actual result, rather than inferring "never done" from a fresh local conversation.

A local operation ID only assists correlation. Remote deduplication also requires checking the key's scope and validity period, same-input constraints, concurrency and failure handling, and what a repeated request returns. Do not reuse an old key to disguise a changed intent as the same request, or use a new key to blindly repeat an operation with an unknown outcome. RFC 9110 §9.2.2 places conditions on automatic retries of non-idempotent requests [T7]. Additional idempotency capabilities of a specific interface require separate verification; neither a function name nor an HTTP method establishes all business effects.

### D3. A documented plan does not authorize handling existing objects or performing recovery

When old data, old messages, or in-flight tasks lack new semantics, choose according to actual needs: continue with old semantics, provide explicit compatibility, perform bounded migration or recalculation, or safely reject. Do not default an unknown version to the newest one. Compatibility exit conditions depend on actual consumers and in-flight work. Do not assume compatibility must last forever or require a platform for handling existing state on an unrelated small change.

Code rollback changes the code being executed. Data restoration returns data to a state and may overwrite later legitimate changes. Business compensation is a new action that can itself fail. A forward fix preserves history and corrects the current situation. Explain their distinct conditions and risks; they are not interchangeable. Writing a recovery or compensation plan does not authorize execution, automatic resending, production restoration, or calls to external systems.

Checks may cover relevant cases such as content changing after confirmation, lost receipts for part of a batch, or an old task lacking a new field. For continuation, retain only non-secret operation and object correlations, known outcomes, unknown scope, and the safe next step. Link existing evidence where needed rather than adding a complete operation log.
