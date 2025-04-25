---
title: "Resume"
permalink: /resume/
layout: single
toc: true
toc_sticky: true
toc_level: 2
---

## Contact Information

📍 Monroe, WA  
📞 +1 425-420-7223  
📧 [nicklee0101@gmail.com](mailto:nicklee0101@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/leen01) • [Portfolio](https://leen01.github.io/portfolio)
<br>
<a href="/assets/Nicholas-Lee-resume.pdf" download class="btn btn--primary">Download Resume (PDF)</a>

---


## 🧠 Summary

Innovative and collaborative with a diverse skillset in molecular biology and data science. Proven success driving product development through rigorous experimentation, stakeholder engagement, and effective cross-department collaboration. Adept in FAIR data practices, scientific computing, and building scalable data tools for research and clinical applications.

---

## 💼 Work Experience

{% for job in site.data.resume.work %}
<div class="flex-split">
  <div class="left">
    <b>{{ job.role }}</b><br>
    <i>{{ job.company }}</i>
  </div>
  <div class="right">
    {{ job.dates }}<br>
    <i>{{ job.location }}</i>
  </div>
</div>

<ul>
  {% for point in job.bullets %}
  <li>{{ point }}</li>
  {% endfor %}
</ul>
{% endfor %}

---

## 🎓 Education

<div class="flex-split">
  <div class="left">
    <strong>M.S. in Information and Data Science</strong><br>
    <i>University of California, Berkeley</i>
  </div>
  <div class="right">
    <small> (Jan 2022 – Aug 2023)</small>
  </div>
</div>

<div class="flex-split">
  <div class="left">
    <strong>B.S. in Cellular and Molecular Biology</strong><br>
    <i>Seattle Pacific University</i>
  </div>
  <div class="right">
    <small> (Sep 2015 – Mar 2019)</small>
  </div>
</div>

---

## 🛠 Skills

**Analytics**
- A/B Experimental Design, Hypothesis Testing, Data Visualization, EDA

**Data Engineering**
- Data Wrangling, FAIR Principles, Data Governance, SQL, PostgreSQL, Ontologies

**Programming & Tools**
- Python, R, Docker, AWS, Bash, Power BI, Tableau, Shiny, Git, RESTful APIs

**Pharmaceutical Domain**
- Drug Development, Benchling, ELNs, GLP, HIPAA, FDA 21 CFR Part 11

**Soft Skills**
- Cross-department Collaboration, Initiative, Communication, Teamwork

---

## 🧾 Certifications

- **AWS Certified Cloud Practitioner** (Nov 2023 – Nov 2026)

---

## Volunteering & Leadership

**Seattle Children’s Hospital** – *Child Life Volunteer* (2016 – 2017)  
- Provided companionship and a safe environment for children undergoing care.

**Evergreen Health** – *Front Desk Receptionist* (2013 – 2016)  
- Assisted with check-in, patient navigation, and HIPAA-compliant data entry.

<link rel="stylesheet" href="/assets/css/projects.css">