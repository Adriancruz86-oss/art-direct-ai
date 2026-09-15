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
python -m unittest discover -s long-form-guide/tests -v
```

The final build and release commands will be added after the PDF builder is implemented.
