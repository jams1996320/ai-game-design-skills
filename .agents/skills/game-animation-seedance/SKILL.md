---
name: game-animation-seedance
description: >
  Converts an approved GDD, GameSpec, or ANIMATION HANDOFF into a production-ready
  animation package for JiMeng Seedance. Use after game-design-decision to define
  animation priorities, reuse existing IP assets, create AnimationSpecs, and produce
  copy-ready Seedance prompts and production sheets without changing core game design.
---

# Game Animation Seedance Skill

## Purpose

Turn approved game design into gameplay-usable animation requirements and Seedance generation instructions.

Do not redesign the core game. Inherit upstream `GameSpec`, `ANIMATION HANDOFF`, asset requirements, and design decisions.

## Inputs

Prefer inputs from `$game-design-decision`:

- GameSpec
- ANIMATION HANDOFF
- Asset Requirements
- IP Library Match
- character / environment references
- existing poses, action clips, or animation references

If information is missing, label conservative assumptions as `ASSUMPTION`.

## STEP 1 — Normalize upstream design

Extract:

- game concept and core loop
- player verbs
- characters and objects
- game states
- critical gameplay moments
- success / failure beats
- camera assumptions
- asset requirements
- existing and missing IP assets
- design restrictions

Output `ANIMATION INPUT SUMMARY`.

## STEP 2 — Decompose animation needs

For each character or object, identify required:

- locomotion
- gameplay actions
- reactions
- state transitions
- expressions
- game-event animations

Classify priority:

- `P0`: required for core gameplay readability
- `P1`: required for a convincing demo
- `P2`: polish or variety

Generate P0 first.

## STEP 3 — Match existing IP / assets

For every animation need classify:

- `MATCHED`
- `PARTIAL_MATCH`
- `MISSING`

Evaluate identity, costume, silhouette, pose, motion, expression, camera, props, and environment separately.

Prefer reusable base actions such as idle, walk, run, jump, fall, land, attack, hit, victory, defeat, emotion, and interaction.

## STEP 4 — Create AnimationSpec

Follow `references/animation-spec-schema.md`.

Each animation must define:

- animation ID
- gameplay purpose and trigger
- start and end states
- action and timing
- loop / interrupt rules
- camera and framing
- expression
- environment and props
- reference assets
- constraints
- acceptance criteria

## STEP 5 — Choose Seedance generation strategy

Choose the most suitable strategy for each animation:

- character-reference driven
- first-frame driven
- image-to-video
- multi-reference driven
- motion-reference driven

Optimize for identity consistency, readable gameplay motion, stable composition, and continuity.

## STEP 6 — Generate Seedance prompts

Use `references/seedance-prompt-template.md`.

Prompts must be directly copyable into 即梦 Seedance and specify:

- subject identity
- starting pose
- exact action sequence
- body mechanics and timing
- direction and expression
- ending state
- camera
- environment
- continuity
- changes to avoid

## STEP 7 — Production package

For every P0 animation output:

- AnimationSpec
- Seedance Prompt
- Seedance Production Sheet
- Reference Manifest
- Generation / Acceptance Notes

The Production Sheet must explicitly state what reference materials the operator should upload into 即梦 before generation.

Use this compact operator block:

```text
即梦 / Seedance

【需要上传】
1.
2.
3.

【生成模式】
...

【时长】
...

【画幅】
...

【提示词】
...

【避免】
...

【合格标准】
...
```

## Design blocker rule

If animation production conflicts with an approved game-design decision, output:

```text
DESIGN BLOCKER
Problem:
Affected design decision:
Why animation production cannot resolve it safely:
What must return to Game Design:
```

Do not silently change core mechanics, player abilities, win / lose rules, character roles, level objectives, or approved visual identity.

## Final output order

1. ANIMATION INPUT SUMMARY
2. Animation Asset List
3. Priority List
4. IP / Existing Asset Match
5. Missing Animation Assets
6. AnimationSpecs
7. Seedance Generation Strategy
8. Seedance Prompts
9. Seedance Production Sheets
10. Reference Manifests
11. Generation / Acceptance Notes
12. DESIGN BLOCKERS, if any

## Quality gate

Verify that every P0 animation has a gameplay purpose, start/end state, priority, asset match status, generation strategy, copy-ready prompt, required upload references, and acceptance criteria.
