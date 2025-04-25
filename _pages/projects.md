---
layout: splash
title: "Projects"
permalink: /projects/
classes: wide
---

<h3 class="portfolio-title">Projects</h3>
<p class="portfolio-subtitle">The projects I've been working on</p>

<div class="portfolio-grid">
  {% for project in site.projects %}
  <a href="{{ project.url }}" style="text-decoration: none;">
    <div class="project-item" data-tags="{{ project.tags | join: ' ' }}">
      <img src="{{ project.thumbnail }}" alt="{{ project.title }}" class="thumbnail" >
      <h3>{{ project.title }}</h3>
      <p>{{ project.excerpt }}</p>
      <p class="project-link">View Project</p>
    </div>
  </a>
  {% endfor %}
</div>

<script src="/assets/js/projects-filters.js"></script>
<link rel="stylesheet" href="/assets/css/projects.css">