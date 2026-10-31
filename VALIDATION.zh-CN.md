# 公开稿的验证记录

[English](VALIDATION.md) | [简体中文](VALIDATION.zh-CN.md)

对象：`0.1.3-candidate`，包括下列方法修订。本记录随相关文件维护；线上内容以已发布提交为准。

## 当前依据

- 方法修订 `CE-COMMITMENT-CHECK-20261031`（2026-10-31）更新双语[主文](skills/clear-engineering/SKILL.zh-CN.md)、[场景选择说明](skills/clear-engineering/references/01-judgment.zh-CN.md)及[虚构发布示例](skills/clear-engineering/examples/composed-publication.zh-CN.md)。关键词：原承诺、真实使用条件、反例、有限停止。修订以原需求作为判断方案的依据，并取消固定场景数量。
- 独立双语审核发现并修正了“经过审核”与“审核通过”的歧义。公开及本机安装 Skill 的 `quick_validate.py` 均通过；六个变更文件的 UTF-8 文本一致，保留安装版入口既有的双语描述。相对链接及新增文本的私人标识检查通过。
- 两个独立、无前文背景的情境检查使用更新后的入口：批量重命名方案因重新枚举已变化目录而违背确认预览，被否决并提出保留预览映射、处理目标名冲突；页面专用间距修改在已有充分 Chrome 证据时被接受，未扩大到无关测试。它们是虚构输入的推理检查，没有运行产品，也未与旧版 Skill 比较。
- 导航行为与限制在[参考 03](skills/clear-engineering/references/03-ledger-and-timeline.zh-CN.md#可选的本地自动目录)维护。
- [导航回归](skills/clear-engineering/scripts/test_build_navigation.py)于 2026-10-26 在公开及本机安装位置通过，使用独立临时材料。覆盖限定范围发现、来源与语境的变化／缺失／歧义、Markdown 解析与局部链接、标题绝对位置、读取／发现失败、源文与输出保护、跨盘渲染及输出字节／修改时间稳定。具体用例与断言保留在该脚本。
- 该次交付的 Skill 格式、公开／本机 UTF-8 一致性、双语说明、导航链接、差异格式及私人标识检查通过。接收任务随后确认真实项目的开篇语境、章节链接及局部链接筛选验收。这是接入反馈，不是实测减负数据。

## 仍适用的依据

- 研究来源、作者与许可核查见[来源说明](skills/clear-engineering/references/06-case-evidence.zh-CN.md#source-licenses)。自有内容采用 MIT；第三方许可不被替换。视频音乐与音效的许可见随附[音频素材说明](media/HUASHU-DESIGN-LICENSE.txt)，没有新增第三方实现源码。
- [单文件示例](skills/clear-engineering/examples/single-file-tool.zh-CN.md)的既有自检曾实际通过；示例行为未变，未重复运行。

## 边界

上述检查支持文件内容、格式和引用，不证明真实任务效率、宿主自动加载或跨项目有效性。文件更新不证明已打开的会话重新读取。
