# United States (Virginia): law history in git

A first build of Virginia law as git: one file per provision, with the text published by the Virginia Division of Legislative Services ([law.lis.virginia.gov](https://law.lis.virginia.gov/vacode/)). It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `united-states/virginia/`. Language: English.

**What is in it now**

| Folder | Law | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of Virginia (1971, as amended) | 1 | Oldest version available (retrieved 2026-10-30) |
| `title-18-2/` | Code of Virginia, Title 18.2 (Crimes and Offenses Generally) | 2 | Chapters 1 to 6 retrieved 2026-10-30; the whole title retrieved 2026-11-02 |
| `title-*/` | Code of Virginia, every other title (Title 1 to Title 67), one folder per title | 1 | Oldest version available (retrieved 2026-11-02) |

Titles were added in parts on 2026-11-02 and 2026-11-03; `data/versions.json` lists what each commit holds.

## What it does not show

- **Past versions.** The Legislative Information System publishes the current Code and Constitution only; sections marked as taking effect after the retrieval day are left out. Each text therefore has one commit, "oldest version available", credited to the publisher and dated by the retrieval day.
- **Other law.** Charters, authorities, compacts, uncodified acts and the Administrative Code are not included.
- **Dated changes.** Where a section is published in two forms ("Effective until ..." and "Effective ..."), the form in force on the retrieval day is kept.
- **Notes.** Source notes, histories and annotations are not law text and are not in the files.

## How it is checked

Every version names its source and the sha256 of the data it was read from. Each version is read back from git and must match `corpus.json` (`tools/check_repo.py`); the results are in `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions | Licence |
| --- | --- | --- | --- |
| [the Virginia Division of Legislative Services](https://law.lis.virginia.gov/vacode/): Code and Constitution pages, and the Virginia Law Library files | Official publisher | no | Statute text is not copyrightable (Georgia v. Public.Resource.Org, 2020) |

## Licence

See `LICENSE`. This repository is not legal advice and not an official publication.
