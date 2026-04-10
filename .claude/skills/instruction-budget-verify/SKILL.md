---
name: instruction-budget-verify
description: Validates instruction-layer files against token budget limits. Use when AGENTS.md, skills, workflows, or subagent files change.
---

Check instruction-layer files against budget limits:

1. Run the budget validation script:
   ```bash
   python3 .benchmark/scripts/check_instruction_budgets.py
   ```
2. Report the results — pass or fail per file, with token counts vs thresholds
3. If any file exceeds its hard limit, flag it for reduction
