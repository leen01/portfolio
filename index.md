---
layout: splash
classes: wide
feature_row:
  - image_path: /assets/img/projects/mimic_iv_project_banner.svg
    title: "MIMIC-IV RWE Study"
    excerpt: "End-to-end RWE pipeline on ICU sepsis — Snowflake, dbt, propensity score matching, Cox survival analysis, and SHAP interpretability."
    url: "/projects/2026-04-17-mimic-iv"
    btn_label: "Read More"
    btn_class: "btn--primary"
  - image_path: /assets/img/projects/therapeutic-accelerator.png
    title: "Therapeutic Accelerator"
    excerpt: "Accelerating therapeutic discoveries with automated literature pipelines and SQL-backed analytics."
    url: "/projects/2023-08-01-therapeutic-accelerator"
    btn_label: "Read More"
    btn_class: "btn--inverse"
  - image_path: /assets/img/projects/ehr_classification_banner.svg
    title: "Electronic Health Records Classification"
    excerpt: "Machine learning classification of EHR records as in-patient vs out-patient based on lab results and vitals."
    url: "/projects/2023-11-01-electronic-health-records"
    btn_label: "Read More"
    btn_class: "btn--inverse"
---

<div class="hero-section">
  <div class="hero-avatar">
    <img src="/assets/img/avatar.jpg" alt="Nick Lee" class="hero-avatar-img">
  </div>
  <h1 class="hero-name">Nick Lee</h1>
  <p class="hero-tagline">Senior Data Scientist | Clinical Data Engineering &amp; Real-World Evidence</p>
  <div class="hero-ctas">
    <a href="/projects/" class="btn btn--primary btn--large">View Projects</a>
    <a href="/assets/Nicholas-Lee-resume.pdf" class="btn btn--info btn--large" download>Download Resume</a>
    <a href="https://linkedin.com/in/leen01" class="btn btn--inverse btn--large" target="_blank" rel="noopener">Connect on LinkedIn</a>
  </div>
</div>

---

I'm a **data engineer and scientist in life sciences** with a background spanning molecular biology, data engineering, and applied machine learning.

I build end-to-end data workflows — from raw EHR and claims tables through dbt-modeled pipelines to survival models and causal inference analyses — using Python, SQL, Snowflake, dbt, and AWS. My molecular biology background (BS + 4 years bench experience) gives me the domain fluency to work directly with clinical and translational teams, not just beside them.

I'm focused on roles where rigorous data engineering and data science accelerate clinical development — whether that's designing RWE studies, building patient cohort infrastructure, or modeling treatment outcomes at scale.

---

## Skills

<div class="skills-section">
  <div class="skills-group">
    <h3>Data Engineering</h3>
    <div class="skills-grid">
      <div class="skill-tile"><span class="skill-icon">🐍</span><span class="skill-label">Python</span></div>
      <div class="skill-tile"><span class="skill-icon">🗄️</span><span class="skill-label">SQL</span></div>
      <div class="skill-tile"><span class="skill-icon">❄️</span><span class="skill-label">Snowflake</span></div>
      <div class="skill-tile"><span class="skill-icon">🔧</span><span class="skill-label">dbt</span></div>
      <div class="skill-tile"><span class="skill-icon">☁️</span><span class="skill-label">AWS</span></div>
      <div class="skill-tile"><span class="skill-icon">🐳</span><span class="skill-label">Docker</span></div>
    </div>
  </div>
  <div class="skills-group">
    <h3>Analytics &amp; ML</h3>
    <div class="skills-grid">
      <div class="skill-tile"><span class="skill-icon">🤖</span><span class="skill-label">scikit-learn</span></div>
      <div class="skill-tile"><span class="skill-icon">📈</span><span class="skill-label">lifelines</span></div>
      <div class="skill-tile"><span class="skill-icon">🔍</span><span class="skill-label">SHAP</span></div>
    </div>
  </div>
</div>

---

## Featured Projects
{% include feature_row %}

---

## Let's Work Together

I'm currently exploring senior data science and clinical data engineering roles in biopharma, RWE, and clinical development.

<div class="cta-buttons">
  <a href="mailto:nicklee0101@gmail.com" class="btn btn--primary">Email Me</a>
  <a href="https://linkedin.com/in/leen01" class="btn btn--inverse" target="_blank" rel="noopener">LinkedIn</a>
</div>

<style>
.hero-section {
  text-align: center;
  padding: 3rem 1rem 2rem;
}
.hero-avatar-img {
  max-width: 200px;
  height: auto;
  border-radius: 50%;
  border: 4px solid #005f73;
  margin-bottom: 1rem;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.hero-name {
  font-size: 2.5rem;
  margin: 0.25rem 0;
  font-weight: 700;
}
.hero-tagline {
  font-size: 1.2rem;
  color: #888;
  margin-bottom: 1.5rem;
}
.hero-ctas {
  display: flex;
  gap: 0.75rem;
  justify-content: center;
  flex-wrap: wrap;
}
.skills-section {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
  margin: 1rem 0 1.5rem;
}
.skills-group {
  flex: 1;
  min-width: 260px;
}
.skills-group h3 {
  margin-bottom: 0.75rem;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #005f73;
  border-bottom: 1px solid #d0dfe3;
  padding-bottom: 0.4rem;
}
.skills-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
}
.skill-tile {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  background: #2e3444;
  border: 1px solid rgba(0, 173, 181, 0.45);
  border-radius: 8px;
  padding: 0.35rem 0.7rem;
  font-size: 0.875rem;
  color: #eaeaea;
}
.skill-label {
  font-weight: 500;
  color: #eaeaea;
}
.cta-buttons {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
  margin-top: 0.5rem;
}
</style>
