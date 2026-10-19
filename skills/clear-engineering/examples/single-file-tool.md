# 单文件小工具：充分理解，不强制拆分

以下业务、文件名、符号与 EX 事件全部为说明性虚构，不对应真实用户代码。两个代码块可组成一个离线示例；实际是否运行及结果应以使用方的验证记录为准，不把示例检查当作真实项目验证或维护成本证明。

## 可以合在一份说明里的当前台账

项目：任务状态报表。目标是界面与导出在相同事实和同一比较日期下采用同一政策。当前只有一个输入来源，不需要为“未来多个来源”先建插件结构。

整体合作：在虚构的 `report.py` 中，`parse_task` 解释来源字段；`state_for` 接收已经明确的数据和比较日期；`show_report` 与 `export_report` 组织不同输出。都留在一个文件，没有接口家族。真实项目也可以用一个清楚的共享函数承担解析和计算；下面分开写是为了展示变化落点，不据此认定更低维护成本。

示例内已接受约定（虚构）：同一比较日期下，完成日期不晚于比较日期则为 completed；否则截止日期早于比较日期则为 overdue；其他为 open。截止当天不算逾期。历史日期导出与今天界面可以不同，不能要求它们总显示相同状态。完成日期与截止日期都是日期，不是要自动换算的时刻。

限制：只有一次完成、没有重开/撤销历史；它按当前已知事实回算指定日期，不复原“当时系统知道什么”。`completed_on` 的 None 在这个例子中明确表示“当前没有完成事实”；缺失字段不能自动解释成 None。真实来源语义不同就需要重新判断。

代码导航：同一假设文件里的解析、共享规则与两个输出入口。输出仅是可交给呈现/序列化部分的 Python 值，不是真实屏幕、CSV 文件或授权实现。未展示的批量、持久化和安全策略不视为已解决。

<a id="code-example"></a>

## 少量代码：明确输入，而不搭建应用

两个 Python 代码块可按顺序放在同一临时文件运行，需 Python 3.10 或以上；只用标准库，没有网络或文件写入。没有在默认参数或规则内部读取当前时钟。函数签名用于展示责任，不是通用的必需拆分方式。

```python
from dataclasses import dataclass
from datetime import date
from typing import Mapping
import re


@dataclass(frozen=True)
class Task:
    task_id: str
    due: date
    completed_on: date | None


def parse_date(value: object) -> date:
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
        raise ValueError("date must use YYYY-MM-DD")
    return date.fromisoformat(value)  # Invalid calendar dates also raise ValueError.


def parse_task(row: Mapping[str, object]) -> Task:
    if not {"id", "due", "completed_on"}.issubset(row):
        raise ValueError("id, due and completed_on are required")
    task_id, completed = row["id"], row["completed_on"]
    if not isinstance(task_id, str) or not task_id.strip():
        raise ValueError("id must be a nonempty string")
    return Task(task_id, parse_date(row["due"]),
                None if completed is None else parse_date(completed))


def state_for(task: Task, *, as_of: date) -> str:
    if type(as_of) is not date:  # Do not silently mix datetime and date semantics.
        raise TypeError("as_of must be a date")
    if task.completed_on is not None and task.completed_on <= as_of:
        return "completed"
    return "overdue" if task.due < as_of else "open"


def show_report(task: Task, *, as_of: date) -> dict[str, str]:
    return {"id": task.task_id, "status_text": state_for(task, as_of=as_of)}


def export_report(task: Task, *, as_of: date) -> tuple[str, str]:
    return task.task_id, state_for(task, as_of=as_of)
```

这里规则依赖的是有意义的 `Task` 和 `as_of`，而不是当前用户、原始字段名或全局时钟。Task 应由可信构造位置提供合法字段；类型标注不是运行时自动校验，绕过解析直接构造对象的其他入口仍需遵守相同数据契约。选择日期的入口也应说明业务日历和用途，不是由内部函数随意选择“今天”。

## 一个有区分力的组合检查

下面不是只比较两个入口互相相等，还分别与政策预期比较，避免两个入口一起错误也通过。一次调用覆盖截止日、逾期日、完成日及显式的来源格式解释；错误输入必须被拒绝。

```python
def check_example() -> None:
    raw = {"id": "T-1", "due": "2026-10-15", "completed_on": "2026-10-17"}
    task = parse_task(raw)
    for day, expected in [(15, "open"), (16, "overdue"), (17, "completed")]:
        as_of = date(2026, 10, day)
        assert show_report(task, as_of=as_of)["status_text"] == expected
        assert export_report(task, as_of=as_of)[1] == expected

    # A hypothetical source renames only the field; its meaning stays unchanged.
    renamed = {"id": "T-1", "deadline": "2026-10-15", "completed_on": "2026-10-17"}
    normalized = {"id": renamed["id"], "due": renamed["deadline"],
                  "completed_on": renamed["completed_on"]}
    assert parse_task(normalized) == task

    invalid_rows = [
        {"id": "T-1", "due": "2026-10-15"},  # Missing is not equivalent to None.
        {**raw, "completed_on": "false"},
        {**raw, "due": "2026-02-30"},
    ]
    for bad in invalid_rows:
        try:
            parse_task(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"invalid input was accepted: {bad!r}")


if __name__ == "__main__":
    check_example()
    print("PASS: illustrative date policy, two outputs, field mapping, invalid input")
```

这组输入能区分“尊重传入日期”与“内部固定使用某一天”，也能识别一个入口绕过共享完成判断。它不证明所有日期、输入或历史情况正确，更不能证明拆开的函数比清楚的共享函数更省维护成本。示例片段检查也不等于真实业务环境验证。

## 两类变化怎样找到落点

只有 `due` 改名为 `deadline`、含义不变时，可以调整来源解释位置；检查保留同一个 Task 和政策结果。上面的局部归一化只是说明这一点，不是建立通用字段映射引擎，也没有证明真实来源只改了名字。

若业务改成“截止日当天就算逾期”，则共享规则的比较和截止日预期需要按新约定变化，两种输出继续核实。若来源把截止日期变成有时区的截止时刻，则不再是单纯字段映射，应重审数据含义和比较策略。不能为了让旧断言通过而无依据改预期。

## 简短时间线也能保留关键演变

EX-01，发生时间未设定：虚构项目接受“相同数据/日期下同政策”的方向。不对应真实项目接受。

EX-02，后续虚构需求：增加历史日期导出。保留共享政策，调整入口日期来源；不把导出与今天界面结果相同作为要求。

EX-03，待观察：若增加第二来源后，字段变化反复影响业务判断，再比较转换函数与当前组织。不能事后认定最初就必须拆分。

上述是示例项目的时间线。实际运行片段属于示例检查，记录在对应验证说明中，不回填为 EX 事件已经在业务环境发生。

## 当前任务的接续点

示例内的工作是假设“接入历史日期输入”。真实接手者应先读自己的两个入口怎样取得日期，再确认规则是否暗读时钟。这里只交付说明性片段，不代表用户代码已改、测试已补或任务已完成。

## 从这个例子保留什么

一个文件可以承担清楚责任，记录也可以合在一份说明中。能接续的关键是共同政策、输入含义、位置和证据边界，而不是 class 清单。真实项目已有等效注释与 README 时，只增加缺失关系和当前停点。代码展示用于理解判断，不作为必须照抄的实现。
