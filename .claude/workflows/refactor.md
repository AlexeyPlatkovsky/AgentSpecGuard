# Workflow: Refactor

## Steps

1. **classify_task** — Confirm task type is `refactor`
2. **discover_context** — Understand the code to be restructured and its dependencies
3. **identify_constraints** — Ensure no behavior changes; identify contracts to preserve
4. **select_skills** — Choose applicable skills for this refactor
5. **generate_plan** — Define the restructuring approach
6. **write_tests** — Write or verify tests that lock current behavior before refactoring (TDD red phase)
7. **define_changes** — Apply the refactoring; all existing tests MUST keep passing (TDD green phase)
8. **define_tests** — Harden tests, add coverage for restructured code
9. **validate_solution** — Confirm behavior is unchanged and structure is improved
