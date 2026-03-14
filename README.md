# Folder Organizer

Portable folder organization workflow for:

- `Codex App`
- `Claude CLI`

This repository ships one installable `Codex App` skill, one copyable
`Claude CLI` excerpt, and one bundled duplicate-audit script. The public scope
stays narrow: safe incremental cleanup, reuse of the user's current structure,
hash-verified exact-duplicate handling, and system Trash safeguards on macOS
and Ubuntu.

## What Ships

- installable skill:
  [`folder-org`](./folder-org)
- copyable CLI file:
  [`claude-code-cli/CLAUDE.folder-org.md`](./claude-code-cli/CLAUDE.folder-org.md)
- bundled references for documents roots, downloads triage, and project-root
  cleanup
- a public duplicate-audit script:
  [`folder-org/scripts/hash_duplicates.py`](./folder-org/scripts/hash_duplicates.py)

## Install / Use

- `Codex App`: install the skill from this repo path `folder-org`
- GitHub install target:
  - repo: `<owner>/folder-organizer`
  - path: `folder-org`
- `Claude CLI`: copy or merge
  `claude-code-cli/CLAUDE.folder-org.md` into your local `CLAUDE.md`

## Coverage

- safe-mode folder cleanup
- reuse of the user's existing buckets before creating new ones
- exact-duplicate removal only after hash verification
- system Trash safeguards on macOS and Ubuntu
- sample maps for `Documents`, `Downloads`, and project roots

## Trigger Examples

- `Use folder-org to clean up this Downloads folder safely.`
- `Organize this Documents subtree without redesigning the whole structure.`
- `Find exact duplicates here and only move low-risk ones to Trash.`

## Non-Trigger Examples

- `Rename every folder to a brand new taxonomy.`
- `Refactor the code inside this Git repository.`
- `Delete duplicates permanently without a Trash safeguard.`

## Privacy Boundary

This public repository keeps the workflow generic and reusable.

- It excludes personal names, school names, course names, and private project
  labels.
- It publishes no personal absolute paths, private memory files, or private
  companion workflows.
- It keeps the sample maps generic rather than extracted from one private
  folder tree.

## Repository Layout

- `folder-org/`: installable `Codex App` skill
- `folder-org/references/`: bundled public references
- `folder-org/scripts/`: bundled duplicate-audit script
- `claude-code-cli/`: minimal CLI excerpt for local `CLAUDE.md`
- `CHANGELOG.md`: release history
- `LICENSE`: `MIT`

## Platform Support

This v1 package is written for:

- macOS
- Ubuntu

Trash behavior:

- macOS uses `~/.Trash`
- Ubuntu uses `~/.local/share/Trash/files`

If the Trash path cannot be confirmed, the workflow should stop the deletion
step instead of permanently deleting files.

Chinese:

- [README.zh-CN.md](./README.zh-CN.md)
