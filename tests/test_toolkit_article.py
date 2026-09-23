import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
ARTICLE = ROOT / "stop-regenerating-ai-illustrations.html"
INDEX = ROOT / "index.html"
OFFER_URL = "https://adrianashley.gumroad.com/l/ai-art-director-toolkit?offer_code=LAUNCH999"


class ToolkitArticleTests(unittest.TestCase):
    def test_article_has_complete_metadata_and_launch_offer(self):
        html = ARTICLE.read_text(encoding="utf-8")
        self.assertIn("<title>Stop Regenerating", html)
        self.assertIn('meta property="og:type" content="article"', html)
        self.assertIn('rel="canonical"', html)
        self.assertGreaterEqual(html.count(OFFER_URL), 2)
        self.assertIn("$9.99", html)
        self.assertIn("$29.99", html)

    def test_homepage_features_the_article(self):
        html = INDEX.read_text(encoding="utf-8")
        self.assertIn("stop-regenerating-ai-illustrations.html", html)
        self.assertIn("Why Your AI Illustrations Keep Drifting", html)


if __name__ == "__main__":
    unittest.main()
