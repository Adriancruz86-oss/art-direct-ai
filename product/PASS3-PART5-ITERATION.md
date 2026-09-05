# Art Direct AI — Pass 3 Copy Build
## Part V: Iterate Like an Art Director
Date: 2026-09-05
Status: working final copy

Editorial purpose: replace slot-machine regeneration with diagnosis, controlled iteration, and local repair. This section should save readers time while improving continuity.

---

# 21 — Stop Regenerating Everything

You finally get a page where the composition works.

The character looks right.
The expression works.
The background is restrained.
There is room for text.

But one hand is malformed.

So you regenerate the entire image.

Now the hand is better — but the face changed, the hoodie gained a zipper, the dog is larger, the background is busier, and your text space disappeared.

You fixed one problem by creating five new ones.

## Preserve correct decisions

When reviewing a generation, separate the page into:

**WORKING**
- scene;
- composition;
- character identity;
- expression;
- medium;
- palette;
- background;
- text space.

**BROKEN**
- anatomy;
- one prop;
- one clothing feature;
- one patch of excessive detail;
- one drifting character feature.

If most of the first list works, do not casually throw it away.

The goal is not to generate the page again.

The goal is to repair what failed.

## Regeneration has a cost

Every full regeneration reopens decisions you may have already solved.

The model gets another chance to change:

- age;
- face;
- hair;
- proportions;
- clothing;
- companion design;
- camera;
- lighting;
- background;
- style;
- negative space.

That is why endless regeneration often creates drift even when each individual image looks acceptable.

### The preservation rule

> **Keep every correct decision you can. Reopen only the decisions that failed.**

---

# 22 — Fix It in Editing

Not every defect is an art-direction failure.

Sometimes the image is simply broken.

Examples:

- extra finger;
- merged hand and object;
- doubled shoe;
- impossible leg;
- malformed ear;
- duplicate background prop;
- accidental symbol;
- broken edge;
- one patch of nonsense texture.

If the rest of the illustration works, treat that as a production defect.

## Local repair beats total replacement

Repair only the smallest useful area.

For example:

**Bad hand**
Keep the character, pose, composition and page. Repair the hand.

**Wrong shoe**
Keep the body and clothing. Correct the shoe against the reference.

**Dog markings drifted**
Keep the dog pose if it works. Restore the canonical markings.

**Background became too busy**
Simplify the background without redesigning the characters.

**Hair became over-rendered**
Reduce the internal strands while preserving the silhouette.

## Do not "improve" the whole image during a repair

A repair instruction should be boringly specific.

If the hand is wrong, do not simultaneously ask for:
- prettier lighting;
- more expression;
- a better background;
- richer color;
- improved composition.

That is not a repair.

That is another regeneration disguised as one.

## Anatomy: prevent what you can

Complex walking and running poses are common failure points.

If movement is not important to the story, a clean standing, seated, kneeling or leaning pose may communicate the same beat with less anatomy risk.

This is not avoiding difficulty.

It is choosing the simplest visual solution that serves the manuscript.

### Repair question

Before replacing a page, ask:

> **How small can the fix be?**

Start there.

---

# 23 — Change One Variable at a Time

When an image feels wrong in several ways, it is tempting to rewrite the entire prompt.

That makes it harder to learn what actually fixed the problem.

Instead, diagnose the dominant failure and change that variable first.

## If the character drifted

Strengthen:
- canonical reference;
- immutable features;
- proportions;
- hair silhouette;
- outfit/companion locks.

Do not rewrite the sunset.

## If the image is too polished

Change:
- rendering ceiling;
- mark-making;
- amount of raw paper;
- facial/hair detail;
- lighting constraints.

Do not redesign the character.

## If the background is too busy

Change:
- number of background shapes;
- allowed props;
- foliage/detail ceiling;
- negative-space instruction.

Do not change the camera unless the camera is also the problem.

## If the composition fails

Change:
- subject placement;
- camera distance;
- text-safe region;
- focal hierarchy.

Keep the visual language stable.

## If the emotion is too strong

Change:
- expression intensity;
- mouth/eye treatment;
- posture;
- gesture.

Do not ask for a completely new scene.

## A controlled iteration loop

1. **Generate.**
2. **Name the failure in one sentence.**
3. **Identify the variable responsible.**
4. **Preserve everything that already works.**
5. **Repair or regenerate only what needs reopening.**
6. **Compare against reference/model pages.**
7. **Repeat only if a specific failure remains.**

This is slower than pressing Generate again.

It is much faster than discovering on page twenty that your book has gradually become a different book.

---

## Worked micro-example

**First result:**  
Boy and dog composition works. Character identity works. Dock and text space work. Boy has malformed shoes and the sunset is too cinematic.

**Bad response:**  
"Try again, make it more hand-drawn and fix his shoes."

This reopens everything.

**Art-directed response:**  
1. Preserve composition and character identity.
2. Correct shoes against canonical reference.
3. Reduce sky rendering separately: flatter wash, no glow, more raw paper.
4. Compare repaired result against model pages.

Two failures. Two controlled corrections.

---

## Part V production notes

- Approximate finished length: 5–6 pages.
- Source #21 Fix It in Editing supplies the core visual lesson.
- Use one clear local-repair example rather than a grid of many tiny examples.
- The malformed walking-pose example is useful only if clearly labeled as a defect; never let it resemble approved art.
- This section should introduce a repeatable behavior, not merely warn against regeneration.
- Keep terminology aligned with Part I diagnosis and Part III drift system.
- The worked micro-example may reuse the canonical boy/dog dock imagery; do not generate another full spread solely for it.
