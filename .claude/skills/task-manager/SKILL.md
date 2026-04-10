---
name: task-manager
description: Orchestrates non-trivial task execution. Use when a task is classified as non-trivial to select the workflow, build the execution pipeline, and produce a structured report.
---

Build the execution pipeline for a non-trivial task:

1. Accept the task classification.
2. Read the matching workflow file from `.claude/workflows/`.
3. Use the workflow step order as the source of truth.
4. Map each step to the skill or subagent needed for the task.
5. Execute the pipeline in workflow order.
6. For non-trivial code tasks, include `code-reviewer` during validation.
7. Produce a task report with:
   - a metadata table containing `Task Type` and `Workflow`
   - a steps table containing `Step | Used`
