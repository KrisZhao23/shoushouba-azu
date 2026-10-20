# Project ledgers, timelines, and understanding others can continue from

[English](03-ledger-and-timeline.md) | [简体中文](03-ledger-and-timeline.zh-CN.md)

Maintain existing records as needed so readers can understand the current system and locate the turning point where reasoning or an approach went wrong. Records are not activity logs; do not create another file when the existing material suffices.

Research influences, authors, and licenses are in the [case and source notes](06-case-evidence.md#source-licenses). This repository's starters are organized separately; they do not include upstream projects' original ledgers or business records.

## 1. Put information where readers need it

| What needs to be understood? | What to record |
|---|---|
| How the current system works | Goals, responsibilities, cooperation, states and constraints, implementation entry points |
| Why a choice was made or changed | Key judgment, evidence that changed it, correction, and necessary evidence references |
| What needs doing now | Brief pending item: owner, next action, check time or trigger |
| How far a conclusion can be trusted | Actual source, applicable object, verification result, and unknowns |

Maintain each fact in one place and reference it elsewhere. These purposes may share a file; no fixed directory layout or set of documents is required.

## 2. Identify the project, create an entry point when needed, and bind it to the working context

A ledger belongs to a project maintained over time. New requests, contributors, conversations, test copies, or moves within that project use its existing entry point; copies state their baseline and differences. Consider a separate project only when its goal, boundaries, and maintenance responsibility are genuinely independent.

Check the designated entry point first, then relevant READMEs, descriptions, and references as needed. Reuse materials that already explain the whole and provide navigation. An inaccessible entry, insufficient permission, or conflicting entry points calls for checking accessible sources, then specific clarification if needed; it is not a reason to create a parallel ledger. Do not search the whole machine or repeatedly request known paths.

When an entry point is genuinely absent, continuity is needed, and writing is authorized, create a minimal truthful record, optionally named `PROJECT-LEDGER.md`. Include goals and scope, main cooperation, valid constraints, implementation entry points, necessary unknowns, and the pending-work location. State when implementation is absent; do not invent symbols or reconstruct unsupported history. Temporary questions do not automatically need a ledger; read-only investigations may still produce findings worth recording within authorization.

Designate one current engineering knowledge entry point per project, expanding it internally as needed. Explain shared platform capabilities where they belong and reference them elsewhere. The entry must explain the whole, not merely list files or require all history to be read first.

Register scope, ledger location, and the path base in an authorized working entry point that will actually be read. Creation, registration, and actual reading are separate facts; a trigger hidden inside an unread Skill does not establish adoption. Ledger-writing permission does not authorize changing AGENTS, startup rules, or permissions. When writing is restricted, identify the proposed content and location without claiming completion. See section 3 of [usage and evaluation](05-usage-and-evaluation.md) for loading checks.

<a id="implementation-map"></a>
## 3. Connect explanations to implementation and cooperation

For existing projects, fill gaps within the actual work scope and identify what remains unknown; do not make documentation of the whole repository a prerequisite for the current action.

The project ledger or existing explanations it links must document each distinct responsibility and behavior that crosses boundaries in writing. Organize by module, key function/interface, or end-to-end behavior so readers can find:

| Content | What must be explained |
|---|---|
| Implementation location | Actual file and function, class, interface, or registration symbol; add line ranges and the corresponding snapshot when useful, updating them when code moves. Line numbers aid navigation but cannot be the sole identifier. |
| Purpose summary | Why this part exists, what it receives and produces, and the responsibility it owns. |
| Dependencies and coupling | Who provides what and who consumes the result; who owns, reads, and writes shared state; shared constraints and required ordering. |
| Connections | The call, interface, event, table, or adapter connecting the parts; where data is translated, who guarantees which contract, and where side effects occur. |
| Change and verification | Which consumers or constraints a change affects, which behavior must remain intact, and where relevant tests or actual evidence live; identify unverified scope. |

Document hidden dependencies that actually exist, including environment or current-user reads, global or shared mutable state, import side effects, initialization/call ordering, and transaction or resource lifecycles. Name the objects and relationships rather than merely listing technologies; an unexamined relationship cannot be described as "no dependency."

A small project may cover this in one paragraph; related helpers may share an explanation rather than requiring a record per function or line. Link sufficient existing code comments or design notes. In a large project, explain overall relationships at the entry point and link the relevant details. Stop expanding when readers can locate the implementation, understand cooperation and impact, and find the basis for verification.

## 4. Distinguish kinds of claims

Separate proposals, accepted agreements, actual observations, runtime evidence, and unknowns. Acceptance needs content, scope, and a basis; silence is not acceptance, and design acceptance is not execution authorization. Visible source is not proof of execution. State implementation, verification, and effect in the environment separately.

Unrecorded does not mean risk-free. When historical details are missing, do not present current diagnostics as facts from that time; leave unrecoverable details unknown.

## 5. Keep only turning points worth revisiting

A timeline helps locate where reasoning or an approach failed: the earlier judgment, the fact that changed it, the correction, and its evidence. Keep only brief causal explanations useful for future understanding, diagnosis, or avoiding recurrence. Routine operations, repeated discussion, and every progress update do not belong in long-term history.

For example: "Service availability was treated as user access; account-filter evidence disproved that judgment; verification now uses the current account's actual entry point. Evidence: <reference>." This locates the error without retaining the entire incorrect plan.

Write each turning point once, within the relevant behavior or task if appropriate. The project ledger needs only those that affect overall understanding.

## 6. Record only the time detail needed to locate events

Distinguish occurrence, recording, implementation, or verification times when relevant. Do not give a completion time to something that has not happened. Leave unknown dates or time zones unknown, or give a supported interval. Timestamps do not prove causation, and a later entry is not automatically more valid.

## 7. Correct the original explanation when a discrepancy appears

Distinguish incorrect or stale records, implementation that violates a valid agreement, and an accepted design not yet reflected in the record. Correct the original using evidence rather than automatically deferring to code or old review, and notify those who actually depend on the claim.

Update locations after symbol moves, check affected consumers when meaning changes, and update applicability when scope changes. Delete disproved claims. For unresolved disputes, retain only the necessary evidence and open question, without presenting either side as settled fact.

<a id="record-updates"></a>
## 8. Maintenance triggers and current pending work

For a small task, record the change, result, and necessary evidence in its existing task or delivery record. Update the relevant explanation when responsibilities, dependencies, state meanings, or connecting contracts are added or changed, or an explanation proves inaccurate; leave accurate content unchanged. Routine verification results belong in the task record; update an existing conclusion at its source when evidence changes it. Leave accurate entry-point links unchanged and do not create sections just to close a task.

Promptly record unknown external effects to prevent repeated execution. Before handoff, fill only gaps that affect continuation; check the saved content and state restrictions or partial saves honestly.

Pending contains only the current arrangement: item, owner, next action, check time or trigger, and necessary record links. Replace old values when updating and delete completed items; do not copy full reports or retain old arrangements. Reuse an existing pending section in the ledger rather than creating another list. Waiting or deferred items need a reason and a resumption condition; renaming unfinished work does not complete it.

<a id="scoped-reading"></a>
**Required retention does not mean reading everything every time.** Read in layers according to the current question:

| Situation | Reading scope |
|---|---|
| First handoff or a new conversation | The project overview, current task checkpoint, and relevant implementation navigation; use these to locate the responsibility involved, without reading all detailed explanations and history. |
| Existing understanding still applies | The current change and affected explanations; reuse verified understanding instead of rereading to prove compliance. |
| Implementation or diagnosis | The affected part's purpose, dependencies, state, and connecting contracts, then relevant code, consumers, and evidence. Expand along specific relationships when impact crosses boundaries, accounts conflict, or important unknowns arise. |

For long documents, search headings, symbols, or task identifiers first and read the relevant sections. If output is truncated, narrow the scope rather than rereading the whole file. After context compaction, recover missing understanding through the current entry point and relevant explanations; do not reconstruct the whole repository by default or assume that having read something earlier means it is still understood.

Stop expanding when you can explain where this change belongs, whom it affects, what must be protected, and how to verify it, with no important relationship affecting this step left unresolved. Further reading should answer a specific question. An interruption is not completion. When an outcome is unknown, verify actual external effects before repeating an action merely because its success was not recorded.

## 9. Multiple roles and concurrent updates

Each task maintains its own scope and checkpoint; shared facts have one primary location. Follow existing coordination rules. When concurrent overwrites are possible, identify who will serially merge the relevant sections rather than letting the last writer win. Compare the baseline before saving and merge again if it changes. Retain necessary evidence for unresolved disputes without overwriting other tasks' valid facts.

## 10. Updating includes deletion

Delete incorrect plan text, expired conditions, superseded arrangements, duplicate explanations, and useless process detail. If an important mistaken judgment is worth revisiting, retain only the brief causal explanation described in section 5. Otherwise delete it; moving clutter into an archive preserves the burden. A summary at the top does not excuse an accumulating body.

Retain explanations of current implementation responsibilities, dependencies, and connections, along with valid constraints, unresolved risks, unknown external effects, and necessary evidence that cannot be reconstructed. Judge retention by the decisions it still supports, not length or reading frequency. Stop once the update lets someone continue and locate the key issue.
