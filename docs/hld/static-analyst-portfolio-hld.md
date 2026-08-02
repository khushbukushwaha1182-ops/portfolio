# High Level Design (HLD): Static Analyst Portfolio (MkDocs)

## 1. Executive Summary & Objectives
The goal of this project is to build a high-performance, aesthetically pleasing, static portfolio website for a **Business / Data Analyst**. 
Built using **MkDocs** and the **MkDocs Material** theme, the site presents deep-dive analytical case studies (SQL/Python analysis, BI Dashboard showcases, and A/B test experiments) in free-form narrative layouts rather than uniform cookie-cutter cards.

---

## 2. Technical Stack & Architecture

| Component | Technology | Rationale |
| :--- | :--- | :--- |
| **Site Generator** | `mkdocs` (Python) | Fast compile time, simple markdown-based content workflow, zero server costs. |
| **Theme** | `mkdocs-material` | Out-of-the-box dark/light mode toggle, mobile-responsive layout, built-in search, and high customizability. |
| **Extensions** | PyMdown Extensions | Enables tabs, admonitions, Mermaid diagrams, code annotations, and inline HTML formatting (`md_in_html`). |
| **Custom Styling** | Vanilla CSS (`extra.css`) | Custom design tokens for KPI metric cards, hero section gradients, and clean case study layouts. |
| **Deployment** | GitHub Pages / Vercel | Instant static hosting with zero maintenance. |

```
                                SYSTEM ARCHITECTURE

  +-----------------------+      +---------------------------+      +-------------------------+
  |  Content Directory    | ---> |   MkDocs Generator        | ---> |  Production Output      |
  |  - docs/index.md      |      |   - mkdocs-material       |      |  - site/                |
  |  - docs/projects/*    |      |   - PyMdown extensions    |      |  - Clean HTML5/CSS/JS   |
  |  - docs/stylesheets/  |      |   - extra.css styling     |      |  - Load time < 0.5s     |
  +-----------------------+      +---------------------------+      +-------------------------+
```

---

## 3. Information Architecture (IA) & Page Hierarchy

```
/ (Root)
├── mkdocs.yml                      # Configuration file
├── requirements.txt                # Python dependencies
└── docs/                           # Content root
    ├── index.md                    # Landing Page: Hero, Bio, Skills Matrix
    ├── resume.md                   # Interactive Resume & PDF Download Link
    ├── projects/                   # Case Studies & Work Directory
    │   ├── index.md                # Projects Directory Overview
    │   ├── ecommerce-churn.md      # Project 1: SQL & Retention Strategy Deep-Dive
    │   ├── executive-bi.md         # Project 2: Interactive BI Dashboard Showcase
    │   └── pricing-ab-test.md      # Project 3: A/B Test & Experiment ROI Story
    ├── assets/                     # Media & PDF Assets
    └── stylesheets/
        └── extra.css               # Custom design system & theme overrides
```

---

## 4. Key Page Layout Specifications

### 4.1 Home / About Me (`docs/index.md`)
- **Hero Banner:** Executive headline, quick elevator pitch, social links (LinkedIn, GitHub, Email), and a prominent `[Download Resume]` call-to-action button.
- **Core Competencies Matrix:** Structured cards showcasing technical tools (SQL, Python, A/B Testing, Tableau/PowerBI, Data Modeling).
- **Featured Case Studies:** Scannable summary cards with key metric teasers linking directly to full case study pages.

### 4.2 Project 1: E-Commerce Churn Analysis (`docs/projects/ecommerce-churn.md`)
- **Focus:** Technical Rigor & Business Recommendations.
- **Design Elements:**
  - Executive summary box with high-level takeaway.
  - Tabbed SQL query snippets with line annotations explaining complex joins/window functions.
  - Actionable business impact callouts.

### 4.3 Project 2: Executive BI Dashboard (`docs/projects/executive-bi.md`)
- **Focus:** Data Visualization & Metric Architecture.
- **Design Elements:**
  - Hero KPI metrics grid (e.g., `ARR: $4.2M (+18%)`, `Churn Rate: 2.1% (-0.5%)`).
  - High-resolution dashboard screenshot spotlights.
  - Interactive preview tabs and direct links to live Tableau/PowerBI instances.

### 4.4 Project 3: Pricing A/B Test (`docs/projects/pricing-ab-test.md`)
- **Focus:** Experimentation & ROI Measurement.
- **Design Elements:**
  - Hypothesis formulation callout.
  - Statistical significance breakdown table (p-values, conversion lift, confidence intervals).
  - Embedded Mermaid.js diagram illustrating user conversion funnels.

---

## 5. Setup & Development Workflow

1. **Environment Setup:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Local Preview:**
   ```bash
   mkdocs serve
   ```
3. **Production Build:**
   ```bash
   mkdocs build --strict
   ```
4. **Deploy to GitHub Pages:**
   ```bash
   mkdocs gh-deploy
   ```
