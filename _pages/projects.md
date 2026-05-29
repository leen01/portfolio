---
layout: splash
title: "Projects"
permalink: /projects/
classes: wide
---

<h3 class="portfolio-title">Projects</h3>
<p class="portfolio-subtitle">Real-world pipelines, clinical data science, and applied machine learning</p>

<div class="project-grid">
  {% assign sorted_projects = site.projects | sort: "date" | reverse %}
  {% for project in sorted_projects %}
    <div class="project-card">
      {% if project.header.image %}
        <a href="{{ project.url }}" class="card-image-link">
          <div class="card-image" style="background-image: url('{{ project.header.image }}');">
            <div class="card-overlay">
              <p>{{ project.excerpt | strip_html }}</p>
            </div>
          </div>
        </a>
      {% elsif project.header.teaser %}
        <a href="{{ project.url }}" class="card-image-link">
          <div class="card-image" style="background-image: url('{{ project.header.teaser }}');">
            <div class="card-overlay">
              <p>{{ project.excerpt | strip_html }}</p>
            </div>
          </div>
        </a>
      {% endif %}
      <div class="card-body">
        {% if project.project_category %}
          <span class="project-category-label">{{ project.project_category }}</span>
        {% endif %}
        <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
        {% if project.subtitle %}
          <p class="project-subtitle-text">{{ project.subtitle }}</p>
        {% endif %}
        {% if project.tags %}
          <div class="project-tags">
            {% for tag in project.tags %}
              <span class="tag">{{ tag }}</span>
            {% endfor %}
          </div>
        {% endif %}
        <a href="{{ project.url }}" class="view-link">View Project →</a>
      </div>
    </div>
  {% endfor %}
</div>

<link rel="stylesheet" href="/assets/css/projects.css">
<link rel="stylesheet" href="/assets/css/projects_test.css">
