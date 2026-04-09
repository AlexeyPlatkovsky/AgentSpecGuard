# idea.md

## Project Name
AgentSpecGuard

---

## Core Idea

AgentSpecGuard is a reusable template that standardizes how AI agents perform development tasks across any repository.

The goal is to make AI behavior:

- predictable
- structured
- testable
- comparable across models

This is not an application.
It is a portable agent operating layer.

---

## Key Objectives

1. Enforce a consistent workflow for all AI-driven tasks
2. Ensure structured, machine-verifiable outputs
3. Provide a modular skill system
4. Keep AI execution surface minimal (KISS)
5. Detect and measure behavioral drift across models and versions
6. Measure token usage (token drain) and pipeline quality via benchmark

---

## System Components

### 1. AGENTS.md (Root Entry Point)

Defines:

- project identity
- task classification
- trivial vs non-trivial routing
- skill selection rules (short table)
- subagent usage rules

Must remain:

- compact
- stable
- routing-only
- free of execution logic
- free of benchmark logic

---

### 2. Skills

Location:
.claude/skills/

Responsibilities:

- execute atomic actions
- implement workflow steps

Rules:

- if a skill matches a task → it MUST be used
- skills are binding
- skills must be minimal and composable
- skills must NOT orchestrate workflows

MVP skills:

- task-manager
- task-discovery
- task-implementation
- task-test-design
- task-validation
- instruction-budget-verify
- instruction-doc-verify
- work-with-beads
- work-with-git

---

### 3. Subagents

Location:
.claude/agents/

Responsibilities:

- independent review
- validation

Rules:

- NOT used for default orchestration
- used only when explicitly required by workflow or user

Mandatory:

- code-reviewer subagent for all non-trivial code tasks

No planner subagent in MVP.

---

### 4. Workflows

Location:
.claude/workflows/

Responsibilities:

- define ordered execution steps per task type
- contain no implementation logic
- stay minimal

Examples:

- bugfix.md
- feature.md
- docs.md
- refactor.md
- test-only.md
- investigation.md
- mixed.md

---

### 5. Task Execution Model

#### Step 1 — Classification

Every task MUST be classified as:

- bugfix
- feature
- refactor
- docs
- test-only
- investigation
- mixed

---

#### Step 2 — Trivial vs Non-Trivial

### Trivial

- small scope
- single file or minimal change
- no contracts or workflows affected

Execution:

- minimal workflow
- minimal skills
- no subagents

---

### Non-Trivial

- multi-step
- affects behavior or structure
- requires validation

Execution:

- MUST invoke `task-manager` skill
- MUST select a workflow from `.claude/workflows/`
- MUST follow workflow steps
- MUST use appropriate skills
- MUST invoke `code-reviewer` subagent for code tasks
- MUST produce structured output

---

### 6. Workflow Contract (Invariant)

Every non-trivial task MUST follow:

1. classify_task
2. discover_context
3. identify_constraints
4. select_skills
5. generate_plan
6. define_changes
7. define_tests
8. validate_solution

Workflows define how this sequence is applied per task type.

---

### 7. Structured Output Requirement

Every non-trivial task MUST produce:

1. Markdown report in table-view (human-readable)
It must include:

- task type
- workflow name
- steps with used skills

---

## Benchmark System

Location:
.benchmark/

Purpose:

- evaluate AI behavior
- measure drift across models
- measure token usage (token drain)
- validate workflow compliance

Contents:

- prompts/
- golden/
- scoring/
- scripts/
- configs/
- reports/

---

## Instruction Budget Validation

Instruction size is validated only when instruction-layer files change.

Applies to:

- AGENTS.md
- skills
- workflows
- subagents

Validation is performed by:

- instruction-budget-verify skill
- external script from `.benchmark/scripts/`

Thresholds are defined in:

.benchmark/configs/instruction-budgets.yaml