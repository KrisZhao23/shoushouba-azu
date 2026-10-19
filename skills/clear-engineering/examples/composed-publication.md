# Composed behavior: matching reviewed content to published content

[English](composed-publication.md) | [简体中文](composed-publication.zh-CN.md)

This example is entirely fictional. It illustrates how overall understanding, design tradeoffs, collaboration across responsibilities, task continuation, and a timeline connect. It prescribes no technology stack, and no code or tests have been run.

## Current understanding: establish the shared commitment first

Goal: only reviewed content may be published. Responsibilities may include editing, review, publication tasks, and actual publication, but these names do not automatically determine module, service, or file boundaries.

Distinguish document identity, content version, review result, and publication effect. What a review applies to, and when publication reads which content, are collaboration contracts rather than private details of a helper function.

Two alternatives may both be reasonable. Option A prevents editing after review passes. Option B allows new drafts but binds the review result and publication task to a stable content version or snapshot. If continued editing is an explicit requirement, A does not meet it. If there is no such requirement and freezing is acceptable, do not build a versioning platform for speculative future needs.

## Record of collaboration across responsibilities

The following assumes that B is accepted only within this fictional example; it does not represent a decision in a real project. Under B, editing produces content versions; review decides on a specified version; the publication task retains enough information to locate that version; execution reads that same version; and result confirmation identifies which version was actually published. After an external call times out, a failed local wait alone cannot justify resetting the outcome to unpublished.

Hypothetical implementation anchors might be `review_content`, `create_publication`, and `execute_publication`, but a real record must obtain its anchors from the source code. The overview makes the shared constraint, "the reviewed object corresponds to the published object," visible. There is no need to register every helper function in an internal queue.

## Different questions for design review and code review

Design review: after version seven is reviewed, a version eight draft appears. When the original publication task executes later, how does the design preserve the commitment? Who ensures version correspondence, and how is the outcome checked after a failure?

Code review: does the actual task store only a document identifier? Does execution read the latest content again? These observations may refute the outline. Also check relevant readers, repeated triggers, or result displays according to actual risk, rather than rechecking the entire repository every time.

Proposed test: construct the sequence "seven reviewed, eight unreviewed, seven's task executes later" and assert that the published content corresponds to the reviewed object. The test should fail for an implementation that incorrectly reads the latest draft. This is a proposed discriminating case, not evidence of a passed test.

## Evolution and progress of the same change

EX-P01, date unspecified, decision: accept the direction "allow continued editing, but publish only reviewed versions." The concrete implementation is pending source exploration.

EX-P02, subsequent static observation (assumed for this example): the existing task stores only a document identifier. This observation means the original plan omitted shared information. It cannot quietly be treated as a private implementation patch; the relevant tasks and contracts need updating.

EX-P03, plan correction: explicitly preserve stable correspondence and investigate how to continue with in-flight tasks that lack that information. Adding a field is not sufficient to declare completion. Do not rewrite the initial plan from the final code as though everything had been anticipated.

EX-P04, current checkpoint: there is no real code or runtime evidence yet. The next contributor should first inspect the task's writers and execution readers, then choose the minimum necessary way to support old tasks. Do not resend publication actions that may already have taken effect without authorization.

## When the whole chain does not need another review

When changing publication page colors without changing behavior, permissions, or the meaning of status messages, focus on the relevant rendering and usability; this does not call for an audit of all publication logic. Changing what the object stored by a task means requires checking the collaboration relationships again, even if only one field changes.
