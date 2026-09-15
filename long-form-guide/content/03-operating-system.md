# Part III: Build the Manuscript Operating System

A long manuscript needs a memory that exists outside any AI conversation. The operating system is a small collection of documents that records what the book is, what has been decided, what each chapter must do, and what changed during drafting.

The point is not paperwork. The point is controlled forgetting. You should not need to carry the whole book in your head or paste the whole manuscript into every session. Each task receives the smallest accurate packet of context it needs.

## 1. The master project bible

The project bible stores stable decisions: promise, reader, scope, voice, key definitions, high-level structure, evidence policy, continuity rules, and sensitive boundaries.

Update it only when a project-level decision changes. Do not add every sentence, research note, or brainstorming option. When a decision changes, record the date, the old decision, the new decision, and the reason.

Use the project bible at the start of architecture, chapter briefing, developmental revision, and any clean conversation.

## 2. The approved outline

The outline stores the current sequence of parts and chapters. Every chapter entry includes its primary job, dependency, target word count, and relationship to the book promise.

The outline is approved, not frozen. A change requires an architectural reason. Record moves, additions, mergers, and deletions in the decision log before drafting proceeds.

[WARNING]
Do not let an AI assistant quietly revise the outline while drafting prose. If a draft introduces a new central idea, stop and decide whether the architecture should change.

## 3. The chapter brief

The chapter brief is the immediate source of truth for a drafting session. It states the chapter's job, reader movement, required evidence or scenes, exclusions, opening, closing, word budget, and unresolved decisions.

The assistant receives the chapter brief. It does not receive permission to redefine the chapter.

At the end of drafting, compare the result to the brief. If the chapter changed for a good reason, update the brief and decision log. Do not rewrite history by pretending the change was always intended.

## 4. The style and voice sheet

The voice sheet describes observable writing behavior. Keep it short enough to use repeatedly.

Include:

- Point of view and relationship to the reader
- Degree of formality and directness
- Sentence and paragraph tendencies
- Vocabulary boundaries
- Treatment of uncertainty
- Humor and metaphor rules
- Preferred examples
- Repeated phrases and structures to avoid
- Two or three approved samples

Update the sheet after a voice revision reveals a useful rule. Do not update it to justify accidental drift.

## 5. The decision log

The decision log prevents the book from relitigating the same questions.

Each entry contains:

- Date
- Question
- Options considered
- Decision
- Reason
- Documents affected
- Review trigger, if any

Example:

> **Question:** Who is the primary reader within ages 13-21?  
> **Decision:** Write to a sixteen- or seventeen-year-old son, with examples marked for younger and older readers.  
> **Reason:** A single developmental center creates a consistent voice while sidebars preserve range.  
> **Affected:** Reader profile, voice sheet, examples, chapter briefs, youth review.

When an assistant offers an option that was previously rejected, the log gives you the reason without rebuilding the discussion.

## 6. The continuity tracker

[FICTION]
The continuity tracker records facts the story must preserve:

- Character appearance and physical limitations
- Relationships and forms of address
- Knowledge by character and chapter
- Objects, clues, injuries, promises, debts, and secrets
- Setting rules and travel time
- Scene date, time, weather, and location
- Setups and planned payoffs

Update it after every approved scene or chapter. Drafting from memory invites contradictions.

[NONFICTION]
Nonfiction continuity includes:

- Defined terms and their exact meanings
- Examples already used
- Claims promised for later treatment
- Objections raised and answered
- Practices introduced
- Terminology choices
- Cross-references and dependencies

A nonfiction manuscript can contradict itself without changing a character's eye color. It happens when "responsibility" means ownership in one chapter and authority in another.

## 7. The open-questions list

Open questions are decisions that block future work but do not need an answer yet.

Give each question:

- Owner
- Deadline or trigger
- Chapters affected
- Safe work that can continue meanwhile

An open question should not be hidden inside a draft comment. Centralize it. When it is resolved, move the answer to the decision log and update affected documents.

## 8. The revision ledger

The revision ledger tracks problems without forcing the author to solve them during drafting.

Record:

- Location
- Problem type
- Description
- Severity
- Revision pass
- Dependencies
- Status

Example: "Chapter 8 repeats the definition from Chapter 3" belongs in the repetition pass. "Chapter 8 relies on a claim without a source" belongs in the evidence pass. Separating the problems protects drafting momentum and produces cleaner revision.

## 9. The claim-and-source ledger

[NONFICTION]
For every meaningful factual claim, record:

- Claim ID
- Exact claim or narrow summary
- Chapter and section
- Source title and creator
- Source type
- Publication details
- Exact location: page, section, timestamp, or stable URL
- Whether the source directly supports the wording
- Verification date
- Quotation and permission status
- Notes or limitations

An AI-generated source suggestion begins with status **lead only**. It becomes usable only after a human opens the source and verifies it.

Do not cite search snippets, summaries of unread sources, or a model's description of a source.

## 10. The biblical citation and interpretation ledger

[BIBLICAL PROJECT]
This ledger prevents Scripture reference, interpretation, and application from collapsing into one unreviewed statement.

Record:

- Passage reference
- Translation used for direct quotation
- Verified wording and location
- Immediate context
- Observation from the text
- Interpretation adopted by the author
- Alternative interpretation requiring acknowledgment
- Theological source or tradition, when relevant
- Principle drawn
- Modern application proposed
- Audience and safety concern
- Human reviewer
- Review status

The ledger is not a substitute for study. It is evidence that study and review occurred.

## 11. The context-reset packet

The context-reset packet starts a clean AI conversation without pasting the entire manuscript.

It contains:

1. Book promise and primary reader
2. Current part and chapter
3. Relevant project-bible rules
4. Approved chapter brief
5. Relevant continuity or source records
6. A short summary of prior chapters needed for this task
7. Approved voice sample
8. Exact task
9. Required output format
10. Decisions the model must not make

Aim for the smallest packet that is still accurate. Extra context is not automatically helpful. Irrelevant material competes with the current task.

## 12. The chapter handoff

At the end of every approved chapter, create a chapter handoff summary:

- What the chapter accomplished
- Key claims, scenes, or changes
- New definitions or facts
- Decisions made during drafting
- Continuity and source updates
- Promises made to later chapters
- Open problems
- Exact ending state

The handoff becomes input to the next chapter brief and to later structural review.

## 13. Document ownership and update rhythm

Use this rhythm:

- **Before a drafting session:** Review project bible, approved outline, chapter brief, and relevant trackers.
- **During drafting:** Record new questions and potential revision issues without derailing the session.
- **After approving a section:** Update continuity or source records.
- **After approving a chapter:** Write the handoff and update the chapter status.
- **After an architectural change:** Update outline, briefs, project bible if needed, and decision log.
- **Before a new conversation:** Build a context-reset packet from current documents.

Only one version of each control document should be current. Archive old versions with dates. Do not keep several files called "final."

## 14. A practical folder structure

Use a structure that remains understandable without special software:

```text
Book Project/
  00 Project Bible/
  01 Architecture/
  02 Chapter Briefs/
  03 Drafts/
  04 Trackers and Ledgers/
  05 Sources/
  06 Revision/
  07 Assembly/
  99 Archive/
```

Name drafts consistently: `C07_v03_2026-09-15.docx` is more useful than `chapter seven newest final really final.docx`.

## 15. Operating-system audit

Before drafting, confirm:

- The current project bible is identifiable.
- The outline and chapter brief agree.
- The voice sheet contains examples and prohibitions.
- Decisions and open questions are separated.
- Fiction continuity or nonfiction source records are ready.
- The biblical citation ledger distinguishes text, interpretation, and application.
- A new conversation can be started from a context-reset packet.
- Every approved chapter will end with a handoff.

If these documents feel heavy, simplify them. Do not remove the decisions they preserve.
