# Simple Customization Guide: How to Update Your Portfolio

Welcome! This guide is written in plain, simple English to help you edit and customize your portfolio website. **You do not need to be a software developer or write code**—all updates are done by editing plain text files.

---

## 1. How Your Website Works (At a Glance)

Your portfolio site is made up of simple text files called **Markdown files** (`.md`). 
Whenever you change text in a file and save it, your website automatically updates its layout, pages, and menus!

* **Home Page & Bio:** Managed in `docs/about.md` and `docs/index.md`.
* **Projects & Case Studies:** Managed inside the `docs/projects/` folder.
* **Resume & Work History:** Managed in `docs/resume.md` and `docs/assets/resume.pdf`.
* **Site Settings & Colors:** Managed in `mkdocs.yml`.

---

## 2. How to Update Your Bio & Skills

To change your personal bio, strengths, or skills table:

1. Open the file named **`docs/about.md`**.
2. Edit the text using any simple text editor:
   * **To change your bio:** Edit the paragraph under `## Executive Bio`.
   * **To change your core skills:** Edit the bullet points under `## Core Analytical Strengths`.
   * **To change your skills table:** Update the text inside the table under `## Technical & Business Competencies`.
3. Save the file. Your Home page will automatically display your new bio and skills!

---

## 3. How to Edit or Add Case Studies (Projects)

Every case study sits inside the **`docs/projects/`** folder.

### Editing an Existing Project:
Open one of the existing project files (e.g. `docs/projects/ecommerce-churn.md`).

At the very top of each project file, you will see a simple **Header Section** surrounded by `---` lines:

```yaml
---
title: E-Commerce Customer Churn & Retention Analysis
category: Customer Retention
tools: SQL, Python, Cohort Analysis
impact: -4.2% Churn Rate (+$420K ARR)
problem: Monthly user churn increased by 14% over two consecutive quarters.
solution: Conducted RFM segmentation and cohort retention analysis to isolate churn drivers.
results: Reduced annual churn rate by 4.2% and reclaimed $420K in annual recurring revenue.
---
```

Simply change the text inside those quotes:
* **`title`**: The name of your project.
* **`tools`**: Tools you used (e.g. SQL, Tableau, Python, Power BI).
* **`impact`**: A quick 1-line result badge.
* **`problem`**: A short summary of the business problem.
* **`solution`**: What you did to solve it.
* **`results`**: The final positive result.

Below the `---` lines, you can write the full narrative story of your project in plain text using normal headings (`#`, `##`) and bullet points (`*`).

### Adding a BRAND NEW Project:
1. Create a new file in `docs/projects/` (for example: `docs/projects/my-new-analysis.md`).
2. Copy the top Header Section (`---` block) from an existing project into your new file.
3. Fill in your project details.
4. Save the file. 

✨ **Magic Feature:** The moment you save a new project file, your portfolio will **automatically list it on your Home Page and All Projects page!** You do not need to manually add links.

---

## 4. How to Update Your Resume

### To Change Resume Text:
1. Open **`docs/resume.md`**.
2. Update your email, LinkedIn URL, work history, and job titles.

### To Replace Your PDF Resume:
1. Save your updated PDF resume on your computer as **`resume.pdf`**.
2. Replace the file inside **`docs/assets/resume.pdf`** with your new file.

---

## 5. How to Change Theme Colors

If you want to change the color scheme of your site:

1. Open **`mkdocs.yml`**.
2. Look for `primary:` and `accent:` under `palette:`:
   ```yaml
   primary: indigo
   accent: teal
   ```
3. You can replace `indigo` or `teal` with colors like:
   `blue`, `deep purple`, `cyan`, `teal`, `green`, `amber`, `deep orange`.

---

## 6. How to Preview Your Website on Your Computer

To see your changes live in your web browser before publishing:

1. Open your computer terminal app.
2. Navigate to your project folder and type:
   ```bash
   python3 -m mkdocs build
   ```
   ```bash
   python3 -m mkdocs serve
   ```
3. Open your browser and go to: `http://127.0.0.1:8000`
4. As you save files, your browser will update instantly!

---

## 7. Summary Cheat Sheet

| I want to change... | File to open |
| :--- | :--- |
| My Bio, Skills, and Mindset | `docs/about.md` |
| Case Study Stories & Results | `docs/projects/*.md` |
| Add a New Case Study | Create a new file in `docs/projects/` |
| My Resume Text & Work Experience | `docs/resume.md` |
| My PDF Resume Download | Replace `docs/assets/resume.pdf` |
| Website Name or Colors | `mkdocs.yml` |
