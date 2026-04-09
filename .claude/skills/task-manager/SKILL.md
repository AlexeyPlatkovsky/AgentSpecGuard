# Skill: task-manager

## Purpose

Orchestrates non-trivial task execution by selecting the appropriate workflow and building the execution pipeline.

## When Used

Invoked for every non-trivial task after classification.

## Inputs

- Task description
- Task classification (bugfix, feature, refactor, docs, test-only, investigation, mixed)

## Outputs

- Selected workflow file path
- Ordered execution pipeline (skills to invoke per workflow step)
- Structured task report (markdown table with task type, workflow name, steps with used skills)
