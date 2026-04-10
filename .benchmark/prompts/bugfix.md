# Benchmark Prompt: Bugfix

## Scenario

A function `calculate_total` in `src/billing.py` returns incorrect totals when discount percentage exceeds 100%. The function should cap discounts at 100%.

## Task

Fix the bug in `calculate_total` so that discounts are capped at 100% and negative totals are not possible.

## Expected Behavior

- `calculate_total(100, 50)` → `50.0`
- `calculate_total(100, 150)` → `0.0`
- `calculate_total(100, 0)` → `100.0`
