---
name: instruction-doc-verify
description: Validates structural consistency of instruction-layer files. Use when AGENTS.md, skills, workflows, or subagent files change.
---

Validate instruction-layer structure only:

1. Check that each skill file has frontmatter with `name` and `description`.
2. Check that each workflow file contains an ordered step list.
3. Check that each subagent file has frontmatter plus `Input Contract` and `Output Contract` sections.
4. Check that `AGENTS.md` contains the routing sections used in this repository.
5. Report structural issues only.
