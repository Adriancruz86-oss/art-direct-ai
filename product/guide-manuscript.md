# ART DIRECTING AI
## A practical guide to children's-book illustration with generative AI

**Working product manuscript — v0.2**

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

Throughout this guide, we will use a structured prompt architecture:

**SCENE** — what is happening.

**COMPOSITION** — where the important things belong.

**VISUAL LANGUAGE** — how the marks, medium, surface, and detail behave.

**CONTINUITY** — what must match established references.

**CONSTRAINTS** — what the model should not beautify, embellish, or invent.

The value of this structure is not that the headings themselves are magical. The value is that it forces you to make decisions before you generate.

---

## Chapter 5 — Character consistency starts before page one

Most creators discover the character-consistency problem too late.

They generate a beautiful first page, then ask for the same child again on page two. The hair changes. The eyes change. The face gets older. The shirt gains a collar. The shoes disappear. The child's body proportions shift. By page six, the book contains six close relatives instead of one character.

The mistake happened before page one.

The first finished illustration should not be the place where you discover who the character is.

### Lock the silhouette first

A character is often recognized from farther away than you think.

Before worrying about eye color or freckles, look at:

- head-to-body proportion;
- hair silhouette;
- height;
- shoulder width;
- leg length;
- posture;
- clothing silhouette;
- one or two memorable shapes.

If the silhouette changes dramatically, tiny matching details will not save continuity.

For a young child, decide whether the design uses a larger head and shorter limbs. For an older child, decide whether the proportions are more naturalistic. Decide whether the hair creates a round, triangular, wide, narrow, curly, or straight outer shape.

The goal is not anatomical precision. The goal is repeatability.

### Divide details into three groups

Create a character sheet with three categories.

**IMMUTABLE**

These should almost never change:

- approximate age;
- skin tone;
- hair color and primary silhouette;
- eye treatment;
- body proportion;
- signature glasses, birthmark, hearing aid, or other identity-defining feature;
- relative height compared with recurring characters.

**SCENE-DEPENDENT**

These can change because the story requires it:

- pose;
- expression;
- direction of gaze;
- outerwear;
- props held in the hand;
- lighting response.

**FLEXIBLE**

These may vary slightly without hurting identity:

- exact placement of a loose hair strand;
- tiny folds in clothing;
- hand position within a similar pose;
- minor asymmetry in pencil marks.

This distinction prevents two opposite problems: uncontrolled drift and over-constrained stiffness.

### Hair is a shape before it is hair

For consistency work, do not define hair primarily as thousands of strands.

Define the large masses.

Instead of:

> shoulder-length brown hair with detailed individual strands

Try thinking:

> dark brown bob forming one rounded outer mass, ending at the jaw, with a simple side fringe; internal strand detail kept minimal

The second description protects the silhouette.

It also prevents the model from spending half the image rendering hair texture that no traditional illustrator would bother drawing on every page.

### Wardrobe needs rules, too

A recurring outfit should be simple enough to reproduce.

If the child wears a yellow dress, decide:

- sleeve length;
- neckline shape;
- hem length;
- whether there is a waist seam;
- whether the fabric is plain;
- shoes and socks;
- any story-relevant accessory.

Then stop.

Do not let the outfit turn into a fashion-design exercise unless the story is about the outfit.

A good continuity note might say:

> Plain mustard-yellow knee-length dress, short sleeves, simple round neck, no printed pattern, no embroidery, no lace, no decorative trim.

That sentence is boring in exactly the right way.

### Reference poses should teach the model the character, not trap it

Build references that show identity from several useful views:

- front;
- three-quarter;
- side;
- neutral standing pose;
- seated pose if the story uses one frequently;
- a small expression range.

You are not trying to create every pose the character will ever perform.

You are teaching the stable design from enough angles that later scenes have somewhere to begin.

Too many creators make one perfect front-facing portrait and then wonder why the character collapses when asked to run, bend, climb, or turn away.

### Expression has a ceiling

Decide how expressive this book is allowed to become.

Some books use broad cartoon acting. Others use tiny eyebrow shifts and head tilts.

If your character design is quiet and handmade, an enormous open-mouth reaction with sparkling eyes may break the style even if the face is technically “consistent.”

Consistency includes emotional rendering.

### The page-one test

Before you begin the book, you should be able to answer these without improvising:

1. What does this character look like from across the room?
2. What five features cannot change?
3. What is the simplest version of the outfit?
4. How much facial detail belongs in this book?
5. What does the character look like from the side?
6. What expression would be too exaggerated for this visual language?

If you cannot answer those yet, you are not ready for page one.

---

## Chapter 6 — Control the page, not just the character

A generated illustration can be gorgeous and still be unusable as a book page.

The most common reason is simple: it was generated as a picture, not designed as a page.

Children's books need room for words, pacing, page turns, quiet moments, visual contrast, and rhythm across a sequence.

A beautiful image that ignores those needs is decoration, not page design.

### Decide where the text lives before you generate

If the manuscript belongs in the upper-left corner, tell the composition to protect the upper-left corner.

Do not ask the model to “leave some room for text.”

That is vague.

Use spatial language:

> Keep the upper-left third mostly open paper with only a very light wash. Place the character low and to the right. No important objects behind the text area.

You are not merely creating blank space. You are assigning hierarchy.

### Negative space is not missing content

Models tend to treat empty areas as unfinished problems.

Illustrators know better.

Negative space can:

- make text readable;
- make a small character feel lonely;
- make a large object feel enormous;
- create calm after a busy spread;
- direct the eye;
- make a page feel handmade rather than filled by an algorithm determined to decorate every inch.

If the model repeatedly fills your quiet space with trees, clouds, stars, flowers, furniture, texture, or floating particles, strengthen the instruction.

> Preserve visible paper. Do not fill the open area with decorative objects or texture.

### Full bleed is not automatically better

A full-bleed spread can feel cinematic and immersive.

That does not mean every page should be full bleed.

Spot illustrations and partial-page compositions can create rhythm. A small drawing floating on paper can be funnier, gentler, or more intimate than a fully rendered environment.

If every spread is a giant polished scene, nothing feels giant anymore.

### Save close-ups for when they matter

AI image generators love character portraits because portraits are visually legible and rewarding.

Books need more variety.

Use:

- wide establishing views;
- medium action views;
- small spot illustrations;
- object-focused moments;
- close-ups;
- occasional near-empty pages.

Do not let every page become a waist-up character looking toward the viewer.

A close-up has power because it is different from what came before it.

### Think in sequences of three

When planning pages, look at the page before, the current page, and the page after.

Ask:

- Are all three compositions the same distance from the character?
- Are all three equally busy?
- Is the character always in the center?
- Does the value pattern repeat?
- Does the next page need to feel bigger or quieter?

A book is not judged only one image at a time.

### Design the page turn

A reveal after a page turn can be more powerful than showing everything early.

If the manuscript says a child hears something enormous outside, you might keep the first page small and restrained: child, window, quiet room.

Turn the page.

Then show the enormous object.

The generator does not know your pacing unless you direct the sequence.

### The poster test

If every page looks like it could be used as a movie poster, the book probably has too much visual intensity.

Ask:

**Does this image serve this page, or is it trying to become the most impressive image in the book?**

Not every page gets to be the cover.

---

## Chapter 7 — Diagnose before you regenerate

A weak result often triggers the worst possible response:

> Try again.

Again with what changed?

If you cannot name the failure, regeneration becomes slot-machine behavior. You pull the lever until something looks good enough.

A professional workflow diagnoses first.

### 1. Scene failure

The model misunderstood the physical action.

Examples:

- the child is standing instead of kneeling;
- two characters are looking at the wrong object;
- the balloon is tied to the wrong hand;
- the door is open when the story requires it closed.

Fix the scene instruction. Do not rewrite your medium and style language.

### 2. Identity drift

The scene is correct, but the character no longer looks like the established character.

Look at:

- face proportion;
- age;
- hair silhouette;
- skin tone;
- height relationship;
- wardrobe;
- recurring accessories.

Strengthen continuity and reference usage.

### 3. Medium drift

The character is right, but the page suddenly looks like a different illustrator made it.

Common signs:

- paper texture disappears;
- pencil becomes smooth digital linework;
- watercolor becomes airbrushed shading;
- gouache becomes 3D rendering;
- edges become too clean.

Repair the rendering behavior, not the scene.

### 4. Detail overflow

The image has the correct subject and medium but too much visual information.

Typical symptoms:

- leaves individually rendered;
- hair overworked;
- fabric patterns invented;
- brick walls rendered brick by brick;
- every shelf object clearly visible;
- tiny decorative props added everywhere.

Lower the detail ceiling.

### 5. Beautification

The model made something prettier than the story needs.

This happens constantly.

A plain bedroom gains string lights and decorative pillows.

A muddy backyard gains perfect wildflowers.

An old coat gains embroidered trim.

A flashlight becomes a glowing magical artifact.

Add explicit ordinariness when necessary.

> Functional, plain, inexpensive object. No decorative embellishment.

### 6. Composition failure

Everything may look good, but the page cannot carry text or the focal point is weak.

Symptoms:

- subject centered when asymmetry is needed;
- important object hidden near the gutter;
- no text-safe region;
- multiple equally strong focal points;
- camera too close or too far.

Fix only the composition layer.

### 7. Invented props

Models often fill ambiguity with plausible objects.

If the story says “kitchen,” the model may invent:

- hanging pans;
- plants;
- patterned towels;
- fruit bowls;
- signs;
- shelves;
- decorative jars.

Some may be harmless. Others become continuity problems three pages later.

Every invented recurring object creates another thing you may need to remember.

### 8. Emotional overstatement

The manuscript says nervous.

The image says terrified.

The manuscript says curious.

The image says ecstatic.

The manuscript says sad.

The image says theatrical devastation.

Generated faces often overperform because strong emotion reads clearly.

Direct emotional intensity like any other design variable.

### 9. Anatomy or artifact failure

Extra fingers, merged objects, impossible joints, broken perspective, unreadable background symbols, accidental duplicates.

These are not art-direction failures. They are production defects.

If the rest of the image works, edit the defect instead of sacrificing the entire generation.

### 10. Page-level mismatch

Sometimes nothing is technically wrong with the image.

It simply does not belong beside the other pages.

That is enough reason to reject it.

### The one-sentence diagnosis rule

Before regenerating, force yourself to complete this sentence:

> The image fails because __________.

If your answer is only “I don't like it,” you are not ready to regenerate.

Name the failure first.

---

# Part III — The AI Fingerprints

## Chapter 8 — The polished face problem

Faces carry enormous visual weight.

That is why a face can make an otherwise restrained illustration suddenly feel synthetic.

The usual problem is not that the face is inaccurate.

It is that the face has been rendered with a level of finish that the rest of the book never asked for.

### Common fingerprints

Watch for:

- perfectly smooth skin;
- tiny gradient transitions across cheeks and nose;
- glossy catchlights in both eyes;
- highly symmetrical features;
- individually rendered eyelashes;
- soft cosmetic-looking blush;
- bright lip highlights;
- cinematic light wrapping around the face;
- detailed teeth inside a wide smile;
- a polished “character design” finish while the rest of the page is supposed to feel loose.

Children's-book faces often work because they are economical.

Two eyes, a nose suggestion, a mouth, one eyebrow angle, and the tilt of the head may be enough.

### Describe the amount of face

Instead of only describing the character, describe how much facial rendering is allowed.

For example:

> Facial features indicated with very few pencil marks. Simple eyes without glossy highlights. Skin mostly flat with only a faint wash. No individual eyelashes. No rendered lips. Keep asymmetry and hand-drawn irregularity.

You are directing restraint, not ugliness.

### Beware the “cute” multiplier

Words like *cute*, *adorable*, *beautiful*, and *charming* can push a model toward familiar signals:

- bigger eyes;
- rounder cheeks;
- smaller noses;
- shinier surfaces;
- sweeter smiles;
- cleaner symmetry.

That may be what you want.

But if the result starts looking like a mascot rather than the child in your book, remove the adjective and describe the actual design.

### The thumbnail test

Shrink the image until the face is small.

Does the expression still read?

If yes, you probably do not need all the micro-detail that appears at full size.

A children's-book reader often sees the page at a modest physical size. Detail that only rewards 300-percent zoom may be wasted labor — and a major AI tell.

---

## Chapter 9 — The hair problem

Hair is one of the easiest places for a generative model to show off.

It can produce hundreds of strands, soft highlights, flyaways, translucent edges, curls inside curls, reflected color, rim lighting, and perfect volume.

That is precisely why hair so often breaks an otherwise restrained children's-book style.

### Human illustrators usually simplify hair aggressively

Look at hair first as:

- silhouette;
- direction;
- one or two large value masses;
- a few accent strokes.

The viewer already knows it is hair.

You do not need to prove it strand by strand.

### A useful hierarchy

Think of hair rendering in four levels.

**Level 1 — Shape only**

One flat or lightly washed mass with outer contour.

**Level 2 — Shape plus direction**

Large mass plus a few strokes showing flow or parting.

**Level 3 — Selective texture**

A handful of curls or strands where they help the design.

**Level 4 — Full rendering**

Many visible strands, highlights, texture changes, flyaways, and dimensional shading.

For the loose children's-book look taught in this guide, most pages should live around Levels 1–2, occasionally 3.

If every page sits at Level 4, the hair may become the most expensive-looking object in every scene.

### Curly hair does not require drawing every curl

This is important.

Simplifying textured or curly hair does not mean erasing its character.

Preserve:

- outer silhouette;
- volume;
- major curl groups;
- direction;
- culturally and personally important styling.

Then reduce redundant internal detail.

A strong instruction might be:

> Preserve the full rounded volume and curl silhouette, but describe internal texture with only a few grouped colored-pencil marks. Do not render individual curls across the entire head.

### Hair continuity is silhouette continuity

If the same child's hair is chin-length on one page and shoulder-length on the next, no amount of matching eye color will fix the drift.

Record:

- length;
- part;
- outer shape;
- bangs/fringe;
- major tie, braid, bun, or clip placement;
- how far the hair extends relative to ears, jaw, neck, and shoulders.

That is more useful than “brown wavy hair.”

---

## Chapter 10 — The fabric problem

Fabric is where “impressive” quietly turns into ridiculous.

A generated dress may look beautiful at first glance. Then look closer.

There are tiny flowers repeated across the fabric. Each flower has several petals. The skirt has realistic folds. The hem has stitched trim. The bodice has subtle embroidery. The sleeves have gathered seams. Highlights describe the weave. Shadows explain every wrinkle.

Now ask the question this guide will keep asking:

**Would a human illustrator actually spend this much time drawing this fabric on this page?**

If the answer is no, the model has spent your detail budget in the wrong place.

### Clothing usually has three jobs

In most children's-book scenes, clothing needs to:

1. identify the character;
2. support the pose;
3. contribute a useful color or silhouette.

That is enough.

Unless clothing matters to the plot, it does not need to demonstrate textile manufacturing.

### Pattern multiplies work

A repeating pattern creates visual labor across every fold, curve, and perspective change.

A traditional illustrator who chooses a patterned dress knows they will need to redraw that pattern again and again across the book.

That cost influences the design decision.

A generator does not feel that cost.

It can invent an elaborate pattern instantly, which means it has no natural reason to simplify.

You have to supply that reason.

### Use plain language for plain clothes

Do not be afraid of instructions that sound aesthetically boring:

> Plain blue cotton shirt. No print, no logo, no texture emphasis, no decorative stitching.

> Simple red sweater with one flat color mass and only two or three folds needed to show the pose.

> Yellow dress with no pattern, embroidery, lace, trim, or visible weave.

These are excellent art-direction instructions.

### Folds should explain form, not show off physics

A few folds can show:

- bent elbow;
- seated posture;
- twisting torso;
- fabric hanging from a knee.

Past that point, additional folds may only add noise.

A useful constraint is:

> Clothing folds limited to those necessary to explain posture; avoid realistic fabric simulation.

### When pattern is actually important

Sometimes clothing detail matters.

A grandmother's handmade quilted coat may be a story object.

A child's striped shirt may be a key continuity marker.

A cultural garment may require accurate construction and decoration.

In those cases, detail is not forbidden.

It is **intentional**.

The question is never “Is detail bad?”

The question is “Why is this detail here?”

If you have an answer, keep it.

If the answer is “the model thought it looked nice,” reconsider it.

---

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
