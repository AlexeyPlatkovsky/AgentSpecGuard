#!/usr/bin/env python3
"""Check instruction-layer files against token budget limits.

Reads thresholds from .benchmark/configs/instruction-budgets.yaml
and approximates token counts (words * 1.3).
Exits with code 1 if any hard limit is exceeded.
"""

import sys
import os
from pathlib import Path

try:
    import yaml
except ImportError:
    # Fallback: parse the simple YAML manually
    yaml = None


def load_config(config_path: str) -> dict:
    with open(config_path, "r") as f:
        if yaml:
            return yaml.safe_load(f)
        # Simple parser for flat YAML with one level of nesting
        config = {}
        current_key = None
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if not line.startswith(" ") and stripped.endswith(":"):
                current_key = stripped[:-1]
                config[current_key] = {}
            elif current_key and ":" in stripped:
                k, v = stripped.split(":", 1)
                config[current_key][k.strip()] = int(v.strip())
        return config


def approximate_tokens(text: str) -> int:
    """Approximate token count: word count * 1.3."""
    words = len(text.split())
    return int(words * 1.3)


def check_file(filepath: str, hard_limit: int) -> tuple[bool, int]:
    with open(filepath, "r") as f:
        content = f.read()
    tokens = approximate_tokens(content)
    return tokens <= hard_limit, tokens


def main():
    root = Path(__file__).resolve().parents[2]
    config_path = root / ".benchmark" / "configs" / "instruction-budgets.yaml"

    if not config_path.exists():
        print(f"Config not found: {config_path}")
        sys.exit(1)

    config = load_config(str(config_path))
    failures = []

    # Check AGENTS.md
    agents_md = root / "AGENTS.md"
    if agents_md.exists():
        limit = config.get("agents_md", {}).get("hard_limit", 1500)
        ok, tokens = check_file(str(agents_md), limit)
        status = "PASS" if ok else "FAIL"
        print(f"  {status}: AGENTS.md — {tokens}/{limit} tokens")
        if not ok:
            failures.append(f"AGENTS.md: {tokens} > {limit}")

    # Check skills
    skills_dir = root / ".claude" / "skills"
    if skills_dir.exists():
        limit = config.get("skills", {}).get("per_file_hard_limit", 500)
        for skill_file in sorted(skills_dir.rglob("SKILL.md")):
            ok, tokens = check_file(str(skill_file), limit)
            rel = skill_file.relative_to(root)
            status = "PASS" if ok else "FAIL"
            print(f"  {status}: {rel} — {tokens}/{limit} tokens")
            if not ok:
                failures.append(f"{rel}: {tokens} > {limit}")

    # Check workflows
    workflows_dir = root / ".claude" / "workflows"
    if workflows_dir.exists():
        limit = config.get("workflows", {}).get("per_file_hard_limit", 400)
        for wf_file in sorted(workflows_dir.glob("*.md")):
            ok, tokens = check_file(str(wf_file), limit)
            rel = wf_file.relative_to(root)
            status = "PASS" if ok else "FAIL"
            print(f"  {status}: {rel} — {tokens}/{limit} tokens")
            if not ok:
                failures.append(f"{rel}: {tokens} > {limit}")

    # Check subagents
    agents_dir = root / ".claude" / "agents"
    if agents_dir.exists():
        limit = config.get("subagents", {}).get("per_file_hard_limit", 500)
        for agent_file in sorted(agents_dir.rglob("AGENT.md")):
            ok, tokens = check_file(str(agent_file), limit)
            rel = agent_file.relative_to(root)
            status = "PASS" if ok else "FAIL"
            print(f"  {status}: {rel} — {tokens}/{limit} tokens")
            if not ok:
                failures.append(f"{rel}: {tokens} > {limit}")

    if failures:
        print(f"\n{len(failures)} file(s) exceeded budget limits.")
        sys.exit(1)
    else:
        print("\nAll files within budget limits.")
        sys.exit(0)


if __name__ == "__main__":
    main()
