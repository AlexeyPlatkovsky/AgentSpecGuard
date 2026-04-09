# Skill: instruction-doc-verify

## Purpose

Validates structural consistency of instruction-layer files.

## When Used

When any instruction-layer file changes (AGENTS.md, skills, workflows, subagents).

## Inputs

- Changed instruction-layer file paths

## Outputs

- Consistency check result (pass/fail)
- Structural issues found (if any)

## Checks

- Required sections are present in each file type
- Cross-references between AGENTS.md, skills, and workflows are valid
- No orphaned or missing skill/workflow references
