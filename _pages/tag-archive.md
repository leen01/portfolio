---
layout: single
permalink: /tags/
title: "Tags"
author_profile: true
---

{% assign rawtags = "" %}
{% for project in site.projects %}
  {% assign ttags = project.tags | join:'|' | append:'|' %}
  {% assign rawtags = rawtags | append:ttags %}
{% endfor %}

{% assign tags = rawtags | split:'|' | uniq | sort %}

<div class="tag-list">
  {% for tag in tags %}
    {% if tag != "" %}
      {% assign projects = site.projects | where_exp: "project", "project.tags contains tag" %}
      <h3 id="{{ tag | slugify }}">
        <a href="{{ site.baseurl }}/tags/#{{ tag | slugify }}">{{ tag }}</a>
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
  .tag-list h3 {
    margin-top: 2em;
    margin-bottom: 0.5em;
    border-bottom: 2px solid #00adb5;
    padding-bottom: 0.3em;
  }
  .tag-list ul {
    list-style: none;
    padding-left: 0;
  }
  .tag-list li {
    margin: 0.3em 0;
  }
  .tag-list a {
    text-decoration: none;
  }
  .tag-list a:hover {
    text-decoration: underline;
  }
</style>
