# 收手吧阿祖

[English](README.md) | [简体中文](README.zh-CN.md)

把事情做清楚，做到足够就停。

一套用于 AI 辅助软件工作的工程判断 Skill 与配套手册。帮助理解目标与现有实现、明确职责和状态、追踪真实消费者、验证变化，并留下足以接续的记录。

Practical engineering judgment for AI-assisted software work: understand the goal, trace real consumers, verify behavior, and leave useful context for the next contributor.

**当前状态：** `0.1.3-candidate` 公开候选版。维护者公开署名为 **KZ**，自有内容采用 [MIT](LICENSE)。当前只有少量使用反馈与说明性案例，跨项目、跨使用者的长期效果仍待检验。

## 60 秒认识阿祖

[![观看收手吧阿祖介绍视频](media/shoushouba-azu-intro-cover.jpg)](media/shoushouba-azu-intro-60s.mp4)

[▶ 观看视频](media/shoushouba-azu-intro-60s.mp4) · 中文 · 60 秒 · [音频素材署名与许可](media/HUASHU-DESIGN-LICENSE.txt)

改个人标签，为什么会影响另一个用户登录？看一个在隔离测试中复现并修复的真实案例，以及怎样借助台账定位代码、接续工作。

## 两套完整阅读路径

英文文档使用 `.md`，简体中文对应稿使用 `.zh-CN.md`。Skill、角色手册、台账模板、示例、参考资料和反馈说明均提供两种语言，每份文档都可切换到对应版本。

两种语言放在同一个 `skills/clear-engineering/` 包中，只需安装一次。宿主发现入口仍为 `SKILL.md`，完整中文阅读入口为 `SKILL.zh-CN.md`。代理按用户偏好的语言沟通，按需阅读对应语言的资料。

## 从哪里开始

- 希望代理使用方法：阅读 [Skill 主文](skills/clear-engineering/SKILL.zh-CN.md)，再按当前问题进入参考资料。
- 希望了解如何组织工作：阅读[调度手册](handbook/coordination.zh-CN.md)、[执行手册](handbook/execution.zh-CN.md)或[审核手册](handbook/review.zh-CN.md)。这是责任视角，可以由同一人承担，不要求创建三个代理或三轮审批。
- 想看小项目如何使用：阅读[单文件小工具](skills/clear-engineering/examples/single-file-tool.zh-CN.md)和[组合行为示例](skills/clear-engineering/examples/composed-publication.zh-CN.md)。案例均为说明性虚构。
- 需要项目接续：按需使用[台账方法](skills/clear-engineering/references/03-ledger-and-timeline.zh-CN.md)与 [assets 中的起始稿](skills/clear-engineering/assets/project-ledger.zh-CN.md)，已有记录足够时更新原处。
- 关心实际作用：阅读[使用与观察说明](skills/clear-engineering/references/05-usage-and-evaluation.zh-CN.md)、[研究依据、作者与许可边界](skills/clear-engineering/references/06-case-evidence.zh-CN.md)和[本仓库验证记录](VALIDATION.zh-CN.md)。

## 怎样使用

`skills/clear-engineering/` 是完整的 Skill 内容目录。需要安装时，按所用宿主当前支持的方式安装该子目录；也可以直接读取主文，将其作为当前任务的工作方法。安装、启用和修改个人配置由使用者按自己的环境与授权决定。

文件可读、技能被发现、正文被读取、判断得到改善是不同事实。通用正文不保证所有代理工具都自动加载，也不保证读过就会做对。其他宿主的加载与继承方式应在实际环境核实。

日常从当前目标、有效项目入口和任务停点开始，按问题展开。已有认识、能力、审核和证据仍然适用时复用；操作前明确必要条件与检查办法，结果在对应动作后取得。足够证据支持本次承诺后停止。

## Skill 与手册怎样联动

通用判断及记录语义以 Skill 主文和它的参考资料为主要说明；手册提供对应角色的使用情境。审核机制的适用与授权边界见[审核手册](handbook/review.zh-CN.md)，具体项目仍遵守自己的约定。

本仓库提供通用内容，使用方的系统地址、模型偏好、运行参数和生产约束保留在自己的项目配置中。没有某种规模、技术栈或代理角色数量是使用本方法的前提。

## 希望收到怎样的反馈

我们尤其想听到：“我照着做了，事情反而更难推进了。”帮助、遗漏、误触发、重复工作和删减建议都值得记录。请尽量讲清哪句话影响了什么行动，以及实际发生了什么；结果还没出来或尚未实际使用，也可以如实说明。

欢迎[提交使用经历或反例](https://github.com/KrisZhao23/shoushouba-azu/issues/new?template=use-case.zh-CN.md)，也可以只写几句话。[案例反馈模板](.github/ISSUE_TEMPLATE/use-case.zh-CN.md)可按需删减。无需公开源码、公司信息、完整台账或聊天，也不要求先准备补丁。反馈的处理与案例收录方式见 [CONTRIBUTING.md](CONTRIBUTING.zh-CN.md)。

## 研究与许可状态

本项目由维护者与 AI 助手协作整理，包含来自公开源码、测试、设计记录和实践报告的研究。原作者的理由、源码观察、实践报告与本项目的迁移推断分别保留，引用不代表原项目认可本方法。

方法研究受到花叔 Huashu 的女娲.skill 启发。各项实际研究、技术说明和仅提及项目的作者、地址、许可及采用范围统一见[第三方来源与许可核对](skills/clear-engineering/references/06-case-evidence.zh-CN.md#source-licenses)。该清单随 Skill 一起保留；引用不改变第三方许可，署名不能替代复用所需的许可条件。

本仓库有权授权的 Skill、手册、台账模板与示例代码采用 [MIT](LICENSE)，版权声明为 `Copyright (c) 2026 KZ`；第三方材料仍遵循各自许可。Skill 子目录附有相同的 [LICENSE](skills/clear-engineering/LICENSE)，单独分发时应一并保留。欢迎分享改进与使用经历，反馈是自愿的，不是许可附加条件。
