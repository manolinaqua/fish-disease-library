# Chapter Naming & Structure Conventions

This document is the naming and structure standard referenced by `README.md`. It exists
because the library grew to 25+ chapters with no written naming rule, and four
incompatible patterns emerged as a result. New chapters and renames of existing ones
should follow this spec.

## 1. Naming

**Default: `Disease Name (Causative Agent)`.**

The title names the clinical entity a veterinarian or farm manager is looking up; the
parenthetical disambiguates which agent this chapter is about. Binomials in the title
follow standard nomenclature: `Genus species`, genus capitalised, species epithet
lowercase (`Moritella viscosa`, not `Moritella Viscosa`).

```
Bacterial Kidney Disease (Renibacterium salmoninarum)
Furunculosis (Aeromonas salmonicida)
Winter Ulcer Disease (Moritella viscosa)
```

### Exceptions

1. **Non-infectious conditions carry no parenthetical.** Gas Bubble Disease,
   Hemorrhagic Diathesis, Nephrocalcinosis have no causative agent to name.
2. **When the agent name is just the disease name plus "virus", keep the acronym
   instead.** `Infectious Pancreatic Necrosis (IPN)` and
   `Infectious Salmon Anemia (ISA)` — spelling out "Infectious Pancreatic Necrosis
   Virus" adds nothing.
3. **Multi-species aetiologies use a genus-level or dual agent.**
   `Vibriosis (Vibrio and Aliivibrio spp.)`, `Tenacibaculosis (Tenacibaculum spp.)`,
   `Sea Lice Infestation (Lepeophtheirus salmonis, Caligus spp.)`. If the chapter's own
   text says the cause is "various pathogens" (e.g. Proliferative Gill Disease), use no
   parenthetical rather than a false-precision one.

### Preserving searchability

Because this replaces well-known acronyms and vernacular names as the *title*, every
chapter's frontmatter must list them under `aliases` so search and old links still find
the page:

```yaml
aliases:
  - BKD
  - Furunculosis
  - Vintersår
```

## 2. Page type — disease vs. pathogen

Not every agent maps one-to-one onto a disease. Some agents (documented case: Piscine
orthoreovirus, which causes HSMI in Atlantic salmon, jaundice syndrome in Chinook salmon,
and EIBS in coho salmon) cause several distinct, differently-named diseases in different
hosts. Naming a chapter after the agent and filling it with only one of the diseases it
causes — or merging a disease chapter into an agent chapter — silently drops the other
diseases. `type:` in frontmatter makes the two page kinds explicit and prevents this:

- **`type: disease`** (default). Titled `Disease Name (Agent)`. Uses the full clinical
  template (section 3).
- **`type: pathogen`**. Only for an agent that causes more than one named disease.
  Titled with the agent alone, e.g. `Piscine orthoreovirus`. Contains taxonomy,
  strains/genotypes, host range, and geographic distribution — **no Clinical Signs,
  Diagnosis, or Treatment sections**, since those differ per disease. Ends with a
  "Diseases caused" table linking to each disease chapter.

If you are about to write a chapter titled after a pathogen, first check its `Causes`
paragraph across a search of the vault: if the agent already appears in more than one
existing or planned disease chapter, it is a `type: pathogen` page, not a disease
chapter.

## 3. Section structure (clinical chapters)

```
## Overview
### What is <Disease>?
## Clinical Signs
### Common Signs
### Causes
### Diagnosis
### Treatment and Prevention
### Case Studies
## Data Insights
### Disease Impact by Country
#### <Country>
## Research and References
### Latest Research Findings
## Conclusion
### Call to Action
```

Notes:
- **"Clinical Signs", not "Symptoms".** Animals do not report symptoms.
- Causes, Diagnosis, Treatment and Case Studies are `###` under `## Clinical Signs`'s
  sibling level — they are not children of Clinical Signs. Keep heading depth flat and
  consistent; do not promote some to `##` and leave others at `###` within the same file.

This structure builds on `draft/disease-chapter-template` (see
`Fish Disease Library/_Disease Chapter Template.md`).

## 4. Frontmatter

```yaml
title: <Disease Name (Agent)>
type: disease   # or: pathogen
aliases:
  - <acronym>
  - <vernacular name>
pathogen: <Genus species>
category: <Bacterial | Viral | Parasitic | Fungal & Oomycete | Environmental & Physical>
description: <one or two sentences>
tags:
  - <CamelCase tags>
```

Keep a single source of tags. Do not also maintain a separate inline `**Tags:**` line at
the foot of the file — the two drift out of sync in practice.

## 5. Style

- **One locale.** This library uses **British English** for medical/veterinary terms
  (`anaemia`, `haemorrhagic`, `septicaemia`, `oedema`) since "septicaemia" was already the
  majority spelling in filenames (`Salmonid Rickettsial Septicaemia`). Everyday prose can
  stay in whichever English the contributor writes naturally; only the veterinary
  vocabulary needs to be consistent.
- **One italic marker** for scientific names: `*Genus species*`. Do not mix `*…*` and
  `_…_` in the same file.
- **One reference label**: `**Citations:**` followed by a bracketed, numbered list in
  APA style with DOIs where available, per `README.md`'s existing citation rule.
- Every scientific binomial is italicised on every mention, including in headings and
  table cells.
- Common (vernacular) virus names are **not** italicised and are written in lower case
  mid-sentence: "caused by piscine orthoreovirus (PRV)", "salmonid alphavirus (SAV)".
  Keep capitals only for proper nouns inside the name (e.g. "West Nile virus") and for
  acronyms. Cited article titles keep the capitalisation they were published with.

## 6. Links

- Use `[[Chapter Name]]` for any reference to another chapter in this library, exactly as
  `CONTRIBUTING.md` already instructs. Never link to another chapter via its published
  `https://fishdiseases.manolinaqua.com/...` URL or an `obsidian://open?...` URI — both
  break outside the author's own vault.
- Run `python3 tools/check-links.py` before opening a PR that adds or renames a chapter.
  It resolves every wikilink and embed against the vault's actual files and flags the two
  fragile patterns above.
