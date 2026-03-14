# Folder Org

Use this workflow to organize local folders on macOS or Ubuntu with a
privacy-safe and low-risk cleanup process.

Behavior:
- default to safe mode
- organize incrementally instead of redesigning everything from scratch
- reuse the current top-level buckets before creating new ones
- preserve working directories such as `assets/`, `scripts/`, `node_modules/`, `preview/`, export folders, and helper files
- delete only exact duplicates verified by content hash
- move removed files to the system Trash instead of permanently deleting them

Inputs to bind:
- `target_path`
- `target_mode`
- `safety_mode`
- `existing_structure_policy`
- `dedupe_policy`

Defaults:
- `target_mode = incremental`
- `safety_mode = safe`
- `existing_structure_policy = preserve current structure and reuse existing buckets first`
- `dedupe_policy = hash-verified exact duplicates only, move removed files to the system Trash`

Audit before moving:
- list top-level files and folders
- identify existing buckets that already express the user's organization
- detect loose files that should be absorbed into those buckets
- detect working directories that must move as one intact subtree
- run a duplicate audit before proposing deletion

Preferred commands:

```bash
rg --files "<target-path>"
find "<target-path>" -maxdepth 2 -mindepth 1 | sort
python3 scripts/hash_duplicates.py --base "<target-path>" --ignore-glob '*/node_modules/*'
```

Classification rules:
- move admin, invoice, reimbursement, tax, visa, or official files into an `Admin` area when that area exists
- move personal profile files into a `Personal` area
- move screenshots, recordings, exports, and meeting captures into a `Capture` area
- move project notes, drafts, deliverables, and supporting resources into a `Projects` or `Research` area
- in `Downloads`, separate files into these outcomes: move to a long-term folder, keep for later import into a document library, move to system Trash, or leave in place as ambiguous

Dedupe rules:
- use hash results as the deletion gate
- keep the copy already in the correct destination bucket
- keep the clearest canonical working name
- keep the highest version when versioned names have identical content
- keep user-facing deliverables over generated preview exports when only one copy is needed
- keep exact duplicates in preserved areas such as `submission/`, `backup/`, `legacy/`, or active experiment trees unless the user explicitly approves removing them

Platform Trash paths:
- macOS: `~/.Trash`
- Ubuntu: `~/.local/share/Trash/files`

If the platform Trash path cannot be confirmed, stop the deletion step and report the unresolved path instead of deleting files permanently.
