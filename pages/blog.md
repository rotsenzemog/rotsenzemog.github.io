---
layout: default
title: "Blog & Relatos"
permalink: /blog/
---

<div class="container" style="padding-top: 40px; padding-bottom: 60px;">
  <div class="section-header">
    <h1 class="section-title">Todos los relatos y publicaciones</h1>
    <p style="color: var(--muted-text); margin-top: 8px;">Explora el catálogo completo de obras, reseñas y artículos.</p>
  </div>

  <div class="grid-3">
    {% for post in paginator.posts %}
    <article class="card">
      <a href="{{ post.url | relative_url }}">
        <img src="{{ post.image | relative_url }}" class="card-img" alt="{{ post.title }}">
      </a>
      <span class="category-tag">{{ post.category }}</span>
      <h2 class="card-title" style="font-size: 1.25rem;">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h2>
      <p class="card-excerpt">{{ post.excerpt | strip_html | truncatewords: 15 }}</p>
      <small style="color: var(--muted-text);">{{ post.date | date: "%d %b %Y" }}</small>
    </article>
    {% endfor %}
  </div>

  <!-- Controles de Paginación -->
  {% if paginator.total_pages > 1 %}
  <div class="pagination" style="margin-top: 50px; display: flex; justify-content: center; gap: 15px; align-items: center;">
    {% if paginator.previous_page %}
      <a href="{{ paginator.previous_page_path | relative_url }}" class="btn-more">&laquo; Anteriores</a>
    {% endif %}

    <span style="color: var(--muted-text);">Página {{ paginator.page }} de {{ paginator.total_pages }}</span>

    {% if paginator.next_page %}
      <a href="{{ paginator.next_page_path | relative_url }}" class="btn-more">Siguientes &raquo;</a>
    {% endif %}
  </div>
  {% endif %}
</div>
