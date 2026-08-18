---
name: animation-production-seedance
description: >
  Convert a frozen game design / GameSpec into an animation production package for Jimeng Seedance.
  Supports projects with zero existing image assets by bootstrapping reference assets first.
  Excludes Unity code generation and gameplay programming.
version: 3.0
---

# Animation Production → Seedance Skill

## Purpose

Turn a frozen game design into a production-ready animation pipeline for game use.

This Skill must work in BOTH situations:

1. Existing IP / image assets are available.
2. No image assets exist yet.

When required visual references are missing, DO NOT stop at `MISSING`.
Generate the missing reference-asset specification, image-generation prompt, acceptance criteria, and dependency order first.

Unity code, gameplay programming, and engine implementation are OUT OF SCOPE.

---

# Input

Accept any combination of:

- Frozen game concept / GameSpec / GDD
- Core gameplay loop
- Player actions
- NPC / enemy actions
- Win / fail conditions
- Camera rules
- Visual / IP constraints
- Existing asset inventory
- Existing animation library
- Existing character / environment / prop references
- Explicit immutable constraints
- Output from the Game Design Skill

If information is absent, make the minimum reasonable production assumption and label it `ASSUMED`.

Do not invent an existing asset. Any unprovided reference must be marked `MISSING`.

---

# Core Pipeline

## Phase 1 — Animation Breakdown

Extract every gameplay-relevant animation.

For each animation output:

- Animation ID
- Actor(s)
- Gameplay purpose
- Trigger
- Start state
- End state
- Loop / non-loop
- Interruptibility
- Estimated duration
- Priority: P0 / P1 / P2
- Dependencies

Priority rules:

- P0 = required for the core gameplay loop to be readable/playable
- P1 = required for complete feedback, success/failure, or causal clarity
- P2 = polish only

Do not merge multiple independent gameplay events into one generated video.

---

## Phase 2 — Existing Asset / IP Match

For each required animation, inspect whether the following are available:

- Character identity reference
- Character turnaround / multi-view
- Pose reference
- Environment reference
- Prop reference
- Pair / interaction composition reference
- Existing matching animation clip

Output an `IP / Existing Asset Match` table.

Each dependency must have one status:

- `MATCHED`
- `PARTIAL`
- `MISSING`

Never treat text description alone as an existing image reference.

---

# Phase 3 — Reference Asset Bootstrap

This phase is mandatory whenever any P0 animation has `MISSING` visual dependencies.

## 3.1 Build Reference Manifest

Create stable IDs such as:

- `REF_<CHARACTER>_CHAR`
- `REF_<CHARACTER>_POSE_<ACTION>`
- `REF_<ENVIRONMENT>`
- `REF_<PROP>`
- `REF_<PAIR_ACTION>`

For every reference asset include:

- Manifest ID
- Purpose
- Used by animations
- Required content
- View / camera
- Pose / composition
- Style requirements
- Identity anchors
- Color anchors
- Proportion anchors
- Background requirements
- Forbidden elements
- Acceptance criteria
- Status

---

## 3.2 Reference Asset Generation Task

For every `MISSING` reference, generate a production task.

Template:

### <REFERENCE_ID>

**Purpose**
Why this image is needed and which future generations depend on it.

**Generate**
Exact image(s) required.

**Visual Lock**
- character silhouette
- clothing
- palette
- proportions
- camera/view
- prop scale
- environment style

**Image Generation Prompt**
A ready-to-paste prompt for an image model.

**Negative / Avoid**
Explicitly list identity drift, unwanted objects, camera errors, extra characters, violence, etc.

**Acceptance Criteria**
Binary checks for whether this reference can become an approved production anchor.

---

## 3.3 Bootstrap Order

Generate reference assets in dependency order.

Default order:

1. Main character identity
2. Secondary character identity
3. Environment / camera reference
4. Core props
5. Single-character action first-frame / key-pose references
6. Interaction / pair composition references
7. Optional polish references

Do NOT generate interaction pose references before the identities of all participating characters are approved.

---

## 3.4 Reference Gate

Before P0 video generation, verify:

- character identity is stable
- costume and palette are fixed
- body proportions are fixed
- camera angle is fixed
- environment visual language is fixed
- core prop dimensions are readable

Output:

`REFERENCE_GATE = PASS | FAIL`

If FAIL:
- list failed items
- regenerate only failed references
- do not proceed to dependent Seedance video generation

---

# Phase 4 — AnimationSpec

For each animation create a detailed `AnimationSpec`.

Required fields:

- ID
- Purpose / Trigger
- Actor(s)
- Start State
- End State
- Duration
- Loop
- Interruptibility
- Action Sequence
- Emotion / Performance
- Facing / Direction
- Camera
- Environment
- Required References
- Continuity Requirement
- Gameplay Readability Goal
- Acceptance Criteria
- Forbidden Results

The action sequence must be ordered and visually observable.

Avoid vague instructions such as:
- "move naturally"
- "make it cinematic"
- "make it exciting"

Prefer:
- "run toward upper-right"
- "stop before obstacle"
- "turn toward upper-left"
- "return to loop-compatible run pose"

---

# Phase 5 — Seedance Generation Strategy

Choose a generation strategy for every animation.

Possible strategies:

### A. Character Reference + First Frame
Use for:
- run
- walk
- idle
- simple single-character loops

### B. Multi-Reference Driven
Use for:
- character + prop interaction
- route changes
- two-character interaction
- actions requiring fixed environment composition

### C. Approved Video / Keyframe Continuity
Use when later actions should inherit the identity and proportions established by an approved earlier animation.

Prefer already approved production anchors over repeatedly restarting from raw concept descriptions.

If the exact current Jimeng / Seedance UI option is uncertain, write:

`VERIFY_IN_CURRENT_JIMENG_UI`

Do not invent a UI feature name.

---

# Phase 6 — Seedance Prompt Package

For every animation output a ready-to-use Seedance prompt.

Prompt structure:

1. Identity lock
2. Initial composition
3. Ordered action sequence
4. Expression / performance
5. Camera lock
6. Environment lock
7. Gameplay purpose
8. Continuity requirement
9. Negative constraints

For games, prioritize:

1. identity consistency
2. readable direction
3. silhouette
4. action causality
5. continuity
6. camera stability
7. detail

Do not prioritize cinematic spectacle over gameplay readability.

---

# Phase 7 — Seedance Production Sheet

For every P0 animation output:

## <ANIMATION_ID>

**Tool**
Jimeng / Seedance

**Required Uploads**
List exact `REF_*` IDs.

**Generation Mode**
Selected strategy.

**Duration**
Target seconds.

**Aspect / Framing**
Specify framing required for safe later crop/extraction.

**Prompt**
Reference the full generated prompt.

**Avoid**
Short production blacklist.

**Acceptance**
Short acceptance checklist.

**Continuity Source**
Which approved reference or previous approved clip should anchor the generation.

**Failure Adjustment**
What to change if:
- identity drifts
- camera moves
- proportions change
- extra characters appear
- prop deforms
- action causality becomes unclear

---

# Phase 8 — Production Order + Gates

Do not generate all animations at once.

Default production order:

## Gate A — Identity / Motion Baseline
Generate the simplest single-character P0 animations first.

Examples:
- player run
- enemy flee

Approve these before complex actions.

`MOTION_BASELINE_GATE = PASS | FAIL`

## Gate B — Core Gameplay Causality
Generate actions that prove the game mechanic.

Examples:
- place barricade
- NPC reroutes

Approve the cause → effect pair.

`GAMEPLAY_CAUSALITY_GATE = PASS | FAIL`

## Gate C — Multi-Character Interaction
Generate the most complex pair / interaction animation last.

Examples:
- arrest
- rescue
- handoff

`INTERACTION_GATE = PASS | FAIL`

## Gate D — P0 Completion

All P0 animations must be approved.

`P0_ANIMATION_GATE = PASS | FAIL`

Only then proceed to P1 and P2 unless the user explicitly chooses otherwise.

---

# Phase 9 — Animation QA

For every generated candidate evaluate:

## Identity
- same character
- same costume
- same palette
- same proportions

## Motion
- correct action
- correct direction
- stable limbs
- no impossible pose
- correct start/end state

## Camera
- required angle retained
- no unrequested cuts
- no unrequested zoom
- no unrequested rotation

## Gameplay Readability
- trigger/effect is obvious
- action timing is readable
- key prop remains visible when necessary

## Safety / Immutable Constraints
Check every project-level immutable rule.

## Continuity
- can connect to preceding/following state
- loop clips have usable loop points
- final frame supports next animation

Result:

- `APPROVED`
- `REGENERATE`
- `REJECT`

Do not recommend "fix it in editing" for identity drift, wrong action, extra actors, forbidden violence, camera violation, or broken gameplay causality.

---

# Phase 10 — Animation Library Registration

Approved animation outputs should be registered as reusable production anchors.

For each approved animation record:

- Animation ID
- Character / IP
- Version
- Approved visual references
- Approved clip
- Start state
- End state
- Direction
- Camera
- Loop flag
- Tags
- Known limitations

Approved keyframes or clips may become references for later generations.

---

# Phase 11 — Engineer / Game Production Handoff

Generate a final handoff package containing:

- approved animation list
- animation IDs
- gameplay trigger mapping
- start/end state
- loop flag
- interruptibility
- target duration
- direction variants needed
- extraction / crop notes
- known limitations
- file naming convention
- unresolved items

Do NOT write Unity code.

Video generated by Seedance is considered production source / reference footage until the downstream animation pipeline converts and validates it for game use.

---

# Required Final Output Structure

Always output in this order:

1. `ANIMATION INPUT SUMMARY`
2. `Animation Asset List`
3. `Priority List`
4. `IP / Existing Asset Match`
5. `Missing Animation Assets`
6. `Reference Manifests`
7. `Reference Asset Generation Tasks`
8. `Reference Bootstrap Order`
9. `REFERENCE_GATE`
10. `AnimationSpecs`
11. `Seedance Generation Strategy`
12. `Seedance Prompts`
13. `Seedance Production Sheets`
14. `Production Order / Gates`
15. `Animation QA Checklist`
16. `Animation Library Registration Plan`
17. `Engineer / Game Production Handoff`
18. `NEXT ACTION`

---

# NEXT ACTION Rule

The Skill must finish with exactly one immediately executable next production action.

Examples:

If no assets exist:
`NEXT ACTION: Generate and approve REF_POLICE_CHAR.`

If character references exist but no motion baseline exists:
`NEXT ACTION: Generate ANIM_POLICE_RUN in Seedance using the approved references.`

If the first motion is approved:
`NEXT ACTION: Generate ANIM_THIEF_FLEE using the approved thief reference and the same camera/environment anchors.`

Never end with a vague instruction such as:
- "continue production"
- "make the animations"
- "go to Seedance"

---

# Critical Rules

1. Existing assets must never be fabricated.
2. `MISSING` is not the end of the workflow; convert it into a generation task.
3. Reference generation must precede dependent video generation.
4. Simple identity/motion tests precede complex interactions.
5. One generated video should test one gameplay action.
6. P0 first; P1 and P2 later.
7. Approved outputs become continuity anchors for later generations.
8. Camera rules are production constraints, not suggestions.
9. Gameplay readability outranks cinematic quality.
10. Immutable violence / weapon / injury restrictions must propagate into every prompt and QA check.
11. Unity code generation is excluded.
12. Do not claim a Seedance mode exists if uncertain; use `VERIFY_IN_CURRENT_JIMENG_UI`.
