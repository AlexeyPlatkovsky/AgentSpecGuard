---
name: feature-implementation
description: Executes code changes according to the plan (TDD green phase). Use during the define_changes workflow step AFTER test-writer has produced failing tests.
---

Implement the planned changes to make failing tests pass (TDD green phase):

1. Confirm failing tests exist from `test-writer` — do NOT proceed without them
2. Apply the minimum code changes needed to make all failing tests pass
3. Run the test suite — all tests MUST pass before completing
4. Respect all constraints and conventions identified during discovery
5. Produce a list of all modified files when done
