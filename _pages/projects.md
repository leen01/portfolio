---
layout: single
title: "Projects"
permalink: /projects/
entries_layout: grid
classes: wide
---

<h1 class="portfolio-title">PORTFOLIO</h1>
<p class="portfolio-subtitle">A glimpse of the projects I've been working on</p>

<div id="portfolio-filters" class="filters">
  <button data-filter="all" class="filter-btn active">Show all</button>
  <button data-filter="nlp" class="filter-btn">NLP</button>
  <button data-filter="dashboard" class="filter-btn">Dashboard</button>
  <button data-filter="dataviz" class="filter-btn">Dataviz</button>
  <button data-filter="ml" class="filter-btn">ML</button>
</div>

<div class="portfolio-grid">
  {% for project in site.portfolio %}
  <div class="project-item" data-tags="{{ project.tags | join: ' ' }}">
    <img src="{{ project.header.overlay_image }}" alt="{{ project.title }}">
    <h3>{{ project.title }}</h3>
    <p>{{ project.excerpt }}</p>
    <a href="{{ project.url }}" class="project-link">View Project</a>
  </div>
  {% endfor %}
</div>

<script src="/assets/js/portfolio-filters.js"></script>
<link rel="stylesheet" href="/assets/css/portfolio.css">