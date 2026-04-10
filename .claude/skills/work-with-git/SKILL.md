---
name: work-with-git
description: Handles all git operations for a task — staging, committing, branching, and pushing. Use at the end of any workflow to record completed work.
---

Perform git operations to record the completed work:
0. All new branches MUST follow the naming convention: `feature/<task-name>`, `chore/<task-name>`, `docs/<task-name>` or `bugfix/<task-name>`
1. All new branches MUST be created from `origin/main` — run `git fetch origin && git checkout -b <branch-name> origin/main`. Only deviate if the user explicitly specifies a different base in their prompt.
2. Run `git status` to review all modified and untracked files
3. Run `git diff` to confirm the changes match what was planned
4. Stage only files relevant to the current task — never use `git add -A` blindly
5. Write a commit message that explains *why* the change was made, not just what changed
6. Commit using the staged files
7. If working on a feature branch, verify the branch name matches the task before pushing
8. Report the commit hash and a one-line summary of what was recorded
