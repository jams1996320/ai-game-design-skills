# AnimationSpec Schema

Recommended JSON-compatible structure:

```json
{
  "animation_id": "",
  "name": "",
  "priority": "P0",
  "subject": {
    "character_id": "",
    "object_id": ""
  },
  "gameplay": {
    "purpose": "",
    "trigger": "",
    "start_state": "",
    "end_state": "",
    "interruptible": false,
    "loop": false
  },
  "timing": {
    "target_duration_seconds": 0,
    "beats": []
  },
  "performance": {
    "action": "",
    "body_mechanics": "",
    "direction": "",
    "expression": "",
    "energy": ""
  },
  "camera": {
    "shot": "",
    "angle": "",
    "movement": "",
    "framing": ""
  },
  "scene": {
    "environment": "",
    "background_constraints": "",
    "props": []
  },
  "references": {
    "character_identity": [],
    "pose": [],
    "motion": [],
    "expression": [],
    "prop": [],
    "environment": []
  },
  "constraints": {
    "must_preserve": [],
    "must_not_change": [],
    "avoid": []
  },
  "output": {
    "expected_usable_segment": "",
    "acceptance_criteria": []
  }
}
```

The spec describes an animation asset that participates in gameplay, not merely a standalone video clip.
