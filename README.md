# United States (Virginia): law history in git

A first build of Virginia law as git: one file per provision, with the text published by the Virginia Division of Legislative Services ([law.lis.virginia.gov](https://law.lis.virginia.gov/vacode/)). It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `united-states/virginia/`. Language: English.

**What is in it now**

| Folder | Law | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of Virginia (1971, as amended) | 1 | Oldest version available (retrieved 2026-10-30) |
| `title-18-2/` | Code of Virginia, Title 18.2 (Crimes and Offenses Generally) | 2 | Chapters 1 to 6 retrieved 2026-10-30; the whole title retrieved 2026-11-02 |
| `title-*/` | Code of Virginia, every other title (Title 1 to Title 67), one folder per title | 1 | Oldest version available (retrieved 2026-11-02) |
| `charter-*/` | 210 current city, town and county charters | 1 each | Oldest version available, dated from the cited charter or latest amendment and its commencement rule |

Titles were added in parts on 2026-11-02 and 2026-11-03; `data/versions.json` lists what each commit holds. Each charter is a single-file act, with the official current text in source order.

## What it does not show

- **Past versions.** The Legislative Information System publishes the current Code, Constitution and charter text. Earlier charter versions are not included. Code sections marked as taking effect after the retrieval day are left out. The original Code and Constitution entries used retrieval days; the labelled correction set below supplies verified source dates; charter commits use dates from the source's charter and amendment citations, with the ordinary commencement rule in Va. Code § 1-214(A) or an expressly stated later date.
- **Other law.** Nine charter records await a verified commencement day. Authorities, compacts, uncodified acts and the Administrative Code are not included.
- **Dated changes.** Where a section is published in two forms ("Effective until ..." and "Effective ..."), the form in force on the retrieval day is kept.
- **Notes.** Source notes, histories and annotations are not law text and are not in the files.

## How it is checked

Every version names its source and the sha256 of the data it was read from. Each version is read back from git and must match `corpus.json` (`tools/check_repo.py`); the results are in `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions | Licence |
| --- | --- | --- | --- |
| [the Virginia Division of Legislative Services](https://law.lis.virginia.gov/law-library/): Code, Constitution and current charter text | Official publisher | no | Statute text is not copyrightable (Georgia v. Public.Resource.Org, 2020) |

## Licence

See `LICENSE`. This repository is not legal advice and not an official publication.

## Source date corrections

The labelled source-date correction set records 27 verified Code title dates from amendment commencement clauses and the ordinary statutory rule. The law text is unchanged. 49 other title dates await verified latest-amendment commencement; they retain their historical retrieval-day entries. Exact dates and source evidence are listed in `data/source-date-corrections.json`.

## Known source text gaps

Subsections (d) of Va. Code 8.9A-322 and (b) of 8.9A-709, and two normative tables in 34-4.2, are absent from the inherited record. The official CSVs contain them. The source-date corrections preserve the law files; separate labelled text corrections are still needed.
