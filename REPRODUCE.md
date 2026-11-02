# How this repository was made (United States (Virginia))

This file is written by the build on 2026-11-02, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Virginia Legislative Information System: Code of Virginia and Constitution of Virginia | <https://law.lis.virginia.gov/vacode/> | 2026-10-30 | Public statute text |
| Virginia Law Library: Code of Virginia, one CSV file per title | <https://law.lis.virginia.gov/law-library/> | 2026-11-02 | Public statute text; the site footer reserves rights in the site, not in the law. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of Virginia | 1 | 2026-10-30 to 2026-10-30 |
| `title-18-2` | Code of Virginia, Title 18.2. Crimes and Offenses Generally | 2 | 2026-10-30 to 2026-11-02 |
| `title-1` | Code of Virginia, Title 1. General Provisions | 1 | 2026-11-02 to 2026-11-02 |
| `title-2-2` | Code of Virginia, Title 2.2. Administration of Government | 1 | 2026-11-02 to 2026-11-02 |
| `title-3-2` | Code of Virginia, Title 3.2. Agriculture, Animal Care, and Food | 1 | 2026-11-02 to 2026-11-02 |
| `title-4-1` | Code of Virginia, Title 4.1. Alcoholic Beverage and Cannabis Control | 1 | 2026-11-02 to 2026-11-02 |
| `title-5-1` | Code of Virginia, Title 5.1. Aviation | 1 | 2026-11-02 to 2026-11-02 |
| `title-6-2` | Code of Virginia, Title 6.2. Financial Institutions and Services | 1 | 2026-11-02 to 2026-11-02 |
| `title-8-01` | Code of Virginia, Title 8.01. Civil Remedies and Procedure | 1 | 2026-11-02 to 2026-11-02 |
| `title-8-1a` | Code of Virginia, Title 8.1A. Uniform Commercial Code — General Provisions | 1 | 2026-11-02 to 2026-11-02 |
| `title-8-2` | Code of Virginia, Title 8.2. Commercial Code - Sales | 1 | 2026-11-02 to 2026-11-02 |
| `title-8-2a` | Code of Virginia, Title 8.2A. Commercial Code — Leases | 1 | 2026-11-02 to 2026-11-02 |
| `title-8-3a` | Code of Virginia, Title 8.3A. Commercial Code — Negotiable Instruments | 1 | 2026-11-02 to 2026-11-02 |
| `title-8-4` | Code of Virginia, Title 8.4. Commercial Code — Bank Deposits and Collections | 1 | 2026-11-02 to 2026-11-02 |
| `title-8-4a` | Code of Virginia, Title 8.4A. Commercial Code — Funds Transfers | 1 | 2026-11-02 to 2026-11-02 |
| `title-8-5a` | Code of Virginia, Title 8.5A. Uniform Commercial Code — Letters of Credit | 1 | 2026-11-02 to 2026-11-02 |
| `title-8-7` | Code of Virginia, Title 8.7. Commercial Code — Warehouse Receipts, Bills of Lading and Other Documents of Title | 1 | 2026-11-02 to 2026-11-02 |
| `title-8-8a` | Code of Virginia, Title 8.8A. Commercial Code — Investment Securities | 1 | 2026-11-02 to 2026-11-02 |
| `title-8-9a` | Code of Virginia, Title 8.9A. Commercial Code — Secured Transactions | 1 | 2026-11-02 to 2026-11-02 |
| `title-8-10` | Code of Virginia, Title 8.10. Commercial Code — Effective Date — Transitional Provisions | 1 | 2026-11-02 to 2026-11-02 |
| `title-8-11` | Code of Virginia, Title 8.11. 1973 Amendatory Act — Effective Date and Transition Provisions | 1 | 2026-11-02 to 2026-11-02 |
| `title-8-12` | Code of Virginia, Title 8.12. Controllable Electronic Records | 1 | 2026-11-02 to 2026-11-02 |
| `title-8-13` | Code of Virginia, Title 8.13. 2022 Amendments – Effective Date and Transition Provisions | 1 | 2026-11-02 to 2026-11-02 |
| `title-9-1` | Code of Virginia, Title 9.1. Commonwealth Public Safety | 1 | 2026-11-02 to 2026-11-02 |
| `title-10-1` | Code of Virginia, Title 10.1. Conservation | 1 | 2026-11-02 to 2026-11-02 |
| `title-11` | Code of Virginia, Title 11. Contracts | 1 | 2026-11-02 to 2026-11-02 |
| `title-12-1` | Code of Virginia, Title 12.1. State Corporation Commission | 1 | 2026-11-02 to 2026-11-02 |

The build made 28 commits:

| Commits | Kind |
| ---: | --- |
| 27 | first version of an act |
| 0 | one law on its in-force day |
| 1 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-02.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 27 laws in the record.
- 28 tags.

## Dates

Each commit is dated at noon (America/New_York) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: No dated history is published: each text is the oldest version available, dated from the retrieval day. https://law.lis.virginia.gov/vacode/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `9edc06203ef339ea13bdd5e101d80977ac470f64071f0e65ddc00786976aa133` (13418021 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- English only. The Constitution and the Code of Virginia (every title).
- Every text has one version, "oldest version available", dated from the retrieval day and credited to the publisher; the site publishes only current text.
- Sections marked "Effective" on a date after 2026-10-30, or "Not in effect", are left out (2 such pages); "Effective until" versions are taken as current.
- The history line at the end of each section (the year and chapter citations) is not law text and is not kept.
- Wave 3 (2026-11-02): every Code of Virginia title in this part is added from the Virginia Law Library CSV files, one act per title, each the oldest version available dated by the retrieval day (2026-11-02).
- A CSV row whose caption begins "(Effective until <date>)" or "(Repealed effective <date>)" is kept only if that date is after the retrieval day; "(Effective <date>)" only if the date is on or before it; of a contingent pair, the "expiration" text is kept and the "effective" one left out; "Not in effect" rows are left out. Sections shown as "Repealed", "Expired" or "Reserved" keep their one-line stub, as in the first build.
- The last paragraph of a CSV body is dropped when it is a history line (it begins with a year, "Acts <year>", "Code <year>" or "R. P. 1948"). Captions end with a full stop, as on the section pages.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none (scripts only; no model wrote or altered legal text)
