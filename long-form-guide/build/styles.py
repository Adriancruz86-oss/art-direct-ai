"""Visual theme and paragraph styles for the long-form guide."""

from __future__ import annotations

from dataclasses import dataclass

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch


@dataclass(frozen=True)
class GuideTheme:
    paper: colors.Color = colors.HexColor("#F7F1E6")
    green: colors.Color = colors.HexColor("#183F36")
    navy: colors.Color = colors.HexColor("#17324D")
    rust: colors.Color = colors.HexColor("#A6533F")
    gold: colors.Color = colors.HexColor("#B58A43")
    charcoal: colors.Color = colors.HexColor("#2D302F")
    muted: colors.Color = colors.HexColor("#66706C")
    pale_green: colors.Color = colors.HexColor("#E5ECE5")
    pale_rust: colors.Color = colors.HexColor("#F2E2DA")
    pale_blue: colors.Color = colors.HexColor("#E7EDF2")
    margin_x: float = 0.68 * inch
    margin_top: float = 0.62 * inch
    margin_bottom: float = 0.62 * inch


BADGE_COLORS = {
    "Fiction": (colors.HexColor("#17324D"), colors.white),
    "Nonfiction": (colors.HexColor("#183F36"), colors.white),
    "Biblical Project": (colors.HexColor("#7A5630"), colors.white),
    "Template": (colors.HexColor("#A6533F"), colors.white),
    "Warning": (colors.HexColor("#8B3A32"), colors.white),
    "Exercise": (colors.HexColor("#35634C"), colors.white),
}


def make_styles(theme: GuideTheme) -> dict[str, ParagraphStyle]:
    sample = getSampleStyleSheet()
    return {
        "body": ParagraphStyle(
            "GuideBody", parent=sample["BodyText"], fontName="Helvetica",
            fontSize=10, leading=12.8, textColor=theme.charcoal,
            spaceAfter=5, allowWidows=0, allowOrphans=0,
        ),
        "small": ParagraphStyle(
            "GuideSmall", parent=sample["BodyText"], fontName="Helvetica",
            fontSize=8.4, leading=10.8, textColor=theme.muted, spaceAfter=5,
        ),
        "h1": ParagraphStyle(
            "GuideH1", parent=sample["Heading1"], fontName="Times-Bold",
            fontSize=27, leading=29, textColor=theme.green, spaceBefore=6,
            spaceAfter=16, keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "GuideH2", parent=sample["Heading2"], fontName="Times-Bold",
            fontSize=17, leading=19.5, textColor=theme.green, spaceBefore=10,
            spaceAfter=6, keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "GuideH3", parent=sample["Heading3"], fontName="Helvetica-Bold",
            fontSize=12.3, leading=15, textColor=theme.rust, spaceBefore=10,
            spaceAfter=5, keepWithNext=True,
        ),
        "title": ParagraphStyle(
            "GuideTitle", parent=sample["Title"], fontName="Times-Bold",
            fontSize=38, leading=40, textColor=theme.green, alignment=TA_LEFT,
            spaceAfter=20,
        ),
        "subtitle": ParagraphStyle(
            "GuideSubtitle", parent=sample["BodyText"], fontName="Times-Italic",
            fontSize=16, leading=21, textColor=theme.navy, spaceAfter=18,
        ),
        "cover_kicker": ParagraphStyle(
            "CoverKicker", parent=sample["BodyText"], fontName="Helvetica-Bold",
            fontSize=9, leading=11, textColor=theme.rust, tracking=1.5,
            spaceAfter=18,
        ),
        "quote": ParagraphStyle(
            "GuideQuote", parent=sample["BodyText"], fontName="Times-Italic",
            fontSize=13, leading=17, leftIndent=18, rightIndent=18,
            borderColor=theme.gold, borderWidth=0, borderPadding=9,
            textColor=theme.green, spaceBefore=8, spaceAfter=10,
        ),
        "bullet": ParagraphStyle(
            "GuideBullet", parent=sample["BodyText"], fontName="Helvetica",
            fontSize=9.8, leading=12.8, leftIndent=16, firstLineIndent=-8,
            bulletIndent=4, textColor=theme.charcoal, spaceAfter=4,
        ),
        "number": ParagraphStyle(
            "GuideNumber", parent=sample["BodyText"], fontName="Helvetica",
            fontSize=9.8, leading=12.8, leftIndent=20, firstLineIndent=-12,
            textColor=theme.charcoal, spaceAfter=4,
        ),
        "badge": ParagraphStyle(
            "GuideBadge", parent=sample["BodyText"], fontName="Helvetica-Bold",
            fontSize=7.5, leading=9, textColor=colors.white, alignment=TA_CENTER,
        ),
        "worksheet_title": ParagraphStyle(
            "WorksheetTitle", parent=sample["Heading1"], fontName="Times-Bold",
            fontSize=23, leading=26, textColor=theme.green, spaceAfter=8,
        ),
        "prompt_title": ParagraphStyle(
            "PromptTitle", parent=sample["Heading2"], fontName="Times-Bold",
            fontSize=15, leading=17, textColor=theme.green, spaceAfter=4,
        ),
        "field": ParagraphStyle(
            "WorksheetField", parent=sample["BodyText"], fontName="Helvetica-Bold",
            fontSize=9, leading=11, textColor=theme.navy,
        ),
        "toc": ParagraphStyle(
            "TOC", parent=sample["BodyText"], fontName="Helvetica",
            fontSize=10, leading=14, textColor=theme.charcoal,
        ),
    }
