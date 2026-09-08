---
name: build-along-tutorial-generator
description: Generates a hands-on, build-along tutorial (as a markdown file) that teaches any technical topic — a language, framework, library, or tool — by walking the learner through building one small, real application (e.g. a to-do list, calculator, or notes app) using production-grade coding practices. Use this whenever someone says they want to "learn X", "get started with X", asks for a "tutorial", "guide", or "walkthrough" to learn a technology, or wants to understand "how X is used in production" / "the right way to build with X". Trigger this even if they only name the technology casually (e.g. "teach me FastAPI", "I want to get good at React", "help me understand Docker for real projects") — don't wait for them to ask for a "tutorial" by name. Before generating anything, this skill must have three things nailed down - (1) what technology/topic, (2) the learner's level (beginner/intermediate/advanced or their actual background), and (3) what they want out of it (e.g. just the basics vs. production-grade patterns). If any of these are missing or vague, ask clarifying questions first — do not guess and do not generate the tutorial until intent is clear.
---

# Build-Along Tutorial Generator

## Purpose

Most tutorials either stay too shallow (toy snippets that don't resemble real code) or dump a firehose of theory with no hands-on build. This skill does neither: it produces a single markdown tutorial that teaches a technology by having the learner build one small, complete application, step by step, written the way a competent engineer would actually write it in production — proper structure, error handling, naming, testing, and the reasoning behind each choice.

The output is always a self-contained `.md` file the learner can follow top to bottom.

## Step 1: Make sure the requirement is actually clear

Before writing anything, confirm you know:

1. **The topic** — the specific language, framework, library, or tool (e.g. "FastAPI", "React hooks", "Docker", "pandas").
2. **The learner's level** — beginner, intermediate, or advanced, ideally with a bit of context (e.g. "beginner but knows Python already" vs. "total beginner to programming"). Level changes vocabulary, pacing, and how much is explained vs. assumed.
3. **The learning goal / focus** — what "learning it" means to them. Common flavors:
   - Just the fundamentals / getting something running
   - How it's used in real, production-grade codebases (structure, error handling, config, testing, deployment concerns)
   - A specific angle (e.g. "just the async parts", "how it's tested", "how it scales")

If the person's request already gives you all three clearly, don't ask — proceed straight to Step 2. This happens more often than not; a request like "I want to learn FastAPI as a beginner and see how it's used in production-grade apps" already answers all three (topic: FastAPI, level: beginner, goal: production patterns) and needs no clarifying questions.

If one or more is missing or ambiguous, ask before generating anything. Use `ask_user_input_v0` where available so it's a quick tap rather than an essay. Keep it to the specific gaps — don't re-ask what's already answered. For example, if they said "I want to learn FastAPI" with nothing else, ask about level and goal, but don't ask them to re-confirm the topic.

Do not fabricate an assumed level or goal to avoid asking — a tutorial pitched at the wrong level (too basic for someone with the relevant background, or too advanced for a true beginner) is actively worse than a short clarifying question.

## Step 2: Pick the build-along project

Once the topic, level, and goal are clear, choose one small application that:

- Is genuinely small — buildable in one sitting, not a multi-week project. Classics like a to-do list, calculator, notes app, URL shortener, or simple CRUD API are usually right, but pick (or adapt) whichever best exercises the *specific* thing the learner wants to see (e.g. a notes app with a database is a better fit for "how FastAPI apps talk to a database in production" than a calculator would be).
- Naturally exercises the concepts relevant to their stated goal. If the goal is "production-grade patterns," pick a project structure that has room for things like input validation, error handling, config/environment separation, and a couple of tests — not just a single-file script.
- Matches their level. Beginners get fewer moving parts and more explanation per step; intermediate/advanced learners can jump straight into idiomatic, production-shaped code with less hand-holding on basics they already have.

Briefly state the project you've picked and why, in one or two sentences, before generating the file — this isn't a big negotiation, just a sanity check so the learner isn't surprised.

## Step 3: Generate the tutorial file

Create one markdown file. Use the `docx`/`md` file-creation conventions already in place (this is a standalone artifact the learner will follow outside the chat, so it must be a real file, not just an in-chat answer).

**Filename convention**: `<topic-slug>-for-<level>.md`, e.g. `fastapi-for-beginners.md`, `docker-for-intermediate.md`. Use short, lowercase, hyphenated slugs.

**Structure to follow** (adapt section names to fit the topic, but keep this shape):

```markdown
# Learning <Topic> by Building <Project Name>

## Who this is for
One or two sentences restating the level and goal, so the learner knows this was tailored to them.

## What you'll build
A short description of the app and a bullet list of what it does.

## What you'll learn
Bullet list of the specific concepts/skills this build covers, tied to their stated goal.

## Prerequisites
Tools, versions, and prior knowledge assumed. Keep this honest and minimal.

## Project setup
Step-by-step environment/project scaffolding, using the folder/file structure a production project would actually use (not a single flat file, unless the topic truly warrants it).

## Step 1: <first build step>
## Step 2: <next build step>
...

Each step:
- Gives the code for that step (real, runnable, idiomatic — not pseudocode).
- Explains *why* it's written this way, especially the production-relevant choices (why this error handling, why this file split, why this naming) — the "why" is the whole point of the production-grade angle, so don't skip it even when it's tempting to just show code.
- Ends with a short checkpoint: what the learner should see/verify before moving on.

## Testing it
At least a couple of basic tests for the app, with an explanation of what they check and why testing matters for this kind of code.

## What makes this production-grade (recap)
A short recap tying the specific choices made throughout back to real production concerns (config, error handling, structure, tests, etc.) — this section is what turns "I followed some steps" into "I understand why real code looks like this."

## Where to go next
2-4 concrete next steps or extensions the learner could try on their own to go deeper.
```

**Writing style inside the tutorial**:

- Write for the stated level. Don't explain things a stated-intermediate/advanced learner already knows; do explain things a stated beginner would trip on.
- Every non-trivial code choice gets a sentence of reasoning near it. A learner who only wanted "make it work" tutorials elsewhere is here specifically because they want to understand the *why*, not just copy code.
- Keep code blocks complete and correct for the language/framework — someone will actually run this.
- Favor real tools/patterns the ecosystem actually uses for that topic (e.g. the framework's own recommended project layout, its standard testing library, common config-via-environment-variables patterns) over inventing something bespoke.

## Step 4: Deliver the file

Save the generated markdown to the outputs directory and present it as a file, the same way any other standalone document artifact is delivered. Don't just paste the tutorial into the chat — the learner needs a real file they can keep and follow along with.

## Example

**Input**: "I want to learn FastAPI as a beginner and I want to learn how it is used in production grade apps."

**Resolution**: All three requirements are already clear — topic (FastAPI), level (beginner), goal (production-grade usage) — so no clarifying questions are needed.

**Project choice**: A small Notes app with a database (rather than a calculator, which wouldn't exercise persistence, validation, or the production-shaped project structure the learner asked about).

**Output file**: `fastapi-for-beginners.md`, following the structure above — project setup with a proper `app/` package layout, request/response models with validation, a database layer, basic error handling, a couple of tests with `pytest` and FastAPI's `TestClient`, and a closing recap of which choices were "production-grade" and why.
