# Art Direct AI — Pass 6 Audit: Crisp Text + Practical Prompt Examples
Date: 2026-09-05
Status: LOCKED corrective pass before final layout audit

## Why this pass exists
The full landscape proof exposed two important production problems:

1. Text that is baked into generated spreads is smaller and softer than the newly typeset editorial pages. On phone/landscape viewing it requires zooming and becomes visibly fuzzy.
2. The guide drifted too far toward principles and away from practical prompt examples. Readers need repeated "instead of this, try this" examples throughout the book.

These are now first-priority fixes.

---

# A. GENERATED-SPREAD TEXT REPAIR

## Core rule
Keep the approved spread composition intact, but do NOT rely on its rasterized generated typography for final reading.

Where a retained generated spread contains instructional text:
- preserve the full spread composition and illustration;
- mask/cover the generated text zones with a matched paper/background tone;
- re-typeset the same lesson copy in crisp vector text;
- increase type size to match the editorial text pages;
- preserve the original visual hierarchy where it works;
- fix spelling/grammar while re-typesetting;
- never enlarge the raster text itself.

This is not "chopping up" the spread. The artwork stays whole; only the baked-in text is replaced.

## Priority spreads for text replacement
- source #1 opening/problem spread
- source #2 same-look/problem spread
- approved Diagnostic Opener
- source #8 Background Detail
- source #9 Fabric/Clothing Detail
- source #13 Faces
- Quiet Page replacement/source placeholder
- source #16 Character Reference Sheet
- source #11 Character Consistency
- source #23 Character Checklist / reference
- source #12 Composition
- source #19 Camera Distance
- source #18 Gutter
- source #24 Page Turn Theory
- source #25 Page Turn Before/After
- source #21 Fix It in Editing
- approved #28 Same Idea, Different Result
- source #29 Production Checklist
- source #30 Print Guide
- source #32 Stop/Do Instead

Workflow page #33 is already planned as a full normal-layout rebuild and should not use generated type.

## Resolution rule
Do not solve this by simply exporting the raster spread larger. The source text is already rasterized. The real fix is normal typesetting.

---

# B. REMOVE INTERNAL PRODUCTION NOTES FROM CUSTOMER PROOF

Delete or convert all visible internal notes such as:
- "Visual note"
- "placeholder"
- "proof note"
- "until the approved replacement is recovered"
- internal asset/recovery language
- source-comp references
- production-only caveats not intended for the reader

Technical guidance that is actually useful to readers stays, but it must be written as reader-facing copy.

---

# C. RESTORE PRACTICAL PROMPT TEACHING

## New recurring feature
Add a recurring callout:

### INSTEAD OF THIS
weak/vague prompt

### TRY THIS
shorter practical art-directed prompt

### WHY IT WORKS
one sentence naming the decisions that changed

Use this feature selectively, not on every page.

## Target prompt examples

### 1. Default AI look / opening
INSTEAD OF:
"Beautiful whimsical children's-book illustration."

TRY:
"Loose colored pencil and light watercolor on warm paper. Sparse facial marks. Plain clothing. Broad background shapes. Leave visible paper. No glossy eyes, rim light, decorative glow, or extra foliage."

WHY:
Replaces vague quality adjectives with rendering limits and prohibitions.

### 2. Background Detail
INSTEAD OF:
"Beautiful detailed forest/lakeside background."

TRY:
"Background suggested with three broad landscape shapes and a few pencil marks. Keep the upper half mostly open paper. No individual leaves, foreground flowers, birds, or detailed reflections."

WHY:
Defines where background detail stops.

### 3. Fabric / Clothing
INSTEAD OF:
"Red hoodie with realistic fabric detail."

TRY:
"Plain red hoodie as one simple color mass. Only two or three folds needed to show the seated pose. No logo, pattern, stitching, fabric texture, or extra trim."

WHY:
Makes clothing serve identity and pose rather than visual decoration.

### 4. Faces
INSTEAD OF:
"Cute expressive boy with detailed face."

TRY:
"Simple child face with very few pencil marks. Small eyes without glossy highlights. Faint flat skin wash. Simple mouth. No eyelashes, rendered lips, or detailed teeth."

WHY:
Preserves expression without triggering polished character rendering.

### 5. Quiet Page
INSTEAD OF:
"Boy alone in a quiet room."

TRY:
"Small boy seated low on the page beside one toy. Keep most of the page untouched warm paper. No wall decorations, extra furniture, plants, window light effects, or balancing objects."

WHY:
Directs absence instead of hoping the model leaves space.

### 6. Character Consistency
INSTEAD OF:
"Same boy as before."

TRY:
"Match the established boy: compact child proportions, rounded medium-brown hair mass ending above the neck, sparse face marks, plain red hoodie, blue jeans, simple sneakers. Do not change age, face shape, hair length, outfit type, or shoe style."

WHY:
Names immutable identity features.

### 7. Camera Distance
INSTEAD OF:
"Show the boy looking worried."

TRY:
"Close view from chest up, slightly off-center, with lots of open paper on the left for text. Keep expression subtle: lowered eyebrows and a small closed mouth. No dramatic pose."

WHY:
Directs camera and emotional intensity instead of only emotion.

### 8. Text Space / Composition
INSTEAD OF:
"Leave room for text."

TRY:
"Place the child low and right. Keep the upper-left third mostly untouched paper with no faces, props, strong contrast, or detailed background marks."

WHY:
Converts vague whitespace into an actual composition decision.

### 9. Page Turn
INSTEAD OF:
"Show the giant robot outside."

TRY — SETUP PAGE:
"Child at the window, seen small from behind. Only a strange shadow visible outside. Keep the source of the sound hidden."

TRY — REVEAL:
"Wide view after the page turn. Giant robot fully visible beyond the house, with the child very small in the foreground."

WHY:
Prompts the sequence rather than one isolated image.

### 10. Local repair
INSTEAD OF:
"Regenerate and fix the hand."

TRY:
"Keep the composition, character, clothing, dog, background, lighting, and crop unchanged. Repair only the boy's right hand so it has five clearly separated fingers naturally gripping the book."

WHY:
Protects solved decisions while reopening only the defect.

### 11. Same Idea, Different Result
Keep the approved full worked comparison as the flagship example, but replace its generated prompt text with crisp typesetting.

### 12. Negative Direction
Include one reusable "restraint block" example:
"No glossy eyes, no cinematic rim lighting, no decorative glow, no elaborate skies, no unnecessary foliage, no individual hair-strand rendering, no ornate clothing, and do not fill empty paper merely to make the image look finished."

---

# D. PAGE COUNT EFFECT
Do not force these prompts into already dense spreads.

Preferred approach:
- prompt callouts can live on the editorial text page that introduces the spread;
- some may become half-page callouts on otherwise quiet text pages;
- only add a new full page when the example materially improves usability.

Expected final length after prompt restoration: approximately 44–48 landscape pages, depending on layout.

---

# E. NEXT BUILD
Before another whole-book audit:
1. rebuild the highest-priority spreads with crisp typeset text;
2. remove all internal production notes;
3. add the prompt callouts above to the relevant editorial pages;
4. export proof v3;
5. audit rhythm/layout as a whole.
