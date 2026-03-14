---
name: folder-organizer
description: Organize local folders on macOS or Ubuntu, classify files into an existing structure, and remove only low-risk exact duplicates with hash verification and system Trash safeguards.
---

# Folder organizer

## Scope

Use this skill for local filesystem organization on macOS or Ubuntu.

Primary targets:
- one folder root chosen by the user
- `Documents` or a similar personal-work root
- `Downloads`
- one project or research workspace subtree

Default behavior:
- default to `safe mode`
- organize incrementally instead of redesigning everything from scratch
- reuse the user's existing top-level buckets before creating new ones
- preserve working directories such as `assets/`, `scripts/`, `node_modules/`, `preview/`, export folders, and helper files
- delete only exact duplicates verified by content hash
- move removed files to the system Trash instead of permanently deleting them

Route adjacent tasks:
- application-level library organization belongs to the user's chosen library tool or document manager
- code refactors inside a software repository belong to the normal coding workflow for that repository

## Input contract

Collect these fields:
- `target_path`
- `target_mode`
- `safety_mode`
- `existing_structure_policy`
- `dedupe_policy`

Apply defaults when missing:
- `target_mode = incremental`
- `safety_mode = safe`
- `existing_structure_policy = preserve current structure and reuse existing buckets first`
- `dedupe_policy = hash-verified exact duplicates only, move removed files to the system Trash`

Load references by path trigger:
- if the target folder basename is `Documents` or a similar home-documents root, read `references/documents-default-map.md`
- if the target folder basename is `Downloads`, read `references/downloads-triage.md`
- if the target folder looks like a projects or research root, read `references/projects-default-map.md`

## Canonical workflow

### 0. Apply safety mode first

Use `safe` as the default execution mode.

In `safe` mode:
- move only files whose destination bucket is clear from current context
- reuse the current folder scheme before proposing any new structure
- keep active project trees intact unless the user explicitly targets a deeper subtree
- delete only exact duplicates that are clearly low-risk cleanup targets
- report ambiguous duplicates instead of deleting them

Treat these as ambiguous by default:
- duplicates across `submission/`, `backup/`, `legacy/`, `archive/`, or similar preservation folders
- duplicates inside active project trees
- files that look similar by name but have not been content-verified
- documents that may still belong in an external document library until intent is clear

Use `aggressive` mode only when the user explicitly asks for broader cleanup.

### 1. Audit before moving

Run these checks first:
- list top-level files and folders
- identify existing buckets that already express the user's organization
- detect loose files that should be absorbed into those buckets
- detect working directories that must move as one intact subtree
- run the duplicate audit script before proposing deletion

Preferred commands:

```bash
rg --files "<target-path>"
find "<target-path>" -maxdepth 2 -mindepth 1 | sort
python3 scripts/hash_duplicates.py --base "<target-path>" --ignore-glob '*/node_modules/*'
```

### 2. Reuse the current scheme

Use this order:
1. Reuse clearly established buckets already present in the target folder.
2. Apply the relevant sample map for `Documents`, `Downloads`, or a project root when it matches the current context.
3. Create only the missing buckets needed for the current files.
4. For any new folder created in this run, capitalize the first word only.

### 3. Classify by role, not extension

Apply these routing rules:
- move admin, invoice, reimbursement, tax, visa, or official files into the current `Admin` area when organizing a documents root
- move personal profile files into the current `Personal` area
- move screenshots, recordings, exports, and meeting captures into the current `Capture` area
- move project notes, drafts, code-free deliverables, and supporting resources into the current `Projects` or `Research` area
- keep project folders intact by default; only classify inside a project folder when the user explicitly targets that subtree
- in `Downloads`, separate files into these outcomes: move to a long-term folder, keep for later import into a document library, move to system Trash, or leave in place as ambiguous

Move whole working directories intact when they already contain their own internal structure.

### 4. Dedupe safely

Use the hash audit output as the deletion gate.

Keep files using this priority order when two or more paths are hash-identical:
1. keep the copy that is already in the correct destination bucket
2. keep the clearest canonical working name
3. if names encode versions and content is identical, keep the highest version
4. keep user-facing deliverables over generated preview exports when only one copy is needed

Move removed duplicates to the system Trash.

Move lock files such as `~$*.pptx` or similar temporary office lock files to the system Trash when the corresponding main file exists.

Skip cleanup candidates that live entirely inside dependency directories such as `node_modules`.

In default `safe` mode, keep exact duplicates when they live in intentionally preserved areas such as `submission/`, `backup/`, `legacy/`, or active experiment trees, unless the user explicitly approves removing that class of copy.

### 5. Respect platform Trash behavior

Use the system Trash rather than permanent deletion.

Platform defaults:
- macOS: `~/.Trash`
- Ubuntu: `~/.local/share/Trash/files`

If the platform Trash path cannot be confirmed, stop the deletion step and report the unresolved path instead of deleting files permanently.

### 6. Verify after changes

Verify all of these:
- top-level buckets match the current local organization scheme for that target
- loose files have been absorbed into the right buckets unless the user explicitly kept them outside
- working directories still contain their internal helper folders
- removed files were moved to the system Trash, not permanently deleted
- the final report lists moved items, trashed items, and any ambiguous leftovers

## Default sample maps

### Documents root

When organizing a `Documents`-style root, prefer these buckets when they match the current structure:
- `Admin`
- `Capture`
- `Courses`
- `Personal`
- `Projects`

Preserve subfolder internals unless the user explicitly targets a deeper subtree.

### Downloads

When organizing `Downloads`, classify each item into one of these outcomes:
- trash exact duplicates already present elsewhere in the user's long-term folders
- trash installers or extension packages that are already installed and no longer needed
- keep reading materials for later import into a document library
- move clear local work files into the correct long-term folder
- leave ambiguous items in place and report them

### Project subtree

When organizing one project or research folder, group by task or deliverable, not by file type.

Prefer keeping one active project folder intact and moving cleanup or dated snapshots under an internal `Archive/` folder when the ownership is clear.

## File operation rules

- prefer `rg --files` for discovery
- prefer absolute paths in reports
- preserve existing file names unless the user asks for renaming
- use whole-directory moves for project trees rather than rebuilding them by hand
- when a move script fails midway, audit current state before continuing
