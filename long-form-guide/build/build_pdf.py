"""Build the complete long-form AI writing guide PDF."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    BaseDocTemplate,
    CondPageBreak,
    Frame,
    HRFlowable,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

BUILD_DIR = Path(__file__).resolve().parent
GUIDE_DIR = BUILD_DIR.parent
ROOT_DIR = GUIDE_DIR.parent
sys.path.insert(0, str(BUILD_DIR))

from components import badge, inline_markup, prompt_card, worksheet  # noqa: E402
from styles import GuideTheme, make_styles  # noqa: E402
from validate import load_markdown_sections, load_yaml_records  # noqa: E402


class GuideDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, theme: GuideTheme, styles: dict[str, Any]):
        super().__init__(
            filename,
            pagesize=letter,
            rightMargin=theme.margin_x,
            leftMargin=theme.margin_x,
            topMargin=theme.margin_top,
            bottomMargin=theme.margin_bottom,
            title="Writing a 60,000-Word Book with AI",
            author="Adrian Cruz",
            subject="A tool-agnostic system for planning, drafting, and revising long-form books with AI",
        )
        self.theme = theme
        self.styles_map = styles
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="normal",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates([
            PageTemplate(id="Cover", frames=frame, onPage=self._cover_page),
            PageTemplate(id="Body", frames=frame, onPage=self._body_page),
        ])

    def _cover_page(self, canvas, _doc):
        canvas.saveState()
        canvas.setFillColor(self.theme.paper)
        canvas.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
        canvas.setFillColor(self.theme.green)
        canvas.rect(0, 0, 0.24 * inch, letter[1], fill=1, stroke=0)
        canvas.restoreState()

    def _body_page(self, canvas, doc):
        canvas.saveState()
        canvas.setFillColor(self.theme.paper)
        canvas.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
        canvas.setStrokeColor(colors.HexColor("#D0C8BA"))
        canvas.line(doc.leftMargin, letter[1] - 0.48 * inch, letter[0] - doc.rightMargin, letter[1] - 0.48 * inch)
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(self.theme.muted)
        canvas.drawString(doc.leftMargin, 0.37 * inch, "WRITING A 60,000-WORD BOOK WITH AI")
        page_text = str(canvas.getPageNumber())
        canvas.drawRightString(letter[0] - doc.rightMargin, 0.37 * inch, page_text)
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            style_name = flowable.style.name
            if style_name in {"GuideH1", "GuideH2"}:
                level = 0 if style_name == "GuideH1" else 1
                text = flowable.getPlainText()
                key = f"heading-{level}-{self.page}-{abs(hash(text))}"
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(text, key, level=level, closed=False)
                self.notify("TOCEntry", (level, text, self.page, key))


def markdown_table(lines: list[str], styles: dict[str, Any], theme: GuideTheme):
    rows = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(set(cell) <= {"-", ":", " "} for cell in cells):
            continue
        rows.append([Paragraph(inline_markup(cell), styles["small"]) for cell in cells])
    if not rows:
        return Spacer(1, 1)
    col_width = 6.65 * inch / len(rows[0])
    table = Table(rows, colWidths=[col_width] * len(rows[0]), repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), theme.green),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#B9B4A9")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


def parse_markdown(text: str, styles: dict[str, Any], theme: GuideTheme):
    flow = []
    lines = text.splitlines()
    index = 0
    paragraph_lines: list[str] = []

    def flush_paragraph():
        if paragraph_lines:
            joined = " ".join(line.strip() for line in paragraph_lines)
            flow.append(Paragraph(inline_markup(joined), styles["body"]))
            paragraph_lines.clear()

    while index < len(lines):
        line = lines[index].rstrip()
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            index += 1
            continue
        if stripped.startswith("```"):
            flush_paragraph()
            code_lines = []
            index += 1
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code_lines.append(lines[index])
                index += 1
            code_style = ParagraphStyle("Code", parent=styles["small"], fontName="Courier", backColor=theme.pale_blue, borderPadding=8)
            flow.append(Paragraph("<br/>".join(inline_markup(item) for item in code_lines), code_style))
            index += 1
            continue
        if stripped.startswith("|") and "|" in stripped[1:]:
            flush_paragraph()
            table_lines = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index])
                index += 1
            flow.append(markdown_table(table_lines, styles, theme))
            flow.append(Spacer(1, 6))
            continue
        if stripped.startswith("# "):
            flush_paragraph()
            flow.extend([CondPageBreak(2.4 * inch), Paragraph(inline_markup(stripped[2:]), styles["h1"]), HRFlowable(width="100%", thickness=1.2, color=theme.gold), Spacer(1, 9)])
        elif stripped.startswith("## "):
            flush_paragraph()
            flow.append(Paragraph(inline_markup(stripped[3:]), styles["h2"]))
        elif stripped.startswith("### "):
            flush_paragraph()
            flow.append(Paragraph(inline_markup(stripped[4:]), styles["h3"]))
        elif stripped in {"[FICTION]", "[NONFICTION]", "[BIBLICAL PROJECT]", "[WARNING]", "[EXERCISE]"}:
            flush_paragraph()
            kind = stripped[1:-1].title()
            flow.extend([Spacer(1, 4), badge(kind, kind, styles), Spacer(1, 5)])
        elif stripped.startswith("> "):
            flush_paragraph()
            flow.append(Paragraph(inline_markup(stripped[2:]), styles["quote"]))
        elif stripped.startswith("- "):
            flush_paragraph()
            flow.append(Paragraph(f"&bull; {inline_markup(stripped[2:])}", styles["bullet"]))
        elif len(stripped) > 3 and stripped[0].isdigit() and ". " in stripped[:4]:
            flush_paragraph()
            number, body = stripped.split(". ", 1)
            flow.append(Paragraph(f"<b>{number}.</b> {inline_markup(body)}", styles["number"]))
        else:
            paragraph_lines.append(stripped)
        index += 1
    flush_paragraph()
    return flow


def cover_story(styles: dict[str, Any], theme: GuideTheme):
    title_style = styles["title"]
    center = ParagraphStyle("CoverCenter", parent=styles["small"], alignment=TA_CENTER, textColor=theme.muted)
    return [
        Spacer(1, 0.65 * inch),
        Paragraph("LONG-FORM WRITING SYSTEM", styles["cover_kicker"]),
        Paragraph("Writing a<br/>60,000-Word<br/>Book with AI", title_style),
        HRFlowable(width="42%", thickness=2, color=theme.gold, hAlign="LEFT"),
        Spacer(1, 18),
        Paragraph("A practical system for planning, drafting, controlling, and revising a long-form manuscript without losing the plot - or your voice.", styles["subtitle"]),
        Spacer(1, 0.55 * inch),
        Table(
            [[Paragraph("PLAN", styles["field"]), Paragraph("DRAFT", styles["field"]), Paragraph("CONTROL", styles["field"]), Paragraph("REVISE", styles["field"])]],
            colWidths=[1.45 * inch] * 4,
            style=TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), theme.pale_green),
                ("BOX", (0, 0), (-1, -1), 0.7, theme.green),
                ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#B9B4A9")),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("TOPPADDING", (0, 0), (-1, -1), 14),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
            ]),
        ),
        Spacer(1, 1.15 * inch),
        Paragraph("For fiction and nonfiction authors", center),
        Spacer(1, 8),
        Paragraph("ADRIAN CRUZ", styles["cover_kicker"]),
        NextPageTemplate("Body"),
        PageBreak(),
    ]


def build_guide(output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    theme = GuideTheme()
    styles = make_styles(theme)
    sections = load_markdown_sections(GUIDE_DIR / "content")
    templates = load_yaml_records(GUIDE_DIR / "data" / "templates.yaml", {"id", "title", "badge", "purpose", "instructions", "fields", "example"})
    prompts = load_yaml_records(GUIDE_DIR / "data" / "prompts.yaml", {"id", "title", "stage", "inputs", "author_decision", "prompt", "output_format", "model_must_not_decide", "example"})

    story = cover_story(styles, theme)
    story.extend([
        Paragraph("How to Use This Guide", styles["h1"]),
        Paragraph("Build the documents as you move through the six phases. The templates are working pages, not bonus material. Print them, copy them into your writing system, or adapt their fields to your preferred tool.", styles["body"]),
        Paragraph("Copyright and responsibility", styles["h2"]),
        Paragraph("Copyright 2026 Adrian Cruz. This guide offers a writing workflow, not legal, medical, mental-health, or pastoral advice. Authors remain responsible for verifying every fact, quotation, source, Scripture reference, permission, and sensitive recommendation in their manuscripts.", styles["body"]),
        PageBreak(),
        Paragraph("Contents", styles["h1"]),
    ])
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle("TOC1", parent=styles["toc"], leftIndent=0, firstLineIndent=0, spaceBefore=5, fontName="Helvetica-Bold"),
        ParagraphStyle("TOC2", parent=styles["toc"], leftIndent=16, firstLineIndent=0, spaceBefore=2),
    ]
    story.extend([toc, PageBreak()])

    for key in sorted(sections):
        story.extend(parse_markdown(sections[key], styles, theme))

    story.extend([PageBreak(), Paragraph("Working Templates", styles["h1"]), Paragraph("Copy these pages into the system where you write. Each template records an author decision or protects a form of manuscript memory.", styles["body"])] )
    for record in templates:
        story.append(CondPageBreak(4.8 * inch))
        story.extend(worksheet(record, styles, theme))

    story.extend([PageBreak(), Paragraph("Prompt Framework Library", styles["h1"]), Paragraph("These frameworks organize decisions. Replace the example inputs with current project documents and verify every factual result outside the model.", styles["body"])] )
    for index, record in enumerate(prompts):
        if index % 3 == 0:
            story.append(PageBreak())
        elif index:
            story.extend([Spacer(1, 8), HRFlowable(width="100%", thickness=0.8, color=theme.gold), Spacer(1, 8)])
        story.extend(prompt_card(record, styles, theme))

    story.extend([
        CondPageBreak(2.8 * inch),
        Paragraph("Final Principle", styles["h1"]),
        Paragraph("AI may generate pages. The author controls the book.", styles["title"]),
        Paragraph("Your name belongs on the manuscript because you accepted responsibility for its promise, structure, truth, voice, judgment, and final language.", styles["subtitle"]),
    ])

    doc = GuideDocTemplate(str(output_path), theme, styles)
    doc.multiBuild(story)
    return output_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT_DIR / "output" / "pdf" / "Writing_a_60000_Word_Book_with_AI.pdf")
    args = parser.parse_args()
    path = build_guide(args.output)
    from pypdf import PdfReader
    print(f"Built {path} ({len(PdfReader(str(path)).pages)} pages)")


if __name__ == "__main__":
    main()
