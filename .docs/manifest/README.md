# AI Instruction Framework

A portable, reusable system for designing, building, and auditing AI instruction architectures across any project.

Suited for open source projects and small-to-medium teams who want predictable, maintainable AI behavior without over-engineering.

---

## What This Is

Most projects that use AI tools end up with scattered, inconsistent, duplicated instructions. This framework provides a principled way to design your AI instruction system from the ground up — or audit and fix an existing one.

The framework is built around one canonical document (`MANIFEST.md`) and three sequential prompts that guide you through creation, expansion, and validation.

---

## Files in This Folder

| File | Role |
|------|------|
| `MANIFEST.md` | The canonical source of truth. Defines all principles, rules, and structural requirements for any AI instruction system. |
| `brainstorm_protocol.md` | Canonical definition of brainstorming behavior. Referenced by prompts and skills — never duplicated. |
| `01_initial.md` | Phase 1 prompt. Builds a minimal viable instruction set for your project from scratch or adjusts an existing one. |
| `02_evolution.md` | Phase 2 prompt. Expands your instruction system based on your team's real workflows and daily routines. |
| `03_review.md` | Phase 3 prompt. Audits your instruction system for compliance with MANIFEST principles. |

---

## How to Use

### Prerequisites

These prompts are designed to be used inside an AI chat session (Claude, Cursor, or any capable AI assistant).

All files in this folder must be provided to the AI at the start of each session. The prompts assume MANIFEST.md and brainstorm_protocol.md are available in context.

### The Pipeline

The three prompts are designed to be used **in order**. Each phase builds on the previous one.

---

#### Step 1 — Build (`01_initial.md`)

**When:** Starting a new project, or setting up AI instructions for the first time.

**What it does:**
- Reads your repository to understand the project
- Identifies your tech stack, scale, and existing instruction files
- Asks targeted gap-filling questions (one at a time)
- Produces a minimal, correct instruction set aligned with MANIFEST

**Goal:** The smallest coherent instruction system that fits your project today.

**How to run:**
1. Open a new AI session
2. Provide: `MANIFEST.md`, `brainstorm_protocol.md`, `01_initial.md`
3. Provide access to your repository (paste key files or use an IDE integration)
4. Follow the AI's phases: Inventory → Discussion → Composition

---

#### Step 2 — Evolve (`02_evolution.md`)

**When:** Your project has grown, your team has expanded, or your workflows have matured beyond the initial setup.

**What it does:**
- Starts with a free-form conversation about your team's daily routines and workflows
- Identifies what skills, agents, and workflows would genuinely help
- Proposes a complete set of additions at once
- You review and approve before anything is created

**Goal:** A comprehensive instruction system built from real usage patterns, not assumptions.

**How to run:**
1. Open a new AI session
2. Provide: `MANIFEST.md`, `brainstorm_protocol.md`, `02_evolution.md`
3. Provide your current instruction files (AGENTS.md, skills, workflows)
4. Be ready to describe your team's actual daily routines in conversation

---

#### Step 3 — Review (`03_review.md`)

**When:** After any significant change to your instruction system, or periodically to catch drift.

**What it does:**
- Audits your entire instruction system against MANIFEST principles
- Produces a compliance score and violations list
- Asks clarifying questions only when genuinely ambiguous
- Produces a minimal fix plan — not a full redesign

**Goal:** Confidence that your instruction system is correct, minimal, and non-duplicated.

**How to run:**
1. Open a new AI session
2. Provide: `MANIFEST.md`, `brainstorm_protocol.md`, `03_review.md`
3. Provide your full instruction system (AGENTS.md, all skills, workflows, agents)
4. Follow the AI's phases: Audit → Clarification → Final Validation

---

## Key Principles (Summary)

The full philosophy is in `MANIFEST.md`. The short version:

- **Minimal context** — only load what's needed, when it's needed
- **No duplication** — every rule exists in exactly one place
- **Separation of concerns** — policy in AGENTS.md, execution in skills/workflows
- **Progressive complexity** — don't start with subagents if a skill will do
- **Brainstorm skill is mandatory** — every project must have one, following `brainstorm_protocol.md`

---

## Typical Project Outcomes

**Small project (solo or 2–3 contributors):**
- `AGENTS.md`
- 2–4 skills including brainstorm
- No workflows, no subagents

**Medium project (active team, multiple domains):**
- `AGENTS.md`
- Skills for each repeated workflow
- 1–2 workflows for non-trivial tasks
- Optional manager skill

**Large project (complex, multi-domain, many contributors):**
- `AGENTS.md`
- Manager skill for routing
- Domain-specific skills and workflows
- Selective subagents
- Reference docs for architecture and conventions

---

## When to Re-run Each Prompt

| Trigger | Use |
|---------|-----|
| Starting from scratch | `01_initial.md` |
| Adjusting existing instructions | `01_initial.md` |
| Project scaled up significantly | `02_evolution.md` |
| Team workflows have matured | `02_evolution.md` |
| After any major instruction change | `03_review.md` |
| Periodic health check | `03_review.md` |
| MANIFEST was updated | `03_review.md` |

---

## Contributing

If you improve MANIFEST.md, update it first — then propagate changes to the prompts.
Never update a prompt to work around a MANIFEST principle. Update MANIFEST first.
