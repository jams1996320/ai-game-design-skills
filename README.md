# AI Game Production Skills

一套可直接随 GitHub 仓库共享给朋友使用的 Codex Skills。

仓库中包含两个连续工作的 Skill：

1. `game-design-decision`
   - 竞品 / 参考对象识别
   - 核心机制拆解
   - KEEP / ADAPT / DROP / EXPLORE 决策
   - 差异化设计
   - GDD / GameSpec
   - 素材需求与 IP 资产匹配

2. `game-animation-seedance`
   - 读取 GameSpec / ANIMATION HANDOFF
   - 动画需求拆解
   - P0 / P1 / P2 优先级
   - IP / 动作素材匹配
   - AnimationSpec
   - 即梦 Seedance Production Sheet
   - 可直接复制的 Seedance Prompt

> Unity 代码实现不在这两个 Skill 的职责范围内。

---

## 仓库结构

```text
ai-game-production-skills/
├── README.md
├── .gitignore
├── .agents/
│   └── skills/
│       ├── game-design-decision/
│       │   ├── SKILL.md
│       │   └── references/
│       │       ├── game-spec-schema.md
│       │       └── example-input.md
│       │
│       └── game-animation-seedance/
│           ├── SKILL.md
│           └── references/
│               ├── animation-spec-schema.md
│               ├── seedance-prompt-template.md
│               └── example-input.md
│
└── examples/
    └── demo-handoff.md
```

---

# 最简单的使用方式（推荐给不会 Terminal 的用户）

1. 打开本仓库 GitHub 页面。
2. 点击 `Code → Download ZIP`。
3. 在 macOS 双击 ZIP 解压。
4. 打开 Codex App。
5. 用 Codex 打开刚解压的整个仓库文件夹。
6. 在 Codex 中输入：

```text
$game-design-decision
```

或者：

```text
使用 $game-design-decision。
我想做一个类似 XXX 的小游戏。
```

完成游戏策划后继续输入：

```text
$game-animation-seedance
```

---

# 推荐的完整使用流程

## 第一步：游戏设计

```text
使用 $game-design-decision。

我想做一个类似 XXX 的小游戏。
目标平台：
目标用户：
我的想法：
参考游戏：

请按完整流程输出，不要写 Unity 代码。
```

Skill 会输出：

```text
Project Brief
Reference / Competitor Map
Core Mechanic Deconstruction
KEEP / ADAPT / DROP / EXPLORE Matrix
Differentiation Strategy
DESIGN DECISION SUMMARY
Complete GDD
GameSpec
Asset Requirements
IP Library Match
Missing Asset Report
ANIMATION HANDOFF
```

## 第二步：动画生产

```text
使用 $game-animation-seedance。

以下是 $game-design-decision 已确认的最终设计。
请继承全部设计决策，不要重新设计核心玩法。

[粘贴 GameSpec]
[粘贴 ANIMATION HANDOFF]
[粘贴 Asset Requirements]
[粘贴 IP Library Match]

请优先完成 P0 动画，并生成完整 Seedance Production Package。
```

---

# Demo 演示链

```text
游戏想法 / 参考游戏
        ↓
$game-design-decision
        ↓
竞品识别
        ↓
核心机制拆解
        ↓
KEEP / ADAPT / DROP / EXPLORE
        ↓
差异化设计
        ↓
GDD + GameSpec
        ↓
ANIMATION HANDOFF
        ↓
$game-animation-seedance
        ↓
动画需求拆解
        ↓
IP 资产匹配
        ↓
AnimationSpec
        ↓
Seedance Production Sheet
        ↓
即梦 Prompt
        ↓
即梦生成动画
```

# 当前工作流边界

本仓库负责：

```text
设计决策 → 游戏策划 → GameSpec → 动画需求 → Seedance Prompt → 动画生产包
```

暂不负责 Unity 程序实现、C# 游戏逻辑、正式联网系统、服务器、动画状态机接入和最终上线发布。
