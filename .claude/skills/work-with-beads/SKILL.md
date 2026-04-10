---
name: work-with-beads
description: Manages Beads issue tracking for non-trivial work. Use when work needs a bead created, updated, deduplicated, or validated against the project backlog rules.
---

Manage Beads work items with a minimal, backlog-first workflow:

1. Use this skill when work touches Beads tracking itself or when a non-trivial task does not already have a bead.
2. Before creating anything, check for duplicates with `bd search <terms>` and inspect likely matches with `bd show <id>`.
3. Every bead ID MUST use `asg-XXX`, where `XXX` is a zero-padded sequential number. If Beads does not generate that format, create the issue with an explicit `--id asg-XXX`.
4. Use priorities only as `P1`, `P2`, or `P3`:
   - `P1` for core system work
   - `P2` for important work
   - `P3` for optional work
5. Create and update beads with `bd create`, `bd update`, and `bd close`. Keep descriptions concrete, scoped to one outcome, and executable by an existing workflow.
6. Structure the backlog as:
   - Epic: high-level unit; MUST contain at least one feature
   - Feature: grouped functionality or subsystem; MUST belong to an epic and contain at least one task
   - Task: atomic unit; MUST belong to a feature, map to a concrete change, and be completable in one session
7. Express hierarchy with parent-child relationships:
   - epic -> feature
   - feature -> task
8. For every non-trivial task, ensure a task bead exists before implementation. If it is missing, create it under the correct feature with a clear description.
9. Keep the backlog minimal:
   - do not create beads per file
   - do not over-split work
   - do not create speculative tasks
   - group tasks by shared functionality or subsystem
10. When validating the backlog, fix only clearly defined gaps:
   - no orphan tasks
   - no features without tasks
   - no epics without features
