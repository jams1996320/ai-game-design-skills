# Seedance Prompt Template

## Main Prompt

```text
[主体 / IP 身份]
保持角色为：{character identity}。
严格保持：{face / hairstyle / costume / body proportion / key identifiers}。

[起始画面]
角色从 {start pose / state} 开始。
角色位于 {screen position / environment}。
身体朝向 {direction}。

[动作]
角色执行 {action}。
动作顺序：
1. {beat 1}
2. {beat 2}
3. {beat 3}

动作重点：
{body mechanics / weight / speed / anticipation / impact / recovery}

[表情]
{expression}

[结束状态]
动作结束时角色进入 {end pose / state}，
便于后续衔接 {next gameplay state / loop}。

[镜头]
{shot size}，{camera angle}。
镜头 {locked / tracking / specified movement}。
不要擅自切镜头。

[场景]
保持 {environment / background} 连续稳定。
{prop constraints}

[用途]
该动画用于游戏中的 {gameplay purpose}，
优先保证动作清晰、轮廓可读、状态衔接稳定，而不是电影化运镜。
```

## Avoid

```text
不要改变角色身份。
不要改变服装和配色。
不要增加或减少肢体。
不要生成多余角色。
不要增加未指定道具。
不要改变动作方向。
不要擅自切镜头。
不要产生不必要的镜头旋转或大幅变焦。
不要让背景随机变化。
不要把关键动作遮挡在画面外。
```

If reference images are required, the Production Sheet must list them before the prompt so the operator knows what to upload into 即梦 Seedance.
