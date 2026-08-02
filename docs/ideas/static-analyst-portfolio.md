# Static Business / Data Analyst Portfolio

## Problem Statement
> **How might we build a simple, lightning-fast static portfolio website that showcases a Business/Data Analyst's unique project stories in a flexible, free-form format while proving technical rigor and quantifiable business impact?**

---

## Recommended Direction
A clean, high-impact single-page static website using modern HTML, vanilla CSS, and minimal JS. The website features:
1. **About Me Section:** Crisp executive bio, analytical mindset, core technical skills (SQL, Python, Tableau/Power BI, A/B testing), and direct contact/resume links.
2. **Free-Form Projects Showcase:** Rather than forcing every project into a rigid, repetitive card template, each project is crafted with a custom layout suited to its specific story:
   - *Project 1 (Deep-Dive Case Study Layout):* Problem narrative, inline SQL query highlights, and key business recommendations.
   - *Project 2 (Visual Dashboard Showcase):* Dashboard screenshot spotlights with key metric callouts and live links.
   - *Project 3 (Experimentation / A/B Test Story):* Hypothesis, statistical results breakdown, and business ROI summary.
3. **Clean Contact Footer:** Quick links for recruiters to get in touch or download your resume.

---

## Key Assumptions to Validate
- [ ] **Scannability:** Free-form project layouts must remain easy for recruiters to scan within 30 seconds (using clear headings and bolded metrics).
- [ ] **Performance:** High-resolution charts and visuals load instantly under 0.5 seconds without framework overhead.
- [ ] **Mobile Responsiveness:** Custom free-form project layouts adapt fluidly to mobile screens.

---

## MVP Scope

| Section | Content & Functionality |
| :--- | :--- |
| **Sticky Navigation** | Logo/Name, `About`, `Projects`, `Contact`, and a highlighted `[Download Resume]` button. |
| **About Me (Hero)** | Executive summary, core competencies (SQL, Python, A/B Testing, BI Tools), and direct LinkedIn/GitHub links. |
| **Project 1 (Free-Form)** | *Example: E-Commerce Churn Analysis* — Story-first layout featuring business problem, SQL snippets, and churn reduction recommendations. |
| **Project 2 (Free-Form)** | *Example: Executive BI Dashboard* — Visual-first layout with interactive preview triggers, key KPI cards, and live Tableau/PowerBI links. |
| **Project 3 (Free-Form)** | *Example: Pricing A/B Test* — Experiment-first layout featuring hypothesis, metric conversion lift, and statistical summary. |
| **Footer / Contact** | Simple, clean footer with email link, LinkedIn, GitHub, and copyright notice. |

---

## Not Doing (and Why)
- **Rigid Uniform Project Cards:** Not forcing projects into identical cookie-cutter cards. Each project gets a tailored layout that fits its specific data narrative.
- **Heavy Frontend Frameworks or Backends:** No React/Next.js overhead or server setup. Pure static HTML/CSS/JS for 0-cost hosting, instant page load, and simple maintenance.
- **Generic / Toy Datasets:** Avoiding basic Iris/Titanic projects. Focus strictly on realistic business scenarios (Churn, Funnel Optimization, A/B Testing).

---

## Open Questions before Building
- What specific 2–3 projects would you like to feature first on the site?
- Do you have a preferred color palette or typography preference, or should we use a polished dark-mode palette with modern Google Fonts (e.g., Inter/Outfit)?
