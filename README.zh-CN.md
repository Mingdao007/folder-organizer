# Folder Organizer

面向两个环境的可复用文件夹整理 workflow：

- `Codex App`
- `Claude CLI`

这个仓库包含一个可安装的 `Codex App` skill、一份可复制的
`Claude CLI` excerpt，以及一个平台无关的 duplicate-audit script。
公开范围保持收敛：安全增量整理、优先复用现有目录结构、基于 hash
的 exact-duplicate 处理，以及 macOS 与 Ubuntu 的 system Trash 保护。

## 包含内容

- 可安装 skill：
  [`folder-org`](./folder-org)
- 可复制 CLI 文件：
  [`claude-code-cli/CLAUDE.folder-org.md`](./claude-code-cli/CLAUDE.folder-org.md)
- 面向 `Documents`、`Downloads` 和 project root 的公开 references
- 公开 duplicate-audit script：
  [`folder-org/scripts/hash_duplicates.py`](./folder-org/scripts/hash_duplicates.py)

## 安装 / 使用

- `Codex App`：从这个仓库安装 skill，repo path 使用 `folder-org`
- GitHub 安装目标：
  - repo: `<owner>/folder-organizer`
  - path: `folder-org`
- `Claude CLI`：把 `claude-code-cli/CLAUDE.folder-org.md` 复制或合并到本地
  `CLAUDE.md`

## 覆盖范围

- `safe mode` 文件夹清理
- 优先复用用户现有 buckets
- 只在 hash 验证后处理 exact duplicates
- macOS 与 Ubuntu 的 system Trash 保护
- 面向 `Documents`、`Downloads` 和 project root 的 sample maps

## 触发示例

- `Use folder-org to clean up this Downloads folder safely.`
- `Organize this Documents subtree without redesigning the whole structure.`
- `Find exact duplicates here and only move low-risk ones to Trash.`

## 非触发示例

- `Rename every folder to a brand new taxonomy.`
- `Refactor the code inside this Git repository.`
- `Delete duplicates permanently without a Trash safeguard.`

## 隐私边界

这个公开仓库保持 workflow 通用、可复用。

- 不包含个人姓名、学校名称、课程名称或私有项目标签。
- 不发布个人绝对路径、私有 memory 文件或私有 companion workflow。
- sample maps 保持通用，不直接抽取自任何私有个人目录树。

## 仓库结构

- `folder-org/`：可安装的 `Codex App` skill
- `folder-org/references/`：公开 references
- `folder-org/scripts/`：duplicate-audit script
- `claude-code-cli/`：本地 `CLAUDE.md` 用的最小 excerpt
- `CHANGELOG.md`：发布历史
- `LICENSE`：`MIT`

## 平台支持

这个 v1 版本面向：

- macOS
- Ubuntu

Trash 路径约定：

- macOS 使用 `~/.Trash`
- Ubuntu 使用 `~/.local/share/Trash/files`

如果无法确认 Trash 路径，流程应当停止删除步骤，而不是做 permanent
delete。
