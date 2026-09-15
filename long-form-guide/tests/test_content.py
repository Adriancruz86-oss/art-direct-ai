from __future__ import annotations

import sys
from pathlib import Path

import tempfile
import unittest


GUIDE_DIR = Path(__file__).resolve().parents[1]
BUILD_DIR = GUIDE_DIR / "build"
CONTENT_DIR = GUIDE_DIR / "content"
DATA_DIR = GUIDE_DIR / "data"
sys.path.insert(0, str(BUILD_DIR))

from validate import find_prohibited_text, load_markdown_sections, load_yaml_records  # noqa: E402


class ValidationUnitTests(unittest.TestCase):
    def test_load_markdown_sections_orders_and_keys_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)
            (path / "01-second.md").write_text("# Second\nBody", encoding="utf-8")
            (path / "00-first.md").write_text("# First\nBody", encoding="utf-8")
            self.assertEqual(list(load_markdown_sections(path)), ["00", "01"])

    def test_load_markdown_sections_rejects_empty_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)
            (path / "00-empty.md").write_text("  ", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "empty"):
                load_markdown_sections(path)

    def test_load_yaml_records_requires_shape_and_unique_ids(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "records.yaml"
            path.write_text('[{"id":"one","title":"First"},{"id":"two","title":"Second"}]', encoding="utf-8")
            records = load_yaml_records(path, {"id", "title"})
            self.assertEqual([record["id"] for record in records], ["one", "two"])

    def test_load_yaml_records_rejects_duplicate_ids(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "records.yaml"
            path.write_text('[{"id":"same"},{"id":"same"}]', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Duplicate id"):
                load_yaml_records(path, {"id"})

    def test_find_prohibited_text(self):
        cases = [
            ("Finish this TODO", "unfinished task marker"),
            ("Lorem ipsum dolor", "dummy filler prose"),
            ("See turn3search2", "tool citation token"),
            ("##   \n", "empty markdown heading"),
        ]
        for text, label in cases:
            with self.subTest(label=label):
                self.assertIn(label, find_prohibited_text(text))


class SourceContractTests(unittest.TestCase):
    def test_all_content_modules_exist(self):
        expected = {f"{index:02d}" for index in range(8)}
        found = {path.name[:2] for path in CONTENT_DIR.glob("*.md")}
        self.assertTrue(expected <= found)

    def test_sources_contain_no_prohibited_text(self):
        violations: list[tuple[str, str]] = []
        source_files = list(CONTENT_DIR.glob("*.md")) + list(DATA_DIR.glob("*.yaml"))
        for path in source_files:
            violations.extend((path.name, hit) for hit in find_prohibited_text(path.read_text(encoding="utf-8")))
        self.assertEqual(violations, [])

    def test_opening_modules_cover_the_core_method(self):
        sections = load_markdown_sections(CONTENT_DIR)
        text = "\n".join(sections.get(key, "") for key in ("00", "01", "02")).casefold()
        required = [
            "do not ask ai to remember the whole book",
            "project bible",
            "chapter brief",
            "60,000-word",
            "[fiction]",
            "[nonfiction]",
            "[biblical project]",
            "20-30 chapters",
        ]
        missing = [item for item in required if item not in text]
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
