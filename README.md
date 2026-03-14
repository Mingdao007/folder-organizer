# folder-organizer

`folder-organizer` is a public, privacy-safe skill package for organizing local folders on macOS or Ubuntu.

It ships a Codex App skill, a Claude CLI excerpt, and a platform-neutral duplicate-audit script. The package focuses on safe incremental cleanup, reuse of the user's existing structure, and hash-verified duplicate handling.

## What ships

- `codex-app-folder-organizer/`
  - installable Codex App skill
- `claude-code-cli/CLAUDE.folder-organizer.md`
  - copyable Claude CLI excerpt

## Codex App

Install the skill from this repository and use the `codex-app-folder-organizer` package path.

The skill behavior is:
- safe mode by default
- incremental organization rather than full redesign
- reuse of existing buckets before creating new ones
- exact-duplicate removal only after hash verification
- system Trash safeguards on macOS and Ubuntu

## Claude CLI

Copy the contents of:

`claude-code-cli/CLAUDE.folder-organizer.md`

into your Claude CLI instruction surface.

## Privacy boundary

This public package does not ship:
- personal names
- school or course names
- private repository names
- absolute personal paths
- private memory or workflow files
- user-specific folder maps from the original private setup

The sample maps in this repository are examples only. They are not extracted from any private personal folder tree.

## Repository layout

- `README.md`
- `README.zh-CN.md`
- `LICENSE`
- `CHANGELOG.md`
- `codex-app-folder-organizer/`
- `claude-code-cli/`

## Platform support

This v1 package is written for:
- macOS
- Ubuntu

Trash behavior:
- macOS uses `~/.Trash`
- Ubuntu uses `~/.local/share/Trash/files`

If the Trash path cannot be confirmed, the workflow should stop the deletion step instead of permanently deleting files.

## License

MIT

## Chinese mirror

See:

`README.zh-CN.md`
