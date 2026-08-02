import glob
import os
import yaml

def define_env(env):
    """
    Custom MkDocs Macros for automatically generating project summaries
    and overview tables from YAML frontmatter in docs/projects/*.md files.
    """
    
    def get_projects_metadata():
        project_dir = env.project_dir
        projects_glob = os.path.join(project_dir, "docs", "projects", "*.md")
        project_files = glob.glob(projects_glob)
        
        projects = []
        for filepath in sorted(project_files):
            filename = os.path.basename(filepath)
            if filename == "index.md":
                continue
            
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    try:
                        meta = yaml.safe_load(parts[1])
                        meta["filename"] = filename
                        projects.append(meta)
                    except Exception as e:
                        pass
        return projects

    @env.macro
    def render_featured_projects(prefix=None):
        projects = get_projects_metadata()
        
        if prefix is None:
            page = env.variables.get("page")
            if page and getattr(page, "url", "").startswith("projects"):
                prefix = ""
            else:
                prefix = "projects/"
        
        cards = []
        for idx, meta in enumerate(projects, 1):
            title = meta.get("title", "Project Case Study")
            filename = meta.get("filename", "")
            problem = meta.get("problem", "")
            solution = meta.get("solution", "")
            results = meta.get("results", meta.get("impact", ""))
            
            rel_path = f"{prefix}{filename}"
            
            card = f"### {idx}. {title}\n"
            if problem:
                card += f"* **Problem:** {problem}\n"
            if solution:
                card += f"* **Solution:** {solution}\n"
            if results:
                card += f"* **Impact:** **{results}**\n"
            card += f"* [Read Full Case Study →]({rel_path})\n"
            cards.append(card)
        
        return "\n".join(cards)

    @env.macro
    def render_projects_table():
        projects = get_projects_metadata()
        rows = []
        for meta in projects:
            title = meta.get("title", "Project Case Study")
            filename = meta.get("filename", "")
            category = meta.get("category", "Analytics")
            tools = meta.get("tools", "")
            impact = meta.get("impact", "")
            
            row = f"| [{title}]({filename}) | {category} | {tools} | **{impact}** |"
            rows.append(row)
        
        header = "| Case Study | Category | Core Tools | Key Result / Impact |\n| :--- | :--- | :--- | :--- |\n"
        return header + "\n".join(rows)
