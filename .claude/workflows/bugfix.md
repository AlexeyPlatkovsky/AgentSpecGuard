# Workflow: Bugfix

## Steps

1. **classify_task** — Confirm task type is `bugfix`
2. **discover_context** — Locate the defect, gather reproduction steps and relevant code
3. **identify_constraints** — Determine affected contracts, dependencies, and risk areas
4. **select_skills** — Choose applicable skills for this bugfix
5. **generate_plan** — Define the fix approach
6. **write_tests** — Write failing tests that reproduce the defect (TDD red phase)
7. **define_changes** — Implement the fix to make failing tests pass (TDD green phase)
8. **define_tests** — Harden tests, add edge cases, refactor tests
9. **validate_solution** — Verify the fix resolves the issue without regressions
