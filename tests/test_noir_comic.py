from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
NOIR_PAGE = ROOT / "i-learned-it-from-watching-you-noir" / "index.html"
VINTAGE_PAGE = ROOT / "blog" / "i-learned-it-from-watching-you" / "index.html"


class ImageCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.viewports = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "img":
            self.images.append(attributes)
        if tag == "meta" and attributes.get("name") == "viewport":
            self.viewports.append(attributes.get("content", ""))


class NoirComicPageTests(unittest.TestCase):
    def test_noir_page_has_all_seven_images_in_reading_order(self):
        parser = ImageCollector()
        parser.feed(NOIR_PAGE.read_text(encoding="utf-8"))

        expected_sources = [
            "../assets/00_cover.png",
            "../assets/01_page_1.png",
            "../assets/02_page_2.png",
            "../assets/03_page_3.png",
            "../assets/04_page_4.png",
            "../assets/05_page_5.png",
            "../assets/06_back_cover.png",
        ]
        self.assertEqual([image.get("src") for image in parser.images], expected_sources)
        self.assertTrue(all(image.get("alt") for image in parser.images))
        self.assertTrue(all((ROOT / source.removeprefix("../")).is_file() for source in expected_sources))

    def test_noir_page_is_mobile_ready(self):
        parser = ImageCollector()
        parser.feed(NOIR_PAGE.read_text(encoding="utf-8"))
        self.assertIn("width=device-width, initial-scale=1", parser.viewports)

    def test_vintage_gallery_still_contains_fifteen_pages(self):
        parser = ImageCollector()
        parser.feed(VINTAGE_PAGE.read_text(encoding="utf-8"))
        vintage_pages = [image for image in parser.images if image.get("src", "").startswith("images/page-")]
        self.assertEqual(len(vintage_pages), 15)


if __name__ == "__main__":
    unittest.main()
