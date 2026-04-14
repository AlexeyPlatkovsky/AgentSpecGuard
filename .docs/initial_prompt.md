Use `MANIFEST.md` as the canonical source of truth for how AI context and instruction systems must be designed.

Your task is to create a draft instruction composition for this project, or adjust the existing one, so it aligns with `MANIFEST.md`.

Important working mode:
- Work in 3 phases: Inventory → Discussion → Composition
- Do NOT skip phases
- Do NOT rewrite instructions immediately after reading files
- During discussion, ask no more than 1 question at a time
- For each discussion point, provide 2–3 concrete options when possible
- Move to the next point only after the previous one is clarified
- Avoid over-engineering
- Prefer the smallest coherent system that fits the project

## Goal

Produce a project-specific AI instruction setup that:
- follows `MANIFEST.md`
- fits the real project size and complexity
- minimizes always-loaded context
- avoids duplication
- stays maintainable as the project evolves

The result must be project- and tech-specific, but the instruction architecture must follow the general rules from `MANIFEST.md`.

---

## Phase 1 — Inventory

First, inspect the repository and build an understanding of the current project.

You must investigate:

### A. Project nature
- what kind of project this is
- its likely scale: small / medium / large
- its current maturity: prototype / active development / stable / legacy
- whether it is single-purpose or multi-domain

### B. Tech stack
- languages
- frameworks
- test stack
- build tools
- CI/CD
- deployment or runtime environment if relevant

### C. Existing documentation
- root docs
- design docs
- architecture docs
- conventions
- workflow docs
- any existing AI instruction files
- any duplicated or conflicting guidance

### D. Existing instruction system
- whether `AGENTS.md` exists
- whether skills / workflows / agents already exist
- whether routing logic already exists
- whether the current setup violates `MANIFEST.md`

### E. Reusable project knowledge
Identify whether the project needs reusable reference docs such as:
- architecture
- code conventions
- test conventions
- domain rules
- repo structure / commands

Do not decide yet what to create. Only identify likely needs.

---

## Phase 1 output

After investigation, stop and provide:

1. Project summary
2. Current instruction-system summary
3. Initial compliance check against `MANIFEST.md`
4. Main risks / gaps / ambiguities
5. A proposed discussion agenda

Do NOT start editing files yet.

---

## Phase 2 — Discussion

Now discuss the missing decisions with the user.

Rules:
- Ask only 1 question at a time
- For each question, provide 2–3 options if reasonable
- Ask only about high-impact decisions
- Do not ask about things already clearly established by the repo
- Keep questions short and concrete
- Prefer decisions that affect:
  - task classification
  - routing/orchestration
  - review and validation policy
  - reference documentation
  - project scale assumptions
  - level of modularity

Typical topics to clarify:
- whether the project should stay minimal or be designed to scale
- whether non-trivial work needs workflows
- whether risk-based review must be introduced
- whether subagents are needed at all
- whether reusable project reference docs are justified
- how strict validation should be
- whether existing docs should be refactored or preserved

Important:
Do not ask multiple bundled questions.
Resolve one decision fully before moving to the next.

---

## Phase 3 — Composition

Only after discussion is complete, create or adjust the instruction system.

### Required design rules
- `MANIFEST.md` remains the canonical meta-level source
- `AGENTS.md` is the project-level operational contract
- Policy and execution must be separated
- Root instructions must stay compact
- Detailed procedures must be modular
- No duplicated logic across files
- Complexity must be progressively disclosed
- The system must match the actual project scale

### Composition task
Based on the repository and clarified decisions:

1. Decide what instruction artifacts are actually needed
2. Propose the minimal coherent target structure
3. Create or refactor the files needed
4. Remove or merge duplicated logic
5. Keep semantics clean and responsibility boundaries explicit

### Possible outputs depending on project size

For a small project, likely enough:
- `AGENTS.md`
- a few minimal skills
- maybe 1–2 reference docs

For a medium project, likely:
- `AGENTS.md`
- skills
- workflows if justified
- selected reference docs

For a large project, likely:
- `AGENTS.md`
- manager skill or equivalent routing layer
- workflows
- selective subagents
- reusable reference docs
- risk-based review path

Do not force a large-project architecture onto a small repo.

---

## Final output format

When composition is finished, provide:

### 1. Final assessment
- what was found
- what was wrong or missing
- what decisions were made

### 2. Target architecture
- what files now exist or should exist
- what each file is responsible for

### 3. Change summary
- what was created
- what was updated
- what was removed or merged

### 4. Remaining tradeoffs
- what is intentionally kept simple
- what can be added later if the project grows

---

## Quality bar

The final system must:
- align with `MANIFEST.md`
- be project-specific, not generic filler
- be as small as possible, but complete
- avoid unnecessary abstraction
- avoid duplicated rules
- support future growth without redesigning everything

If the current project does not justify a more complex setup, explicitly keep it simple.