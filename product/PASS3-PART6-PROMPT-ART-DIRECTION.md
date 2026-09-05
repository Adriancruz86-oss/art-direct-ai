# Art Direct AI — Pass 3 Copy Build
## Part VI: From Bad Prompt to Art Direction
Date: 2026-09-05
Status: working final copy

Editorial purpose: turn everything taught so far into a repeatable prompting method. This is not a library of magic prompts. It teaches readers how to translate visual decisions into usable direction.

---

# 24 — Prompt for Decisions, Not Pretty Pictures

A long prompt is not automatically a directed prompt.

You can write 500 words of adjectives and still leave the important decisions to the model.

The goal is not to describe everything you can think of.

The goal is to communicate the decisions that matter for this page.

## A practical prompt hierarchy

Build direction in this order:

### 1. SUBJECT
Who or what must appear?

Be concrete enough to establish scene truth.

> A nine-year-old boy and his medium-sized spotted dog.

### 2. ACTION
What are they actually doing?

> Sitting side by side at the end of a wooden dock, looking across the lake.

Avoid adding movement simply to make the image dynamic.

### 3. COMPOSITION
Where do the important elements belong?

> Boy and dog low on the right half. Keep the upper-left area mostly open for text. Medium-wide view from slightly behind.

This turns a scene description into a page.

### 4. CHARACTER LOCKS
What must match established references?

> Match the established boy: compact child proportions, simplified medium-brown hair mass, plain red hoodie, blue jeans, simple sneakers. Match the established cream-and-brown spotted dog, including size, floppy ears and markings.

Do not rewrite the character from memory differently on every page.

### 5. MEDIUM + SURFACE
How should marks behave?

> Loose graphite and colored pencil with a very light watercolor wash on warm off-white paper. Visible paper grain. Imperfect hand-drawn edges.

Describe behavior, not only a style label.

### 6. DETAIL LEVEL
Where is rendering allowed?

> Faces use sparse pencil marks. Hair described as large masses with only a few internal strokes. Clothing mostly flat shapes with only enough folds to show the seated pose. Distant shoreline suggested broadly.

### 7. MOOD
What emotional temperature belongs on the page?

> Quiet, reflective, ordinary evening. No exaggerated expressions.

Mood should guide the scene, not trigger a pile of cinematic effects.

### 8. WHAT TO AVOID
What defaults are likely to damage this project's visual language?

> No cinematic rim light, decorative glow, glossy eyes, elaborate sunset, individual hair-strand rendering, ornate fabric, foreground flowers, floating particles or unnecessary props. Preserve raw paper.

That final layer is not there to make the prompt sound sophisticated.

It protects decisions already made.

## Not every prompt needs every sentence

Once references and project-level rules are established, some systems may allow you to reuse them rather than repeating everything.

The hierarchy is a thinking tool.

Use enough direction to protect the page.

Do not turn every generation into a legal contract.

---

# 25 — Same Idea, Different Result

Use the approved rebuilt boy-and-dog dock comparison.

## The vague version

> A boy and his dog sitting on a dock at sunset, beautiful children's-book illustration.

The scene is understandable.

But the model still controls nearly everything else:

- camera;
- character design;
- amount of detail;
- sky intensity;
- lighting;
- rendering finish;
- background density;
- clothing complexity;
- negative space;
- visual hierarchy.

If the result looks generic, the model did not necessarily fail.

It answered questions you never answered.

## The art-directed version

> A nine-year-old boy and his medium-sized spotted dog sit quietly side by side at the end of a wooden dock, seen in a medium-wide view from slightly behind. Place them low and right; preserve open warm paper in the upper-left for text.
>
> Match the established boy: compact proportions, simplified medium-brown hair mass, plain red hoodie, blue jeans and simple sneakers. Match the established cream-and-brown dog with floppy ears and stable markings.
>
> Loose graphite and colored pencil with a very light watercolor wash on warm off-white paper. Sparse facial marks. Broad shoreline shapes. Water indicated with only a few horizontal marks. Quiet evening color.
>
> No dramatic sunset, glow, rim light, glossy rendering, decorative foliage, foreground flowers, detailed reflections or filled-in sky. Leave substantial paper untouched.

The important difference is not prompt length.

The second version contains **decisions**.

## What changed?

**Scene:** stayed essentially the same.

**Composition:** became intentional.

**Character:** became anchored.

**Medium:** became behavioral rather than a vague "watercolor style."

**Detail:** received a ceiling.

**Mood:** became quiet instead of automatically spectacular.

**Negative direction:** blocked the defaults most likely to make the page look generic.

That is art direction.

---

# 26 — Negative Direction Matters

Positive direction tells the model what you want.

Negative direction protects the image from what you do not want.

This matters because many AI fingerprints are not errors.

They are embellishments.

The model may add:

- prettier lighting;
- richer fabric;
- more foliage;
- cleaner skin;
- shinier eyes;
- more atmospheric effects;
- a more dramatic sky;
- extra props;
- more complete rendering.

If those additions violate the visual language, name them.

## Be specific about the failure

Weak:

> Don't make it look AI.

That does not describe a visual behavior.

Useful:

> No glossy eyes. No rim light. No individual hair strands. No decorative foreground plants. No fabric pattern. No cinematic sunset. Do not fill open paper with clouds or texture.

Those are observable constraints.

## Negative direction is project-specific

Do not copy a giant universal negative list into every book.

A graphic, highly polished children's book may intentionally use clean edges and saturated color.

A magical scene may genuinely require glow.

An ornate costume may be essential to the story.

The question is:

> **What does this book refuse to do?**

Write that list.

Those prohibitions become part of the visual bible.

## Build a project restraint block

For the visual language used throughout this guide, a reusable block might be:

> Restraint: no glossy eyes, cinematic rim lighting, decorative glow, elaborate skies, unnecessary foliage, ornate clothing, individual hair-strand rendering, dense background props or filling empty areas merely to make the image look finished. Preserve visible paper and imperfect hand-drawn edges.

Then add page-specific constraints only when needed.

## Do not fight the model with contradictions

Avoid directions such as:

> Highly detailed but very simple.

> Cinematic but flat and quiet.

> Perfectly polished hand-drawn imperfection.

Decide which quality actually matters.

Constraint works because it narrows the target.

Contradiction makes the target fuzzy again.

---

# Prompt Builder — Working Template

This can become a reusable worksheet/reference page.

**SUBJECT**  
Who or what must appear?

**ACTION**  
What is physically happening?

**COMPOSITION**  
Camera distance, placement, focal point, text-safe area.

**CHARACTER LOCKS**  
What must match the canonical references?

**MEDIUM + SURFACE**  
How should the marks and material behave?

**DETAIL CEILING**  
Where is detail allowed, and what stays simplified?

**MOOD**  
What emotional temperature belongs here?

**RESTRAINT / AVOID**  
Which model defaults would damage this page or project?

### Final check

Before generating, ask:

> Have I directed the decisions that matter — or have I mostly described something I hope will look pretty?

---

## Part VI production notes

- Approximate finished length: 6–8 pages.
- Chapter 24 should be highly practical but visually calm. Do not cram the eight prompt layers into eight equal dashboard boxes.
- Consider two pages/spread for the hierarchy: one clean vertical sequence plus one worked mini-example.
- Chapter 25 uses the newly approved #28 comparison art. Final prompt copy is real typography outside the illustration.
- Do not preserve faux book seam from any old source comp.
- Chapter 26 should distinguish useful negative direction from giant generic "negative prompt" lists.
- Prompt Builder should be reusable and detachable-looking without becoming another dense reference dashboard.
- Reiterate that the system is model-agnostic: exact interface features differ, but visual decision-making remains useful across generative image tools.
- Do not claim that wording guarantees identical results. Direction improves control; generation remains variable.
