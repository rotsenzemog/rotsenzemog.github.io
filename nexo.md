---
layout: default
title: "Nexo: Novedades del panorama Csi-fi"
permalink: /nexo/
---

<div class="container" style="padding-top: 20px; padding-bottom: 60px;">

  <div class="section-header" style="text-align: center; margin-bottom: 40px;">
    <h1 class="section-title">Nexo: Novedades del panorama Csi-fi</h1>
    <p style="color: var(--muted-text); margin-top: 8px;">Enlaces de interés y mis comentarios.</p>
  </div>

  <!-- CONTENEDOR DE LA LISTA EN 1 SOLA COLUMNA -->
  <div class="news-feed">
    {% assign noticias_ordenadas = site.noticias | sort: 'date' | reverse %}
    {% for item in noticias_ordenadas %}
      <article class="news-item">
        
        <!-- COLUMNA IZQUIERDA: Imagen con enlace -->
        <div class="news-col-left">
          <a href="{{ item.link_url }}" target="_blank" rel="noopener noreferrer">
            <img src="{{ item.image_url }}" alt="{{ item.title }}" class="news-img">
          </a>
        </div>

        <!-- COLUMNA CENTRO: Título + Comentario -->
        <div class="news-col-center">
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
