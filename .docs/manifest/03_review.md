# 03_review.md — Instruction System Review

## Context Required

Before starting, ensure the following files are available in this session:
- `MANIFEST.md` — canonical source of truth
- `brainstorm_protocol.md` — canonical brainstorming behavior
- Your full instruction system: `AGENTS.md`, all skills, workflows, agents, and reference docs

If any are missing, stop and ask the user to provide them.

---

## Purpose

Your task is to validate that the current instruction system fully complies with `MANIFEST.md` principles.

This is NOT an implementation task.
This is a strict audit and verification process.

Assume the system is **wrong until proven correct**.
Be critical, not optimistic.
Do not suggest fixes before completing the audit.

---

## Working Mode

Work in exactly 3 phases. Do not skip or merge phases.

1. **Audit** — full analysis against MANIFEST principles
2. **Clarification** — resolve genuine ambiguities with the user
3. **Final Validation** — verdict and minimal fix plan

During Clarification: follow `brainstorm_protocol.md` exactly.
Do NOT modify files at any point during this process.
Do NOT suggest implementation until Phase 3.

---

## Phase 1 — Audit

Read all provided instruction files. Validate each against MANIFEST principles.

---

### 1. Context Minimization

- Is the root context (AGENTS.md) minimal?
- Is anything unnecessarily always-loaded?
- Are skills, workflows, and reference docs on-demand only?

---

### 2. Separation of Policy and Execution

- Does AGENTS.md contain only policy (WHAT / WHEN), not execution (HOW)?
- Are procedures confined to skills and workflows?
- Is any execution logic embedded in AGENTS.md?

---

### 3. Progressive Disclosure of Complexity

- Is complexity introduced only when needed?
- Does the system start from direct execution and escalate appropriately?
- Are subagents used only where genuinely justified?
- Is the system over-engineered relative to the project size?

---

### 4. No Duplication

Check for duplicated rules across:
- AGENTS.md and skills
- skills and workflows
- multiple skills
- reference docs and skills

Any rule that exists in more than one place is a violation.

---

### 5. Responsibility Boundaries

- Does each file have exactly one responsibility?
- Do any skills contain orchestration logic?
- Do any workflows contain implementation details?
- Does AGENTS.md contain execution steps?
- Does the manager skill (if present) duplicate AGENTS.md?

---

### 6. Composability

- Are skills atomic and self-contained?
- Are workflows pure orchestration (referencing skills, not redefining them)?
- Are components reusable independently?

---

### 7. Determinism

- Are critical behaviors explicitly defined?
- Is any behavior left to "AI will figure it out"?
- Are routing decisions unambiguous?

---

### 8. Brainstorm Skill (Mandatory)

- Does a brainstorm skill exist?
- Is it registered in AGENTS.md?
- Does it reference `brainstorm_protocol.md` without redefining it inline?
- Is it correctly scoped (discussion only, not execution)?

If the brainstorm skill is missing → this is a **Critical violation**.

---

### Architecture Validation

- Does the system complexity match the project size?
- Is there unnecessary manager / workflow / subagent infrastructure?
- Is routing logic centralized correctly?
- Are subagents used only when context isolation is genuinely beneficial?

---

### Context Efficiency

- Are skills modular and loaded on demand?
- Are workflows lightweight?
- Are reference docs used correctly (not always loaded)?
- Are there any large monolithic files that should be split?

---

### Risk-Based Execution

- Is the execution matrix from MANIFEST actually applied?
- Are high-risk tasks routed through review loops?
- Are trivial tasks handled directly without unnecessary overhead?

---

## Phase 1 Output

Provide:

### Compliance Score
A score from 0 to 100 reflecting overall alignment with MANIFEST.

### Violations List

Group by severity:

**Critical (must fix before system is usable):**
- List each violation with: location, principle violated, description

**Major (significant risk or inconsistency):**
- List each violation with: location, principle violated, description

**Minor (low impact, worth fixing eventually):**
- List each violation with: location, principle violated, description

### Suspicious Areas
List anything that is unclear, potentially risky, or could be interpreted multiple ways.

### Over-Engineering Signals
List any complexity that appears unjustified by the project's actual scale.

### Under-Engineering Risks
List anything that is dangerously absent given the project's apparent needs.

---

STOP after Phase 1 output.
Do not proceed to Phase 2 until the user acknowledges the audit results.

---

## Phase 2 — Clarification

Resolve genuine ambiguities identified in Phase 1.

Ask questions ONLY if:
- a rule interpretation is unclear
- the design intent is ambiguous
- multiple valid interpretations exist and the choice affects the fix plan

Follow `brainstorm_protocol.md` exactly:
- one question at a time
- 2–3 concrete options per question
- stop and wait after each question

Do NOT ask about:
- things clearly established by the repository
- violations that are unambiguously wrong
- trivial details

Focus only on high-impact ambiguities that affect the fix plan.

If there are no genuine ambiguities → skip Phase 2 and proceed directly to Phase 3.
State explicitly that no clarification is needed and why.

---

## Phase 3 — Final Validation

After clarification (or if Phase 2 was skipped):

---

### Final Compliance Score

Revised score after clarification, with brief justification.

---

### Final Verdict

Choose exactly one:
- **Compliant** — system fully follows MANIFEST, no fixes required
- **Conditionally Compliant** — minor issues present, system is functional but should be improved
- **Non-Compliant** — critical or major violations present, system must be fixed before relying on it

---

### Minimal Fix Plan

IMPORTANT:
- Do NOT propose a full redesign
- Do NOT propose nice-to-have improvements
- Only propose the minimum changes required to reach compliance

For each required fix:
- **File:** which file to change
- **Issue:** what is wrong
- **Fix:** exactly what change is needed
- **Severity:** Critical / Major / Minor

Order fixes by severity. Address Critical first.

---

### Structural Correctness Summary

Confirm or deny each of the following:

- [ ] No duplication exists across files
- [ ] Responsibility boundaries are clear and enforced
- [ ] Context is minimal — nothing unnecessary is always-loaded
- [ ] Layering is correct — policy in AGENTS.md, execution in skills/workflows
- [ ] Complexity matches project scale — no over or under engineering
- [ ] Brainstorm skill is present, correctly scoped, and registered
- [ ] Brainstorm protocol is referenced, not duplicated

If any item cannot be confirmed → it must appear in the fix plan.

---

## Quality Bar

The system is valid ONLY if:

- MANIFEST principles are fully respected
- No duplicated logic exists
- Context is minimal
- Complexity matches project scale
- Brainstorm skill is correctly implemented
- System behavior is understandable from `AGENTS.md` alone

If any of these fail → system is NOT compliant.

---

## Critical Rule

If unsure about anything:
- do not assume
- ask in Phase 2

Validation without certainty is invalid.
