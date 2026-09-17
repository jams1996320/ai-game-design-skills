# 执行参考

以下命令由 Codex 执行，使用者无需学习终端。`<python>` 替换为 setup 输出的解释器完整路径，`<scripts>` 替换为当前 skill 的 scripts 目录。PowerShell 调用带空格的可执行路径使用 `&`。

## 安装

Windows（优先已有 PowerShell 会话执行，不设置永久策略）：

```powershell
& "<scripts>\setup-windows.ps1"
```

如果本机策略阻止运行脚本，先读取报错并遵循平台授权；可在允许的情况下仅对新启动的单次 PowerShell 进程使用 `-ExecutionPolicy Bypass -File ...`，不得修改机器策略或绕过企业管控。winget 的源和包协议会在安装过程中接受，安装前简述将安装 Python 和固定版本依赖。

macOS/Linux（已有 Python 3.9+，推荐 3.12）：

```sh
python3 "<scripts>/setup.py"
```

可用 `--root <目录>` 指定运行环境位置。安装包来自 PyPI；固定版本便于测试，不代表完整供应链哈希锁定。FFmpeg Windows wheel 是否适配 ARM64 等架构应以安装结果为准，当前 Windows x64 脚本待实机验证。没有 winget/Python、下载失败、受管权限拒绝时，报告准确原因，不反复盲试。

## 初次处理

```sh
"<python>" "<scripts>/process.py" process --video "input.mp4" --out "output/job-v1" --prefix eff_hero
```

已知交接帧率才加 `--fps 24`。自动检测失败或错误时查看原始帧，然后显式 `--color '#C04AFF'` 并使用新目录。用 `IMAGEIO_FFMPEG_EXE` 环境变量指定已验证的 FFmpeg 可执行文件（仅当前进程）。源视频不会修改。脚本失败可能留下部分输出目录，保留检查后另建任务目录，不覆盖继续。

## 修复

```sh
"<python>" "<scripts>/process.py" repair --job "output/job-v1" --out "output/job-v2" --frames 35-42,78 --similarity 0.09 --blend 0.06
"<python>" "<scripts>/process.py" repair --job "output/job-v2" --out "output/job-v3" --frames 78 --decontaminate
"<python>" "<scripts>/process.py" repair --job "output/job-v3" --out "output/job-v4" --frames 35 --restore-mask "restore-0035.png"
```

参数不是通用答案，按实际帧调节。restore mask 在白色区域会恢复原始 RGB 并提高 Alpha，因此不能包含背景。修复只作用于指定输出帧号（从 1 开始，非源视频时间码）。同一命令的遮罩作用于所有选中帧；移动主体要分别准备遮罩。

直接打开 review.html 即可本地审核。若当前浏览器阻止本地图片，可以在任务目录启动仅绑定 127.0.0.1 的临时 HTTP 服务，完成后关闭。不要对外网公开原始素材。

## 自检

```sh
"<python>" "<scripts>/test_pipeline.py"
```

自检生成绿/紫纯色背景短动画，检查自动检测、透明背景、前景保留、编号、修复隔离、旧版保护和 ZIP。合成测试不能替代真实即梦 MP4 的边缘及闪烁验收。Windows 安装需另做实机验证。
