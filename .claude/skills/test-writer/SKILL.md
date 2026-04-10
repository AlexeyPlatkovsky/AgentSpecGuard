---
name: test-writer
description: Writes failing tests before implementation (TDD red phase). Use before feature-implementation in any code-changing workflow to establish the test-first contract.
---

Write tests BEFORE any production code changes (TDD red phase):

1. Review the plan and requirements from discovery
2. Identify the expected behaviors and edge cases
3. Write test cases that express the desired behavior
4. Run the tests — they MUST fail (red phase confirms the behavior is not yet implemented)
5. If any test passes, it does not cover new behavior — revise or remove it
6. Report the list of failing tests as the contract for implementation
