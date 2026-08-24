---
layout: default
title: "Lore"
permalink: /lore/
---

<div class="yo-hero">
  <h1 class="yo-title">Lore & Worldbuilding</h1>
  <p class="yo-subtitle">Archivos, tecnologías, conceptos y gráficos del universo de ficción.</p>
</div>

<!-- GRID DINÁMICO TIPO MASAICO -->
<div class="yo-grid" id="loreGrid">
  {% assign sorted_lore = site.lore | reverse %}
  {% for item in sorted_lore %}
    
    {% if item.card_type == 'photo-card' %}
      <div class="yo-card photo-card lore-item">
        <div class="photo-wrapper">
          <img src="{{ item.image | relative_url }}" alt="{{ item.title }}" onerror="this.src='https://picsum.photos/400/500?grayscale'">
        </div>
        {% if item.caption %}
          <span class="photo-caption">{{ item.caption }}</span>
        {% endif %}
      </div>

    {% elsif item.card_type == 'quote-card' %}
      <div class="yo-card quote-card lore-item">
        <blockquote>"{{ item.quote | default: item.content }}"</blockquote>
      </div>

    {% else %}
      <div class="yo-card {{ item.card_type }} lore-item">
        <h3>{{ item.title }}</h3>
        {{ item.content }}
      </div>
    {% endif %}

  {% endfor %}
</div>

<!-- CONTROLES DE PAGINACIÓN -->
<div class="pagination-container" style="margin-top: 40px; text-align: center;">
  <button id="prevBtn" onclick="changePage(-1)" class="btn-pagination">&laquo; Anteriores</button>
  <span id="pageIndicator" style="color: var(--muted-text); font-weight: 600; margin: 0 15px;"></span>
  <button id="nextBtn" onclick="changePage(1)" class="btn-pagination">Siguientes &raquo;</button>
</div>

<!-- SCRIPT DE PAGINACIÓN FLUIDA -->
<script>
  const ITEMS_PER_PAGE = 9; // Cantidad de bloques por página
  let currentPage = 1;
  const allItems = Array.from(document.querySelectorAll('.lore-item'));
  const grid = document.getElementById('loreGrid');

  function updatePagination() {
    const totalPages = Math.ceil(allItems.length / ITEMS_PER_PAGE) || 1;
    if (currentPage > totalPages) currentPage = totalPages;
    if (currentPage < 1) currentPage = 1;

    allItems.forEach((item, index) => {
      const start = (currentPage - 1) * ITEMS_PER_PAGE;
      const end = start + ITEMS_PER_PAGE;
      
      if (index >= start && index < end) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });

    document.getElementById('pageIndicator').innerText = `Página ${currentPage} de ${totalPages}`;
    document.getElementById('prevBtn').disabled = (currentPage === 1);
    document.getElementById('nextBtn').disabled = (currentPage === totalPages);
  }

  function changePage(direction) {
    currentPage += direction;
    updatePagination();
    window.scrollTo({ top: grid.offsetTop - 100, behavior: 'smooth' });
  }

  document.addEventListener("DOMContentLoaded", () => {
    updatePagination();
  });
</script>
