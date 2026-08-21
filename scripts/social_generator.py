import os
import glob
import json
import subprocess
import frontmatter
import google.generativeai as genai
import requests

GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
SITE_URL = os.environ.get("SITE_URL", "https://rotsenzemog.github.io/panel.html")

genai.configure(api_key=GEMINI_KEY)

def get_latest_post_info():
    list_of_files = glob.glob('_posts/*.md') + glob.glob('_posts/*.markdown')
    if not list_of_files:
        return None, False
    
    latest_file = max(list_of_files, key=os.path.getctime)
    
    # Verificamos si el archivo es NUEVO o una EDICIÓN mediante Git
    try:
        res = subprocess.run(['git', 'log', '--oneline', latest_file], capture_output=True, text=True)
        commits_count = len(res.stdout.strip().split('\n'))
        is_new_file = commits_count <= 1
    except Exception:
        is_new_file = True

    return latest_file, is_new_file

def generate_social_copys(post_content, post_title):
    model = genai.GenerativeModel('gemini-3.6-flash')
    prompt = f"""
    Eres Social Media Manager. Basándote en el artículo "{post_title}", genera:
    1. Hilo de 3 tuits para X.
    2. Post para Facebook/LinkedIn.
    3. Breve boletín para Substack.

    Responde ESTRICTAMENTE en formato JSON válido con la siguiente estructura (sin Markdown alrededor del JSON):
    {{
      "twitter": "Texto del hilo para X aquí",
      "facebook": "Texto para Facebook aquí",
      "substack": "Texto para Substack aquí"
    }}

    Contenido del artículo:
    {post_content[:3500]}
    """
    response = model.generate_content(prompt)
    
    # Limpiar formato por si Gemini incluye bloques de código
    clean_text = response.text.strip().replace('```json', '').replace('```', '')
    return json.loads(clean_text)

def update_web_panel(title, copys_json):
    # Genera/actualiza un archivo HTML interactivo
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Panel de Publicación Social</title>
    <style>
        body {{ font-family: system-ui, sans-serif; background: #0f172a; color: #f8fafc; padding: 20px; max-width: 800px; margin: auto; }}
        .card {{ background: #1e293b; padding: 20px; border-radius: 12px; margin-bottom: 20px; border: 1px solid #334155; }}
        h1 {{ color: #38bdf8; font-size: 1.5rem; }}
        h2 {{ color: #f1f5f9; font-size: 1.1rem; border-bottom: 1px solid #334155; padding-bottom: 8px; }}
        textarea {{ width: 100%; height: 120px; background: #0f172a; color: #f8fafc; border: 1px solid #475569; border-radius: 6px; padding: 10px; box-sizing: border-box; font-family: monospace; }}
        .btn {{ background: #3b82f6; color: white; border: none; padding: 10px 16px; border-radius: 6px; cursor: pointer; font-weight: bold; margin-right: 8px; margin-top: 8px; text-decoration: none; display: inline-block; }}
        .btn-green {{ background: #22c55e; }}
        .btn-gray {{ background: #64748b; }}
    </style>
</head>
<body>
    <h1>🚀 Panel Social: {title}</h1>
    
    <div class="card">
        <h2>🧵 Hilo para X (Twitter)</h2>
        <textarea id="tw">{copys_json.get('twitter', '')}</textarea>
        <button class="btn" onclick="copyToClipboard('tw')">📋 Copiar Texto</button>
        <a class="btn btn-green" href="https://twitter.com/intent/tweet" target="_blank">🐤 Abrir X</a>
    </div>

    <div class="card">
        <h2>📘 Post para Facebook / LinkedIn</h2>
        <textarea id="fb">{copys_json.get('facebook', '')}</textarea>
        <button class="btn" onclick="copyToClipboard('fb')">📋 Copiar Texto</button>
        <a class="btn btn-green" href="https://www.facebook.com" target="_blank">📘 Abrir Facebook</a>
    </div>

    <div class="card">
        <h2>✉️ Boletín para Substack</h2>
        <textarea id="sub">{copys_json.get('substack', '')}</textarea>
        <button class="btn" onclick="copyToClipboard('sub')">📋 Copiar Texto</button>
    </div>

    <script>
        function copyToClipboard(id) {{
            const copyText = document.getElementById(id);
            copyText.select();
            navigator.clipboard.writeText(copyText.value);
            alert("¡Copiado al portapapeles!");
        }}
    </script>
</body>
</html>
"""
    with open("panel.html", "w", encoding="utf-8") as f:
        f.write(html_content)

def send_telegram_notice(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    latest_post_path, is_new = get_latest_post_info()
    
    # Permitir forzar ejecución si se pasa un parámetro manual
    force_run = os.environ.get("FORCE_RUN", "false").lower() == "true"
    
    if latest_post_path:
        post = frontmatter.load(latest_post_path)
        title = post.get('title', 'Nuevo Post')
        body = post.content
        
        if is_new or force_run:
            print(f"Procesando con Gemini: {title}")
            copys = generate_social_copys(body, title)
            update_web_panel(title, copys)
            
            msg = (
                f"🚀 **NUEVA PUBLICACIÓN DETECTADA**\n\n"
                f"📌 **Título:** {title}\n\n"
                f"Se han generado los borradores para tus redes sociales.\n"
                f"🔗 **Accede al panel para revisar y publicar:**\n{SITE_URL}"
            )
            send_telegram_notice(msg)
        else:
            print(f"Post actualizado ({title}). Omitiendo Gemini.")
            msg = (
                f"📝 **POST ACTUALIZADO**\n\n"
                f"📌 **Título:** {title}\n\n"
                f"El artículo se ha modificado. No se ejecutó Gemini automáticamente para no consumir API.\n"
                f"Si deseas regenerar borradores, entra al panel web:\n{SITE_URL}"
            )
            send_telegram_notice(msg)
