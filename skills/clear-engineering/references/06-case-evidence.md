# 案例、证据与迁移边界

证据基线：早期研究稿 v0.1.0。候选修订日期：2026-10-17。本轮重新核实 Git 固定提交的 `read-cache.c` 相关定义及 `c8ad9d0` 差异；第 2—4 节其余案例保留 v0.1.0 的既有阅读记录，不冒称本轮全部重读。第 5 节官方承载入口定向复核，新增专题的原始依据见第 8 节。

下文“本轮”若出现在保留的历史案例描述中，指 v0.1.0 的研究记录；本候选修订的新核实会明确写“本次修订”。区分维护者理由、源码/测试阅读、实践报告和迁移推断。未进行全库审计，未运行 Git、SQLite、Starlette 或使用方真实项目的测试。

这不是把所有开源项目的长处拼成一个架构。旧报告中的 Odoo、ERPNext、Temporal、Debezium 等仍可作为未来专题材料，但本轮没有重新核实其全部证据，不能借其名义为本版所有条目背书。v0.1.0 主要整理 Git 的具体变化链，并用不同性质的项目限制泛化；本次只修正链条中实际消费者定位等明确问题。

## 1. 深入案例：Git 的共享路径语义改变与 stash 回归

### 阅读锚点与原目标

固定源码锚点：`c8ad9d04c6a51cb5c73ebc9e42b627314eeafe2f`。它是历史研究对象，不是推荐安装的 Git 版本。

维护者在 `6e773527b6` 的提交说明中解释：把稀疏范围以外的目录用目录条目表示，以转换完整索引；转换受当时的模式与状态限制，一些命令仍需要展开后的索引。源码变更还放宽了路径校验，以支持尾部分隔符的目录条目。[G1]

这里存在两种消费者：理解特殊目录表示的索引条目构造/加入位置，以及仍依赖公共路径校验原含义的普通使用者。这个区别不是目录结构所能直接表达的。

### 实际变化与失败记录

`fc5e90b` 的作者说明指出，此前 `stash` 会忽略子仓库，相关放宽引入了回归；该提交添加一个预期失败测试。[G2]

随后 `2a1ae64` 引入内部结果分类，把普通合法、非法、带尾部分隔符目录区分开；此提交声明不打算改变外部行为。[G3]

最后 `c8ad9d0` 恢复公共校验的原含义，在条目构造和索引加入的相应校验位置接受特殊结果，并把回归测试改为预期成功。[G4]

这三个修复链提交具有可读的父子关系：`fc5e90b → 2a1ae64 → c8ad9d0`。没有从页面可靠取得全部事件日期，因此本记录不补造精确日期；研究记录日期与历史事件时间不同。

### 从完整入口追到真实消费者

在固定锚点中，静态源码可以确认以下连接：

`stash` 获取未跟踪项目名称，交给保存未跟踪内容的逻辑；该逻辑启动 `update-index` 子进程，通过标准输入传递名称，并通过 `GIT_INDEX_FILE` 指定临时索引。[G5]

`update-index` 的标准输入路径进入 `update_one`；它取得文件状态后调用公共 `verify_path`。校验不接受时会忽略路径，否则继续处理；目录处理还有自己的分支。[G6]

本次修订在固定源码与差异中复核：公共 `verify_path` 仅对 `PATH_OK` 返回真；`make_cache_entry` 和 `add_index_entry_with_check` 在相应校验处调用 `verify_path_internal`，仅拒绝 `PATH_INVALID`，因而可以接纳分类为 `PATH_DIR_WITH_SEP` 的路径。`make_transient_cache_entry` 仍调用公共 `verify_path`，不是这两处特殊接纳位置之一。[G4、G7]

这是对 v0.1.0 消费者定位的事实更正。`make_transient_cache_entry` 仅作为普通校验消费者的对照；本次没有追踪它的全部上游用途，也不将上述校验概括为所有加入/替换路径的完整检查。

因此，只查询 `stash` 的直接函数调用或只看 `read-cache.c` 的差异，会漏掉子进程、标准输入和环境指定索引串起的合作关系。本结论是基于所读源码路径的分析；目录遍历的所有文件系统分支没有穷举，实际错误输出没有运行复现。

### 测试到底支持什么

`fc5e90b` 增加的测试在一个子目录初始化仓库，再执行 `stash -u`；固定锚点的 `t/t3905-stash-include-untracked.sh` 把此情形作为成功预期。[G2、G8]

我阅读了断言文本，未执行。该新增测试主要检查这条命令能否成功结束，不能单独证明所有未跟踪内容、子仓库数据和恢复行为均正确。若本地进一步复现，值得补查保留内容和索引结果；这是验证建议，不是已有运行结果。

原引入提交还讨论了稀疏与完整表示的对照测试。[G1] 本轮没有重跑这些测试，也不能把公开合并修复当作全部平台上的验证结果。

### 本版提炼的判断

共享判断更宽容，不一定对旧消费者安全。增加局部能力时，需要辨认是能力扩展还是公共语义改变；对旧消费者维持旧含义，对理解特殊语义的位置显式提供能力，是本事件中的合适选择。

修复在原文件中完成，没有以新增模块或服务解决。由此不能推出“边界必须拆文件”，也不能推出“所有共享函数永远保持兼容”。旧消费者不存在、可整体同步迁移或旧语义本来错误时，需要不同选择。

若为这条行为建立台账，值得留下的是两类合法性含义、各自消费者、跨进程连接与回归证据，而不是所有调用图。时间线应保留放宽、发现回归、分类准备、恢复公共含义这几次认识变化；不能从最终实现倒推所有取舍最初就已想到。

### 第一手阅读位置

- [G1：引入变化 6e773527b6](https://github.com/git/git/commit/6e773527b6)
- [G2：回归测试 fc5e90b](https://github.com/git/git/commit/fc5e90b)
- [G3：内部分类 2a1ae64](https://github.com/git/git/commit/2a1ae64)
- [G4：恢复公共含义 c8ad9d0](https://github.com/git/git/commit/c8ad9d04c6a51cb5c73ebc9e42b627314eeafe2f)
- [G5：固定版本 builtin/stash.c](https://raw.githubusercontent.com/git/git/c8ad9d04c6a51cb5c73ebc9e42b627314eeafe2f/builtin/stash.c)，重点 `get_untracked_files`、`save_untracked_files`。
- [G6：固定版本 builtin/update-index.c](https://raw.githubusercontent.com/git/git/c8ad9d04c6a51cb5c73ebc9e42b627314eeafe2f/builtin/update-index.c)，重点标准输入分支、`update_one`、`process_directory`。
- [G7：固定版本 read-cache.c](https://raw.githubusercontent.com/git/git/c8ad9d04c6a51cb5c73ebc9e42b627314eeafe2f/read-cache.c)，重点 `verify_path`、`verify_path_internal`、`make_cache_entry`、`add_index_entry_with_check`；对照 `make_transient_cache_entry` 仍走公共校验。
- [G8：固定版本 t3905 测试](https://raw.githubusercontent.com/git/git/c8ad9d04c6a51cb5c73ebc9e42b627314eeafe2f/t/t3905-stash-include-untracked.sh)。

## 2. SQLite：把整体保证写成有适用范围的义务（沿用 v0.1.0 记录）

官方架构说明区分编译执行、B-tree、pager 与底层接口的责任。`version-3.47.2/src/pager.c` 开头把关键写入、同步、锁和恢复关系表达为不变量，并明确该段约束不适用于 WAL、MEMORY、OFF 等日志模式。[S1、S2]

官方测试说明介绍用替代 VFS 模拟崩溃，再检查完整性及事务完成或回滚，而不只检查函数返回值。[S3] 本轮仅阅读说明及上述源码注释，没有执行这些测试。

本版借鉴：记录重要承诺的承担关系、环境前提和对应证据。不能把数据库局部保证推广到外部系统效果，也不能把这些层和故障测试规模搬进每个小工具。

- [S1：官方架构](https://www.sqlite.org/arch.html)
- [S2：固定标签 pager.c](https://raw.githubusercontent.com/sqlite/sqlite/version-3.47.2/src/pager.c)
- [S3：官方测试说明，Crash Testing](https://www.sqlite.org/testing.html)

## 3. Starlette：用局部兼容修复限制过度设计（沿用 v0.1.0 记录）

PR #2526（页面显示合并于 2024-02-26，差异提交 `3031ee0`）从 `TestClient` 构造中删除传给 HTTPX 的弃用 `app` 参数，保留已有 transport；差异只有该文件的一行删除。[H1]

这是源码差异观察，不是本轮运行验证。它支持“识别具体依赖契约，再选择有针对性的修复”，不支持新增包装层是必要的，也不代表所有版本组合已经兼容。

- [H1：PR #2526 的差异](https://github.com/Kludex/starlette/pull/2526/files)

## 4. 项目知识组织：借鉴长处，保留不同责任（沿用 v0.1.0 记录）

| 材料 | 本轮实际看见的做法 | 本版借鉴 | 不照搬或不能证明的部分 |
|---|---|---|---|
| rust-analyzer 架构说明 | 模块代码入口、架构约束、更深材料与测试方向 | 入口不仅列位置，还解释有意不存在的依赖 | 文档主张不等于本轮源码审计；不要求相同模块结构 |
| GitLab 设计记录工作方式 | 概览、决定、按需子页，随实现吸收发现 | 设计可以从小开始，历史决定有取代关系 | 团队岗位、合并请求与组织审批不成为通用规则 |
| Codified Context 保存系统记录 | 服务责任、运行中状态与持久状态、实现锚点 | 保存难以反复推导的合作关系 | 主分支记录可能变化；未核实其全部应用代码 |
| Codified Context 掉落系统节选 | 遇理解缺口后读代码、写记录，再用于讨论 | 在真实任务中增长知识，不先建全库台账 | 精选交互不是长期效果对照证明 |
| Nygard 的 ADR | 背景、决定、后果，旧决定标为被取代 | 保存重要判断依据与演变 | 不拿 ADR 单独承担当前代码导航 |

rust-analyzer 的当前架构页面说明 `base-db` 不掌握 Cargo 的具体机制和文件路径，并给出多种实现入口。本轮把它作为作者的架构说明，而不是宣称当前全部实现满足这些约束。[R1]

GitLab 明确允许设计从一小段开始，随着探索和实现修正；关键决定和技术细节可放子页，作者选择需要的章节。[L1] 本版采用信息分层与演变方式，不采用固定团队流程。

Codified Context 的 `save-system.md` 页面自带 `last-verified: 2026-02-15` 标记；这是作者记录的状态，不是我们的验证日期。掉落系统节选展示了按任务发现知识缺口并新增说明。[C1、C2]

论文 v1 自述过旧说明引导代码走回废弃路径，并承认单人、单项目、观察性研究与未验证的跨工具迁移。[C3] 因此，本版保留按需记录，但拒绝“代理应该绝对相信文档”以及“有台账自然有效”的推论。

- [R1：rust-analyzer 架构页面](https://rust-analyzer.github.io/book/contributing/architecture.html)，动态页面，阅读日 2026-10-17，未取得本轮固定提交。
- [L1：GitLab Architecture Design Workflow](https://handbook.gitlab.com/handbook/engineering/architecture/workflow/)，动态页面，阅读日 2026-10-17。
- [C1：保存系统记录](https://github.com/arisvas4/codified-context-infrastructure/blob/main/case-study/context-docs/save-system.md)，本轮阅读 main，未固定提交。
- [C2：掉落系统交互节选](https://github.com/arisvas4/codified-context-infrastructure/blob/main/data/case-study-excerpts/cs6-drop-system.md)，本轮阅读 main，未固定提交。
- [C3：Codified Context 论文 v1](https://arxiv.org/html/2602.20478v1)，重点 5.2、5.3。
- [A1：Nygard，Documenting Architecture Decisions，2011-11-15](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)。

## 5. Skill 技术承载的依据，不等于方法效果

本版使用带 `name`、`description` 的 `SKILL.md`，把按需资料和模板保留在同一 Skill 目录；可选 `agents/openai.yaml` 表达宿主显示信息与隐式调用策略。技术格式与发现机制来自 v0.1.0 的官方阅读记录；本次修订定向重读官方 Skills 与 AGENTS.md 入口，确认此处的格式、同名不自动合并与作用域说明仍有文档依据，不更改宿主 YAML。[O1、O2]

简短工作入口可以放在现有 `AGENTS.md` 中，但它有作用域和加载时机，不保证所有子代理、每个会话或所有环境继承。详细项目事实不塞进启动说明。[O2]

- [O1：OpenAI 官方 Skills 入口](https://developers.openai.com/codex/skills/)，本轮重定向到 `learn.chatgpt.com/docs/build-skills`。
- [O2：OpenAI 官方 AGENTS.md 入口](https://developers.openai.com/codex/guides/agents-md/)，本轮重定向到 `learn.chatgpt.com/docs/agent-configuration/agents-md`。

这些是截至阅读时的公开说明，不是用户本地版本已支持的保证。加载验收必须在本地做，文件检查不能替代。

## 6. 研究材料怎样进入本版

研究方法受到花叔 Huashu 的 [女娲.skill](https://github.com/alchaincyf/nuwa-skill) 启发：从材料中辨认判断方法，整理成可使用的 Skill，再观察实际任务中的作用与局限。本库把研究对象转向软件工程案例，不沿用人物模拟、固定代理数量或评分结论；没有收录女娲的原 Skill、模板、脚本或图片。作者、许可与具体借鉴范围统一见[来源及许可核对](#source-licenses)。

早期研究稿整理了变化、状态、授权、提交与效果、存量和验证等关注点。公开稿保留可说明判断依据的内容及其来源性质；历史材料提到某个项目，不代表已重新核实其全部机制。

公开源码案例、维护者说明和实践报告分别标出阅读范围与固定版本条件。未重新核实的结论保留原证据边界，不因为公开整理而升级为新的验证结果。

不同入口可以采用符合各自边界的实现方式，不要求机械调用同一位置。实际使用方仍需沿自己的入口、状态与消费者核实适用性；说明性示例不能代替真实项目的行为验证。

## 7. 证据不足时的方法地位

现有真实案例较强地支持共享契约回归、局部兼容修复和知识组织；尚不足以声称已完成“大型项目整体架构形成与持续演变”的充分研究或迁移验证。这不阻止在明确边界下开始使用，也不要求本轮补齐大型案例。

有代码案例支持某条判断，不等于本版表达能可靠触发模型，也不等于跨项目长期有效。这里的推理关系是可使用、可修订的初版。与实际情况不符时，保留反例，缩小适用条件或删减条目；不靠更多历史例子给任何结论补充事后理由。

<a id="technical-sources"></a>

## 8. 本次修订新增技术主张的定向依据

阅读日期：2026-10-17。下列为官方文档/规范的阅读，不是源码全审计或运行测试；它们分别支持具体限制，不能合并宣称整套工程方法已验证。专题中的组织与取舍为本候选的工程建议，可由本地反例修正。

| 编号与第一手入口 | 直接支持的事实 | 使用边界 |
|---|---|---|
| [T1：Flask 3.1.x 请求上下文](https://flask.palletsprojects.com/en/stable/reqcontext/) | 请求上下文局部可用；在上下文之外访问相关代理会报错 | 框架行为，不推广为所有语言/框架；不证明任意后台委托已经合法 |
| [T2：Python 3.11 asyncio，Task Cancellation](https://docs.python.org/3.11/library/asyncio-task.html#task-cancellation) | 取消时建议清理资源，显式捕获取消后通常应传播；吞掉取消可能影响相关机制 | 不保证进程崩溃后的清理或远端效果撤销 |
| [T3：OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | 最小权限以及逐请求授权检查的官方安全建议 | 指南，不是本地策略正确性证明；独立发布/业务委托仍需实际策略 |
| [T4：RFC 9111 §3.5](https://www.rfc-editor.org/rfc/rfc9111.html#section-3.5) | 对带 Authorization 请求的共享 HTTP 缓存复用规定限制和例外 | 不是应用缓存权限隔离或即时撤权的完整方案 |
| [T5：PostgreSQL 17 §47.2.2](https://www.postgresql.org/docs/17/logicaldecoding-explanation.html#LOGICALDECODING-REPLICATION-SLOTS) | 逻辑解码位置在检查点持久化，崩溃后近期变化可能重发，消费者需处理重复 | 单个来源的机制，不能当作所有事件都有相同顺序保证 |
| [T6：Stripe webhook，Event ordering](https://docs.stripe.com/webhooks#event-ordering) | 交付不保证按产生顺序；时间戳不足以独自承担去重或排序 | 动态接口文档，本轮未固定 SDK/API 版本，未调用服务；用于说明应核对来源能力 |
| [T7：RFC 9110 §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) 与 [§13.1.1](https://www.rfc-editor.org/rfc/rfc9110.html#section-13.1.1) | 非幂等请求自动重试的条件，以及 If-Match 的条件请求语义 | HTTP 规范，不代表对端已实现或某个业务操作因此具备绝对一次效果 |

这些链接用于核实新增段落中的具体技术主张，不扩展为新的开源项目研究清单。v0.1.0 的大型架构证据限制继续保留；真实使用、加载和长期收益仍需各自取得证据。

<a id="source-licenses"></a>

## 9. 第三方来源、署名与许可核对

核对日期：2026-10-18。范围是本公开稿的 Skill、台账方法与起始稿、手册、示例及其中提及的研究材料，不是某个业务项目的依赖审计。作者栏采用原文署名或公开维护方；多人合作的项目不强行归功于一人，具体提交、文件和文档的署名仍以原来源为准。

### 已进入方法、案例或技术说明的来源

| 项目或材料与地址 | 作者／公开维护方 | 本库采用什么、位置在哪里 | 核实到的许可及第一手依据 |
|---|---|---|---|
| [女娲.skill / nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | 花叔 Huashu（alchaincyf） | 第 6 节的研究方法启发；未收录上游 Skill、模板或媒体 | [MIT；版权行 2026 Huashu（花叔）](https://raw.githubusercontent.com/alchaincyf/nuwa-skill/main/LICENSE) |
| [Git](https://github.com/git/git) | Git 贡献者；本例引入提交作者 Derrick Stolee，回归测试与修复作者 René Scharfe，相关提交由 Junio C Hamano 集成 | 第 1 节的提交链、行为分析及文件／符号定位；没有附带 Git 实现或测试文件 | [所引固定版本 COPYING：GPL v2，除非另有明确声明](https://raw.githubusercontent.com/git/git/c8ad9d04c6a51cb5c73ebc9e42b627314eeafe2f/COPYING) |
| [SQLite](https://www.sqlite.org/) | Richard Hipp 及 SQLite 作者与维护者 | 第 2 节的架构、不变量与测试方法概括 | [交付代码及文档为公有领域；构建脚本等可能另有许可](https://www.sqlite.org/copyright.html) |
| [Starlette](https://github.com/Kludex/starlette) | Encode OSS Ltd 及贡献者；[本例 PR 作者 osoken](https://github.com/Kludex/starlette/pull/2526) | 第 3 节的局部兼容修复分析；没有复制实现片段 | [所引 3031ee0 版本 LICENSE.md：BSD-3-Clause](https://raw.githubusercontent.com/Kludex/starlette/3031ee0/LICENSE.md) |
| [rust-analyzer 架构文档](https://rust-analyzer.github.io/book/contributing/architecture.html) | The rust-analyzer authors | 第 4 节的责任、入口及依赖组织借鉴 | [主仓库说明 MIT／Apache-2.0 双许可](https://github.com/rust-lang/rust-analyzer#license)；未见所引架构页另行声明许可 |
| [GitLab Architecture Design Workflow](https://handbook.gitlab.com/handbook/engineering/architecture/workflow/) | GitLab 与 Handbook 贡献者 | 第 4 节对工作方式的概括与方法启发；没有收录原页面或其模板 | [Handbook 明确采用 CC BY-SA 4.0](https://handbook.gitlab.com/handbook/about/handbook-usage/#external-use-of-the-handbook)；不能用软件根目录的 MIT 声明替代 |
| [Codified Context 配套仓库](https://github.com/arisvas4/codified-context-infrastructure) | Aris Vasilopoulos；许可证版权行署名 Aris | 第 4 节对保存系统记录及交互节选的分析；借鉴按需积累知识，未收录其记录、代理或 MCP 实现 | [MIT](https://raw.githubusercontent.com/arisvas4/codified-context-infrastructure/main/LICENSE)；[CITATION.cff](https://github.com/arisvas4/codified-context-infrastructure/blob/main/CITATION.cff) 请求引用论文 |
| [Codified Context 论文 v1，arXiv:2602.20478v1](https://arxiv.org/abs/2602.20478v1) | Aristidis Vasilopoulos（配套仓库署名 Aris Vasilopoulos） | 第 4 节对观察报告及其局限的中文概括；未收录论文、图或原文段落 | 论文入口的许可链接为 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)；与仓库 MIT 分开记录 |
| [Documenting Architecture Decisions，2011-11-15](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | Michael Nygard；发布方 Cognitect | 第 4 节以及台账方法中的背景、决定、后果和取代关系；本库记录片段另行组织 | 原页面就本文明示在法律允许范围内放弃版权及相关权利；该声明不扩大到整个站点 |
| [Flask 请求上下文文档](https://flask.palletsprojects.com/en/stable/reqcontext/) | Pallets 及 Flask 贡献者 | T1 与参考 07·A2 的特定框架行为概括 | [Flask 文档许可页：BSD-3-Clause](https://flask.palletsprojects.com/en/stable/license/) |
| [Python 3.11 asyncio 文档](https://docs.python.org/3.11/library/asyncio-task.html#task-cancellation) | Python Software Foundation 及 Python 贡献者 | T2 与参考 07·A3 的取消和清理建议；本库单文件示例使用标准库 API，没有附带 Python 实现 | [软件／文档适用 PSF License Agreement；文档中的示例代码另可选 0BSD](https://docs.python.org/3.11/license.html) |
| [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | OWASP Cheat Sheet Series 贡献者 | T3 与参考 07·B 的授权建议概括和进一步工程分析；没有收录原文、图或清单 | [Cheat Sheet Series：CC BY-SA 4.0](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/master/LICENSE.md) |
| [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html) 与 [RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html) | 编辑 Roy T. Fielding、Mark Nottingham、Julian Reschke；IETF Trust 及文档作者 | T4／T7 与参考 07 对规范语义的概括；没有复制规范正文或代码组件 | 各 RFC 版权段明确适用 BCP 78 和发表时的 [IETF Trust 法律条款](https://trustee.ietf.org/license-info)；提取代码组件另须遵守所述 Revised BSD 条件 |
| [PostgreSQL 17 逻辑解码文档](https://www.postgresql.org/docs/17/logicaldecoding-explanation.html#LOGICALDECODING-REPLICATION-SLOTS) | PostgreSQL Global Development Group；许可页另保留加利福尼亚大学董事会的部分版权 | T5 与参考 07·C2 对重复交付条件的概括 | [PostgreSQL 17 文档许可说明](https://www.postgresql.org/docs/17/legalnotice.html)：PostgreSQL License，覆盖软件和文档 |
| [Stripe webhook 文档](https://docs.stripe.com/webhooks#event-ordering) | Stripe 及其文档作者／权利人 | T6 与参考 07·C2 对交付顺序事实的概括；没有收录 SDK 或文档段落 | 未确认该网页采用通用开源许可；[官方条款](https://stripe.com/legal/ssa)保留文档权利并限制复制／再分发，不以 SDK 的许可证推定网页许可 |
| [OpenAI Skills](https://learn.chatgpt.com/docs/build-skills) 与 [AGENTS.md 文档](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | OpenAI | 第 5 节的格式及承载机制说明；没有附带客户端、生成器或网页正文 | 所引页面未见明确通用开源许可；按[官方条款](https://openai.com/policies/terms-of-use/)区分服务、文档、输出及第三方内容，不把开源工具的许可推及站点全部文本 |

表中的中文概括和工程迁移分析由本库整理，不是原作者的逐字陈述；具体来源性质仍按前文区分。署名与链接不表示原作者参与、认可或为本项目担保。

### 仅提及、未作为本版实现或直接研究依据的项目

以下几项在前文作为历史材料或案例依赖出现，也补足身份和许可位置。这里只核对公开主仓库的许可现状；不能冒充已核实早期研究所用版本、所有插件或商业发行版。

| 项目与地址 | 作者／公开维护方 | 当前稿中的用途 | 许可核对 |
|---|---|---|---|
| [Odoo Community](https://github.com/odoo/odoo) | Odoo 及贡献者 | 开头的历史背景提及；未收录代码或模板 | [19.0 主仓库 LGPL v3；单独第三方文件可能不同](https://raw.githubusercontent.com/odoo/odoo/19.0/LICENSE)；不涵盖 Enterprise |
| [ERPNext](https://github.com/frappe/erpnext) | Frappe／ERPNext 贡献者 | 开头的历史背景提及；未收录代码或模板 | [主仓库 GPL v3](https://raw.githubusercontent.com/frappe/erpnext/develop/license.txt) |
| [Temporal](https://github.com/temporalio/temporal) | Temporal Technologies Inc.、Uber Technologies, Inc. 及贡献者 | 开头的历史背景提及；未收录服务端、SDK 或工作流实现 | [服务端主仓库 MIT](https://raw.githubusercontent.com/temporalio/temporal/main/LICENSE)；其他组件另查 |
| [Debezium](https://github.com/debezium/debezium) | Debezium 社区与贡献者 | 开头的历史背景提及；未收录连接器或其他实现 | [主仓库 Apache-2.0](https://raw.githubusercontent.com/debezium/debezium/main/LICENSE.txt) |
| [HTTPX](https://github.com/encode/httpx) | Encode OSS Ltd 及贡献者 | 第 3 节 Starlette 案例中的依赖名称；没有单独提炼其实现 | [主仓库 BSD-3-Clause](https://raw.githubusercontent.com/encode/httpx/master/LICENSE.md) |

### 当前判断与后续复用边界

本次检查未发现随包分发上述项目的实现、图片、原始记录或大段原文；未发现明确违反已核实许可的复制内容。此前缺少统一作者／许可说明以及女娲方法启发署名，本节补足可核实的出处。该判断针对当前文本及能找到的直接来源，不是全量相似性鉴定，也不替代权属认定。

研究软件行为、概括事实和借鉴方法，不自动使本库采用所研究软件的许可证；但翻译、改写或由 AI 整理，也不自动排除受保护表达的复制或改编。区分依据见 [WIPO 对思想与表达的说明](https://www.wipo.int/en/web/copyright/protection)和 [Creative Commons 对改编的说明](https://creativecommons.org/faq/#when-is-my-use-considered-an-adaptation)。

以后真正纳入第三方代码、原文、译文、图或模板时，应就纳入部分保留具体来源、版本、修改说明及原许可要求的版权、许可和免责声明。MIT／BSD 等许可要求的通知不能只用一个来源链接代替；复制或实质改编 CC BY-SA 内容时，应保留署名、许可、修改说明，并为相应改编内容遵守相同方式共享要求。不能把这些内容一并宣称为本库自有、统一改授 MIT。未确认许可的网页不作为可任意复制材料。

本库有权授权的自有内容采用 [MIT](../LICENSE)，公开署名为 KZ；该选择不替代本节列明的第三方许可，也不代表已公开发布。新增真正采用的来源时在此补充相应行；只使用某个制作或检查工具，不等于分发该工具本身，无需把全部环境工具列为方法来源。
