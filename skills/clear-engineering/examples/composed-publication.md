# Composed behavior: matching reviewed content to published content

[English](composed-publication.md) | [简体中文](composed-publication.zh-CN.md)

This example is entirely fictional. It illustrates how overall understanding, design tradeoffs, collaboration across responsibilities, task continuation, and a timeline connect. It prescribes no technology stack, and no code or tests have been run.

## Current understanding: establish the shared commitment first

Goal: only approved content may be published, and editors must be able to continue editing after approval. Publication tasks may execute later. Completion means the content actually published matches an approved version; a successful task status alone is insufficient.

Distinguish document identity, content version, review result, and publication effect. What a review applies to, and when publication reads which content, are collaboration contracts rather than private details of a helper function.

Initial proposal: store only the document identifier in the publication task and read the latest content when it executes. Check this proposal against the known usage sequence: version seven is approved, an unapproved version eight is then edited, and the original publication task executes later. Each step can follow this design correctly, yet version eight is published and the original commitment fails.

Revise the proposal: bind the review result and publication task to a stable content version or snapshot. Freezing edits would violate this example's requirement to keep editing. Under different requirements where freezing is acceptable, that simpler option may suffice; versioning is not a universal requirement.

## Record of collaboration across responsibilities

Under the revised proposal in this fictional example, editing produces content versions; review decides on a specified version; the publication task retains enough information to locate that version; execution reads that same version; and result confirmation identifies which version was actually published. After an external call times out, a failed local wait alone cannot justify resetting the outcome to unpublished.

Hypothetical implementation anchors might be `review_content`, `create_publication`, and `execute_publication`, but a real record must obtain its anchors from the source code. The overview makes the shared constraint, "the approved object corresponds to the published object," visible. There is no need to register every helper function in an internal queue.

## Different questions for design review and code review

Design review: who preserves the correspondence across review, task creation, and publication, including when execution is delayed? How is the actual publication outcome checked after a failure?

Code review: does the actual task store only a document identifier? Does execution read the latest content again? These observations may refute the outline. Also check relevant readers, repeated triggers, or result displays according to actual risk, rather than rechecking the entire repository every time.

Proposed test: use the sequence above and compare the content actually published with approved version seven. The check must reject publication of version eight even if the task reports success. This is a proposed discriminating case, not evidence of a passed test.

## Evolution and progress of the same change

EX-P01, date unspecified, initial proposal: store the document identifier and read the latest content during publication.

EX-P02, design check: the delayed-publication sequence above refutes the initial proposal without changing either user requirement.

EX-P03, revised proposal: preserve stable version correspondence. Inspect the actual writers and readers and investigate how to handle in-flight tasks lacking that information. Adding a field is not sufficient to declare completion.

EX-P04, current checkpoint: there is no real code or runtime evidence yet. The next contributor should first inspect the task's writers and execution readers, then choose the minimum necessary way to support old tasks. Do not resend publication actions that may already have taken effect without authorization.

## When the whole chain does not need another review

When changing publication page colors without changing behavior, permissions, or the meaning of status messages, focus on the relevant rendering and usability; this does not call for an audit of all publication logic. Changing what the object stored by a task means requires checking the collaboration relationships again, even if only one field changes.
