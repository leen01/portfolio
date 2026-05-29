#!/usr/bin/env python3
# Dependencies: requests, python-frontmatter, PyYAML

import os
import re
import sys
import requests
import frontmatter
import yaml
from pathlib import Path

PROJECTS_DIR = Path("_projects")
DATA_DIR = Path("_data")
OUTPUT_FILE = DATA_DIR / "readmes.yml"

SECTION_HEADERS = ["results", "methods", "overview", "usage", "installation"]

GITHUB_API = "https://api.github.com"


def get_headers():
    headers = {"Accept": "application/vnd.github.raw+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def fetch_readme(repo_slug):
    url = f"{GITHUB_API}/repos/{repo_slug}/readme"
    try:
        resp = requests.get(url, headers=get_headers(), timeout=15)
    except requests.RequestException as exc:
        return None, f"request error: {exc}"
    if resp.status_code == 404:
        return None, "404 not found"
    if resp.status_code == 403:
        return None, "403 rate limited"
    if resp.status_code != 200:
        return None, f"HTTP {resp.status_code}"
    return resp.text, None


def extract_sections(content):
    sections = {h: "" for h in SECTION_HEADERS}
    pattern = re.compile(r"^##\s+(.+)$", re.MULTILINE)
    matches = list(pattern.finditer(content))

    for i, match in enumerate(matches):
        header_text = match.group(1).strip().lower()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        section_body = content[start:end].strip()

        for key in SECTION_HEADERS:
            if key in header_text:
                sections[key] = section_body
                break

    return sections


def main():
    DATA_DIR.mkdir(exist_ok=True)

    results = {}
    project_files = sorted(PROJECTS_DIR.glob("*.md"))

    if not project_files:
        print("No project files found in _projects/")
        sys.exit(1)

    for filepath in project_files:
        post = frontmatter.load(filepath)
        repo_slug = post.get("github_repo")
        if not repo_slug:
            continue

        repo_key = repo_slug.replace("/", "__")
        print(f"Fetching README for {repo_slug}...", end=" ", flush=True)

        readme_content, error = fetch_readme(repo_slug)

        if error:
            print(f"ERROR: {error}")
            results[repo_key] = {"full": "", "sections": {h: "" for h in SECTION_HEADERS}}
            continue

        sections = extract_sections(readme_content)
        found = [k for k, v in sections.items() if v]
        section_summary = ", ".join(found) if found else "none"
        print(f"OK ({len(found)} sections: {section_summary})")

        results[repo_key] = {
            "full": readme_content,
            "sections": sections,
        }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        yaml.dump(results, f, allow_unicode=True, sort_keys=True, default_flow_style=False)

    print(f"\nWrote {len(results)} entries to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
