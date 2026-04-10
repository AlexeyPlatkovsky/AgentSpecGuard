# Workflow: Mixed

## Steps

1. **classify_task** — Confirm task type is `mixed`; identify constituent types
2. **discover_context** — Gather context for all constituent task types
3. **identify_constraints** — Determine combined constraints across all types
4. **select_skills** — Choose applicable skills for each constituent type
5. **generate_plan** — Plan execution order respecting dependencies between types
6. **write_tests** — For code-changing constituents, write failing tests first (TDD red phase)
7. **define_changes** — Implement all changes; failing tests MUST pass (TDD green phase)
8. **define_tests** — Harden tests, add edge cases across all constituent types
9. **validate_solution** — Validate each constituent type and overall coherence
