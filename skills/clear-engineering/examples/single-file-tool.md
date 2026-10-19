# A single-file tool: understand enough without forcing a split

[English](single-file-tool.md) | [简体中文](single-file-tool.zh-CN.md)

The business scenario, filenames, symbols, and EX events below are all illustrative fiction and do not correspond to real user code. The two code blocks form one offline example. Whether it was actually run, and with what result, must be established by the user's validation record. Example checks are not real project verification or proof of maintenance costs.

## A current ledger that fits in one document

Project: a task status report. The goal is for the display and export to apply the same policy to the same facts and comparison date. There is currently one input source, so no plugin structure is needed for hypothetical future sources.

How the whole works together: in the fictional `report.py`, `parse_task` interprets source fields; `state_for` receives explicit data and a comparison date; `show_report` and `export_report` organize different outputs. Everything stays in one file, without a family of interfaces. A real project could also use one clear shared function for parsing and calculation. They are separated below to illustrate where changes belong, not to establish lower maintenance costs.

Agreement accepted within the fictional example: for a given comparison date, the status is completed if the completion date is no later than that date; otherwise it is overdue if the due date is earlier than the comparison date, and open otherwise. The due date itself is not overdue. An export for a historical date can differ from today's display; they need not always show the same status. Completion and due dates are dates, not instants to convert automatically.

Limits: there is only one completion, with no history of reopening or reversal. The rule calculates status for a specified date using currently known facts; it does not reconstruct what the system knew at that time. In this example, `None` for `completed_on` explicitly means "there is currently no completion fact." A missing field must not automatically be interpreted as `None`. Different source semantics require reassessment.

Code navigation: parsing, a shared rule, and two output entry points in the same hypothetical file. Outputs are only Python values that could be passed to presentation or serialization code; they are not a real screen, CSV file, or authorization implementation. Batch processing, persistence, and security policies that are not shown are not thereby solved.

<a id="code-example"></a>

## A little code: explicit inputs without an application framework

Place the two Python blocks in order in one temporary file to run them with Python 3.10 or later. They use only the standard library and perform no network access or file writes. Neither default arguments nor the rule read the current clock. Function signatures illustrate responsibilities, not a universally required way to split code.

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

The rule depends on a meaningful `Task` and `as_of`, rather than the current user, raw source field names, or a global clock. Trusted construction sites should provide valid `Task` fields. Type annotations do not perform automatic runtime validation; other entry points that construct objects directly without parsing must still obey the same data contract. The entry point choosing a date should explain the business calendar and purpose; an internal function should not choose "today" arbitrarily.

## One discriminating check of the combined behavior

The following checks each output against the policy's expected result instead of merely comparing the two entry points with each other, which could pass when both are wrong. A single call covers the due date, an overdue date, the completion date, and explicit interpretation of the source format. Invalid input must be rejected.

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

These inputs distinguish respecting the supplied date from using one fixed day internally, and can detect an entry point bypassing the shared completion check. They do not establish correctness for all dates, inputs, or historical situations, nor do they prove that separate functions cost less to maintain than a clear shared function. Checking these snippets is not verification in a real business environment.

## Finding the right place for two kinds of change

If only the field name changes from `due` to `deadline` and its meaning stays the same, adjust the source interpretation and check that it preserves the same Task and policy results. The local normalization above illustrates that point; it is not a general field-mapping engine and does not establish that a real source changed only the name.

If the business rule changes to "overdue on the due date itself," update the shared rule's comparison and the due-date expectation under the new agreement, and continue checking both outputs. If the source changes a due date into a timezone-aware deadline instant, that is no longer a simple field mapping; revisit the data meaning and comparison policy. Do not change expectations without a basis just to make old assertions pass.

## A short timeline can preserve key developments

EX-01, occurrence time unspecified: the fictional project accepts the direction "same policy for the same data and date." This is not acceptance by a real project.

EX-02, a subsequent fictional requirement: add export for historical dates. Preserve the shared policy and adjust where the entry point obtains its date. Do not require the export to match today's display.

EX-03, pending observation: if adding a second source causes field changes to repeatedly affect business judgments, compare conversion functions with the current organization. Do not conclude afterward that a split was mandatory from the outset.

This is the example project's timeline. Actually running the snippets is an example check, recorded in the corresponding validation notes; it does not retroactively make the EX events facts that occurred in a business environment.

## Current task continuation point

The hypothetical task in this example is to accept a historical date as input. A real successor should first read how their own two entry points obtain dates, then confirm whether the rule reads the clock implicitly. This example provides illustrative snippets; it does not mean the user's code has been changed, tests have been added, or the task is complete.

## What to retain from this example

One file can hold clear responsibilities, and one document can hold the records. Shared policy, input meaning, locations, and evidence boundaries make continuation possible; a class inventory does not. If a real project already has equivalent comments and a README, add only missing relationships and the current checkpoint. The code helps explain the judgment; it is not a required implementation to copy.
