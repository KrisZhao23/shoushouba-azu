# Project ledgers, timelines, and understanding others can continue from

[English](03-ledger-and-timeline.md) | [简体中文](03-ledger-and-timeline.zh-CN.md)

Purpose: read this as needed when starting project records, choosing what a record should cover, updating shared understanding, handling outdated information, or continuing work across conversations. When the existing entry point and stopping point are enough to continue, reuse them and add the current differences; do not add files or copy records merely to demonstrate use of the method.

Research influences on knowledge organization, their authors, and their licenses are collected in the [case and source notes](06-case-evidence.md#source-licenses). This repository's starter documents are organized separately using these judgments; they do not include upstream projects' original ledgers or business records.

## 1. Place information according to the reader's question

| What is the reader asking? | Organize the record around | What understanding should it add? |
|---|---|---|
| What is this part responsible for, and why does it belong here? | A responsibility | Goal, boundary, key dependencies, and implementation anchors |
| How is this result achieved, and what does failure mean? | Complete behavior | Entry points, flow of facts, participants, states/effects, and consumers |
| What meaning do several parts rely on together? | A shared contract or state | Authority, read/write permissions, versions, failure meaning, and maintenance location |
| Why was this choice made, and when should it change? | An important decision | Context, alternatives, costs, applicable conditions, and what it supersedes or is superseded by |
| What supports this conclusion? | Evidence or an unknown | Source, applicable snapshot, assertions/observations, and uncovered scope |
| How far has this task progressed, and what comes next? | A task | Current goal, progress, differences, blockers, and a safe point to continue from |

These purposes can be combined; they do not require six kinds of file in every project. Prefer one explanation for a stable responsibility or question. Give an important state its own referenceable contract when multiple behaviors share it. Different views should refer to the same explanation rather than restate its meaning independently.

## 2. Identify the project, create an entry point when needed, and bind it to the working context

A project ledger belongs to a project maintained over time, not to a conversation, role, or individual request. Identify the project from its established goal, boundaries, maintenance responsibility, workspace, and task context. A directory, module, test copy, or new request does not by itself create a new project. Renaming or moving a project usually means updating its location while continuing the existing understanding. A copy or branch should state its baseline and differences, not present itself as another designated current entry point. Consider a separate project only when its goal, boundaries, and maintenance responsibility are genuinely independent; this does not require a global project-ID system.

First check the designated current project knowledge entry point. If no binding instruction exists, inspect the relevant README, project descriptions, and their references; use a bounded search of paths and names if necessary. Reuse material that can explain the whole and provide navigation, rather than creating a parallel index. A known entry point that will not open, an unmounted target directory, insufficient permissions, or several descriptions each claiming to be current do not mean there is no ledger. Check accessible location information and sources first. If the project association still cannot be resolved, ask for specific clarification; retain the current draft without declaring a new entry point. Once the search has been proportionate and no leads to an existing entry point remain unresolved, decide whether to create one. There is no need to search the entire machine or all repository history. Do not repeatedly ask for the same paths and rules for ongoing work whose scope is already clear.

When an entry point is genuinely missing, the task needs ongoing work or continuity, and existing authorization permits the relevant records to be written, create a minimal but truthful entry point. `PROJECT-LEDGER.md` is a possible default name; its location follows project conventions. Save the supported goal and scope, main responsibilities and cooperation, important constraints, implementation entry points, unknowns, and the current task stopping point, retaining the nature of the sources. If there is no implementation, say so: do not invent symbols, reconstruct the project's entire history, or pre-create empty templates. Do not mechanically create a ledger for a simple question or a temporary example that has not become a lasting project. A read-only investigation of an existing project may still produce information worth preserving for continuity within the authorized scope; "no code was changed" does not mean a record is never needed.

Designate one current project knowledge entry point per project; this does not mean there can be only one file. Initially, the overview, key behaviors, timeline, and tasks may share a file. Split them out when reading or independent maintenance warrants it. A platform and a logical project within it may each have clearly scoped entry points. Explain shared capabilities where they actually belong and reference that explanation elsewhere. The main entry point should retain the overall explanation, important constraints, and directions for deeper reading. It must not become merely a directory listing or require reading all history to discover the current understanding.

After creating or reusing records, register the project scope, current ledger location, and the base for resolving its path in a working entry point that you are authorized to edit and that will actually be read. Creating a record, registering its location, and reading it successfully in a particular environment are three different facts. Plain text can distinguish them; a status table is not mandatory. General instructions should cover identification, discovery, and use; project-specific binding should cover scope and location. Keep the detailed rules in this section rather than copying them everywhere. A general trigger rule cannot exist only inside a Skill that has not yet been triggered. Integrate it through working instructions the host already reaches or through an explicit task handoff; the method cannot declare itself active.

Routine records covered by existing authorization and project conventions do not require asking for the same permission again each time. Permission to write a ledger does not automatically authorize changing startup rules, `AGENTS.md`, or permissions. Under read-only or scope restrictions, provide the proposed text and maintenance location, stating whether it has not been saved, registered, or verified as readable. Continue safe, independent work using accessible facts. For checking actual reading later, see section 3 of [usage and evaluation](05-usage-and-evaluation.md).

## 3. Trace down to implementation and across to cooperation

Trace vertically from goals to responsibilities and implementation. Trace horizontally from a user result through shared facts, producers, consumers, resources, and failures. Constraints spanning modules should be discoverable at the higher level, with related locations pointing back to the same explanation.

Describe a dependency as "what is needed from whom, when it is used, and whose change affects what," rather than merely labeling something "coupled to the database." Initialization order, environment reads, shared identities, cache invalidation, and message protocols may also deserve a record, but actual behavior determines whether to expand on them.

Use file paths and symbols as the main implementation anchors, with line numbers as aids. A correct location does not establish a correct responsibility description. Associate key anchors with relevant code/environment snapshots; every sentence does not need a timestamp.

## 4. Separate proposals, accepted agreements, current conditions, evidence, and unknowns

Plain text is usually enough to distinguish the following. Short labels can help when the distinction matters; every record need not have a status table.

- Proposal: a direction or constraint not yet accepted; it does not automatically become an established premise for implementation.
- Accepted agreement: what was explicitly accepted, within what scope, and on what basis. Anything beyond that scope still needs judgment. An assistant's suggestion or the absence of objection is not acceptance.
- Observation: what was seen in which code/configuration snapshot. Do not call static reading runtime verification.
- Evidence: which execution, test, or check supports which claim, and what it does and does not cover.
- Unknown/inference: what is not currently known, the basis for the inference, and which check could change the current choice.

When a proposal is accepted, retain the actual basis for acceptance. When it is withdrawn or superseded, link the corresponding event. Acceptance of a design does not grant permission to install software, modify data, or execute production actions.

"Decision accepted," "actually implemented," "verification completed," and "effective in the environment" are not interchangeable states in one state machine. Express them separately in the relevant events; a fixed status matrix is not required for every record.

An unrecorded area indicates missing coverage, not the absence of dependencies or risks. An accepted design may not yet be implemented, and the running system may violate a valid agreement.

## 5. Divide the work between the current explanation and the timeline

The current explanation answers how to understand the project today. The timeline records important changes: what new fact appeared, which judgment or implementation changed because of it, who was involved, and where the evidence or follow-up task is.

Let the reader reach the current explanation first, then history as needed. The project knowledge entry point indexes events that affect the whole; local history stays with the corresponding behavior or task. Keep one primary account of each event and use an event ID or link elsewhere, rather than copying diverging versions into several places.

Events usually worth recording include changed shared assumptions, important failures and fixes, superseded accepted designs, verification overturning a conclusion, resolution of a major unknown, and pauses or resumptions that affect continuity. Do not turn every tool call and everyday edit into required historical reading.

Both the evolution of project decisions and task progress need to be understandable to someone continuing the work. Not all task history belongs in the long-term project history: promote stable new understanding, key tradeoffs, and failures with future implications into the current explanation or decision records.

## 6. Express time accurately

An event's occurrence/observation time differs from its recording time; preserve both when needed. Record decisions, implementation, verification, and release/effect separately. An event that has not happened cannot have a completion time.

Use the project's actual date conventions by default. Record times with a time zone when precise order matters. Do not infer the time of a local action from the assistant's current date or guess an unknown time zone. When the occurrence time cannot be recovered, record the confirmable snapshot interval and the time of the retrospective entry.

Event IDs provide links; actual relationships explain order. Timestamps do not prove causation. Parallel branches may have their own events, followed by explicit merge or supersession relationships; a later timestamp does not establish which one overrides another.

When correcting an error later, retain its relationship to the original event and the reason for correction. Everyday typos can be corrected directly; history that affects judgment must not be silently rewritten. This timeline records engineering understanding; it is not a tamper-proof system or a store of business facts.

## 7. Identify the kind of outdated information before correcting it

Outdated location: a symbol moved or was renamed. Update the location and check whether its responsibility also changed.

Outdated meaning: the location still exists, but its actual role, writers, consumers, or assumptions have changed. Stop relying on the incorrect claim, then verify the affected relationships.

Outdated scope: a new entry point, configuration, version, or runtime arrangement makes the old explanation incomplete. Preserve its accuracy for the old scope while updating the current applicability boundary.

A discrepancy can mean three different things: the record is wrong or outdated; the implementation violates a valid agreement; or an accepted new design was not reflected in the record. Neither "the code wins" nor "the reviewed outline wins" is a sufficient automatic rule. State the current claim, observation, and discrepancy; correct what evidence overturns and notify the participants who actually rely on it.

Verify only important claims relevant to the current work. A recent file modification time, a working link, or a page marked "reviewed" does not establish semantic consistency.

## 8. When to maintain records, and what makes work ready to continue

Before updating, ask: if the next reader continues to rely on the existing explanation, will they misunderstand, miss something, repeat an investigation, or repeat an action? Update the primary record for the relevant responsibility, behavior, contract, decision, or task; do not create a separate explanation for every role.

During work, promptly save the basis and impact of important findings, overturned understanding, hard-to-reconstruct results, or continuity risks. Mark a new approach worth discussing as a proposal; update the effective agreement and its basis when the proposal is accepted, superseded, or changes scope. If implementation changes responsibilities, interface meaning, state ownership, dependencies, permissions, lifecycles, or external effects, or if verification yields a result that changes the judgment, maintain the corresponding explanation and distinguish design acceptance, actual implementation, runtime verification, and effect in the environment. Record the actual result or unknown outcome of an external action promptly; do not wait until the task ends and reconstruct it from memory.

New findings usually enter the task record first. Stable understanding worth relying on later then enters the project's primary explanation. But when existing evidence already makes an important current claim unreliable, promptly mark the original as overturned, limited, or disputed, and link the finding and evidence; do not wait for a complete replacement design. Unverified guesses remain guesses, and marking a problem in an old explanation does not automatically accept a new approach. Preserve the reasons for key changes as described in sections 5–6; do not put every routine edit and tool call into long-term history.

Before finishing, handing off, or a foreseeable interruption, fill only the gaps that affect continuity: the current goal, applicable baseline, what has been done and verified, what comes next, and actions that must not be repeated. Reuse existing delivery notes, task records, or coordination stopping points when they serve these purposes. Do not copy the same facts into several documents; parallel tasks retain their own scopes and stopping points.

After saving, check the actual target and relevant content. A brief delivery note may say "Project ledger updated: <location>," "Project understanding is unchanged; no update needed. Task results: <location>," or "Revision needed but not yet saved: <reason, location, and proposed text>." Task results can live in existing records or an appropriate delivery response; this does not force the creation of a file. If only some writes succeed, state the result at each location rather than masking failures with a single "updated." When writing is restricted, provide text that can be saved; do not claim it is on disk.

An interruption is not completion. On resuming, first obtain the overall project knowledge entry point and the relevant task stopping point, then check snapshot and state differences that affect the next step; do not investigate the entire repository again. The last action before an abrupt interruption may not have been recorded. When an external outcome is unknown, first verify it or recover safely using the capabilities actually available; do not repeat the action merely because the process record lacks a success entry.

## 9. Multiple roles and concurrent updates

The role that discovers a change can draft it, and relevant reviewers can check its claims; no single role needs to own all design authority. When shared facts conflict, preserve the evidence on both sides and let an authorized decision-maker resolve the conflict within a proportionate scope.

Shared records follow the project's existing write-coordination rules. Rereading and comparing the baseline before saving can expose outdated information, but rereading alone does not prevent both writers from reading and then overwriting each other. If coordination is unavailable and concurrent overwrites are possible, each task should first save its own proposed revision and identify who will serially merge the shared sections for this round. No fixed role or new locking service is required, and unrelated work need not stop. If the baseline changes during the merge, compare again rather than overwrite it with an old snapshot. Merge facts and evidence before wording. Preserve each side's basis while a dispute remains unresolved; the last writer does not win by default.

Each task preserves its own progress, and the project knowledge entry point links to the tasks that are actually active. Avoid a single global "current task" repeatedly overwritten by parallel work. One person on a small project may need only one task section.

## 10. Long-term retention and reduction

Retain currently valid constraints, important reasons, necessary history, and explanations of facts that cannot readily be reconstructed. Temporary exploration and ordinary operational details can leave the current navigation when a task closes, but first preserve results that will prevent repeated investigation.

Remove copied field tables, unhelpful indexes, and redundant descriptions superseded by clear code. Do not delete solely by access frequency: a rarely read decision can still explain an important limit. The first version need not reconstruct the project's entire history; grow it from what can currently be verified.
