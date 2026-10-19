# Public candidate validation record

[English](VALIDATION.md) | [简体中文](VALIDATION.zh-CN.md)

Scope: public candidate content based on `0.1.3-candidate`. Project-owned content is licensed under MIT, with the public name KZ. Checks below retain their original stages; earlier file counts, license status, and unpublished status describe those snapshots. The available repository commit determines the content actually online.

## Initial checks completed

- The Skill format validator returned `Skill is valid!`. This checks file format, not installation, automatic discovery, or correct use.
- The two Python code blocks in the single-file example were executed in order under Python 3.11.9, using their existing `check_example()`. Checks passed for the due date, overdue date, completion date, two output entry points, field normalization, and rejection of invalid input. Only the standard library was used, with no network calls or business-file writes.
- Checked 23 public files and 62 local Markdown file references; no missing targets were found.
- Scanned known private identifiers, personal and absolute paths, host addresses, emails, conversation identifiers, and common secret patterns. After correcting references to internal background materials, no matches remained. Public third-party names and links were retained; business source code, runtime logs, chat screenshots, and historical Git data were not included.
- Native PowerShell UTF-8 reads and Python reads agreed for all 23 files; normalized text hashes matched.
- At this stage, there was no Git history or license file, and no remote repository, commit, or upload had been created.

## Evidence limits

File checks and offline examples support only their stated scope. They do not prove compatibility with every agent environment, correctness for all inputs, or general effectiveness. Reading third-party research and checking this repository are separate activities; these checks are not presented as validation of an adopter's business system.

Update relevant actual results here after changes. A separate validation report is not required for every edit.

## 2026-10-18: sources, attribution, and licenses

- Reviewed the public content and its third-party references against original repositories, pinned-version licenses, official documentation license pages, or specification copyright sections. Reference 06 section 9 lists 21 source groups: 16 research/inspiration/technical groups and 5 projects merely mentioned. Nuwa's author and source were added explicitly.
- Key distinctions: GitLab Handbook content uses CC BY-SA 4.0, not the software repository's root license; the Codified Context repository's MIT license is separate from the paper's CC BY 4.0 license. Cited Stripe and OpenAI pages were not labeled as generally open-licensed for copying. No clearly noncompliant copying under the checked licenses was identified in the current materials; this was not a comprehensive similarity or ownership assessment.
- Coordinated changes were limited to the public README, Skill navigation, ledger method, reference 06, and this record. The attribution inventory stays inside the Skill directory so it accompanies a separate copy. Installed Skills, global instructions, and business projects were not changed.
- The format validator returned `Skill is valid!` with the process option `python -X utf8`. The initial default-GBK read failure was a check-command encoding issue; files and global encoding settings were not rewritten because of it.
- There were still 23 public files, with 65 valid local Markdown file/anchor references. Known private identifiers, paths, host addresses, emails, and common credential patterns had no matches. Native PowerShell UTF-8 and Python content hashes matched for all 23 files; the later record update received a separate native-read check. Unchanged example code was not rerun.
- The earlier independent read-only privacy review covered the files before this source supplement. This check covered the new public sources and explanations without extending the other reviewer's conclusion. At this stage, the project-owned license, public attribution, and future Git publication metadata remained undecided; no license, commit, remote, or upload had been created.

## 2026-10-18: voluntary case feedback and MIT

- The maintainer chose MIT and the public name KZ. Identical standard license text was added at the root and in the Skill directory, with `Copyright (c) 2026 KZ`. The README, Skill, source inventory, and repository instructions were aligned. A separately distributed Skill retains the license and source inventory; third-party license boundaries did not change.
- The README states that case evidence and cross-project validation remain limited. The contribution guide explains how to summarize existing records, handle feedback, and confirm inclusion of a case. One Markdown issue template provided four optional prompts. Reference 05 was aligned on voluntary sharing, avoiding duplicate ledgers, and no automatic uploads. Repository instructions now permit de-identified experiences confirmed safe for publication by their provider.
- A narrow read-only continuity check found that the three role handbooks already required reuse of existing records, so no feedback step was added to each role. Installed Skills, personal settings, and other projects were not changed; no trial users were contacted or recruited.
- At this stage, there were 26 public files and 74 valid local file/explicit-anchor references. The two LICENSE files matched. The issue template's YAML frontmatter parsed with valid name and about fields. Its location and format were checked against [GitHub's official documentation](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates); the template wording was written for this project.
- The Skill format check returned `Skill is valid!`. Native PowerShell UTF-8 and Python hashes matched for all 26 files; known private identifiers, personal paths, and credential patterns had no matches. The later maintenance-note and validation-record edits received separate native-read checks. Unchanged examples were not rerun.
- These checks covered local content, links, and format. At that stage, the default branch had not been pushed, the online template chooser had not been tested, and no new community cases had been received. No commit, push, or publication had occurred, and Git publication identity and remote settings were not configured.

## 2026-10-18: preparation for the first Git publication

- The maintainer authorized public publication. A fresh independent Git repository included only the 26 public files, without history from another project. Commits used KZ and a GitHub noreply email; identity was set only for this repository, without changing global Git configuration.
- The README and contribution guide were updated to public-candidate wording and the actual issue URL. A read-only review of the new license, feedback guidance, and template found no specific private information or mandatory feedback obligation. This does not guarantee the safety of future contributions.
- Checked the actual staged file list, UTF-8 text, and known private identifiers. All 26 entries were expected regular files; staged content matched local Python and native PowerShell reads. One extra trailing blank line was removed, and the two subsequently changed documents received the same checks. Example behavior was unchanged.
- This section records checks before publication. Actual GitHub branches and commits establish the remote result; local template-format validation is not presented as online chooser or real feedback-effectiveness validation.

## 2026-10-18: public-name correction

- The public project name is "收手吧阿祖" (Shoushouba Azu), at `KrisZhao23/shoushouba-azu`. The homepage, maintenance instructions, and feedback links were aligned. The Skill remains installed and invoked as `clear-engineering`; its content directory and existing relative references did not change.
- Only naming, description, addresses, and records changed. UTF-8 text, staged content, and links in the changed documents were checked; unaffected examples were not rerun. Actual publication results establish the remote name and commit.

## Complete English and Simplified Chinese reading paths

- Preserved all 22 original Chinese Markdown documents as corresponding `.zh-CN.md` files and translated all 22 main documents into English. Both paths cover the Skill, three role handbooks, four ledger/record templates, two examples, seven references, contribution guidance, and maintenance records. Both issue templates offer the same four optional prompts.
- Added language switches and language-specific internal links. The same Skill package includes both languages, retains the `clear-engineering` invocation name, and asks the agent to use the user's preferred language. UI metadata is bilingual. Meaning changes should update the affected counterparts; users need not read both versions or file duplicate feedback.
- Reviewed translation conditions, exceptions, authorization, evidence limits, and attribution. Corrected an English feedback paragraph whose imperative wording could assign the maintainer's follow-up responsibilities to the reporter. Remaining Chinese text in English documents consists of the public project name and attributed source names.
- Checked all 48 public files: 22 document pairs and 232 local file/explicit-anchor references. Both issue frontmatters parsed; Skill UI metadata retained implicit invocation and a valid prompt. The Skill format validator returned `Skill is valid!`. Both licenses match, and all 67 distinct URLs in the evidence/source reference were preserved in each language.
- Native PowerShell UTF-8 and Python content hashes matched for all 48 files. Known private identifiers, personal paths, and credential patterns had no matches. The two example Python blocks remained identical to their originals; running the existing `check_example()` passed. Later additions to this record and its Chinese counterpart receive separate native-read and staged-content checks before committing.
- Scope is the public repository only; installed personal Skills and global settings were not changed. These results validate document coverage, local links, encoding, format, and the stated example behavior. They do not prove automatic host loading, equivalent model behavior across languages, online issue-chooser behavior, or cross-project effectiveness.
