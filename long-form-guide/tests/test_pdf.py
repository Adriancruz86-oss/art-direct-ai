from __future__ import annotations

import sys
import unittest
from pathlib import Path


GUIDE_DIR = Path(__file__).resolve().parents[1]
BUILD_DIR = GUIDE_DIR / "build"
sys.path.insert(0, str(BUILD_DIR))

from components import prompt_card, worksheet  # noqa: E402
from styles import BADGE_COLORS, GuideTheme, make_styles  # noqa: E402


class ComponentTests(unittest.TestCase):
    def setUp(self):
        self.theme = GuideTheme()
        self.styles = make_styles(self.theme)

    def test_every_required_badge_kind_has_colors(self):
        required = {"Fiction", "Nonfiction", "Biblical Project", "Template", "Warning", "Exercise"}
        self.assertEqual(required - BADGE_COLORS.keys(), set())

    def test_body_type_is_readable(self):
        self.assertGreaterEqual(self.styles["body"].fontSize, 10)
        self.assertGreaterEqual(self.styles["body"].leading / self.styles["body"].fontSize, 1.28)

    def test_worksheet_contains_fields(self):
        record = {
            "title": "Test Worksheet", "badge": "Template", "purpose": "Test purpose.",
            "instructions": "Complete it.", "fields": ["One", "Two"], "example": "Example.",
        }
        flow = worksheet(record, self.styles, self.theme)
        self.assertGreaterEqual(len(flow), 6)

    def test_prompt_card_contains_boundary_sections(self):
        record = {
            "title": "Test Prompt", "stage": "Drafting", "inputs": ["Brief"],
            "author_decision": "Choose.", "prompt": "Diagnose.", "output_format": "Table.",
            "model_must_not_decide": "Meaning.", "example": "Example.",
        }
        flow = prompt_card(record, self.styles, self.theme)
        self.assertGreaterEqual(len(flow), 9)


if __name__ == "__main__":
    unittest.main()
