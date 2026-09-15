# Long-Form Guide Source

This directory contains the editable source and deterministic PDF build for
**Writing a 60,000-Word Book with AI**.

## Editorial rules

- Keep instructions tool-agnostic. Product names may appear only when discussing portability.
- Never invent quotations, Bible verses, citations, statistics, or source details.
- Distinguish source text, observation, interpretation, theological choice, and application.
- Use `[FICTION]`, `[NONFICTION]`, `[BIBLICAL PROJECT]`, `[WARNING]`, and `[EXERCISE]` markers for branch-specific material.
- Use ASCII hyphens in source and output.
- Every worksheet and prompt needs a purpose, instructions, and a worked example.
- Guidance affecting readers ages 13-21 must require qualified human review where appropriate.

## Source layout

- `content/` contains the eight ordered manuscript modules.
- `data/templates.yaml` contains the working worksheets and trackers.
- `data/prompts.yaml` contains adaptable prompt frameworks.
- `build/` contains validation and PDF-generation code.
- `tests/` contains content and finished-PDF checks.
- `qa/` contains the visual review record and temporary rendered pages.

## Development checks

```bash
/Users/adriancruz/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  -m unittest discover -s long-form-guide/tests -v
```

## Build

Run from the repository root:

```bash
/Users/adriancruz/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  long-form-guide/build/build_pdf.py
```

The finished file is written to:

`output/pdf/Writing_a_60000_Word_Book_with_AI.pdf`

## Release record

- Build date: 2026-09-15
- Format: US Letter PDF
- Page count: 70
- Automated checks: 16 passing
- SHA-256: `3a79850b8317cbd08b4f2af8f4e74f5998f0908aca46de93367a019d2a92bd9e`
- Editorial and visual QA records: `long-form-guide/qa/`
