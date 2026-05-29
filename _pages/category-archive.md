---
layout: single
permalink: /categories/
title: "Categories"
author_profile: true
---

{% assign rawcats = "" %}
{% for project in site.projects %}
  {% assign tcats = project.categories | join:'|' | append:'|' %}
  {% assign rawcats = rawcats | append:tcats %}
{% endfor %}

{% assign categories = rawcats | split:'|' | uniq | sort %}

<div class="category-list">
  {% for category in categories %}
    {% if category != "" %}
      {% assign projects = site.projects | where_exp: "project", "project.categories contains category" %}
      <h3 id="{{ category | slugify }}">
        <a href="{{ site.baseurl }}/categories/#{{ category | slugify }}">{{ category }}</a>
      </h3>
      <ul>
        {% for project in projects %}
          <li><a href="{{ project.url }}">{{ project.title }}</a></li>
        {% endfor %}
      </ul>
    {% endif %}
  {% endfor %}
</div>

<style>
  .category-list h3 {
    margin-top: 2em;
    margin-bottom: 0.5em;
    border-bottom: 2px solid #00adb5;
    padding-bottom: 0.3em;
  }
  .category-list ul {
    list-style: none;
    padding-left: 0;
  }
  .category-list li {
    margin: 0.3em 0;
  }
  .category-list a {
    text-decoration: none;
  }
  .category-list a:hover {
    text-decoration: underline;
  }
</style>
