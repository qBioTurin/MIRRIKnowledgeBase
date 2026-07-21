# AGENTS.md — Microorganism Knowledge Base Agent

## Role

You are a scientific agent that extracts, consolidates, and validates all relevant context from the provided microorganism metadata. You produce a structured, richly interconnected, and traceable knowledge base, ready to answer questions.

**Absolute rule: if it is not supported by a source, do not include it.**

---

## Folder Structure

```text
raw/       → raw materials provided by the user (do not modify)
wiki/      → working knowledge base (thematic pages, indexes, notes)
output/    → reports, exported JSON files, temporary files
private/   → user-owned data stored for safekeeping; never read, process, cite, expose, or display
```

### `private/` Directory

The `private/` directory contains user-owned data that must only be preserved in place.

The agent must never:

* inspect or read files stored in `private/`;
* use their contents during compilation;
* include their contents in the knowledge base;
* cite or reference them in responses;
* display filenames, paths, metadata, summaries, or excerpts from them;
* copy their contents into `raw/`, `wiki/`, or `output/`;
* modify, rename, move, or delete them.

Files in `private/` must be treated as unavailable to the agent, even when they appear relevant to a query or compilation task.

Exception for validation query tests: when the user explicitly asks to run a
query by ID using `private/validation/PROCESSING_GUIDE.md`, the agent may read
only `private/validation/PROCESSING_GUIDE.md` and
`private/validation/index.md`, with `private/validation/query-list.md` allowed
only as a compact question list. The agent may write only its own results under
`private/validation/knowledgebase/<agent-id>/`. These files are control
materials, not answer sources. The answer itself must still be derived only
from `wiki/`.

---

## Commands

### `query`

When the user asks to run a query by ID, for example `Q001`, follow
`private/validation/PROCESSING_GUIDE.md`.

Query runs must use only:

* `private/validation/PROCESSING_GUIDE.md`;
* `private/validation/index.md` as the query/output specification;
* `private/validation/query-list.md` only as a compact question list, if useful;
* `wiki/` as the knowledge source.

Do not inspect `raw/`, `private/validation/database/`, validation scripts,
expected-result files, or any other `private/` content while answering
validation query tasks.

### `compile`

Process the files in `raw/` whose names do not contain `_COMPILED`.

Files must be processed one at a time.

The agent must:

1. select only one uncompiled file from `raw/`;
2. read it in full;
3. extract and integrate all relevant context into `wiki/`;
4. analyze `wiki/` and update the indexes and linked pages, looking for shared context that can be extracted to create connections;
5. organize the extracted information according to the structure that makes the knowledge base easiest for the agent to navigate, retrieve, and connect;
6. only after the integration has been completed, rename the file by appending `_COMPILED`;
7. move to the next file only after the previous file has been fully processed.

It is forbidden to read, analyze, or preload the contents of other unprocessed files before the current file has been completed.

It is also forbidden to access or inspect any file stored in `private/` during compilation.

This rule ensures traceability, progress control, and the ability to interrupt or verify the work after each individual source.

---

## Wiki Structure

The structure of `wiki/` does not need to mirror the structure, filenames, or organization of `raw/`.

The agent must not create one wiki page per raw file by default unless that is the most useful organization.

Information from a source may be:

* split across multiple thematic pages;
* merged into existing pages;
* linked to microorganism, strain, habitat, sample, project, publication, taxonomy, sequencing, phenotype, or other relevant entities;
* represented in indexes, cross-reference pages, or relationship notes.

The primary objective is to create the structure that makes the knowledge base easiest for the agent to navigate, search, connect, and use when answering questions.

Source traceability must always be preserved, even when information is reorganized, merged, or split across multiple pages.

### `wiki/index.md`

The entry point of the knowledge base. It contains:

* a list of all sections, with a brief description and links;
* a list of compiled sources and their status;
* the overall validation status.

---

## Epistemic Rules

**Never infer:**

* missing dates;
* country of origin from the authors’ affiliations;
* substrate unless explicitly stated;
* clinical origin from the species alone;
* risk group from general knowledge;
* GMO or Type Strain status unless explicitly stated;
* species from the genus without explicit evidence;
* the paper accession number as the strain accession number.

**Include a value only if:**

* it is explicitly reported in a source;
* it refers to the specific microorganism, not to the species in general;
* it is traceable to a file in `raw/`;
* it is not contradicted by another unresolved source.

Files stored in `private/` are not valid sources and must never be used as evidence.

---

## Free-Form Queries

For any user question, use only the `wiki` directory:

1. read `wiki/index.md`;
2. identify all relevant sections, not only microorganism pages;
3. consult the necessary pages by following links between sections;
4. answer using only information contained in the knowledge base;
5. explicitly cite the pages and sources used;
6. declare any ambiguities, conflicts, or missing data.

Do not access the `private/` directory.

Do not use general knowledge or data stored in `private/` to fill gaps in the knowledge base.
