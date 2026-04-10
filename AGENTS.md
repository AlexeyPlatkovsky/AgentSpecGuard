# AgentSpecGuard

A portable agent operating layer that standardizes how AI agents perform development tasks.

---

## Task Classification

Every task MUST be classified as one of:

| Type            | Description                    |
|-----------------|--------------------------------|
| bugfix          | Fix a defect                   |
| feature         | Add new functionality          |
| refactor        | Restructure without behavior change |
| docs            | Documentation only             |
| test-only       | Add or modify tests only       |
| investigation   | Research / analysis            |
| mixed           | Combines multiple types        |

---

## Trivial vs Non-Trivial

### Trivial

A task is trivial when ALL of the following are true:

- Small scope (single file or minimal change)
- No contracts or workflows affected
- No structural or behavioral impact

Trivial tasks use minimal execution: apply the change directly, no subagents.

### Non-Trivial

A task is non-trivial when ANY of the following are true:

- Multi-step
- Affects behavior or structure
- Requires validation

Non-trivial tasks MUST be routed to the `task-manager` skill.

---

## Routing

```
Task received
  ├── Trivial → execute directly (minimal skills, no subagents)
  └── Non-Trivial → invoke `task-manager` skill
```

---

## Skill Table

| Skill                      | When Used                                                    |
|----------------------------|--------------------------------------------------------------|
| business-analyst           | Clarifies requirements, acceptance criteria, and business rules |
| feature-implementation     | Implements code changes to pass failing tests (TDD green phase) |
| instruction-budget-verify  | Validates instruction file sizes against budget limits       |
| instruction-doc-verify     | Validates structural consistency of instruction files        |
| task-discovery             | Gathers context and constraints for a task                   |
| task-manager               | Orchestrates non-trivial task execution                      |
| task-test-design           | Hardens and refactors tests after implementation             |
| task-validation            | Validates solution against requirements                      |
| test-writer                | Writes failing tests before implementation (TDD red phase)   |
| work-with-git              | Stages, commits, and pushes completed work at end of workflow |

---

## Subagent Rules

- `code-reviewer` is **mandatory** for all non-trivial code tasks
- Subagents are NOT used for orchestration
- Subagents are used only when explicitly required by a workflow or user

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:ca08a54f -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd dolt push
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->
