---
layout: default
title: "Nexo: Novedades del panorama Sci-fi"
permalink: /nexo/
---

<div class="container" style="padding-top: 30px; padding-bottom: 60px;">

  <div class="section-header" style="text-align: center; margin-bottom: 40px;">
    <h1 class="section-title" style="color: #00aeef; font-size: 2.2rem; margin-bottom: 5px;">Nexo: Novedades del panorama Sci-fi</h1>
    <p style="color: var(--muted-text, #64748b); font-size: 1.05rem;">Enlaces de interés, noticias y mis comentarios personales.</p>
  </div>

  <!-- CONTENEDOR PRINCIPAL DE NEXOS -->
  <div class="nexo-feed" style="margin: 0 auto;">
    {% assign nexos_ordenados = site.nexos | sort: 'date' | reverse %}
    {% for item in nexos_ordenados %}
      <article class="nexo-card">
        
        <!-- CABECERA: Fuente / Categoría + Fecha -->
        <div class="nexo-meta">
          {% if item.source %}
            <span class="nexo-badge">{{ item.source }}</span>
          {% else %}
            <span class="nexo-badge">Sci-Fi</span>
          {% endif %}
          
          <time class="nexo-date">{{ item.date | date: "%d %b %Y" }}</time>
        </div>

        <!-- TITULAR CON ENLACE EXTERNO -->
        <h2 class="nexo-title">
          <a href="{{ item.link_url }}" target="_blank" rel="noopener noreferrer">
            {{ item.title }}
            <svg class="external-icon" viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round">
              <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
              <polyline points="15 3 21 3 21 9"></polyline>
              <line x1="10" y1="14" x2="21" y2="3"></line>
            </svg>
          </a>
        </h2>
        
        <!-- BLOQUE DE COMENTARIO / MI OPINIÓN -->
        <div class="nexo-opinion">
          <div class="nexo-author-tag">Mi opinión:</div>
          <div class="nexo-comment-body">
            {{ item.content | markdownify }}
          </div>
        </div>

      </article>
    {% endfor %}
  </div>

</div>

<!-- ESTILOS ESTRUCTURALES DE LA SECCIÓN NEXO -->
<style>
  .nexo-feed {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }

  /* Tarjeta Principal */
  .nexo-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #00aeef; /* Acento con tu azul principal */
    border-radius: 8px;
    padding: 1.5rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }

  .nexo-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.07);
  }

  /* Meta información arriba */
  .nexo-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.75rem;
  }

  .nexo-badge {
    background-color: #e0f2fe;
    color: #0369a1;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 4px;
    text-transform: uppercase;
    font-size: 0.75rem;
    letter-spacing: 0.5px;
  }

  .nexo-date {
    color: #94a3b8;
    font-size: 0.85rem;
    font-weight: 500;
  }

  /* Titular de la Noticia */
  .nexo-title {
    margin: 0 0 1rem 0;
    font-size: 1.3rem;
    font-weight: 700;
    line-height: 1.4;
  }

  .nexo-title a {
    color: #0f172a;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: color 0.2s ease;
  }

  .nexo-title a:hover {
    color: #00aeef;
  }

  .external-icon {
    color: #00aeef;
    flex-shrink: 0;
    display: inline-block;
  }

  /* Bloque de Opinión del Autor */
  .nexo-opinion {
    background-color: #f8fafc;
    border-radius: 6px;
    padding: 1rem 1.25rem;
    border: 1px solid #f1f5f9;
  }

  .nexo-author-tag {
    font-size: 0.8rem;
    font-weight: 700;
    color: #00aeef;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.3rem;
  }

  .nexo-comment-body {
    color: #334155;
    font-size: 0.98rem;
    line-height: 1.6;
  }

  .nexo-comment-body p {
    margin: 0 0 0.5rem 0;
  }

  .nexo-comment-body p:last-child {
    margin-bottom: 0;
  }
</style>
