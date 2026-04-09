# Skill: instruction-budget-verify

## Purpose

Validates that instruction-layer files stay within defined token budget limits.

## When Used

When any instruction-layer file changes (AGENTS.md, skills, workflows, subagents).

## Inputs

- Changed instruction-layer file paths

## Outputs

- Budget check result (pass/fail per file)
- Token counts vs thresholds

## Mechanism

Invokes the external script `.benchmark/scripts/check_instruction_budgets.py` which reads thresholds from `.benchmark/configs/instruction-budgets.yaml`.
