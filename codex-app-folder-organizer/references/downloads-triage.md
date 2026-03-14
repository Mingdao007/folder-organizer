# Downloads triage

Use this file when the target path is `Downloads`.

Classification outcomes:
- move to the correct long-term folder
- keep for later import into a document library
- move to the system Trash
- leave in place and report as ambiguous

## Trash rules

Move an item to the system Trash when one of these is true:
- its content hash matches a file already stored in a long-term folder
- it is an installer package and the application is already installed
- it is an old or already installed extension package
- it is an exact duplicate inside `Downloads`

## Move-to-folder rules

Move an item from `Downloads` into a long-term folder when:
- it is a clear course work file
- it is a clear project or research file
- it is an admin or finance file
- it is a personal profile file

## Document-library rule

Prefer a document library as the long-term home for:
- lecture PDFs
- handouts
- reading papers
- reference PDFs that are primarily for study rather than local editing

## Verification rule

Do not treat name similarity as duplicate proof.

Use content-level verification such as SHA-256 hash before deleting a claimed duplicate.
