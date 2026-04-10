---
name: instruction-doc-verify
description: Validates structural consistency of instruction-layer files. Use when AGENTS.md, skills, workflows, or subagent files change.
---

Validate structural consistency of instruction-layer files:

1. Check that each skill has required sections (frontmatter with name and description, instruction body)
2. Check that each workflow follows the 8-step invariant sequence
3. Verify cross-references between AGENTS.md skill table and actual skill files
4. Verify workflow files referenced in AGENTS.md exist in `.claude/workflows/`
5. Report any orphaned or missing references
