---
layout: single
title: "Projects"
permalink: /projects/
---

{% for post in site.portfolio %}
  - ### [{{ post.title }}]({{ post.url }})
    {{ post.excerpt }}
{% endfor %}
