[English](README.md) | [简体中文](README_CN.md)

<div align="center">

# 🧠 PaperChain

### AI Pipeline for Academic Writing

Transform research ideas into structured papers and fully formatted documents.

<br>

<a href="https://www.witploy.cn/paperchain">
<img src="https://img.shields.io/badge/🌐%20Website-PaperChain-blue"/>
</a>

<a href="https://github.com/MuXiangChen/PaperChain">
<img src="https://img.shields.io/badge/GitHub-PaperChain-black?logo=github"/>
</a>

<img src="https://img.shields.io/github/stars/MuXiangChen/PaperChain?style=social"/>

<img src="https://img.shields.io/badge/license-MIT-green"/>

</div>

---

**PaperChain** is an AI-driven academic writing pipeline that helps generate structured papers from research ideas to fully formatted Word documents, with modular components that can be extended for different academic disciplines.

PaperChain treats **LLMs as interchangeable generators**. Different AI providers or local models can be used while the structure control, standards system, and document generation pipeline remain stable.

The system focuses on **structured academic writing**, ensuring that papers follow rigorous formatting, logical structure, and methodological conventions even when the research idea itself is exploratory.

---
# Project Structure

```
paperchain/
├─ apps/
│  ├─ cli/                    # CLI entry (generate / export / validate)
│  └─ web/                    # (optional) Web UI for interactive workflow
│
├─ packages/
│  ├─ core/                   # Paper IR types + validators + shared utils
│  │  ├─ ir/                  # Paper IR schema / types
│  │  ├─ validators/          # guideline/rubric/schema validators
│  │  └─ state/               # project state model (project.json, etc.)
│  │
│  ├─ canon-analyzer/         # exemplar paper analysis -> Writing Guideline
│  ├─ ideagraph/              # topic extraction + clustering + idea graph
│  ├─ evidence-builder/       # retrieval + provenance + evidence workspace
│  ├─ outline-weaving/        # outline mapping + candidate pools + curation
│  ├─ refinement/             # rewriting + coherence + compliance checks
│  │
│  ├─ figurelab/              # charts + diagrams + layout hints
│  │  ├─ charts/              # matplotlib/plotly adapters
│  │  ├─ diagrams/            # graphviz/mermaid adapters
│  │  └─ layout/              # size/density/placement hints
│  │
│  ├─ exporters/              # Export Renderers (Word / LaTeX)
│  │  ├─ word/                # docx template renderer
│  │  └─ latex/               # tex + bib renderer
│  │
│  ├─ standards/              # Discipline Packs runtime + rubric engine
│  └─ plugins/                # Assist plugin interface + built-in plugins
│
├─ domain-packs/
│  ├─ domain-cs/              # discipline pack examples
│  ├─ domain-med/
│  └─ domain-law/
│
├─ examples/
│  ├─ minimal/                # minimal end-to-end pipeline example
│  └─ templates/              # sample docx/latex templates (if allowed)
│
├─ docs/
│  ├─ paper-ir.md             # Paper IR explanation + examples
│  ├─ discipline-packs.md     # plugin/packs API guide
│  └─ exporters.md            # Word/LaTeX export guide
│
├─ .env.example               # environment variables template
├─ LICENSE
└─ README.md

```

---

# Usage

## 🌐 Online

[🧠Paperchain](https://www.witploy.cn/paperchain)

## 💻 Local Installation

PaperChain can also be deployed locally for research, customization, or private use.

---
# Core Architecture

## Canon Analyzer

The **Canon Analyzer** performs deep structural analysis on a small set of exemplar papers to extract writing patterns, structural elements, and methodological conventions.

It derives a standardized **Writing Guideline**, which is then used to guide generation and validate document quality.

Even if the research contribution is limited, PaperChain ensures that **methodology and writing conventions remain academically rigorous**.

### Analysis Flow

```
sample papers (1~3)
      ↓
deep structural analysis
      ↓
writing elements extraction
      ↓
logic pattern discovery
      ↓
standardized guideline
      ↓
writing + validation
```

### Responsibilities

```
Canon Analyzer
│
├─ Document structure extraction
│   (sections / subsections / hierarchy)
│
├─ Writing pattern analysis
│   (argument flow / rhetorical patterns)
│
├─ Methodology pattern detection
│   (problem framing / method explanation)
│
├─ Section expectation modeling
│   (length / content types / evidence patterns)
│
└─ Guideline synthesis
    (canonical writing blueprint)
```

### Output

```
Writing Guideline
│
├─ outline template
├─ section requirements
├─ rhetorical patterns
├─ citation expectations
└─ validation rules
```

---

## IdeaGraph Engine

The **IdeaGraph Engine** organizes user conversations into structured research branches.

It extracts topics from multi-turn dialogue, clusters related ideas, and expands them into **macro-to-micro concept trees** that serve as the foundation of the paper.

### Idea Structuring Flow

```
chaotic ideas
      ↓
topic branches
      ↓
idea clusters
      ↓
macro → micro breakdown
      ↓
structured research map
```

### Output

* structured topic branches (topics / subtopics)
* editable reasoning nodes (claims / questions / assumptions)
* evidence requirements for retrieval and citation

---

## Outline Weaving Engine

The **Outline Weaving Engine** maps and organizes ideas from the IdeaGraph into a predefined outline generated by the Canon Analyzer.

Each section becomes a **candidate pool of arguments or ideas**, which users can curate interactively.

When gaps are detected, the system can return to the IdeaGraph to expand ideas or retrieve additional evidence.

### Core Capabilities

**Outline Mapping**

* map IdeaGraph content into outline sections
* each section may contain multiple candidate arguments

**Interactive Curation**

* users can select the most appropriate arguments
* reorder, merge, or replace content blocks

**Narrative Coherence**

* generate transitions between paragraphs
* ensure logical flow across sections

**Gap Detection**

* detect missing arguments, examples, or comparisons
* expand the IdeaGraph and refill the candidate pool

---

# Editing & Refinement Engine

The **Editing & Refinement Engine** converts generated content fragments into a coherent and academically compliant paper.

It also performs validation based on the **Guideline and Discipline Pack standards**.

### Responsibilities

**Structure Stabilization**

* outline → sections → paragraphs

**Writing Refinement**

* clarity
* coherence
* academic tone
* stylistic consistency

**Constraint Validation**

* section completeness
* citation presence and formatting
* word count requirements
* structural constraints
* repetition and logical consistency

### Output

Validated **Paper IR (Intermediate Representation)** used for final export.

### Goal

Ensure that the paper structure and writing quality remain **academically rigorous**, even if the research idea itself is exploratory.

---

## Idea Workspace & Evidence Builder

The **Idea Workspace & Evidence Builder** converts user ideas into **traceable, citation-ready writing materials**.

It connects idea generation with academic evidence retrieval.

### Responsibilities

**Idea Collection**

Multi-turn interaction collects:

* research question
* thesis
* scope
* definitions
* assumptions
* methodological constraints

**Academic Retrieval**

* retrieve papers and academic sources
* retrieval channels defined by Discipline Packs

**Evidence Extraction**

Each generated idea can be linked to sources such as:

* academic papers
* URLs
* extracted evidence snippets

### Output

* evidence-backed writing workspace
* citation-ready writing materials

---

## FigureLab

**FigureLab** generates publication-ready figures used in academic papers.

It supports both **data visualization** and **structural diagrams**, while automatically adapting figure layout for Word and LaTeX documents.


### Statistical & Data Charts

| Chart Type                | Libraries           |
| ------------------------- | ------------------- |
| Line / Bar / Scatter      | matplotlib, plotly  |
| Box / Heatmap / Histogram | seaborn, matplotlib |
| Radar                     | matplotlib          |


### Advanced Scientific Visualization

| Visualization                 | Libraries            |
| ----------------------------- | -------------------- |
| Error bars / Multi-axis plots | matplotlib           |
| Confidence interval plots     | seaborn              |
| Density plots                 | seaborn              |
| Cluster visualization         | sklearn + matplotlib |


### Architecture & Workflow Diagrams

| Diagram Type                     | Libraries             |
| -------------------------------- | --------------------- |
| Architecture / Dataflow diagrams | graphviz              |
| Technical roadmap diagrams       | mermaid / graphviz    |
| Knowledge graph visualization    | networkx + matplotlib |


--- 

## Layout & Styling Support

FigureLab automatically ensures publication-ready figure formatting.

Features include:

* caption generation
* automatic figure numbering
* consistent academic styling
* adaptive size and layout suggestions

---

## Assist Plugins

The **Assist Plugin System** allows additional tools to extend the writing pipeline without affecting the core architecture.

Examples include:

* grammar checks
* terminology consistency verification
* citation lookup (DOI / metadata completion)
* repetition and similarity detection
* domain-specific utilities (formula helpers, dataset description templates)

FigureLab can also expose its capabilities through the plugin system.

### Goal

Keep the core pipeline stable while allowing extensibility through plugins.

---

## Standards System (Discipline Packs)

The **Standards System** enables vertical expansion across different academic disciplines.

Discipline Packs define writing standards for specific fields.

### Provided Standards

* paper-type outline templates
  (survey, empirical, proposal, etc.)

* section requirements and rhetorical patterns

* academic retrieval sources and search strategies

* rubric-based full-document review

### Usage

The system is used for:

1. generating standardized writing plans
2. validating final paper quality and compliance

---

## Export Renderers

The **Export Renderers** convert validated Paper IR into publication-ready documents.

Supported formats include:

* Word (.docx)
* LaTeX (.tex)



### Word Renderer

* load official `.docx` templates

* preserve template styles:

  * headings
  * body text
  * captions
  * references

* inject content via anchors or placeholders

Output:

```
paper.docx
```



### LaTeX Renderer

* export `.tex` + `.bib`

* support multiple document classes:

  * article
  * report
  * IEEEtran
  * acmart

* handle:

  * equations
  * figures
  * cross references
  * citation styles (natbib / biblatex)

---

# Roadmap

The following features are planned for future iterations of PaperChain.

## Near-term

- [ ]  **Document Import**
    
    Import existing papers or drafts into PaperChain and convert them into **Paper IR** for further editing, analysis, and restructuring.
    
    Supported formats (planned):
    
    - Word (`.docx`)
    - LaTeX (`.tex`)
    - Markdown (`.md`)
    - PDF (structure extraction)
    
    This will allow users to:
    
    - continue editing existing papers inside the PaperChain pipeline
    - analyze structure and writing quality using the **Canon Analyzer**
    - restructure drafts using the **Outline Weaving Engine**
    - automatically improve citations, figures, and formatting


## Planned Features

- [ ]  **Collaborative Editing**
    
    Multi-user collaboration for research teams working on the same paper.
    
- [ ]  **More Discipline Packs**
    
    Expanded academic discipline support (e.g., medicine, economics, law).
    
- [ ]  **Dataset & Experiment Integration**
    
    Automatically generate experiment descriptions and result sections from datasets or experiment logs.
    
- [ ]  **Citation Manager Integration**
    
    Integration with tools such as Zotero, BibTeX, and reference managers.
    
- [ ]  **Interactive Outline Editor**
    
    Visual interface for editing the IdeaGraph and outline structure.
    
- [ ]  **Plugin Marketplace**
    
    Community-developed plugins for domain-specific tools.
    

## Long-term Vision

PaperChain aims to become a **structured infrastructure for AI-assisted academic writing**, enabling reproducible research writing workflows across disciplines.

---

# Target Users & Product Evolution

PaperChain is designed with a **two-stage evolution of users and workflows**.


## Current Focus: Beginner Researchers

The current version of PaperChain primarily targets **students or early-stage researchers** who are unfamiliar with academic writing.

Typical challenges for this group include:

- not knowing how to structure a paper
- having only a few reference papers
- difficulty organizing research ideas
- uncertainty about academic writing conventions

PaperChain addresses this by providing a **guided writing pipeline**.

The current workflow is centered around **interactive dialogue**, where users:

1. describe their research idea through multi-turn conversations
2. gradually refine their research question and structure
3. organize ideas into an **IdeaGraph**
4. generate a structured outline and draft based on exemplar-derived guidelines

This approach helps beginners move from **"I don't know how to write" → "I have a structured paper draft."**


## Future Focus: Professional Researchers

Future iterations of PaperChain will increasingly focus on **experienced researchers who already understand their research problem and methodology**.

For these users, the main challenge is **not what to write, but the time required to write it**.

The goal is to help them **convert research plans into structured papers more efficiently**.

Planned workflow improvements include:

- importing existing **research plans or outlines**
- converting structured outlines directly into Paper IR
- accelerating the writing of method, experiment, and discussion sections
- integrating datasets, experiment logs, and figures into the writing pipeline

In this stage, PaperChain shifts from:

**helping users discover what to write**

to:

**helping users efficiently transform research into publishable papers**

## Long-Term Direction

PaperChain aims to support the **entire spectrum of academic writing workflows**, from idea exploration to final publication.

```jsx
Beginner Workflow
idea → structure → draft

↓

Advanced Workflow
research plan → structured paper → publication
```

The long-term vision is to build a **structured infrastructure for AI-assisted academic writing**, enabling researchers to focus more on **research itself rather than document production**.

---

# Contributing

We welcome contributions from the community.

If you are interested in improving PaperChain, there are several ways to contribute:

- report bugs or issues
- suggest new features
- improve documentation
- develop new discipline packs
- build plugins for the Assist Plugin system
- improve exporters or visualization modules

### Development Workflow

1. Fork the repository
2. Create a new branch for your feature or fix
3. Commit your changes with clear messages
4. Open a Pull Request

Please make sure your code follows the existing project structure and includes appropriate documentation.

### Ideas for Contributions

Some areas that are particularly helpful for contributors:

- new **Discipline Packs** for different academic fields
- improved **FigureLab visualizations**
- new **export formats**
- additional **retrieval integrations**
- improved **Paper IR validation tools**

---

# License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this software in accordance with the terms of the license.

See the LICENSE file for more details.

---
