---
layout: default
title: "Nexo: Novedades del panorama Sci-fi"
permalink: /nexo/
---

<div class="container" style="padding-top: 20px; padding-bottom: 60px;">

  <div class="section-header" style="text-align: center; margin-bottom: 40px;">
    <h1 class="section-title">Nexo: Novedades del panorama Sci-fi</h1>
    <p style="color: var(--muted-text); margin-top: 8px;">Enlaces de interés y mis comentarios.</p>
  </div>

  <!-- CONTENEDOR DE LA LISTA EN 1 COLUMNA -->
  <div class="news-feed">
    {% assign nexos_ordenados = site.nexos | sort: 'date' | reverse %}
    {% for item in nexos_ordenados %}
      <article class="news-item">
        
        <!-- COLUMNA IZQUIERDA: Imagen o Favicon de respaldo -->
        <div class="news-col-left">
          <a href="{{ item.link_url }}" target="_blank" rel="noopener noreferrer">
            {% if item.image_url and item.image_url != "" %}
              <!-- Imagen personalizada o externa con bypass anti-hotlink -->
              <img src="{{ item.image_url }}" alt="{{ item.title }}" class="news-img" referrerpolicy="no-referrer">
            {% else %}
              <!-- Respaldo: Muestra el logo/favicon del sitio externo automáticamente -->
              <div class="news-favicon-box">
                <img src="https://www.google.com/s2/favicons?domain={{ item.link_url }}&sz=128" alt="Fuente" class="news-favicon-img">
              </div>
            {% endif %}
          </a>
        </div>

        <!-- COLUMNA CENTRO: Fuente + Título + Comentario -->
        <div class="news-col-center">
          
          {% if item.source %}
            <span class="news-source-badge">{{ item.source }}</span>
          {% endif %}

          <h2 class="news-title">
            <a href="{{ item.link_url }}" target="_blank" rel="noopener noreferrer">
              {{ item.title }} <span class="external-icon">↗</span>
            </a>
          </h2>
          
          <div class="news-comment">
            {{ item.content | markdownify }}
          </div>
        </div>

        <!-- COLUMNA DERECHA: Fecha -->
        <div class="news-col-right">
          <time class="news-date">{{ item.date | date: "%d %b %Y" }}</time>
        </div>

      </article>
    {% endfor %}
  </div>

</div>
