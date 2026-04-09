# Benchmark Prompt: Feature

## Scenario

The project needs a new utility function `parse_duration` that converts human-readable duration strings (e.g., "2h30m", "45s", "1d12h") into total seconds.

## Task

Implement `parse_duration` in `src/utils.py` with tests.

## Expected Behavior

- `parse_duration("2h30m")` → `9000`
- `parse_duration("45s")` → `45`
- `parse_duration("1d12h")` → `129600`
- Invalid input raises `ValueError`
