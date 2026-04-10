import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / ".benchmark"
    / "scripts"
    / "check_instruction_budgets.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location("check_instruction_budgets", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class CheckInstructionBudgetsTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_build_report_marks_all_sections_passed(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            self.write_file(root / "AGENTS.md", "brief instructions")
            self.write_file(root / ".claude" / "skills" / "sample" / "SKILL.md", "skill content")
            self.write_file(root / ".claude" / "workflows" / "feature.md", "workflow content")
            self.write_file(root / ".claude" / "agents" / "reviewer.md", "agent content")

            report = self.module.build_report(root, self.config(limit=100))

            self.assertEqual(report["overall_status"], "PASSED")
            self.assertEqual(report["sections"]["agents_md"]["status"], "PASSED")
            self.assertEqual(report["sections"]["agents_md"]["total_files"], 1)
            self.assertEqual(report["sections"]["skills"]["total_files"], 1)
            self.assertEqual(report["sections"]["workflows"]["total_files"], 1)
            self.assertEqual(report["sections"]["subagents"]["total_files"], 1)
            self.assertEqual(report["failures"], [])

    def test_build_report_lists_exact_failing_file_paths(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            self.write_file(root / "AGENTS.md", "brief instructions")
            self.write_file(
                root / ".claude" / "skills" / "oversized" / "SKILL.md",
                "word " * 20,
            )
            self.write_file(root / ".claude" / "workflows" / "feature.md", "workflow content")
            self.write_file(root / ".claude" / "agents" / "reviewer.md", "agent content")

            report = self.module.build_report(root, self.config(limit=10))

            self.assertEqual(report["overall_status"], "FAILED")
            self.assertEqual(report["sections"]["skills"]["status"], "FAILED")
            self.assertEqual(report["sections"]["skills"]["failed_files"], 1)
            self.assertEqual(
                report["sections"]["skills"]["failures"][0]["path"],
                ".claude/skills/oversized/SKILL.md",
            )
            self.assertEqual(
                report["failures"][0]["path"],
                ".claude/skills/oversized/SKILL.md",
            )

    @staticmethod
    def config(limit: int) -> dict:
        return {
            "agents_md": {"hard_limit": limit},
            "skills": {"per_file_hard_limit": limit},
            "workflows": {"per_file_hard_limit": limit},
            "subagents": {"per_file_hard_limit": limit},
        }

    @staticmethod
    def write_file(path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)


if __name__ == "__main__":
    unittest.main()
