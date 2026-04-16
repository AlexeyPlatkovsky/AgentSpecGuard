# MANIFEST.md

## Purpose

This document defines the canonical philosophy and rules for managing:
- AI instructions
- context distribution
- orchestration
- modular execution

It is **technology-agnostic** and **project-agnostic**.

It answers one question:

> How should any AI system be structured to work efficiently, predictably, and without context waste?

This document is the **single source of truth** for:
- designing instruction systems
- evolving orchestration
- validating architectural decisions

---

# Core Principles

## 1. Minimize Always-Loaded Context

Only the **minimum required rules** must be loaded by default.

Everything else must be:
- modular
- on-demand
- explicitly invoked

Violation of this principle leads to:
- token waste
- degraded reasoning quality
- unpredictable behavior

---

## 2. Separate Policy from Execution

Two fundamentally different things must never be mixed:

### Policy (WHAT / WHEN)
- global rules
- classification
- constraints
- permissions
- expected outputs

### Execution (HOW)
- step-by-step procedures
- workflows
- implementation logic

Policy lives in:
- `AGENTS.md`

Execution lives in:
- skills
- workflows

Exception: for small projects, `AGENTS.md` may contain inline routing logic
(trivial vs non-trivial decision tree) in place of a manager skill.
This is the only permitted policy/execution overlap, and it must remain minimal.

---

## 3. Progressive Disclosure of Complexity

The system must reveal complexity **only when needed**.

Order of escalation:
1. Direct execution (trivial tasks)
2. Skill-based execution
3. Workflow-based execution
4. Multi-role / subagent execution

Never start from level 4.

---

## 4. No Duplication Rule (Critical)

Any rule must exist **only once**.

Allowed:
- referencing a rule

Forbidden:
- redefining the same rule in multiple places

Typical violations:
- task classification repeated in multiple files
- validation rules copied into workflows
- git rules duplicated in skills and root

Duplication = inconsistency risk.

---

## 5. Composability over Complexity

Build systems from:
- small
- well-defined
- reusable units

Avoid:
- large "do everything" instructions
- monolithic workflows
- tightly coupled components

---

## 6. Explicit Responsibility Boundaries

Each layer must have a **single responsibility**.

If a file does more than one job → it is wrong.

---

## 7. Deterministic > Implicit Behavior

Critical behaviors must be:
- explicitly defined
- predictable

Avoid relying on:
- "AI will figure it out"
- implicit conventions

---

## 8. Optimize for Real Tasks, Not Theory

The system must:
- minimize overhead for simple tasks
- scale for complex tasks

Avoid:
- forcing heavy orchestration on simple work
- designing for edge cases first

---

# Single Entry Point

`AGENTS.md` is the **only** entry point for any AI tool.

Every AI tool used in the project must be configured to read `AGENTS.md` first.
The method for wiring each AI tool to `AGENTS.md` varies by tool and must be
discovered at setup time — it must NOT be hardcoded in this document.

**Responsibility:** `01_initial.md` is responsible for:
- asking which AI tools the project uses
- searching for the correct setup method per tool at the time of setup
- creating the necessary entry point configuration for each tool

This keeps the framework decoupled from any specific AI tool's conventions,
which change over time.

---

# Canonical Pipeline Templates

MANIFEST defines the canonical execution pipelines. Projects may add steps
when genuinely justified, but may not remove or reorder the base steps.

## Trivial Tasks

```
plan → execute → validate
```

Used when:
- task is self-contained
- risk is low
- no orchestration is needed

For very low-risk tasks (e.g. grammar fixes), `validate` may be omitted.
This must be explicitly stated in `AGENTS.md` when permitted.

## Non-Trivial Tasks (medium/large projects)

```
invoke manager → (manager selects workflow) → execute workflow → validate
```

Used when:
- task spans multiple steps or domains
- risk is medium or higher
- a workflow file exists for the task type

## Non-Trivial Tasks (small projects, no manager)

```
plan → execute → validate
```

When no manager skill exists, non-trivial tasks follow the same pipeline
as trivial tasks. The AI applies judgment on step depth, not pipeline shape.

---

# Canonical Structure

## Root Layer

### `MANIFEST.md`
- philosophy
- principles
- system design rules

### `AGENTS.md`
- single entry point for all AI tools
- operational contract
- rules AI must follow
- task classification and inline routing (small projects only)
- capability registry (skills, workflows, agents)

---

## Execution Layer (Stored under `.claude/` by default)

### `.claude/skills/`
Atomic, reusable procedures.

Examples:
- implement feature
- validate
- work with git

Rules:
- must be self-contained
- must not include orchestration logic

---

### `.claude/workflows/`
Multi-step execution patterns.

Used only for:
- non-trivial tasks on medium/large projects

Rules:
- define order of steps
- reference skills
- do not redefine skills

---

### `.claude/agents/`
Specialized roles (subagents).

Used only when:
- context isolation is beneficial
- independent reasoning improves results

Examples:
- code reviewer
- architect
- researcher

---

# Mandatory Skills

## Brainstorm Skill (Required in Every Project)

Every project built with this framework **must** include a brainstorm skill.

This is non-negotiable regardless of project size.

### Why it is mandatory

Discussion and design decisions are a core part of any project lifecycle.
Without a canonical brainstorm skill:
- AI behavior during discussions is unpredictable
- question/answer protocols are inconsistent
- design decisions are not properly structured

### What it must implement

The brainstorm skill must follow the protocol defined in `brainstorm_protocol.md`.

It must:
- ask exactly one question at a time
- provide 2–3 concrete, comparable options per question
- highlight risks, trade-offs, and edge cases
- stop and wait for user input after presenting options
- never mix brainstorming with execution
- defer final decisions to the user

### Where it lives

`.claude/skills/brainstorm.md`

It must reference `brainstorm_protocol.md` as its canonical behavior source.
It must NOT redefine the protocol inline.

### Registration

It must be registered in `AGENTS.md` like any other skill:
- name: brainstorm
- purpose: structured discussion and design decision support
- when to use: any time a design, architecture, or workflow decision must be made
- when not to use: during execution phases; after a decision is already made

---

## Manager Skill (Required for Medium and Large Projects)

Medium and large projects **must** include a manager skill.

This is non-negotiable for those project sizes.
Small projects may add it explicitly if the user requests it.

### Why it is mandatory for medium/large

As the number of workflows and skills grows, inline routing in `AGENTS.md`
becomes unmanageable. Manager centralizes orchestration without bloating the
root operational contract.

### What it must implement

The manager skill is responsible for:
- receiving non-trivial task descriptions
- consulting the workflow table to select the correct workflow
- reading and executing the selected workflow
- falling back to `plan → execute → validate` if no matching workflow exists
- consulting the subagent table if the task requires specialized roles

It must NOT:
- duplicate rules already in `AGENTS.md`
- implement execution steps directly (delegate to workflows and skills)
- define new policy

### Where it lives

`.claude/skills/manager.md`

### Required contents

The manager skill file must contain:

1. **Workflow table** — maps task types to workflow files
2. **Subagent table** — maps task types to subagents (if applicable)
3. **Fallback rule** — explicit statement that missing workflows default to `plan → execute → validate`
4. **Routing logic** — how to classify an incoming task and select the correct path

### Fallback behavior

If no workflow matches the task:

```
plan → execute → validate
```

This fallback must be explicitly stated in the manager skill file.

### Registration

It must be registered in `AGENTS.md`:
- name: manager
- purpose: routing and orchestration for non-trivial tasks
- when to use: any non-trivial task
- when not to use: trivial tasks; brainstorming phases

---

# Capability Registry

AGENTS.md must contain the canonical registry of all available:

- skills
- workflows (medium/large projects)
- agents (if present)

Each entry must include:
- name
- purpose
- when to use
- when not to use

This registry exists to ensure:
- all actors (main agent and subagents) share the same capabilities view
- consistent routing and decision making
- no hidden or implicit functionality

Restrictions:
- AGENTS.md must NOT contain implementation details
- AGENTS.md must NOT duplicate skill or agent logic
- Detailed behavior must remain in corresponding files

If a capability is not listed in AGENTS.md:
- it is considered non-existent for orchestration purposes

---

# Task Classification Model

## Dimension 1: Complexity

- Trivial
- Non-trivial

## Dimension 2: Risk

- Low
- Medium
- High
- System-level (cross-cutting)

---

## Execution Matrix

| Type | Small Project | Medium/Large Project |
|------|--------------|----------------------|
| Trivial + Low Risk | `plan → execute → validate` (direct) | `plan → execute → validate` (direct) |
| Trivial + Low Risk, minimal | `plan → execute` (if validate not needed) | `plan → execute` (if validate not needed) |
| Non-trivial + Low/Medium Risk | `plan → execute → validate` | Manager → workflow + validation |
| Non-trivial + High Risk | `plan → execute → validate` + review | Manager → workflow + review loop |
| System-level | `plan → execute → validate` + review | Manager → architect + full pipeline |

---

# Review Strategy

Review is **not mandatory for every task**.

Use when:
- logic is complex
- changes affect multiple areas
- risk is high

Skip or simplify when:
- change is isolated
- behavior is obvious
- risk is low

---

# Validation Rules

Validation is mandatory unless task is purely informational.

Types:
- tests
- lint
- type checks

Validation must:
- be automated
- be repeatable
- not depend on AI judgment

---

# Context Management Rules

## Always Loaded

- AGENTS.md

## On Demand

- skills
- workflows
- subagents
- reference docs

---

## Context Anti-Patterns

Avoid:

- large root files
- loading all skills at once
- mixing unrelated instructions
- embedding workflows in root files

---

# Project Size Definitions

These definitions are used by `01_initial.md` to determine project scale.
Size must be explicitly confirmed by the user — never assumed silently.

## Small

- Solo or 2–3 contributors
- Single domain or purpose
- No established release pipeline
- Workflows are either absent or trivially simple

System composition:
- `AGENTS.md` with inline routing
- Brainstorm skill (mandatory)
- 2–4 additional skills
- No manager, no workflows, no subagents (unless explicitly requested)

## Medium

- Active team, multiple contributors
- Multiple domains or workflow types
- Established release or review pipeline
- Repeated non-trivial tasks that benefit from defined workflows

System composition:
- `AGENTS.md`
- Brainstorm skill (mandatory)
- Manager skill (mandatory)
- Skills for each repeated task type
- 1–3 workflows
- Subagents optional

## Large

- Multi-team or complex domain structure
- Many distinct workflow types
- High routing complexity
- Risk-based execution is critical

System composition:
- `AGENTS.md`
- Brainstorm skill (mandatory)
- Manager skill (mandatory)
- Domain-specific skills and workflows
- Subagents (selectively)
- Reference docs for architecture and conventions

---

# Reference Documentation Strategy

Optional but recommended for reusable knowledge:

Examples:
- architecture
- conventions
- domain rules

Rules:
- only create if reused by multiple skills
- must not be always loaded
- must be referenced, not embedded

---

# Evolution Rules

The system must evolve based on:

- real usage
- observed failures
- measurable improvements

When updating:
- update MANIFEST.md first
- then propagate changes

---

# What This System Optimizes For

- minimal context usage
- predictable execution
- modular extensibility
- cross-AI compatibility
- maintainability over time

---

# What This System Avoids

- over-engineering
- instruction duplication
- unnecessary abstraction
- AI-specific lock-in
- hidden behavior

---

# Final Rule

If a new idea:
- increases complexity
- duplicates logic
- or increases always-loaded context

→ it must be rejected or redesigned.

---
