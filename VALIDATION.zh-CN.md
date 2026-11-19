# 公开稿的验证记录

[English](VALIDATION.md) | [简体中文](VALIDATION.zh-CN.md)

对象：`0.1.3-candidate`，包括下列方法修订。本记录随相关文件维护；线上内容以已发布提交为准。

## 当前依据

- 已核对中英文主文的审核自问：对照送审做法判断预期结果，说明追加检查的依据，并在审结时写清通过的事项及实际检查的起止范围。源文和本机安装版的问句一致，两处 Skill 均通过 `quick_validate.py`。将公开版 `SKILL.md` 安装到项目中后，Codex 重新扫描并将它列为已启用。台账中关于决定变更和任务收尾的问句均与本机安装版的中英文正文一致。调度手册中批准方案前的问句已核对中英文，中文与现用调度手册一致。修改后，Codex 强制重扫仍将用户安装版列为已启用。

- 双语[主文](skills/clear-engineering/SKILL.zh-CN.md)和[台账说明](skills/clear-engineering/references/03-ledger-and-timeline.zh-CN.md#frozen-audit-records)的既有检查覆盖审单首行与复审范围、操作结果与固定原证、待办与交接缺口、停止扩读、单写与共写的选择、条目归属和会话 ID。本轮核对覆盖当前结果与后续安排、撤下失效说明、审核引用与冻结原件、哈希用途、版本比较与依据复用、部分保存失败，以及兼顾截图附件引用的局部文字修改。八个源文与安装文件的替换文字均已核对，新句无重复、被替代旧段已移除，三个原有锚点保留。源文与安装版相关正文一致，安装入口既有双语描述保留；UTF-8 读取、`git diff --check` 和两处 Skill 的 UTF-8 模式 `quick_validate.py` 均通过。具体写入工具和工程哈希范围未作规定；使用效果留待试行。

- 方法修订 `CE-RECORD-IN-PLACE-20261103` 更新双语[主文](skills/clear-engineering/SKILL.zh-CN.md)和[维护说明](skills/clear-engineering/references/03-ledger-and-timeline.zh-CN.md#record-updates)：合并相关信息、原位修正说明，按实际对象与条件更新验证结论和原证引用，不按消息或操作逐条追加。独立双语差量审核未发现维护时点或证据保留边界改变。公开及本机安装 Skill 的 `quick_validate.py` 均通过；四个变更文本一致，安装版英文前置信息保留。这些检查不证明实际工作量减少或接续改善。
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
