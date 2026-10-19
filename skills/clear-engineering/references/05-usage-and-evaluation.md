# Practical Use, Loading Checks, and Building Evidence Over Time

[English](05-usage-and-evaluation.md) | [简体中文](05-usage-and-evaluation.zh-CN.md)

Purpose: guidance for using and observing this Skill. Read it as needed when adopting it, changing environments, upgrading the method, or reviewing experience. In everyday work, follow the main text and the existing project knowledge entry point; do not add another round of method acceptance checks.

## 1. Distinguish four things

The method has supporting evidence; it transfers to other settings; the host actually loads it and can read the relevant materials; using it produces additional improvement. None of these establishes the others. Copying files does not establish discoverability; discoverability does not establish automatic triggering; triggering does not establish that every judgment is correct.

The Skill's default description covers engineering planning, design, implementation, review, and continuation. Hosts typically expose its name, description, and path first; participants then actively read the body based on a match or an explicit rule such as AGENTS. Reading it because a rule requires it does not require the user to invoke it manually every time. Visibility in a catalog does not establish that the full text is already in context. The exact mechanism depends on the actual host and version; this repository's adoption instructions and file-format checks do not establish that the current environment is configured to use it.

## 2. Provide a working entry point that does not rely on remembering

Place brief navigation in the project instructions, pointing to the actual current project knowledge entry point and requiring relevant engineering tasks to use the method. Keep detailed facts in the project ledger; do not put the entire ledger into startup instructions. When creating subtasks, pass the goal, shared constraints, record locations, and working baseline. Require recipients to work from materials they can actually access, rather than claiming all subagents automatically inherit them.

Distinguish Skill discovery, reading the main text, reading references, and applying the method. Inspect existing tool traces when relevant to a question; a reading confirmation form is not required every turn. Reuse understanding that remains valid, and read the necessary parts when loading fails or context is missing. Do not present material read now as having been read earlier, or claim that judgment was correct merely because the main text was read.

## 3. Check adoption through behavior, not just a claim of understanding

In a trial that makes no business writes, check whether the main text can be found, references can be read as needed, and the actual project ledger is used to locate relevant responsibilities and consumers. After explicit invocation succeeds, observe in a new conversation whether an ordinary engineering request triggers the method and whether unrelated tasks avoid expanding the entire method.

Inspect actual reads when the host provides tool traces; model self-report alone is weaker evidence. A harmless local sample task can test navigation and scope judgment; do not introduce secrets as test markers. Check each role or environment actually used, rather than generalizing one conversation's success to all of them.

During initial adoption or a loading problem, record the relevant host, scope, actual location, and unchecked items in the existing adoption record, then reference it. Do not create a separate adoption report for an ordinary task, or describe a format check as behavioral acceptance.

### 3.1 Minimal checks for creating, binding, reading, and maintaining a ledger

The following are observation scenarios to select as needed, not gates before every task. Record the actual verification status in the corresponding adoption record. When a trial is needed, use authorized existing materials or an isolated copy; do not create an official ledger or make real business writes just to test the mechanism. See sections 2, 8, and 9 of [Ledgers and Timelines](03-ledger-and-timeline.md) for the mechanism.

| Scenario | Minimal observation | Signs of failure |
|---|---|---|
| First entering a project | Actually find and reuse a suitable existing entry point. Create and register one only if none exists and trial writes are authorized, then confirm a successor context can read it. Also cover an inaccessible binding target: report the access gap without creating another official entry point. | Concluding that no ledger exists based only on a filename; claiming adoption is complete after creation without registration; creating a replacement whenever a link is lost. |
| Successive new requirements in the same project | Give two successive tasks for the same project. The later task reuses the same project entry point and adds a task record without creating a parallel ledger. | Creating a new ledger per requirement, executor, or conversation; promoting a temporary copy to another current entry point. |
| Continuing without the predecessor's conversation | Give a fresh context only the working entry point, project and task locations, and other handoff information, without the original conversation. It locates completed work, unverified work, actions that must not be repeated, and the next step, and checks the relevant baseline. | Merely repeating the method; finding the wrong task; describing unverified work as complete; repeating actions whose outcome is unknown. |
| An important understanding changes | In an isolated sample, provide facts that refute a previous claim. Observe the task record, the invalidation or dispute notice in the original explanation, and subsequent stable updates; readers can find the evidence. If parallel use actually occurs, also check that merging shared records does not overwrite each other's discoveries. | Recording only the task process while leaving an incorrect current explanation in force without a warning; treating a new proposal as accepted; overwriting with an old snapshot. |
| A local change that does not alter project understanding | Complete a local, low-risk task in isolation and save its result only where delivery or task needs require it. The current project description and long-term timeline may remain unchanged. | Adding useless events, duplicate indexes, or unrelated documents just to show that records were maintained. |

For each host, starting location, scope, and role actually used, state which of these were checked: file readability, entry-point registration, actual reading, explicit use, implicit matching, and behavior in a new conversation. Actual tool traces and file differences can provide evidence; self-report alone is weaker. Say when something was not performed. Successful explicit reading does not establish implicit triggering or verification for other roles. Do not make users supply the project path every time to conceal a binding that was never established. These scenarios support the workflow under the conditions checked, not a claim of long-term method effectiveness.

## 4. Observe results in real subsequent work

During changes that would be made anyway, retain the expected impact before editing, relevant snapshots, and later discoveries. Observe whether a new participant finds the correct responsibility sooner, misses important entry points, repeats the same policy explanation, makes unrelated changes, or uses verification that can detect actual defects.

Consider the total burden of creating, updating, reading, investigating, implementing, and reviewing. Leave concrete examples in existing task records when there is a substantive problem. Reading less code may mean more accurate navigation or missed checks; reading more may uncover risks or simply repeat work. Do not require another itemized timesheet merely to quantify the method.

Dependency direction, duplicated rules, unchanged consumers, combined behavior, and the quality of later changes are more informative than counts of directories, functions, tests, or documentation words. Allow multiple reasonable solutions.

If willing to give feedback, summarize one concrete experience from existing records: what you intended to do, which action the method influenced, what you observed, and what you would keep or change. Help, getting stuck, no obvious effect, and heavier process are all worth reporting; preserve uncertainty when the outcome or loading status is unknown. Feedback is voluntary, is not a condition of use, task completion, or handoff, and never automatically uploads project records. The full repository's contribution guide provides a case-reporting entry point. Using this package on its own does not require another feedback archive.

## 5. Separate contributions gradually; do not build a large experiment platform in the first version

In a small number of isolated tasks, compare the existing approach, the general method alone, accurate project records alone, and both together. You need not run all four groups in every round; the aim is to be clear about what changed. Keep necessary requirements, constraints, source code, and permissions consistent. Do not give only one group crucial business facts.

To test information organization, compare ordinary prose with records that expose the same facts through responsibilities, behavior, and evidence. To test the method's wording, compare the candidate with general reminders of similar length. Record the model, tool budget, and effort so that extra analysis time is not mistaken for the method's contribution.

Have a new conversation or someone who did not participate in the original design continue the work. Distinguish the benefit of thinking while creating records from the benefit of reading them. A model may already have seen public historical fixes; those alone are not strong evidence of transfer.

## 6. A few observations that distinguish useful behavior

A representation change followed by a rule change: does each have a suitable place to change, beyond merely adding names such as parser or service?

A shared fact changes: does the participant recognize invalidated assumptions and trace unchanged entry points, existing objects, and actual consumers?

A small task that does not warrant a framework: does the implementation remain clear without adding useless layers, and can it adapt reasonably to later changes?

A record's meaning is stale while its path is still correct: are key claims checked and corrected for the current task, or does the record simply increase confidence in the wrong direction?

Resuming interrupted work: can participants distinguish implemented from unverified work, avoid repeating external actions, and continue from existing results?

Parallel changes: are conflicts in a shared agreement detected, instead of letting the last-written record win?

## 7. Allow failure and reduction

If records grow longer while the same entry point is still missed, more layers are added while changes still spread widely, or the ledger and code remain in conflict, revise or remove the ineffective parts. If the candidate has no repeatable advantage over ordinary reminders, do not advertise an additional benefit.

One success supports only its own conditions. A few cases help identify wording and adoption problems; they do not prove universal or long-term effectiveness. Observation should not delay use indefinitely, and use should not remove the responsibility to correct the method.
