# Benchmark Scoring Rules

## 1. Workflow Compliance

- All required steps for the task type must be present in the task report
- Steps must appear in correct order
- Each step must reference at least one skill or subagent used
- Score: 0–100 (percentage of steps correctly completed)

## 2. Skill Usage

- Required skills (from golden file) must be invoked
- No unnecessary skill invocations
- Score: 0–100 (percentage of required skills used correctly)

## 3. Schema Validation

- Structured output must match expected format
- Task type, workflow name, and steps table must be present
- Score: pass/fail

## 4. Token Usage

- Total tokens consumed during task execution
- Measured per task and aggregated per benchmark run
- Used for drift detection across models and versions
