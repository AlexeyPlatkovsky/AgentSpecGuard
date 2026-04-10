---
name: task-manager
description: Orchestrates non-trivial task execution. Use when a task is classified as non-trivial to select the workflow, build the execution pipeline, and produce a structured report.
---

You are orchestrating a non-trivial task. Follow these steps:

1. Accept the task classification (bugfix, feature, refactor, docs, test-only, investigation, mixed)
2. Select the matching workflow file from `.claude/workflows/`
3. Read the workflow file to get the ordered steps
4. For each workflow step, determine which skill(s) to invoke
5. Execute the pipeline by invoking skills in order
6. After execution, produce a structured task report as a markdown table:

| Field         | Value             |
|---------------|-------------------|
| Task Type     | (classification)  |
| Workflow      | (workflow file)   |
| Step          | Skill(s) Used     |

Include one row per workflow step showing which skill(s) were used.
