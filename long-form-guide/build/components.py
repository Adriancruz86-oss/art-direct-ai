"""Reusable ReportLab components for the guide."""

from __future__ import annotations

from html import escape
from typing import Any

from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether, Paragraph, Spacer, Table, TableStyle

from styles import BADGE_COLORS, GuideTheme


def inline_markup(text: str) -> str:
    value = escape(text.strip())
    while "**" in value:
        value = value.replace("**", "<b>", 1).replace("**", "</b>", 1)
    return value.replace("  ", " ")


def badge(text: str, kind: str, styles: dict[str, Any]):
    background, foreground = BADGE_COLORS.get(kind, BADGE_COLORS["Template"])
    cell = Paragraph(escape(text.upper()), styles["badge"])
    table = Table([[cell]], colWidths=[1.62 * inch], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), background),
        ("TEXTCOLOR", (0, 0), (-1, -1), foreground),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return table


def callout(title: str, body: str, kind: str, styles: dict[str, Any], theme: GuideTheme):
    background = {
        "Warning": theme.pale_rust,
        "Biblical Project": colors.HexColor("#EFE7D7"),
        "Fiction": theme.pale_blue,
        "Nonfiction": theme.pale_green,
        "Exercise": theme.pale_green,
    }.get(kind, theme.pale_blue)
    contents = [badge(kind, kind, styles), Spacer(1, 7)]
    if title:
        contents.append(Paragraph(inline_markup(title), styles["h3"]))
    contents.append(Paragraph(inline_markup(body), styles["body"]))
    table = Table([[contents]], colWidths=[6.65 * inch], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), background),
        ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#C8C1B4")),
        ("LEFTPADDING", (0, 0), (-1, -1), 13),
        ("RIGHTPADDING", (0, 0), (-1, -1), 13),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    return table


def worksheet(record: dict[str, Any], styles: dict[str, Any], theme: GuideTheme):
    flow = [badge(record["badge"], record["badge"], styles), Spacer(1, 9)]
    flow.append(Paragraph(escape(record["title"]), styles["worksheet_title"]))
    flow.append(Paragraph(f"<b>Purpose:</b> {escape(record['purpose'])}", styles["body"]))
    flow.append(Paragraph(escape(record["instructions"]), styles["body"]))
    rows = []
    for field in record["fields"]:
        rows.append([Paragraph(escape(field), styles["field"]), ""])
    table = Table(rows, colWidths=[2.05 * inch, 4.55 * inch], rowHeights=[0.35 * inch] * len(rows), repeatRows=0)
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (0, -1), theme.pale_green),
        ("GRID", (0, 0), (-1, -1), 0.45, colors.HexColor("#B9B4A9")),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
    ]))
    flow.extend([table, Spacer(1, 10), callout("Worked example", record["example"], "Exercise", styles, theme)])
    return flow


def prompt_card(record: dict[str, Any], styles: dict[str, Any], theme: GuideTheme):
    flow = [badge("Prompt Framework", "Template", styles), Spacer(1, 9)]
    flow.append(Paragraph(escape(record["title"]), styles["prompt_title"]))
    flow.append(Paragraph(f"<b>Stage:</b> {escape(record['stage'])}", styles["small"]))
    flow.append(Paragraph(f"<b>Inputs:</b> {escape('; '.join(record['inputs']))}", styles["small"]))
    flow.append(Paragraph(f"<b>The author decides:</b> {escape(record['author_decision'])}", styles["small"]))
    prompt_box = Table([[Paragraph(escape(record["prompt"]), styles["small"])]], colWidths=[6.5 * inch])
    prompt_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), theme.pale_blue),
        ("BOX", (0, 0), (-1, -1), 0.8, theme.navy),
        ("LEFTPADDING", (0, 0), (-1, -1), 13),
        ("RIGHTPADDING", (0, 0), (-1, -1), 13),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    flow.extend([Spacer(1, 5), prompt_box, Spacer(1, 9)])
    flow.append(Paragraph(f"<b>Output:</b> {escape(record['output_format'])}", styles["small"]))
    flow.append(Paragraph(f"<b>The model must not decide:</b> {escape(record['model_must_not_decide'])}", styles["small"]))
    flow.append(Paragraph(f"<b>Example:</b> {escape(record['example'])}", styles["small"]))
    return flow
