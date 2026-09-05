# Art Direct AI — New Section: Don't Fight the AI
Date: 2026-09-05
Status: LOCKED for insertion during targeted rebuild pass

## Placement
Insert in the Iteration section, immediately before or after "Fix It in Editing."

This lesson should deliberately echo a real production failure:
the user gives a clear correction, the model repeats the same wrong solution anyway, and repeated retries make the result worse.

## Working title
# DON'T FIGHT THE AI

### Subhead
When the model keeps making the same mistake, stop trying to win the argument.

## Opening visual concept
One restrained illustration:
an illustrator/author at a desk, mildly pulling at their hair in frustration while the screen shows several nearly identical failed versions of the same page.

The joke should be obvious but the art must stay in the book's established loose pencil/colored-pencil/light-wash style.

No exaggerated cartoon rage.
No polished digital rendering.
No complex screen UI.
No generated readable text on the screen—only simple thumbnail-like repeated images.

## Reader-facing copy

You tell the model:

> Make the background simpler.

It gives you almost the same background.

So you try:

> Much simpler. Remove the extra trees.

It gives you the same trees with slightly different branches.

Then:

> REMOVE THE TREES.

Now it changes the character, the camera, the dog, and the lighting—but somehow the trees are still there.

At some point, you are no longer art-directing.

You are arguing with a probability machine.

## WHY THIS HAPPENS

Image models do not edit a picture the way a human illustrator opens a file and deliberately changes one object.

Even when you give a precise correction, the model may reconstruct large parts of the image from the same underlying visual pattern that produced the mistake in the first place.

That means a strong feature can keep reappearing:
- the same unwanted hairstyle;
- decorative foliage;
- extra clothing detail;
- the wrong composition;
- a troublesome hand pose;
- a repeated prop;
- the same over-polished face.

Your instruction can be perfectly clear and the model can still keep returning to the same visual neighborhood.

That is not a signal to write the same correction fifteen different ways.

It is a signal to change tactics.

## DON'T KEEP PULLING THE LEVER

### If the image is mostly right:
Repair the smallest possible area.

### If one feature keeps returning:
Change the reference, crop, mask, composition, or source asset instead of repeating the prompt.

### If the whole image keeps snapping back to the same look:
Start from a different generation, simplify the scene, or rebuild the problem area outside the generator.

### If the generator keeps damaging solved decisions:
Stop regenerating the full image.

## INSTEAD OF THIS

> "Keep everything exactly the same, but please remove the detailed sweater texture. Do not change anything else."

Repeated five more times.

## TRY THIS

Use the current approved illustration as the source asset.

Then:
- locally replace or simplify the sweater;
- mask only the clothing area;
- use a cleaner reference;
- or rebuild the page around the approved art rather than asking for another full image.

## THE IMPORTANT SHIFT

The goal is not to make the AI obey.

The goal is to finish the book.

Sometimes the fastest, most professional decision is to stop prompting.

## Key Takeaway
**If the model repeats the same mistake after clear correction, stop escalating the prompt. Change the workflow.**

## Production lesson locked from this project's own build
Do not "repair" a successful generated spread by repeatedly chopping, cropping, and pasting pieces into a new design.

If a spread was created as a complete spread and works as a complete spread:
- keep it intact;
- add an editorial page before/after it;
- or rebuild the WHOLE spread deliberately.

Do not fight the source format.
