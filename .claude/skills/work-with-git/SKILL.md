---
name: work-with-git
description: Handles git operations for a task. Use when branch, diff, staging, commit, or push work is needed, but do not commit or push unless the user explicitly asks for it.
---

Perform git operations needed for the task:
0. All new branches MUST follow the naming convention: `feature/<task-name>`, `chore/<task-name>`, `docs/<task-name>` or `bugfix/<task-name>`
1. All new branches MUST be created from `origin/main` — run `git fetch origin && git checkout -b <branch-name> origin/main`. Only deviate if the user explicitly specifies a different base in their prompt.
2. Run `git status` to review all modified and untracked files
3. Run `git diff` to confirm the changes match what was planned
4. Stage only files relevant to the current task — never use `git add -A` blindly
5. Do NOT create a commit or push to a remote unless the user explicitly asks for that action.
6. If the user explicitly asks for a commit, write a commit message that explains *why* the change was made, not just what changed, then commit using only the staged files.
7. If the user explicitly asks for a push, verify the branch name matches the task before pushing.
8. Report the git state you changed. If you committed, include the commit hash. If you did not commit or push, say so explicitly.
