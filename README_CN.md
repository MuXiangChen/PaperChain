[English](README.md) | 简体中文

<div align="center">

# 🧠 PaperChain

### AI 驱动的学术论文写作流程系统

将研究想法逐步转化为结构化论文内容，并生成符合规范的完整文档。

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

**PaperChain** 是一个面向学术论文写作的 AI 驱动结构化写作系统，它能够将研究想法逐步转化为结构清晰的论文内容，并最终生成符合规范的 Word 文档。同时，系统采用模块化设计，可以根据不同学科领域扩展相应的写作规范和组件。

在 PaperChain 中，大语言模型（LLM）被视为**可替换的生成引擎**。无论使用不同的 AI 服务提供商还是本地部署的模型，论文结构控制、写作规范体系以及文档生成流程都保持稳定一致。

PaperChain 的核心理念是将论文写作视为一个**结构化流程**，而不是简单的文本生成任务。通过结构约束与规范指导，系统能够帮助用户生成在格式、逻辑结构和研究方法表达上都更加严谨的论文内容，即使研究想法仍处于探索阶段，也能够形成符合学术规范的论文框架与初稿。

---
# 目录结构

```
paperchain/
├─ apps/
│  ├─ cli/                    # 命令行入口（生成 / 导出 / 校验）
│  └─ web/                    # （可选）Web 界面，用于交互式论文写作流程
│
├─ packages/
│  ├─ core/                   # Paper IR 类型定义 + 校验器 + 通用工具
│  │  ├─ ir/                  # Paper IR 数据结构定义
│  │  ├─ validators/          # guideline / rubric / schema 校验
│  │  └─ state/               # 项目状态模型（project.json 等）
│  │
│  ├─ canon-analyzer/         # 范文分析模块 -> 生成 Writing Guideline
│  ├─ ideagraph/              # 主题提取 + 想法聚类 + IdeaGraph 构建
│  ├─ evidence-builder/       # 文献检索 + 溯源 + 证据素材构建
│  ├─ outline-weaving/        # 大纲映射 + 内容候选池 + 内容编织
│  ├─ refinement/             # 文本重写 + 逻辑优化 + 规范校验
│  │
│  ├─ figurelab/              # 图表与结构图生成 + 版面布局建议
│  │  ├─ charts/              # matplotlib / plotly 图表适配
│  │  ├─ diagrams/            # graphviz / mermaid 图示适配
│  │  └─ layout/              # 图表尺寸 / 密度 / 版面布局建议
│  │
│  ├─ exporters/              # 导出模块（Word / LaTeX）
│  │  ├─ word/                # docx 模板渲染器
│  │  └─ latex/               # tex + bib 文档渲染器
│  │
│  ├─ standards/              # 学科规范包运行时 + 评分/校验系统
│  └─ plugins/                # 插件接口 + 内置辅助插件
│
├─ domain-packs/
│  ├─ domain-cs/              # 学科规范示例（计算机领域）
│  ├─ domain-med/             # 医学领域规范
│  └─ domain-law/             # 法学领域规范
│
├─ examples/
│  ├─ minimal/                # 最小端到端示例（完整 pipeline 示例）
│  └─ templates/              # 示例 Word / LaTeX 模板
│
├─ docs/
│  ├─ paper-ir.md             # Paper IR 结构说明与示例
│  ├─ discipline-packs.md     # 学科规范包（插件）开发指南
│  └─ exporters.md            # Word / LaTeX 导出说明
│
├─ .env.example               # 环境变量配置模板
├─ LICENSE
└─ README.md

```

---

# 使用方式

## 🌐 在线使用

[🧠Paperchain](https://www.witploy.cn/paperchain)

## 💻 本地部署

PaperChain can also be deployed locally for research, customization, or private use.

---
# 核心架构（Core Architecture）

## Canon Analyzer（范文分析模块）

Canon Analyzer 通过对少量权威范文进行深度结构分析，提取论文写作中的结构模式、写作要素以及研究方法表达方式。

该模块会生成一套标准化的 Writing Guideline（写作规范），用于指导后续的论文生成过程，并对生成内容进行质量校验。

即使研究内容仍处于探索阶段，PaperChain 也能够确保论文在 研究方法表达与写作规范层面保持学术严谨性。

### 分析流程（Analysis Flow）

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

### 核心职责（Responsibilities）

```
Canon Analyzer
│
├─ Document structure extraction
│   （论文结构解析：章节 / 小节 / 层级关系）
│
├─ Writing pattern analysis
│   （写作模式分析：论证逻辑 / 修辞结构）
│
├─ Methodology pattern detection
│   （研究方法表达模式：问题定义 / 方法描述）
│
├─ Section expectation modeling
│   （章节内容建模：篇幅、内容类型、证据形式）
│
└─ Guideline synthesis
    （生成标准化写作规范）
```

### 输出结果（Output）

```
Writing Guideline
│
├─ outline template
│   （论文大纲模板）
│
├─ section requirements
│   （各章节内容要求）
│
├─ rhetorical patterns
│   （写作与论证模式）
│
├─ citation expectations
│   （引用规范与证据要求）
│
└─ validation rules
    （内容与结构校验规则）
```

---

## IdeaGraph Engine（研究思路图引擎）

IdeaGraph Engine 用于将用户在多轮对话中的信息整理为结构化的研究思路分支。

该模块会从对话内容中提取研究主题，对相关想法进行聚类，并逐层展开为 从宏观到微观的概念树结构（macro-to-micro concept tree），作为论文结构与内容生成的基础。

### 思路结构化流程（Idea Structuring Flow）

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
也就是说，系统会将最初零散的想法逐步整理为清晰的研究思路图谱。

### 输出结果（Output）

* 结构化的研究主题分支（topics / subtopics）
* 可编辑的推理节点（claims / questions / assumptions）
* 用于文献检索与引用的证据需求（evidence requirements）

---

## Outline Weaving Engine（大纲编织引擎）

Outline Weaving Engine 负责将 IdeaGraph 中的研究思路映射到 Canon Analyzer 生成的标准论文大纲 中，并组织成结构化的章节内容。

在这一阶段，每个章节会形成一个 候选内容池（candidate pool），其中包含多个可能的论点或写作内容，用户可以在其中进行选择与调整。

当系统检测到某个章节内容不足时，可以返回 IdeaGraph 继续扩展思路或检索新的证据材料。

### 核心能力（Core Capabilities）

**Outline Mapping（大纲映射）**

* 将 IdeaGraph 中的内容映射到具体章节
* 每个章节可以包含多个候选论点或内容块

**Interactive Curation（交互式内容选择）**

* 用户可以选择最合适的论点
* 支持对内容块进行排序、合并或替换

**Narrative Coherence（叙事连贯性）**

* 自动生成段落之间的过渡内容
* 保证章节与段落之间的逻辑连贯

**Gap Detection（内容缺口检测）**

* 检测缺失的论证、示例或对比内容
* 自动扩展 IdeaGraph 并补充新的候选内容

---

## Editing & Refinement Engine（编辑与优化引擎）

Editing & Refinement Engine 负责将生成的内容片段整合为一篇结构连贯、符合学术规范的论文。

同时，该模块会根据 Writing Guideline 和 Discipline Pack（学科规范包） 对内容进行自动校验，确保论文在结构和写作规范上满足学术要求。
### 核心职责（Responsibilities）

**Structure Stabilization（结构稳定化）**

将内容组织为稳定的论文结构：

* outline → sections → paragraphs

即从论文大纲逐步展开为章节与段落。

**Writing Refinement（文本优化）**
对生成内容进行语言和表达层面的优化，包括：

* 提升表达清晰度（clarity）
* 保证逻辑连贯性（coherence）
* 维持学术写作语气（academic tone）
* 保持整体写作风格一致（stylistic consistency）

**Constraint Validation（约束校验）**
根据论文规范对内容进行结构与质量校验，包括：

* 章节内容完整性（section completeness）
* 引用是否存在以及格式是否正确（citation presence and formatting）
* 字数与篇幅要求（word count requirements）
* 论文结构规范（structural constraints）
* 内容重复与逻辑一致性检查（repetition and logical consistency）


### 输出结果（Output）

生成经过校验的 Paper IR（Intermediate Representation，论文中间表示），用于后续的文档导出流程。

### 目标（Goal）

确保生成的论文在 结构、逻辑与写作规范层面保持学术严谨性，即使研究内容仍处于探索阶段，也能够形成符合学术标准的论文框架与文本。

---

## Idea Workspace & Evidence Builder（思路工作区与证据构建模块）

Idea Workspace & Evidence Builder 负责将用户的研究想法转化为 可追溯、可引用的写作素材，并将思路生成与学术证据检索连接起来。

该模块的核心作用，是把用户的想法从“概念层”逐步转化为 有来源、有证据支撑的论文材料。

### 核心职责（Responsibilities）

**Idea Collection（想法收集）**

通过多轮交互对话收集和整理用户的研究信息，包括：

* 研究问题（research question）

* 研究主张或核心观点（thesis）

* 研究范围（scope）

* 关键概念定义（definitions）

* 研究假设（assumptions）

* 方法与研究约束条件（methodological constraints）

**Academic Retrieval（学术检索）**

* 检索相关论文与学术资料
* 检索渠道由 Discipline Pack（学科规范包） 定义

**Evidence Extraction（证据提取）**

系统会将生成的想法与相关证据进行关联，每个观点都可以绑定具体来源，例如：
* 学术论文（academic papers）
* 在线资料链接（URLs）
* 从文献中提取的关键证据片段（evidence snippets）

### 输出结果（Output）

* 具备证据支撑的写作素材工作区（evidence-backed writing workspace）
* 可直接用于论文引用的写作材料（citation-ready writing materials）

---

## FigureLab（图表与结构图生成模块）

**FigureLab** 用于生成论文中使用的 **可发表级别图表（publication-ready figures）**。

该模块既支持 **数据可视化图表**，也支持 **结构类图示（如架构图、流程图等）**，并能够根据 Word 或 LaTeX 文档版面自动调整图表布局，以保证论文排版整洁规范。

---

### 统计与数据图表（Statistical & Data Charts）

| 图表类型            | 使用库                 |
| --------------- | ------------------- |
| 折线图 / 柱状图 / 散点图 | matplotlib, plotly  |
| 箱线图 / 热力图 / 直方图 | seaborn, matplotlib |
| 雷达图             | matplotlib          |

---

### 高级科研可视化（Advanced Scientific Visualization）

| 可视化类型        | 使用库                  |
| ------------ | -------------------- |
| 误差线图 / 多坐标轴图 | matplotlib           |
| 置信区间图        | seaborn              |
| 密度分布图        | seaborn              |
| 聚类可视化        | sklearn + matplotlib |

---

### 架构图与流程图（Architecture & Workflow Diagrams）

| 图示类型         | 使用库                   |
| ------------ | --------------------- |
| 系统架构图 / 数据流图 | graphviz              |
| 技术路线图        | mermaid / graphviz    |
| 知识图谱可视化      | networkx + matplotlib |


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

 

### 布局与样式支持（Layout & Styling Support）

FigureLab 会自动确保生成的图表符合 **论文发表级别的排版规范**。

主要功能包括：

* 自动生成图注（caption）
* 自动进行图表编号（figure numbering）
* 统一学术风格的图表样式（consistent academic styling）
* 根据文档版面自动调整图表尺寸，并提供合理的布局建议（adaptive size and layout suggestions）

---

## Assist Plugins（辅助插件系统）

**Assist Plugin System** 允许通过插件的方式扩展论文写作流程，而不会影响核心架构的稳定性。

该系统可以接入各种辅助工具，用于提升论文写作的效率与质量。

常见插件示例包括：

* 语法检查（grammar checks）
* 术语一致性校验（terminology consistency verification）
* 引用检索（DOI 查询 / 文献元数据补全）
* 内容重复与相似度检测（repetition and similarity detection）
* 领域专用工具（如公式辅助、数据集描述模板等）

此外，**FigureLab** 的部分功能也可以通过插件形式对外提供调用。

### 目标（Goal）

在保持核心写作流程稳定的前提下，通过插件机制实现系统能力的灵活扩展。

---

## Standards System（学科规范系统 / Discipline Packs）

**Standards System** 用于支持不同学科领域的纵向扩展。

通过 **Discipline Pack（学科规范包）**，系统可以为不同领域定义专门的论文写作标准与规范。

### 提供的规范内容（Provided Standards）

* **论文类型的大纲模板**
  （例如：综述论文、实证研究论文、研究计划 / proposal 等）

* **章节结构要求与论证模式**
  （section requirements and rhetorical patterns）

* **学术文献检索来源与检索策略**
  （academic retrieval sources and search strategies）

* **基于评分标准（rubric）的全文质量评估**
  （rubric-based full-document review）

### 使用方式（Usage）

该系统主要用于：

1. 生成标准化的论文写作计划（writing plan）
2. 对生成的论文进行结构与规范层面的质量校验

---

## Export Renderers（文档导出模块）

**Export Renderers** 用于将经过验证的 **Paper IR（论文中间表示）** 转换为可发布或提交的最终文档格式。

当前支持的导出格式包括：

* Word（`.docx`）
* LaTeX（`.tex`）

---

### Word Renderer

Word 渲染模块用于生成符合模板规范的 `.docx` 文档。

主要功能包括：

* 加载官方或用户提供的 `.docx` 模板

* 保留模板中的样式结构，例如：

  * 标题层级（headings）
  * 正文文本（body text）
  * 图表标题（captions）
  * 参考文献格式（references）

* 通过锚点或占位符将生成内容写入模板

输出文件：

```
paper.docx
```

---

### LaTeX Renderer

LaTeX 渲染模块用于生成 `.tex` 论文源文件。

主要功能包括：

* 导出 `.tex` 文件及 `.bib` 文献引用文件

* 支持多种文档类型（document class），例如：

  * `article`
  * `report`
  * `IEEEtran`
  * `acmart`

* 自动处理以下内容：

  * 数学公式（equations）
  * 图表（figures）
  * 交叉引用（cross references）
  * 引用样式（natbib / biblatex）

---

# 路线图（Roadmap）

以下功能是 PaperChain 未来版本计划实现的方向。

## 近期计划

* [ ] **文档导入（Document Import）**

  支持将已有论文或草稿导入 PaperChain，并转换为 **Paper IR**，用于后续编辑、分析与结构重组。

  计划支持的格式：

  * Word（`.docx`）
  * LaTeX（`.tex`）
  * Markdown（`.md`）
  * PDF（结构解析）

  该功能将使用户能够：

  * 在 PaperChain 写作流程中继续编辑已有论文
  * 使用 **Canon Analyzer** 分析论文结构和写作质量
  * 通过 **Outline Weaving Engine** 对草稿结构进行重组
  * 自动改进引用、图表以及文档格式

---

## 计划中的功能

* [ ] **协作编辑（Collaborative Editing）**

  支持多人协作写作，适用于科研团队共同撰写论文。

* [ ] **更多学科规范包（Discipline Packs）**

  扩展对更多学科领域的支持，例如医学、经济学、法学等。

* [ ] **数据与实验集成（Dataset & Experiment Integration）**

  从数据集或实验日志中自动生成实验描述和结果分析部分。

* [ ] **文献管理工具集成（Citation Manager Integration）**

  支持与 Zotero、BibTeX 等文献管理工具集成。

* [ ] **交互式大纲编辑器（Interactive Outline Editor）**

  提供可视化界面，用于编辑 IdeaGraph 与论文大纲结构。

* [ ] **插件市场（Plugin Marketplace）**

  支持社区开发并共享领域专用插件。

---

## 长期愿景

PaperChain 的目标是成为一个 **结构化的 AI 学术写作基础设施**，支持跨学科的可复现科研写作流程。

---

# 目标用户与产品演进

PaperChain 的设计基于 **两个阶段的用户需求演进**。

---

## 当前阶段：论文写作新手

当前版本主要面向 **刚接触学术写作的学生或初级研究者**。

这类用户在写论文时通常会遇到以下问题：

* 不知道论文应该如何组织结构
* 只有少量范文可以参考
* 想法比较零散，不知道如何整理
* 不熟悉学术论文的写作规范

PaperChain 通过 **结构化写作流程（guided writing pipeline）** 来帮助解决这些问题。

当前的使用方式主要是通过 **多轮对话逐步完善论文思路**：

1. 用户通过多轮对话描述研究想法
2. 系统帮助用户逐步明确研究问题和研究方向
3. 将想法整理为结构化的 **IdeaGraph（研究思路图）**
4. 基于范文分析得到的写作规范生成论文大纲和初稿

这一流程帮助用户完成从：

**“不知道论文应该写什么、怎么写”**

到

**“拥有一篇结构清晰、符合学术规范的论文初稿”**

的转变。

---

## 未来阶段：专业研究者

在未来的版本中，PaperChain 将逐步面向 **有一定科研经验、需要频繁撰写论文的研究者**。

对于这类用户而言，问题往往不是不知道研究什么，而是：

* 已经有明确的研究问题
* 已经设计好研究方法或实验方案
* 已经有了论文结构或大纲

他们的主要需求是：

**不希望在论文写作本身花费过多时间。**

因此，未来版本将更加侧重 **提升论文写作效率**。

计划中的能力包括：

* 导入已有的 **研究方案或论文大纲**
* 将结构化大纲直接转换为 **Paper IR**
* 自动生成方法、实验和讨论部分的文本初稿
* 与实验数据、图表生成以及结果分析流程集成

在这一阶段，PaperChain 的角色将从：

> 帮助用户探索“写什么”

逐渐转变为：

> 帮助用户高效完成“怎么写”

---

## 长期发展方向

PaperChain 的目标是支持 **完整的学术写作流程**，从研究想法到论文发表。

```
初学者流程
想法 → 结构 → 初稿

↓

进阶流程
研究方案 → 结构化论文 → 发表
```

长期来看，PaperChain 希望构建一个 **AI 辅助学术写作的结构化基础设施**，让研究者能够把更多精力放在 **研究本身，而不是论文写作与排版** 上。

---

# 贡献（Contributing）

我们欢迎社区贡献者参与 PaperChain 的开发。

如果你有兴趣改进这个项目，可以通过以下方式参与：

* 提交 Bug 或问题反馈
* 提出新的功能建议
* 改进文档
* 开发新的 Discipline Pack（学科规范包）
* 为 Assist Plugin 系统开发插件
* 改进导出模块或可视化模块

---

### 开发流程

1. Fork 本仓库
2. 为你的功能或修复创建新的分支
3. 提交代码并写清晰的 commit 信息
4. 提交 Pull Request

请确保你的代码遵循项目现有结构，并包含必要的文档说明。

---

### 推荐贡献方向

以下方向尤其欢迎贡献：

* 为不同学科开发新的 **Discipline Packs**
* 改进 **FigureLab 可视化能力**
* 新增 **文档导出格式**
* 扩展 **文献检索集成**
* 改进 **Paper IR 校验工具**

---

# License

本项目基于 **MIT License** 开源。

你可以在遵循许可证条款的前提下自由使用、修改和分发该软件。

详细信息请参阅项目中的 **LICENSE** 文件。

---