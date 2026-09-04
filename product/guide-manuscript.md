# ART DIRECTING AI
## A practical guide to children's-book illustration with generative AI

**Working product manuscript — v0.1**

> AI should give you material to work with — not permission to stop working.

---

# Introduction — The problem is not that you used AI

People are getting better at spotting the default AI look.

That is not the same thing as saying every image made with generative AI is bad. The problem is what happens when the model is allowed to make every creative decision for you.

Give a model a vague request for a “beautiful children's-book illustration” and it has to fill in everything you did not specify. It chooses the finish. It chooses the lighting. It chooses how detailed the hair should be. It chooses whether every inch of the background needs something in it. It chooses how polished the face should look. It chooses how dramatic the scene should feel.

And because the model has learned patterns from enormous amounts of visual material, its safest choices tend to look familiar. The result can be technically impressive and still feel anonymous.

That is where art direction begins.

An art director does not merely ask for a picture. An art director makes decisions about what the picture is allowed to become.

This book is about those decisions.

It is not a collection of magic prompts. It is not a shortcut for publishing a children's book in an afternoon. It is not a promise that you can press a button, walk away, and come back to a finished book.

The goal is the opposite.

The goal is to make you more involved in the process, not less.

You will learn how to decide what the book should look like before you generate pages, how to keep the model from overworking every surface, how to maintain visual consistency, how to control detail, how to diagnose an image that feels “AI,” and how to know when the right move is to edit rather than regenerate.

The core idea is simple:

**Do not ask the model to make the best image it can. Ask it to make the image your book needs.**

---

# Part I — Stop Letting the Model Make the Important Decisions

## Chapter 1 — A prompt is not art direction

A prompt can describe a scene perfectly and still produce the wrong illustration.

Consider this:

> A little girl in a yellow dress walks through a forest carrying a red balloon. Children's-book watercolor illustration.

Nothing in that request is technically wrong. The subject is clear. The action is clear. The medium is named.

But almost every important visual decision is still open.

How old does the girl look?

How simple is her face?

Is the watercolor transparent and loose, or dense and digitally polished?

Is the forest made from three broad masses, or two hundred carefully rendered leaves?

Is her dress a flat yellow shape, or is it covered with embroidery, folds, stitching, printed flowers, lace, highlights, and texture?

Does the balloon sit quietly above her, or glow like a magical object?

Are there shafts of cinematic light coming through the trees?

Does the background fade away, or does the model fill every available space?

If you do not make these decisions, the model will.

That is the difference between prompting and art direction.

### Prompting answers: What is in the picture?

Art direction answers questions such as:

- What deserves attention?
- What should remain simple?
- What should be omitted?
- What should look unfinished?
- What should stay identical from page to page?
- What should never appear unless explicitly requested?
- How should the reader's eye move through the page?
- How much work should the image look like it took to make?

That last question matters more than it first appears.

A children's-book illustration does not need to display maximum technical effort everywhere. In traditional illustration, an artist may spend ten minutes suggesting a tree with a few marks because the tree is not the point of the scene. The reader understands the tree immediately. More rendering would not add more meaning.

Generative models often do the opposite. They are very good at continuing to add visual information. If a dress can have folds, embroidery, texture, stitching, reflective highlights, and a repeating fabric pattern, the model may happily provide all of them.

The result may look “better” in isolation while becoming worse for the book.

### The first rule of this guide

Before generating an illustration, ask yourself:

**What decisions would I be annoyed if the model made for me?**

Those are the decisions that belong in your direction.

---

## Chapter 2 — The model's favorite word is “more”

When people first begin generating illustration, they often try to improve weak results by adding more descriptive language.

More beautiful.

More detailed.

More magical.

More cinematic.

More expressive.

More professional.

More whimsical.

That usually gives the model permission to increase visual intensity everywhere at once.

For a children's book, this can create a familiar group of problems:

- every strand of hair becomes visible;
- skin becomes perfectly smooth and softly lit;
- eyes become glossy and oversized;
- clothing receives unnecessary patterns and fabric texture;
- background foliage becomes dense and decorative;
- rim light appears around characters;
- floating particles, sparkles, or glowing dust appear without narrative reason;
- every object receives equal rendering attention;
- scenes become visually louder than the manuscript.

The model is not doing this because it “doesn't understand art.” It is doing what the instruction rewards. If you ask for impressive, polished, magical work, it reaches for visual signals associated with those ideas.

The solution is not always a longer prompt.

Often the solution is **constraint**.

### Constraint is a creative instruction

Compare these two directions.

**Loose direction:**

> Hand-painted watercolor children's-book illustration. Beautiful and detailed.

**Constrained direction:**

> Loose watercolor and colored pencil on warm paper. Large simple shapes. Sparse facial marks. Clothing should read as a single flat shape with only enough folds to show posture. Background suggested with broad washes. No decorative fabric pattern. No glow. No rim light. No floating particles. Leave quiet paper visible.

The second direction is not “better” because it contains more words.

It is better because those words eliminate decisions you do not want the model making.

### Detail has a budget

Think of every illustration as having a limited detail budget.

If the story moment is the child's expression, spend the detail there.

If the story moment is the enormous tree behind the house, spend it on the tree.

If the dress is not narratively important, do not spend half the detail budget on the dress.

A useful question is:

**If a human illustrator had two hours to finish this page, where would they spend those two hours?**

Then direct the model accordingly.

If the answer is “certainly not hand-rendering a tiny repeating flower pattern across the entire skirt,” remove it.

---

## Chapter 3 — Build a visual language before you build pages

The easiest way to make twenty generated illustrations feel like twenty different projects is to begin every page from a blank prompt.

A book needs rules.

Those rules are not there to make every page identical. They give every page the same visual ancestry.

Think about a traditionally illustrated book. The artist may change composition, scale, lighting, emotion, and location from spread to spread, but the reader never wonders whether a new illustrator took over halfway through.

That consistency comes from repeated decisions.

Before generating finished pages, define the visual language of the project.

Your working visual language should answer six categories:

### 1. Surface

What does the artwork appear to live on?

Examples:

- warm cold-press watercolor paper;
- bright white sketch paper;
- toned kraft paper;
- smooth gouache board;
- rough graphite sketchbook stock.

Surface affects everything else. A loose drawing on warm paper feels different from the exact same drawing on a perfectly white digital background.

### 2. Mark-making

How are forms described?

Examples:

- broken graphite outlines;
- dry colored-pencil strokes;
- flat gouache shapes;
- transparent watercolor edges;
- heavy ink contour with minimal interior detail.

Avoid vague labels when you can describe behavior.

“Watercolor style” is broad.

“Transparent washes with visible paper between shapes and no fully rendered gradients” is useful direction.

### 3. Detail ceiling

Decide how finished the image is allowed to become.

For example:

- hair described as two or three large masses;
- clothing without repeating patterns unless story-relevant;
- faces using only essential marks;
- distant foliage grouped into simple shapes;
- small props simplified rather than fully rendered.

This category is where many projects either preserve or lose their handmade feeling.

### 4. Color behavior

Do not only choose colors. Decide how color behaves.

Is the palette muted?

Are shadows cooler than local color?

Are some objects left mostly uncolored?

Does one accent color repeat through the book?

Is skin rendered with several tones or nearly flat?

### 5. Composition behavior

Decide what kinds of pages belong in this book.

You might use:

- lots of negative space for text;
- low eye-level compositions;
- small characters inside large environments;
- occasional close-ups reserved for emotional beats;
- asymmetry rather than centered portraits.

### 6. Prohibitions

This is the category most people skip.

Write down what the book does **not** do.

Examples:

- no cinematic rim lighting;
- no sparkling particles;
- no ornate clothing unless specified;
- no glossy eyes;
- no individual hair-strand rendering;
- no decorative flowers added simply to make a scene prettier;
- no facial detail beyond the established character design;
- no filling empty space just because empty space exists.

Prohibitions are not negative prompting for its own sake. They protect the visual identity of the project.

---

# Part II — The Working System

## Chapter 4 — Separate the scene from the style

A common prompt problem is mixing every instruction into one paragraph until it becomes difficult to diagnose what went wrong.

A better working habit is to think in layers.

The first layer is **scene truth**: what must physically happen in the illustration.

The second is **composition**: how the scene is arranged on the page.

The third is **visual language**: how the world is rendered.

The fourth is **constraints**: what the model must resist doing.

The fifth is **continuity**: what must remain unchanged from previous pages.

This separation matters because when an image fails, you can identify which category failed.

If the character is standing instead of sitting, that is a scene problem.

If there is nowhere to place the text, that is a composition problem.

If the page suddenly looks like polished animation, that is a visual-language problem.

If the child's jacket changed color, that is a continuity problem.

If the trees have become absurdly detailed, that is a constraint problem.

Do not rewrite everything when only one layer is broken.

### A working prompt architecture

The full paid edition will use a structured prompt template throughout the examples. Its logic is simple:

**SCENE** — what is happening.

**COMPOSITION** — where the important things belong.

**VISUAL LANGUAGE** — how the marks, medium, surface, and detail behave.

**CONTINUITY** — what must match established references.

**CONSTRAINTS** — what the model should not beautify, embellish, or invent.

The value of this structure is not that the headings themselves are magical. The value is that it forces you to make decisions before you generate.

---

## Chapter 5 — Character consistency starts before page one

[Draft next]

Topics to cover:
- lock silhouette before facial detail;
- height relationships;
- hair as shape rather than individual strands;
- wardrobe rules;
- reference poses;
- expression range;
- immutable details versus flexible details;
- when to reuse references and when doing so causes stiffness.

---

## Chapter 6 — Control the page, not just the character

[Draft next]

Topics to cover:
- page-design thinking;
- text-safe space;
- full bleed versus spot art;
- quiet pages;
- page-turn reveals;
- focal hierarchy;
- scale variation;
- why every spread should not be a cinematic poster.

---

## Chapter 7 — Diagnose before you regenerate

[Draft next]

Planned diagnostic categories:
- scene wrong;
- identity drift;
- medium drift;
- detail overflow;
- beautification;
- composition failure;
- invented props;
- emotional overstatement;
- anatomy/artifact issue;
- page-level mismatch.

---

# Part III — The AI Fingerprints

## Chapter 8 — The polished face problem

[Draft next]

## Chapter 9 — The hair problem

[Draft next]

## Chapter 10 — The fabric problem

[Draft next]

## Chapter 11 — The everything-is-important problem

[Draft next]

## Chapter 12 — The glow problem

[Draft next]

## Chapter 13 — Decorative clutter

[Draft next]

## Chapter 14 — The same-face problem

[Draft next]

---

# Part IV — Build a Book, Not a Folder of Pictures

## Chapter 15 — A repeatable page workflow

[Draft next]

## Chapter 16 — Editing versus regenerating

[Draft next]

## Chapter 17 — The human pass

[Draft next]

## Chapter 18 — The complete worked example

Planned structure:

1. manuscript line;
2. visual interpretation;
3. intentionally weak first prompt;
4. first output diagnosis;
5. visual-language decisions;
6. character/reference decisions;
7. composition decision;
8. constrained prompt;
9. improved output;
10. edit notes;
11. finished spread;
12. what changed and why.

---

# Appendix A — Prompt diagnostic checklist

Before regenerating, identify the failure:

- Did the model misunderstand what is happening?
- Is the composition wrong for the page?
- Did the character drift?
- Did the medium drift?
- Did the image become more detailed than the book allows?
- Did the model invent decoration that does not serve the story?
- Did it beautify an intentionally ordinary object?
- Is every part of the image competing for attention?
- Is this actually a generation problem, or would a small edit solve it faster?

---

# Appendix B — The restraint test

Before accepting an image, ask:

1. What detail could disappear without hurting the story?
2. Is any background object more rendered than the main idea requires?
3. Would a traditional illustrator realistically spend this much time on that fabric, hair, leaf, brick, or prop?
4. Is there enough quiet space?
5. Did the model add “beauty” that I never requested?
6. Does this page look like it belongs beside the previous page?
7. Am I keeping this result because it serves the book, or because it is impressive by itself?

If the answer to the last question is “because it is impressive,” look again.
