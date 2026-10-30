# Chapter Conventions

This document is the single source of truth for how a chapter is named, structured,
tagged, cited and linked. `README.md`, `CONTRIBUTING.md`, the pull request template and
`Fish Disease Library/_Disease Chapter Template.md` point here instead of restating these
rules; if one of them disagrees with this file, this file wins and the other one is the
bug. New chapters and edits to existing ones should follow this spec.

It exists because the library grew to 25+ chapters with no written rules, and
incompatible patterns emerged as a result.

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
## Clinical Signs of <Disease>
### Common Signs
### Causes of <Disease>
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
---
**Last Modified:** <YYYY-MM-DD>
##### Other <Category>
[[<Related chapter>]]
**Citations:**
```

`<Disease>` is the chapter title as written in frontmatter, including its parenthetical
agent.

Notes:
- **"Clinical Signs", not "Symptoms".** Animals do not report symptoms. This applies to
  body text as well as headings.
- Common Signs, Causes, Diagnosis, Treatment and Prevention, and Case Studies are all
  `###` subsections of `## Clinical Signs of <Disease>`, matching the outline in
  `README.md`. Do not promote some of them to `##`.
- The footer after `---` holds, in this order: the `**Last Modified:**` date, links to
  the other chapters in the same category folder, and the citation list (§5). Existing
  chapters may still have an inline `**Tags:**` line there; see §4.
- **`Last Modified` is required.** It tells readers how current the chapter is (and how
  far to trust it when citing the library), and tells contributors which chapters are due
  a review. Update it whenever you change the content (new information, corrected facts,
  new citations); formatting and typo fixes do not count.
- **No information is better than bad information.** If you have no sourced information
  for a section, keep its heading and use this line as its only content, instead of
  filling it with unsourced text:

  ```
  *No data currently available. Want to edit this section? [Start here](https://github.com/manolinaqua/fish-disease-library/blob/main/CONTRIBUTING.md).*
  ```
- `Fish Disease Library/_Disease Chapter Template.md` is this outline with placeholders.
  Start new chapters from it.

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

`title` and `description` feed search and navigation on the
[Fish Disease Library website](https://fishdiseases.manolinaqua.com/). `description` is
the 1-2 sentence summary shown in search results: name the disease, the affected species,
and what the reader will learn.

`tags` power search and filtering on the website, so they only work if the same thing is
always tagged the same way. They are CamelCase with no spaces and include, at minimum: the
disease name, the pathogen, each affected species, the countries the chapter reports on,
and exactly one category tag matching `category`. Before creating a new tag, check whether
another chapter already uses one for the same thing (`AtlanticSalmon`, not `SalmoSalar` in
one chapter and `AtlanticSalmon` in another).

```yaml
tags:
  - Furunculosis           # disease
  - AeromonasSalmonicida   # pathogen
  - AtlanticSalmon         # affected species, one tag each
  - RainbowTrout
  - Norway                 # countries the chapter reports on
  - Chile
  - BacterialDiseases      # category tag, from the table below
```

| `category` | Category tag |
|---|---|
| Bacterial | `BacterialDiseases` |
| Viral | `ViralDiseases` |
| Parasitic | `ParasiticDiseases` |
| Fungal & Oomycete | not yet defined; set when Saprolegniasis moves to this category (see `tools/rename-map.tsv`) |
| Environmental & Physical | `EnvironmentalConditions` |

Tags live in the frontmatter. Until the website displays frontmatter tags, do not remove
existing inline `**Tags:**` lines; once it does, they will be removed in a clean-up PR.

## 5. Style

Anything not covered below follows Obsidian's
[style guide](https://help.obsidian.md/Contributing+to+Obsidian/Style+guide).

- **One locale.** This library uses **British English** for medical/veterinary terms
  (`anaemia`, `haemorrhagic`, `septicaemia`, `oedema`) since "septicaemia" was already the
  majority spelling in filenames (`Salmonid Rickettsial Septicaemia`). Everyday prose can
  stay in whichever English the contributor writes naturally; only the veterinary
  vocabulary needs to be consistent.
- **One italic marker** for scientific names: `*Genus species*`. Do not use `_…_` or
  HTML `<i>…</i>`.
- **One reference label**: `**Citations:**` followed by a bracketed, numbered list in
  [APA style](https://apastyle.apa.org/instructional-aids/reference-examples.pdf), with
  DOIs where available.
- **Inline citations** are the source's number linked to its URL, placed right after the
  claim: `...in Norway.[1](https://doi.org/...)`. The number matches the entry in the
  `**Citations:**` list.
- **Latest Research Findings** is a numbered list. Each entry has a bold title, an
  `Authors:` line, a `Reference:` line in APA, and a `[Link to study](url)`.
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
