from __future__ import annotations

import sys
import unittest
from pathlib import Path


GUIDE_DIR = Path(__file__).resolve().parents[1]
BUILD_DIR = GUIDE_DIR / "build"
sys.path.insert(0, str(BUILD_DIR))

from components import prompt_card, worksheet  # noqa: E402
from styles import BADGE_COLORS, GuideTheme, make_styles  # noqa: E402


OUTPUT_PDF = GUIDE_DIR.parent / "output" / "pdf" / "Writing_a_60000_Word_Book_with_AI.pdf"


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


class FinishedPdfTests(unittest.TestCase):
    def test_finished_pdf_structure(self):
        from pypdf import PdfReader

        self.assertTrue(OUTPUT_PDF.is_file())
        self.assertEqual(OUTPUT_PDF.read_bytes()[:4], b"%PDF")
        reader = PdfReader(str(OUTPUT_PDF))
        self.assertGreaterEqual(len(reader.pages), 50)
        self.assertLessEqual(len(reader.pages), 70)
        self.assertEqual(reader.metadata.title, "Writing a 60,000-Word Book with AI")
        text = "\n".join((page.extract_text() or "") for page in reader.pages)
        for required in ["Build the Foundation", "Architect 60,000 Words", "Working Templates", "Prompt Framework Library"]:
            self.assertIn(required, text)


if __name__ == "__main__":
    unittest.main()
