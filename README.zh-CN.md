# folder-organizer

`folder-organizer` 是一个公开的、以隐私保护为前提的 skill package，用来在 macOS 或 Ubuntu 上整理本地文件夹。

它包含 Codex App skill、Claude CLI excerpt，以及一个平台无关的 duplicate audit script。这个仓库强调安全增量整理、优先复用现有目录结构，以及只在 hash 验证后处理 exact duplicates。

## 包含内容

- `codex-app-folder-organizer/`
  - 可安装的 Codex App skill
- `claude-code-cli/CLAUDE.folder-organizer.md`
  - 可直接复制的 Claude CLI excerpt

## Codex App

从这个仓库安装 skill，并使用 `codex-app-folder-organizer` 这个 package path。

默认行为：
- 默认 `safe mode`
- 以增量整理为主，不做整体重构
- 先复用已有 buckets，再创建新目录
- 只有在 hash 验证后才处理 exact duplicates
- 在 macOS 和 Ubuntu 上都使用 system Trash 保护删除动作

## Claude CLI

把下面文件的内容复制到 Claude CLI 的指令面：

`claude-code-cli/CLAUDE.folder-organizer.md`

## 隐私边界

这个公开包不包含：
- 个人姓名
- 学校或课程名称
- 私有仓库名
- 个人绝对路径
- 私有 memory 或 workflow 文件
- 来自私有环境的个人目录地图

仓库中的 sample maps 只是示例，不是从任何私有个人目录树直接抽出的内容。

## 仓库结构

- `README.md`
- `README.zh-CN.md`
- `LICENSE`
- `CHANGELOG.md`
- `codex-app-folder-organizer/`
- `claude-code-cli/`

## 平台支持

这个 v1 版本面向：
- macOS
- Ubuntu

Trash 路径约定：
- macOS 使用 `~/.Trash`
- Ubuntu 使用 `~/.local/share/Trash/files`

如果无法确认 Trash 路径，流程应当停止删除步骤，而不是做 permanent delete。

## License

MIT
