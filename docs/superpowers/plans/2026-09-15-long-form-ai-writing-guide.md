# Long-Form AI Writing Guide Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a polished, tool-agnostic, 50-70-page PDF that teaches fiction and nonfiction authors to build a coherent manuscript of approximately 60,000 words with AI assistance.

**Architecture:** Store the guide as focused Markdown content modules plus structured YAML data for worksheets and prompt templates. Validate content requirements before passing the modules to a deterministic ReportLab builder, render the resulting PDF to page images, and perform text and visual QA before publishing the final PDF under `outputs/`.

**Tech Stack:** Markdown, YAML, Python 3, ReportLab, PyYAML, pypdf, pdfplumber, Poppler (`pdftoppm` and `pdfinfo`), pytest

**Spec:** `docs/superpowers/specs/2026-09-15-long-form-ai-writing-guide-design.md`

## Global Constraints

- The finished designed PDF must contain 50-70 pages, targeting roughly 60 pages.
- The workflow must remain tool-agnostic and must not depend on vendor-specific features.
- The guide must support fiction and nonfiction through one shared workflow with clearly marked branches.
- The recurring nonfiction example is a 60,000-word book defining biblical manhood for sons and young men ages 13-21.
- The biblical example demonstrates process and must not prescribe one denomination's doctrine.
- No fabricated quotations, verses, citations, sources, statistics, or claims are permitted.
- Source text, interpretation, doctrine, and application must remain visibly distinct.
- Every promised worksheet and prompt framework must include instructions and a worked example.
- Sensitive advice for ages 13-21 must explicitly require qualified human review.
- Final output must pass content, page-count, typography, overflow, broken-link, and visual consistency checks.

## File Structure

- `long-form-guide/README.md` - build instructions, source organization, and editorial rules
- `long-form-guide/content/00-front-matter.md` - title material, introduction, and long-form failure modes
- `long-form-guide/content/01-foundation.md` - promise, reader, project bible, voice, sources, and boundaries
- `long-form-guide/content/02-architecture.md` - 60,000-word structure, chapter map, budgets, and stress tests
- `long-form-guide/content/03-operating-system.md` - trackers, ledgers, context packets, and decision logs
- `long-form-guide/content/04-drafting.md` - chapter-by-chapter drafting workflow and branch guidance
- `long-form-guide/content/05-revision.md` - controlled revision passes and human review
- `long-form-guide/content/06-assembly.md` - file control, manuscript assembly, beta readers, and final checks
- `long-form-guide/content/07-worked-examples.md` - biblical-manhood and fiction examples
- `long-form-guide/data/templates.yaml` - eighteen worksheet/template definitions and worked examples
- `long-form-guide/data/prompts.yaml` - fourteen adaptable prompt frameworks
- `long-form-guide/build/styles.py` - color, typography, spacing, badges, callouts, and page templates
- `long-form-guide/build/components.py` - reusable ReportLab flowables for chapters, prompts, worksheets, warnings, and diagrams
- `long-form-guide/build/build_pdf.py` - content loader, document assembly, TOC, links, headers, footers, and PDF export
- `long-form-guide/build/validate.py` - source and finished-PDF validation
- `long-form-guide/tests/test_content.py` - content, template, prompt, and prohibited-placeholder tests
- `long-form-guide/tests/test_pdf.py` - page count, metadata, bookmarks, text, and output-file tests
- `long-form-guide/qa/visual-review.md` - page-by-page visual review record
- `outputs/Writing_a_60000_Word_Book_with_AI.pdf` - final user-facing guide

---

### Task 1: Establish the guide source contract and validation harness

**Files:**
- Create: `long-form-guide/README.md`
- Create: `long-form-guide/build/validate.py`
- Create: `long-form-guide/tests/test_content.py`

**Interfaces:**
- Produces: `load_markdown_sections(content_dir: Path) -> dict[str, str]`
- Produces: `load_yaml_records(path: Path, required_keys: set[str]) -> list[dict[str, object]]`
- Produces: `find_prohibited_text(text: str) -> list[str]`
- Consumes later: all Markdown and YAML source files

- [ ] **Step 1: Write tests for required sections and prohibited text**

Create tests that require content files `00` through `07`, reject unfinished-task markers, dummy filler prose, fabricated citation tokens, and empty headings, and require each YAML record to have `id`, `title`, `purpose`, `instructions`, and `example`.

```python
def test_all_content_modules_exist():
    expected = {f"{i:02d}" for i in range(8)}
    found = {p.name[:2] for p in CONTENT_DIR.glob("*.md")}
    assert expected <= found

def test_sources_contain_no_placeholders():
    violations = []
    for path in SOURCE_FILES:
        violations.extend((path.name, hit) for hit in find_prohibited_text(path.read_text()))
    assert violations == []
```

- [ ] **Step 2: Run the test and verify the empty source tree fails**

Run: `pytest long-form-guide/tests/test_content.py -v`

Expected: FAIL because the content and data files do not exist.

- [ ] **Step 3: Implement the source loaders and validation helpers**

Implement UTF-8 loading, YAML list validation, stable ID uniqueness checks, and case-insensitive placeholder detection. Document the editorial rules and local build commands in `README.md`.

- [ ] **Step 4: Run focused validation tests**

Run: `pytest long-form-guide/tests/test_content.py -v`

Expected: loader unit tests PASS; file-presence tests remain failing until Tasks 2-5.

- [ ] **Step 5: Commit the validation foundation**

```bash
git add long-form-guide/README.md long-form-guide/build/validate.py long-form-guide/tests/test_content.py
git commit -m "test: add long-form guide content contract"
```

### Task 2: Author the foundation and architecture modules

**Files:**
- Create: `long-form-guide/content/00-front-matter.md`
- Create: `long-form-guide/content/01-foundation.md`
- Create: `long-form-guide/content/02-architecture.md`

**Interfaces:**
- Consumes: editorial rules from `long-form-guide/README.md`
- Produces: Markdown with semantic markers `[FICTION]`, `[NONFICTION]`, `[BIBLICAL PROJECT]`, `[WARNING]`, and `[EXERCISE]`
- Produces: canonical terminology used by all later modules

- [ ] **Step 1: Add content assertions for the opening modules**

Require the exact central principle, all five Part I topics, all seven Part II topics, a 20-30-chapter model, a concrete 60,000-word budget, and all four branch markers.

```python
def test_opening_modules_cover_the_core_method():
    text = read_modules("00", "01", "02")
    required = [
        "Do not ask AI to remember the whole book",
        "project bible",
        "chapter brief",
        "60,000-word",
        "[FICTION]",
        "[NONFICTION]",
        "[BIBLICAL PROJECT]",
    ]
    assert all(item.casefold() in text.casefold() for item in required)
```

- [ ] **Step 2: Author `00-front-matter.md`**

Write the title page copy, contents overview, introduction, the limits of one-conversation drafting, failure modes, author-responsibility statement, and central principle. Target 2,500-3,000 words.

- [ ] **Step 3: Author `01-foundation.md`**

Cover promise, reader transformation, project bible, voice sheet, decisions versus open questions, source standards, fiction premise/genre/character setup, nonfiction thesis/evidence setup, and the biblical project's audience and theological boundaries. Target 4,000-4,800 words.

- [ ] **Step 4: Author `02-architecture.md`**

Cover parts/acts, 20-30 chapter mapping, chapter function, word budgets, dependencies, chapter briefs, outline stress tests, and a worked 60,000-word allocation. Include a biblical-manhood progression and a compact fiction architecture. Target 4,000-4,800 words.

- [ ] **Step 5: Run opening-module tests and editorial scans**

Run: `pytest long-form-guide/tests/test_content.py -k 'opening or placeholder' -v`

Expected: PASS.

- [ ] **Step 6: Commit the opening modules**

```bash
git add long-form-guide/content/00-front-matter.md long-form-guide/content/01-foundation.md long-form-guide/content/02-architecture.md long-form-guide/tests/test_content.py
git commit -m "docs: author long-form foundation and architecture"
```

### Task 3: Author the operating-system and drafting modules

**Files:**
- Create: `long-form-guide/content/03-operating-system.md`
- Create: `long-form-guide/content/04-drafting.md`
- Modify: `long-form-guide/tests/test_content.py`

**Interfaces:**
- Consumes: canonical terms from Tasks 1-2
- Produces: lifecycle rules for project bible, outline, briefs, ledgers, trackers, context packets, and handoff summaries
- Produces: the chapter drafting loop used by templates and prompts

- [ ] **Step 1: Add tests for every operating document and drafting stage**

Require all ten operating documents, the eight-step drafting loop, clean-conversation criteria, fiction scene controls, nonfiction argument controls, and Scripture-verification rules.

- [ ] **Step 2: Author `03-operating-system.md`**

Define the purpose, contents, update timing, owner, and stability rule for each operating document. Explain compact context packets and why manuscript memory must live outside the chat. Target 3,500-4,200 words.

- [ ] **Step 3: Author `04-drafting.md`**

Teach the full chapter loop from approved brief through section drafting, review, tracker updates, summary, and handoff. Include fiction and nonfiction branches and the biblical project's quotation, interpretation, audience, and scenario rules. Target 4,500-5,200 words.

- [ ] **Step 4: Run drafting coverage tests**

Run: `pytest long-form-guide/tests/test_content.py -k 'operating or drafting or scripture' -v`

Expected: PASS.

- [ ] **Step 5: Commit the manuscript operating system**

```bash
git add long-form-guide/content/03-operating-system.md long-form-guide/content/04-drafting.md long-form-guide/tests/test_content.py
git commit -m "docs: add long-form manuscript operating system"
```

### Task 4: Author revision, assembly, and worked examples

**Files:**
- Create: `long-form-guide/content/05-revision.md`
- Create: `long-form-guide/content/06-assembly.md`
- Create: `long-form-guide/content/07-worked-examples.md`
- Modify: `long-form-guide/tests/test_content.py`

**Interfaces:**
- Consumes: chapter loop and operating documents from Tasks 2-3
- Produces: nine-pass revision workflow and final assembly workflow
- Produces: primary biblical-manhood example and secondary fiction example used in templates

- [ ] **Step 1: Add tests for revision passes, assembly stages, and human review**

Require nine named revision passes, theological consistency, Scripture context, youth suitability, shame-language and risk checks, file/version rules, beta-reader preparation, and both worked examples.

- [ ] **Step 2: Author `05-revision.md`**

Write each revision pass as a separate goal, input, method, warning, and completion test. Explicitly prevent AI self-verification of facts, quotations, Scripture, doctrine, and sensitive advice. Target 4,000-4,800 words.

- [ ] **Step 3: Author `06-assembly.md`**

Cover file naming, versioning, chapter status, manuscript assembly, transition checks, front/back matter, notes, bibliography, beta-reader workflow, feedback triage, permissions, disclosure choices, and export checks. Target 2,500-3,200 words.

- [ ] **Step 4: Author `07-worked-examples.md`**

Create one end-to-end nonfiction example for the biblical-manhood project and one compact fiction example. Show the actual progression from promise to bible, architecture, chapter brief, context packet, excerpt plan, tracker update, and revision finding. Avoid making denominational conclusions for the reader. Target 4,000-5,000 words.

- [ ] **Step 5: Run the full Markdown content suite**

Run: `pytest long-form-guide/tests/test_content.py -k 'not yaml' -v`

Expected: PASS.

- [ ] **Step 6: Commit the closing modules and examples**

```bash
git add long-form-guide/content/05-revision.md long-form-guide/content/06-assembly.md long-form-guide/content/07-worked-examples.md long-form-guide/tests/test_content.py
git commit -m "docs: complete revision assembly and examples"
```

### Task 5: Build the worksheet and prompt libraries

**Files:**
- Create: `long-form-guide/data/templates.yaml`
- Create: `long-form-guide/data/prompts.yaml`
- Modify: `long-form-guide/tests/test_content.py`

**Interfaces:**
- Produces: exactly 18 template records
- Produces: exactly 14 prompt records
- Each template record: `id`, `title`, `badge`, `purpose`, `instructions`, `fields`, `example`
- Each prompt record: `id`, `title`, `stage`, `inputs`, `author_decision`, `prompt`, `output_format`, `model_must_not_decide`, `example`

- [ ] **Step 1: Add schema, count, ID-uniqueness, and example tests**

```python
def test_template_and_prompt_inventory():
    templates = load_yaml_records(TEMPLATES, TEMPLATE_KEYS)
    prompts = load_yaml_records(PROMPTS, PROMPT_KEYS)
    assert len(templates) == 18
    assert len(prompts) == 14
    assert len({x["id"] for x in templates}) == 18
    assert len({x["id"] for x in prompts}) == 14
```

- [ ] **Step 2: Write all eighteen worksheet/template records**

Implement the exact inventory from the specification, including the claim-and-source ledger and biblical citation-and-interpretation ledger. Every example must use either the biblical-manhood project or the compact fiction example.

- [ ] **Step 3: Write all fourteen prompt-framework records**

Use adaptable language such as "the AI assistant" rather than vendor names. Each framework must declare its required documents, the author's decision, the requested output, and decisions the model must not make.

- [ ] **Step 4: Run YAML and content validation**

Run: `pytest long-form-guide/tests/test_content.py -v`

Expected: PASS with 18 templates, 14 prompts, unique IDs, complete examples, and no placeholders.

- [ ] **Step 5: Commit the working-system resources**

```bash
git add long-form-guide/data/templates.yaml long-form-guide/data/prompts.yaml long-form-guide/tests/test_content.py
git commit -m "docs: add long-form writing templates and prompts"
```

### Task 6: Implement the PDF design system and reusable components

**Files:**
- Create: `long-form-guide/build/styles.py`
- Create: `long-form-guide/build/components.py`
- Create: `long-form-guide/tests/test_pdf.py`

**Interfaces:**
- Produces: `GuideTheme` dataclass containing colors, margins, type sizes, leading, and spacing
- Produces: `make_styles(theme: GuideTheme) -> dict[str, ParagraphStyle]`
- Produces: `badge(text: str, kind: str) -> Flowable`
- Produces: `callout(title: str, body: str, kind: str) -> Flowable`
- Produces: `worksheet(record: dict[str, object]) -> list[Flowable]`
- Produces: `prompt_card(record: dict[str, object]) -> list[Flowable]`

- [ ] **Step 1: Add component construction tests**

Test that every badge kind maps to a color, text styles meet minimum size/leading rules, worksheets contain their title and fields, and prompt cards contain the author-decision and model-boundary sections.

- [ ] **Step 2: Run the component tests and verify they fail**

Run: `pytest long-form-guide/tests/test_pdf.py -k component -v`

Expected: FAIL because `styles.py` and `components.py` do not exist.

- [ ] **Step 3: Implement the visual theme**

Use warm paper `#F7F1E6`, deep green `#183F36`, navy `#17324D`, rust `#A6533F`, gold `#B58A43`, and charcoal `#2D302F`. Use readable serif headings and sans-serif utility/body styles, minimum 10-point body text, and at least 1.28 line-height.

- [ ] **Step 4: Implement the reusable flowables**

Build consistent fiction, nonfiction, biblical-project, template, and warning badges; bordered callouts; worksheet field tables; prompt cards; phase dividers; and chapter budget tables. Ensure all table cells can split or wrap without clipping.

- [ ] **Step 5: Run component tests**

Run: `pytest long-form-guide/tests/test_pdf.py -k component -v`

Expected: PASS.

- [ ] **Step 6: Commit the design system**

```bash
git add long-form-guide/build/styles.py long-form-guide/build/components.py long-form-guide/tests/test_pdf.py
git commit -m "feat: add long-form guide PDF design system"
```

### Task 7: Build the complete PDF

**Files:**
- Create: `long-form-guide/build/build_pdf.py`
- Modify: `long-form-guide/tests/test_pdf.py`
- Create: `outputs/Writing_a_60000_Word_Book_with_AI.pdf`

**Interfaces:**
- Consumes: all Markdown modules, YAML records, styles, and components
- Produces: `build_guide(output_path: Path) -> Path`
- Produces: PDF metadata title `Writing a 60,000-Word Book with AI`

- [ ] **Step 1: Add failing finished-PDF tests**

Test output existence, `%PDF` signature, 50-70 pages, non-empty text on all content pages, required title and section names, metadata, page numbers, and internal TOC/bookmark destinations.

- [ ] **Step 2: Run the finished-PDF tests and verify they fail**

Run: `pytest long-form-guide/tests/test_pdf.py -k finished -v`

Expected: FAIL because the builder and PDF do not exist.

- [ ] **Step 3: Implement Markdown and marker parsing**

Convert headings, paragraphs, lists, quotes, tables, and semantic branch markers into ReportLab flowables. Keep parsing deterministic and reject unknown markers with a descriptive exception containing the source path and line number.

- [ ] **Step 4: Implement document assembly**

Create cover, copyright/disclaimer page, contents, six main parts, worked examples, templates, prompt library, and final checklist. Add running headers, page numbers, PDF metadata, TOC, and outline bookmarks.

- [ ] **Step 5: Build the PDF**

Run: `python long-form-guide/build/build_pdf.py --output outputs/Writing_a_60000_Word_Book_with_AI.pdf`

Expected: command exits 0 and prints the output path and page count.

- [ ] **Step 6: Run PDF structure tests**

Run: `pytest long-form-guide/tests/test_pdf.py -v`

Expected: PASS, including a page count between 50 and 70.

- [ ] **Step 7: Commit the builder and first complete PDF**

```bash
git add long-form-guide/build/build_pdf.py long-form-guide/tests/test_pdf.py outputs/Writing_a_60000_Word_Book_with_AI.pdf
git commit -m "feat: build complete long-form AI writing guide"
```

### Task 8: Perform source-accuracy and editorial QA

**Files:**
- Modify: relevant files under `long-form-guide/content/`
- Modify: `long-form-guide/data/templates.yaml`
- Modify: `long-form-guide/data/prompts.yaml`
- Modify: `outputs/Writing_a_60000_Word_Book_with_AI.pdf`

**Interfaces:**
- Consumes: complete source and built PDF
- Produces: source with no unsupported quotations or unverified claims

- [ ] **Step 1: Extract and inspect every quotation-like passage**

Run a validation report listing quoted strings, Scripture references, statistics, named studies, named translations, and external factual claims. Treat every item as unverified until traced to an authoritative source or rewritten as an illustrative example.

- [ ] **Step 2: Verify biblical-example boundaries**

Confirm the example distinguishes Scripture reference, observation, interpretation, theological choice, and application. Use Scripture references without reproducing copyrighted translation text unless the wording and permissions have been verified.

- [ ] **Step 3: Perform audience and safety review**

Check all material aimed at ages 13-21 for age appropriateness, shame-based framing, unsupported universal claims, risky pastoral/medical/legal guidance, and the required qualified-human-review language.

- [ ] **Step 4: Perform tool-agnostic review**

Search for `ChatGPT`, `Claude`, `Gemini`, vendor-specific controls, and claims about model context sizes. Retain names only when explaining portability; rewrite instructions so the method works with any capable assistant.

- [ ] **Step 5: Rebuild and rerun all tests**

Run: `python long-form-guide/build/build_pdf.py --output outputs/Writing_a_60000_Word_Book_with_AI.pdf`

Run: `pytest long-form-guide/tests -v`

Expected: PASS.

- [ ] **Step 6: Commit editorial corrections**

```bash
git add long-form-guide/content long-form-guide/data outputs/Writing_a_60000_Word_Book_with_AI.pdf
git commit -m "fix: complete long-form guide editorial review"
```

### Task 9: Render and visually inspect every page

**Files:**
- Create: `long-form-guide/qa/visual-review.md`
- Modify: PDF source files when defects are found
- Modify: `outputs/Writing_a_60000_Word_Book_with_AI.pdf`

**Interfaces:**
- Consumes: final candidate PDF
- Produces: `long-form-guide/qa/rendered/page-001.png` through final page
- Produces: completed visual-review record

- [ ] **Step 1: Render every PDF page to PNG**

Run: `mkdir -p long-form-guide/qa/rendered && pdftoppm -png -r 130 outputs/Writing_a_60000_Word_Book_with_AI.pdf long-form-guide/qa/rendered/page`

Expected: one PNG per PDF page.

- [ ] **Step 2: Generate contact sheets for rapid inspection**

Create contact sheets in batches of 12 pages while retaining full-resolution page renders for detailed review.

- [ ] **Step 3: Inspect every page and record findings**

For each page, mark PASS or document exact defects involving clipping, overlap, widows/orphans, weak hierarchy, cramped tables, unreadable worksheet fields, inconsistent badges, excessive blank space, broken characters, or page-number/header errors.

- [ ] **Step 4: Correct all recorded defects and rebuild**

Update source or component rules rather than editing the PDF directly. Rebuild and rerender affected pages after every correction batch.

- [ ] **Step 5: Require a clean final visual-review record**

The review is complete only when every page is marked PASS and the issue list contains zero open items.

- [ ] **Step 6: Run final automated verification**

Run: `pytest long-form-guide/tests -v`

Run: `pdfinfo outputs/Writing_a_60000_Word_Book_with_AI.pdf`

Expected: all tests PASS; page size, title, author, page count, and PDF version are reported correctly.

- [ ] **Step 7: Commit the visually approved guide**

```bash
git add long-form-guide/qa/visual-review.md long-form-guide/build long-form-guide/content long-form-guide/data outputs/Writing_a_60000_Word_Book_with_AI.pdf
git commit -m "chore: approve long-form guide visual QA"
```

### Task 10: Create the publish-ready handoff

**Files:**
- Modify: `long-form-guide/README.md`
- Verify: `outputs/Writing_a_60000_Word_Book_with_AI.pdf`

**Interfaces:**
- Consumes: visually approved PDF and passing test suite
- Produces: final documented build and release procedure

- [ ] **Step 1: Document the final build and QA commands**

Add exact dependency, build, test, render, and output-location instructions to `README.md`. Include the source-accuracy and human theological-review requirements.

- [ ] **Step 2: Verify reproducibility from the documented command**

Run the documented build from the repository root and confirm it regenerates the same titled PDF within the required 50-70-page range.

- [ ] **Step 3: Verify final file integrity**

Run: `shasum -a 256 outputs/Writing_a_60000_Word_Book_with_AI.pdf`

Record the hash in the release section of `README.md` alongside the page count and build date.

- [ ] **Step 4: Run the final release gate**

Run: `pytest long-form-guide/tests -v`

Expected: PASS with no warnings treated as open release defects.

- [ ] **Step 5: Commit the publish-ready handoff**

```bash
git add long-form-guide/README.md outputs/Writing_a_60000_Word_Book_with_AI.pdf
git commit -m "docs: finalize long-form writing guide handoff"
```
