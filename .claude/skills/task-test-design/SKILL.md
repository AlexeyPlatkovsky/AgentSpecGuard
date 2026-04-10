---
name: task-test-design
description: Reviews and hardens tests after implementation (TDD green/refactor phase). Use during the define_tests workflow step to verify coverage and add edge cases.
---

Review and harden tests after the implementation passes (TDD green/refactor phase):

1. Confirm all tests written by `test-writer` now pass (green phase)
2. Add edge-case and regression tests missed in the red phase
3. Refactor tests for clarity without changing behavior
4. Assess final test coverage and report any remaining gaps
