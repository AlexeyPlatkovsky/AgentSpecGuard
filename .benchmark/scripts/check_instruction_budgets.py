#!/usr/bin/env python3
"""Check instruction-layer files against token budget limits.

Reads thresholds from .benchmark/configs/instruction-budgets.yaml
and approximates token counts (words * 1.3).
Exits with code 1 if any hard limit is exceeded.
"""

import argparse
import json
import sys
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


def get_required_limit(config: dict, section: str, field: str) -> int:
    section_data = config.get(section)
    if not isinstance(section_data, dict) or field not in section_data:
        raise KeyError(f"Missing config value: {section}.{field}")
    return int(section_data[field])


def status_label(ok: bool) -> str:
    return "PASSED" if ok else "FAILED"


def empty_section(key: str, name: str, limit: int) -> dict:
    return {
        "key": key,
        "name": name,
        "status": "PASSED",
        "limit": limit,
        "total_files": 0,
        "passed_files": 0,
        "failed_files": 0,
        "files": [],
        "failures": [],
    }


def add_file_result(section: dict, rel_path: str, ok: bool, tokens: int, limit: int) -> None:
    file_result = {
        "section": section["name"],
        "path": rel_path,
        "status": status_label(ok),
        "tokens": tokens,
        "limit": limit,
    }
    section["files"].append(file_result)
    section["total_files"] += 1
    if ok:
        section["passed_files"] += 1
    else:
        section["failed_files"] += 1
        section["status"] = "FAILED"
        section["failures"].append(file_result)


def build_report(root: Path, config: dict) -> dict:
    agents_limit = get_required_limit(config, "agents_md", "hard_limit")
    skills_limit = get_required_limit(config, "skills", "per_file_hard_limit")
    workflows_limit = get_required_limit(config, "workflows", "per_file_hard_limit")
    subagents_limit = get_required_limit(config, "subagents", "per_file_hard_limit")

    report = {
        "root": str(root),
        "overall_status": "PASSED",
        "sections": {
            "agents_md": empty_section("agents_md", "AGENTS.md", agents_limit),
            "skills": empty_section("skills", "Skills", skills_limit),
            "workflows": empty_section("workflows", "Workflows", workflows_limit),
            "subagents": empty_section("subagents", "Subagents", subagents_limit),
        },
        "failures": [],
    }

    agents_md = root / "AGENTS.md"
    if agents_md.exists():
        ok, tokens = check_file(str(agents_md), agents_limit)
        add_file_result(report["sections"]["agents_md"], "AGENTS.md", ok, tokens, agents_limit)

    skills_dir = root / ".claude" / "skills"
    if skills_dir.exists():
        for skill_file in sorted(skills_dir.rglob("SKILL.md")):
            ok, tokens = check_file(str(skill_file), skills_limit)
            rel = str(skill_file.relative_to(root))
            add_file_result(report["sections"]["skills"], rel, ok, tokens, skills_limit)

    workflows_dir = root / ".claude" / "workflows"
    if workflows_dir.exists():
        for workflow_file in sorted(workflows_dir.glob("*.md")):
            ok, tokens = check_file(str(workflow_file), workflows_limit)
            rel = str(workflow_file.relative_to(root))
            add_file_result(report["sections"]["workflows"], rel, ok, tokens, workflows_limit)

    agents_dir = root / ".claude" / "agents"
    if agents_dir.exists():
        for agent_file in sorted(agents_dir.rglob("*.md")):
            ok, tokens = check_file(str(agent_file), subagents_limit)
            rel = str(agent_file.relative_to(root))
            add_file_result(report["sections"]["subagents"], rel, ok, tokens, subagents_limit)

    failures = []
    for section in report["sections"].values():
        failures.extend(section["failures"])
        if section["status"] == "FAILED":
            report["overall_status"] = "FAILED"

    report["failures"] = failures
    return report


def print_human_report(report: dict) -> None:
    sections = report["sections"]
    print_section_files(sections["agents_md"])
    print_section_files(sections["skills"])
    print_section_files(sections["workflows"])
    print_section_files(sections["subagents"])

    if report["failures"]:
        print(f"\n{len(report['failures'])} file(s) exceeded budget limits.")
    else:
        print("\nAll files within budget limits.")


def print_section_files(section: dict) -> None:
    for file_result in section["files"]:
        status = "PASS" if file_result["status"] == "PASSED" else "FAIL"
        print(
            f"  {status}: {file_result['path']} "
            f"— {file_result['tokens']}/{file_result['limit']} tokens"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Emit the full report as JSON.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parents[2]
    config_path = root / ".benchmark" / "configs" / "instruction-budgets.yaml"

    if not config_path.exists():
        print(f"Config not found: {config_path}")
        return 1

    config = load_config(str(config_path))

    try:
        report = build_report(root, config)
    except KeyError as exc:
        print(str(exc))
        return 1

    if args.json_output:
        print(json.dumps(report, indent=2))
    else:
        print_human_report(report)

    return 1 if report["failures"] else 0


if __name__ == "__main__":
    sys.exit(main())
