---
name: game-design-decision
description: >
  A decision-first game design workflow for turning a game idea, reference title,
  competitor, or prototype brief into an auditable game concept, competitor analysis,
  core-mechanic breakdown, KEEP/ADAPT/DROP/EXPLORE decisions, differentiation strategy,
  decision-maker summary, GDD, GameSpec, asset requirements, and IP-library gap analysis.
  Use this skill before implementation or animation production. Do not write Unity code.
---

# Game Design Decision Skill

## Purpose

Turn an early game idea or reference title into a **decision-ready game design package**.

This skill must not jump directly from “reference game” to “new game idea”.

It must first expose:

1. What the reference game is doing.
2. Why its important mechanics work.
3. Which mechanics should be retained.
4. Which mechanics should be adapted.
5. Which mechanics should be removed.
6. Which new directions should be explored.
7. How the resulting game becomes meaningfully differentiated.

The final design must inherit these decisions.

---

# Hard boundary

This skill ends at the design / specification / asset-requirement stage.

Do **not**:

- implement Unity code;
- generate C# gameplay systems;
- create production networking code;
- build a final playable project;
- silently redesign decisions after the decision summary has been established.

Unity implementation is explicitly outside this workflow.

---

# Inputs

Accept any combination of:

- game idea;
- one or more reference games;
- screenshots;
- gameplay videos;
- store page or public description;
- target platform;
- target audience;
- play-session length;
- monetization constraints;
- control constraints;
- available IP / character library;
- available art / animation assets;
- production constraints;
- decision-maker preferences.

If important information is missing, make conservative assumptions and label them `ASSUMPTION`.

Do not stop the workflow simply because all inputs are not available.

---

# STEP 1 — Requirement Intake

Create a concise project brief.

Capture:

## 1.1 Product goal

- What is being made?
- Why is the project being made?
- Is the current target a concept, prototype, vertical slice, or demo?
- What is the expected player experience?

## 1.2 Target constraints

Capture where known:

- platform;
- audience;
- session length;
- player count;
- control method;
- camera;
- orientation;
- online/offline expectation;
- level structure;
- progression;
- score / ranking;
- content scope.

## 1.3 Existing assets

Identify:

- existing IP characters;
- character images;
- model sheets;
- existing animations;
- existing environments;
- UI assets;
- audio assets;
- reusable gameplay concepts.

## 1.4 Unknowns

Create:

```text
KNOWN
ASSUMED
UNKNOWN
```

Do not hide uncertainty.

---

# STEP 2 — Reference / Competitor Identification

If the user already supplied reference titles, begin with them.

Otherwise identify the closest relevant reference objects.

Do not produce a generic list of famous games.

Choose references because they illuminate a particular design question.

For each reference, state:

```text
Reference:
Why it matters:
Relevant mechanic:
What we should learn:
What we should NOT blindly copy:
```

Separate references into:

## Primary reference

The closest product-level comparison.

## Mechanic references

Games that solve one specific mechanic especially well.

## Experience references

Games useful for pacing, feel, presentation, onboarding, or social structure.

## Production references

Examples relevant to scope or production efficiency.

---

# STEP 3 — Core Mechanic Deconstruction

Break the primary reference into systems.

At minimum inspect:

- player verbs;
- core loop;
- moment-to-moment actions;
- challenge;
- failure;
- success;
- feedback;
- progression;
- level structure;
- scoring;
- rewards;
- social / multiplayer behavior if relevant;
- session structure;
- content variation;
- difficulty ramp;
- retention drivers.

Use the following structure:

```text
MECHANIC
Player action:
System response:
Player feedback:
Why it is satisfying:
Dependency:
Production cost:
Risk if removed:
```

Then identify:

## Core mechanics

Without these, the reference loses its identity.

## Supporting mechanics

They strengthen the experience but are not the core identity.

## Replaceable mechanics

They can be changed without destroying the experience.

## Expensive mechanics

High implementation, content, animation, networking, balance, or UX cost.

---

# STEP 4 — KEEP / ADAPT / DROP / EXPLORE Decision Matrix

Every major mechanic must receive one explicit decision.

Allowed decisions:

### KEEP

Retain the mechanic because it is essential and compatible with the new product.

### ADAPT

Retain the underlying value but change execution.

### DROP

Remove it because it conflicts with scope, audience, differentiation, or production reality.

### EXPLORE

Introduce a new mechanic or direction that creates new value.

Use this table:

| Mechanic | Reference role | Decision | Reason | New implementation | Risk |
|---|---|---|---|---|---|

Do not write “keep most things but make it different”.

Each decision must be specific enough that another designer can act on it.

---

# STEP 5 — Differentiation Strategy

The new game must not merely be a reskin.

Define differentiation at several levels.

## 5.1 Player fantasy

What fantasy is stronger or different?

## 5.2 Interaction

What does the player do differently?

## 5.3 Decision-making

What new choices does the player make?

## 5.4 Progression

How does the longer-term experience differ?

## 5.5 Content structure

How do levels, events, characters, hazards, or combinations create variety?

## 5.6 Social / online layer

If relevant, specify:

- connected play;
- asynchronous competition;
- points;
- ranking;
- persistent progression;
- level continuity;
- cooperative or competitive structure.

## 5.7 IP leverage

How can an existing IP character library be reused across multiple games?

Prefer reusable character capability definitions such as:

- idle;
- run;
- jump;
- attack;
- hit;
- victory;
- defeat;
- emotion;
- interaction.

Do not make every new game require a completely new character pipeline unless necessary.

---

# STEP 6 — Decision-Maker Review

Before expanding into the full specification, produce a compact review block.

Use:

# DESIGN DECISION SUMMARY

## Product sentence

One sentence describing the proposed game.

## Reference

Primary reference and why.

## What we KEEP

Bullets.

## What we ADAPT

Bullets.

## What we DROP

Bullets.

## What we EXPLORE

Bullets.

## Key differentiation

Maximum five points.

## Biggest risks

Maximum five points.

## Demo scope

What must exist to prove the idea.

## Out of scope

Especially expensive or distracting features excluded from the demo.

---

# Decision inheritance rule

Everything written after STEP 6 must inherit the decisions above.

If a later idea contradicts a STEP 4 or STEP 6 decision:

1. flag the contradiction;
2. explain why the decision should change;
3. explicitly update the decision matrix.

Never silently drift away from the approved direction.

---

# STEP 7 — Production-Ready Design Package

Generate the following deliverables.

## A. Complete GDD

At minimum:

### Game overview

- working title;
- genre;
- target platform;
- target player;
- core promise;
- reference positioning;
- differentiation.

### Core loop

Describe:

```text
INPUT
→ PLAYER ACTION
→ GAME RESPONSE
→ FEEDBACK
→ REWARD / FAILURE
→ NEXT DECISION
```

### Controls

Define all important player verbs.

### Rules

Explicitly define:

- win;
- lose;
- score;
- health / lives if relevant;
- time;
- collision;
- spawn;
- movement;
- hazards;
- interactions.

### Characters

For each:

- gameplay role;
- personality / visual identity if known;
- required actions;
- states;
- animation implications.

### Game states

Examples:

```text
BOOT
MENU
READY
PLAYING
PAUSED
SUCCESS
FAILURE
RESULT
NEXT_LEVEL
```

Adapt to the actual design.

### Level structure

Define:

- level objective;
- entry state;
- progression;
- challenge escalation;
- completion;
- transition;
- continuity between levels.

### Progression

Where relevant:

- points;
- stars;
- unlocks;
- ranking;
- chapters;
- level chains;
- multiplayer or connected progression.

### Feedback

Specify:

- visual;
- animation;
- UI;
- sound;
- haptic if relevant.

### Demo content

Specify the smallest meaningful content set.

---

## B. GameSpec

Produce a structured specification using the schema in:

```text
references/game-spec-schema.md
```

The GameSpec is the preferred handoff to downstream Skills.

---

## C. Asset Requirements

Produce an asset inventory grouped by:

```text
CHARACTER
ANIMATION
ENVIRONMENT
PROP
VFX
UI
AUDIO
REFERENCE
```

For every item provide:

```text
Asset ID:
Purpose:
Required:
Reusable:
Existing candidate:
Missing:
Priority:
Notes:
```

---

## D. IP Library Match

If an IP / asset library is available, classify every requirement:

```text
MATCHED
PARTIAL_MATCH
MISSING
NOT_REQUIRED
```

For characters, separate:

- visual identity;
- pose;
- action;
- expression;
- costume;
- prop;
- camera requirement.

The goal is to reuse an existing IP library whenever practical.

---

## E. Missing Asset Report

List only assets that block the next stage.

Prioritize:

```text
P0 — blocks core demo
P1 — materially improves demo
P2 — polish / expansion
```

---

# Final Output Order

Always output in this order:

1. Project Brief
2. Reference / Competitor Map
3. Core Mechanic Deconstruction
4. KEEP / ADAPT / DROP / EXPLORE Matrix
5. Differentiation Strategy
6. DESIGN DECISION SUMMARY
7. Complete GDD
8. GameSpec
9. Asset Requirements
10. IP Library Match
11. Missing Asset Report
12. Handoff to Animation

---

# Handoff to Animation

End with a normalized block titled:

```text
ANIMATION HANDOFF
```

It must contain:

- game concept;
- core loop;
- characters;
- player actions;
- NPC / object actions;
- game states;
- critical moments;
- success / failure beats;
- level / scene requirements;
- camera assumptions;
- animation asset list;
- matched IP assets;
- missing IP assets;
- visual restrictions;
- design decisions that downstream work must not change.

This handoff is intended for the `game-animation-seedance` skill.

---

# Quality Gate

Before completing, verify:

- Did we identify real references?
- Did we break down the reference rather than merely summarize it?
- Did every major mechanic receive KEEP / ADAPT / DROP / EXPLORE?
- Is differentiation mechanical, not merely cosmetic?
- Does the full GDD inherit the decisions?
- Is the demo scope small enough to execute?
- Are asset requirements explicit?
- Is IP reuse considered?
- Is the animation handoff complete?
- Did we avoid Unity implementation?

If any answer is no, fix it before finishing.
