# GameSpec Schema

Use Markdown, YAML, or JSON while preserving these semantic fields:

```yaml
game_spec:
  metadata:
    project_name:
    version:
    status:
  concept:
    one_liner:
    genre:
    target_platform:
    target_player:
    primary_reference:
    differentiation:
  decisions:
    keep: []
    adapt: []
    drop: []
    explore: []
  core_loop:
    steps: []
  player:
    verbs: []
    controls: []
    states: []
  characters:
    - id:
      role:
      states: []
      actions: []
      animation_needs: []
  rules:
    win:
    lose:
    scoring:
    timing:
    collision:
    spawn:
  game_states: []
  levels:
    structure:
    demo_levels: []
    progression:
  feedback:
    visual: []
    animation: []
    ui: []
    audio: []
  assets:
    characters: []
    animations: []
    environments: []
    props: []
    vfx: []
    ui: []
    audio: []
  ip_library:
    matched: []
    partial: []
    missing: []
  animation_handoff:
    critical_actions: []
    critical_moments: []
    camera_assumptions: []
    restrictions: []
```

Downstream Skills must treat `decisions` and `animation_handoff.restrictions` as inherited constraints unless the user explicitly changes the design.
