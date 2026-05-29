---
layout: splash
title: "Projects"
permalink: /projects/
classes: wide
---

<h3 class="portfolio-title">Projects</h3>
<p class="portfolio-subtitle">The projects I've been working on</p>

<div class="project-grid">
  {% assign sorted_projects = site.projects | sort: "date" | reverse %}
  {% for project in sorted_projects %}
    <div class="project-card">
      {% if project.header.teaser %}
        <a href="{{ project.url }}" class="card-image-link">
          <div class="card-image" style="background-image: url('{{ project.header.teaser }}');">
            <div class="card-overlay">
              <p>{{ project.excerpt | strip_html }}</p>
            </div>
          </div>
        </a>
      {% endif %}
      <div class="card-body">
        <h3>{{ project.title }}</h3>
        <a href="{{ project.url }}" class="view-link">View Project</a>
      </div>
    </div>
  {% endfor %}
</div>

<link rel="stylesheet" href="/assets/css/projects_test.css">
