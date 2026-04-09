# idea.md

## Project Name (working)
AgentSpecGuard (Portable Agent System)

---

## Core Idea

This project is a reusable template that standardizes how AI agents perform development tasks across any repository.

The goal is to make AI behavior:

- predictable  
- structured  
- testable  
- comparable across models  

This is not an application.  
It is a portable agent operating layer that can be integrated into any project.

---

## Key Objectives

1. Enforce a consistent workflow for all AI-driven tasks  
2. Ensure structured, machine-verifiable outputs  
3. Provide a modular skill system  
4. Control and validate context size (prompt budget)  
5. Detect and measure behavioral drift across models and versions  

---

## System Components

### 1. AGENTS.md (Root Entry Point)

Defines:

- global workflow contract
- task classification rules
- skill selection rules
- structured output requirement
- context budget constraints

Must remain:

- compact  
- stable  
- implementation-agnostic  

---

### 2. Skills

Location:
.claude/skills/

Responsibilities:

- define execution logic  
- cover different domains (planning, coding, testing, etc.)  
- be modular and reusable  

Rules:

- if a skill matches a task → it MUST be used  
- skills are binding, not optional  

---

### 3. Subagents

Location:
.claude/subagents/

Responsibilities:

- orchestration  
- validation  
- review  

---

### 4. Workflows

Location:
.claude/workflows/

Responsibilities:

- define ordered execution steps  
- provide task-type-specific flows  

---

### 5. Contracts

Location:
.claude/contracts/

Defines:

- allowed workflow steps  
- step ordering rules  
- required skills per task type  
- output schema  

---

### 6. Evaluation System

Location:
.claude/eval/

Responsibilities:

- validate agent behavior  
- detect drift  
- compare outputs across models  

Includes:

- golden prompts  
- expected structured outputs  
- scoring rules  

---

### 7. Context Budget System

Location:
.claude/contracts/context-budget.yaml

Purpose:

- control prompt size  
- prevent instruction bloat  
- maintain performance and stability  

---

## Workflow Contract (Invariant)

Every non-trivial task MUST follow:

1. classify_task  
2. discover_context  
3. identify_constraints  
4. select_skills  
5. generate_plan  
6. define_changes  
7. define_tests  
8. validate_solution  

Rules:

- no step may be skipped silently  
- skipped steps must be justified  

---

## Task Classification

Mandatory first step.

Allowed types:

- bugfix  
- feature  
- refactor  
- docs  
- test-only  
- investigation  
- mixed  

---

## Structured Output Requirement

Every non-trivial task MUST produce:

1. Markdown output (human-readable)  
2. JSON output (machine-readable)  

JSON must include:

- task_type  
- workflow  
- steps  
- skills_used  
- validation  

---

## Context Budget Constraints

Context usage is a first-class constraint.

Must validate:

1. Individual file size  
2. Assembled task context size  
3. Bundle size for task types  

---

### Budget Rules

- prefer minimal context  
- avoid duplication  
- move details from global → local  
- keep AGENTS.md lightweight  

---

### Budget Validation Requirement

If modified:

- AGENTS.md  
- skills  
- subagents  
- workflows  

Then MUST run:

- context-budget-verify  
- doc-verify (if structure changed)  

---

### Thresholds

Each entity must support:

- recommended (soft limit)  
- hard limit  

Behavior:

- exceed soft → warning  
- exceed hard → failure  

---

## Anti-Drift System

The system must detect deviations in:

- workflow steps  
- step ordering  
- skill selection  
- output structure  

Deviation without justification = failure  

---

## Evaluation Tests

1. Workflow Compliance Tests  
2. Skill Selection Tests  
3. Output Schema Tests  
4. Context Budget Tests  
5. Cross-Model Stability Tests  

---

## Scoring System

Evaluation should produce a score based on:

- task classification correctness  
- workflow compliance  
- step ordering  
- skill selection  
- output schema validity  

---

## Constraints

Mandatory:

- workflow must always be followed  
- structured output is required  
- skills must be used when matched  
- context must be validated  

Forbidden:

- skipping workflow steps  
- unstructured output  
- ignoring skills  
- uncontrolled context growth  
- mixing unrelated changes  

---

## Design Principles

- modularity over monolith  
- composition over duplication  
- explicit over implicit  
- measurable over subjective  

---

## Success Criteria

- consistent workflow across runs  
- comparable structured outputs  
- measurable drift  
- controlled context size  

---

## Non-Goals

- perfect code generation  
- model-specific tuning  
- replacing human judgment  

---

## Summary

This project defines a standard for AI behavior.

It combines:

- workflow contract  
- skill system  
- structured outputs  
- context control  
- evaluation framework  

to ensure consistent, predictable, and measurable AI execution.
