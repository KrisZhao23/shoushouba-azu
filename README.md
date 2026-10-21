# 收手吧阿祖 · Shoushouba Azu

[English](README.md) | [简体中文](README.zh-CN.md)

Do the work clearly. Stop when it is enough.

A reusable engineering-judgment Skill and companion handbooks for AI-assisted software work. Understand the goal and existing implementation, clarify responsibilities and state, trace actual consumers, verify changes, and leave enough context for the next contributor.

**Status:** Public candidate `0.1.3-candidate`. Maintained under the public name **KZ**; project-owned content is licensed under [MIT](LICENSE). We have limited usage feedback and illustrative examples. Long-term results across projects and users still need to be tested.

## Watch the 60-second intro

[![Watch the Shoushouba Azu introduction](media/shoushouba-azu-intro-cover.jpg)](media/shoushouba-azu-intro-60s.mp4)

[▶ Watch the video](media/shoushouba-azu-intro-60s.mp4) · Chinese · 60 seconds · [Audio credits and license](media/HUASHU-DESIGN-LICENSE.txt)

A hidden link between saving personal tags and another user's login, reproduced and fixed in isolated tests; plus a look at using project records to find code and resume work.

## Two complete reading paths

English files use `.md`; their Simplified Chinese counterparts use `.zh-CN.md`. The Skill, role handbooks, ledger templates, examples, references, and feedback guidance are available in both languages. Each document links to its counterpart.

Both languages are included in the same `skills/clear-engineering/` package; install it once. The discoverable entry remains `SKILL.md`, with a complete Chinese reading entry at `SKILL.zh-CN.md`. The agent should communicate in the user's preferred language and read the relevant language's materials as needed.

## Where to start

- To use the method with an agent, read the [Skill](skills/clear-engineering/SKILL.md), then follow only the references relevant to the task.
- To understand how to organize the work, read the [coordination](handbook/coordination.md), [execution](handbook/execution.md), or [review](handbook/review.md) handbook. These are responsibility perspectives that one person can cover; they do not require three agents or three approval rounds.
- For small-project examples, read the [single-file tool](skills/clear-engineering/examples/single-file-tool.md) and [composed-behavior example](skills/clear-engineering/examples/composed-publication.md). Both are fictional illustrations.
- For project continuity, use the [ledger method](skills/clear-engineering/references/03-ledger-and-timeline.md) and [starter template](skills/clear-engineering/assets/project-ledger.md) when needed. Update existing records when they are already sufficient.
- For evidence of usefulness, read [usage and evaluation](skills/clear-engineering/references/05-usage-and-evaluation.md), [research evidence, attribution, and license boundaries](skills/clear-engineering/references/06-case-evidence.md), and the [repository validation record](VALIDATION.md).

## How to use it

`skills/clear-engineering/` is the complete Skill directory. Install that subdirectory using the mechanism currently supported by your host, or read the main document directly and use it as the working method for the current task. Installation, activation, and personal configuration changes remain subject to your own environment and authorization.

File readability, skill discovery, reading the instructions, and improving decisions are separate facts. The instructions do not guarantee automatic loading in every agent tool, or correct behavior after reading. Verify the actual host's loading and inheritance behavior in your environment.

Start with the current goal, a valid project knowledge entry point, and the current task state; expand only as questions arise. Reuse understanding, capabilities, reviews, and evidence while their assumptions remain valid. Establish the necessary prerequisites and verification method before an action; obtain its results after the action. Stop when sufficient evidence supports the current commitment.

## How the Skill and handbooks fit together

The Skill and its references define the shared reasoning and record semantics. The handbooks apply them to particular responsibilities. See the [review handbook](handbook/review.md) for review applicability and authorization boundaries; each project still follows its own agreements.

Keep system addresses, model preferences, runtime parameters, and production constraints in the adopting project's own configuration. No particular project size, technology stack, or number of agent roles is required.

## The feedback we want

We especially want to hear: **"I followed this, and the work became harder to move forward."** Useful results, omissions, false triggers, repeated work, and suggestions to remove rules all matter. Describe which wording affected an action and what actually happened. If the result is still unknown, or you have not tried the method, say so.

[Share a use case or counterexample](https://github.com/KrisZhao23/shoushouba-azu/issues/new?template=use-case.md), or write a few sentences in your own format. The [case template](.github/ISSUE_TEMPLATE/use-case.md) is optional and can be shortened. You do not need to disclose source code, company details, a complete ledger, or chat history, or prepare a patch first. See [CONTRIBUTING.md](CONTRIBUTING.md) for how feedback is handled and cases are included.

## Research and licensing

This project was developed collaboratively by the maintainer and AI assistants, drawing on public source code, tests, design records, and practice reports. Authors' stated reasons, source observations, reported experience, and this project's transfer inferences are distinguished. A citation does not imply endorsement by the source project.

The research approach was inspired by Huashu's (花叔) Nuwa Skill. Authors, URLs, licenses, and the scope of use for actual research sources, technical references, and projects merely mentioned are collected in the [third-party attribution and license review](skills/clear-engineering/references/06-case-evidence.md#source-licenses). This inventory stays inside the Skill package. Attribution does not replace the license conditions required for reuse.

The Skill, handbooks, ledger templates, and example code that this project has the right to license are provided under [MIT](LICENSE), with `Copyright (c) 2026 KZ`. Third-party materials retain their own licenses. An identical [LICENSE](skills/clear-engineering/LICENSE) is included in the Skill subdirectory and must accompany separate distributions. Sharing improvements and experiences is welcome and voluntary, not an additional license condition.
