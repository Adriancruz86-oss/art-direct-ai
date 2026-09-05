# Art Direct AI — Final Paid Guide Architecture
Date: 2026-09-05
Status: LOCKED WORKING ARCHITECTURE after structural + visual audit

## Product promise
This is not a generic "how to illustrate a children's book with AI" guide.

It teaches authors/illustrators to ART DIRECT AI so the result does not look like default AI children's-book art.

Core editorial test:
> Does this page teach the reader to make an intentional visual decision instead of accepting the model's default visual decision?

If not, cut or merge it.

## Production rules
- No generated typography in final pages.
- Generated spreads are visual comps/assets only.
- No fake book seams unless explicitly teaching gutter behavior.
- Do not regenerate an entire spread to fix one local problem.
- Prefer local edits and controlled illustration assets.
- "Good" examples must demonstrate restraint: warm raw paper, loose graphite/colored pencil, light watercolor/dry gouache, simplified hair, sparse faces, plain clothing, broad backgrounds, unfinished areas, white space.
- Avoid walking/running poses unless movement matters.
- Recurring boy/dog must use one canonical reference.
- Do not add pages merely to increase page count.
- Target: approximately 44–50 finished single pages.

## Final architecture

### PART I — Why Your AI Art Looks Like AI
1. Stop Making AI-Looking Children's Books
2. Why Everyone Is Getting the Same Look
3. You're the Art Director Now
4. Diagnose Your Illustration

Purpose: identify default AI aesthetics quickly, then pivot to art direction.

### PART II — Remove the AI Fingerprints
5. The Detail Budget
6. Background Detail
7. Fabric & Clothing Detail
8. Faces Are Where AI Gives Itself Away
9. The Power of the Quiet Page

Core principle: AI tends to fill and beautify; the art director decides what to remove.

### PART III — Make a Character, Not 30 Versions of One
10. Decide What Cannot Change
11. Build a Useful Reference Sheet
12. Consistency Is More Than the Face
13. Catch Drift Before It Spreads
14. Character Reference Checklist

Consolidates source #7/#10/#11/#16/#20/#23/#31. Do not restore these as seven separate lessons.

Canonical locks to emphasize:
- silhouette
- apparent age
- proportions
- face structure
- hair mass
- core clothing
- major colors
- companion design

Flexible features:
- expression
- pose
- angle
- lighting
- temporary/story-required props

### PART IV — Art Direct the Page, Not Just the Picture
15. Composition Before Decoration
16. Vary Your Camera
17. Design for the Words
18. Two Pages Are One Composition
19. Make the Page Turn Do Something
20. Page Turn: Before & After

### PART V — Iterate Like an Art Director
21. Stop Regenerating Everything
22. Fix It in Editing
23. Change One Variable at a Time

Core principle: preserve correct decisions. Fix the wrong variable rather than throwing away an otherwise successful image.

### PART VI — From Bad Prompt to Art Direction
24. Prompt for Decisions, Not Pretty Pictures
25. Same Idea, Different Result
26. Negative Direction Matters

Prompt hierarchy:
Subject -> Action -> Composition -> Character locks -> Medium -> Detail level -> Mood -> What to avoid

### PART VII — Make It a Book
27. Build Model Pages
28. Final Illustration Check
29. Production Checklist
30. Children's Book Print Guide

All print/export claims must be fact-checked and labeled as common practice vs printer/platform-specific requirements.

### PART VIII — Your Anti-AI-Slop System
31. Stop Doing This / Do This Instead
32. From Idea to Finished Illustration
33. Quiet Closing Page

Workflow:
Clear Idea -> Detailed Prompt -> Generate & Review -> Refine & Iterate -> Finalize & Prepare -> Add to Your Book

Closing idea:
"The goal was never to make AI better at drawing. The goal was to get better at deciding."
Wording may be polished later; keep the conceptual point.

## Current visual status
- Diagnostic opener: replacement approved.
- Quiet Page: replacement approved.
- Detail-control material: approved direction.
- Character Reference / Keep It Consistent easy fix: approved enough; final type must be rebuilt normally.
- Same Idea, Different Result (#28): replacement approved.
- Workflow Map (#33): concept resolved; DO NOT generate another full spread. Build final flat layout with real type.
- Background Detail: original retained art is sufficient; accidental later regeneration is redundant.
- Clothing-consistency accidental generation: redundant; do not create a new standalone chapter from it.
- Character-consistency accidental regeneration: do not expand the already-merged character cluster.

## Next production action
Begin copy + technical accuracy work against this architecture.

First substantive build:
PART I copy/content pass:
1. Opening hook
2. Default-AI problem statement
3. Art-director philosophy
4. Diagnostic opener

Then proceed through the book in architecture order.

Do not return to broad image generation unless a specific missing/failed illustration asset is identified during assembly.
