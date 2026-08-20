import os
import glob
import frontmatter
import google.generativeai as genai
import requests

# Configurar variables de entorno desde los secretos
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

genai.configure(api_key=GEMINI_KEY)

def get_latest_post():
    # Encuentra el archivo de post más reciente en la carpeta _posts/
    list_of_files = glob.glob('_posts/*.md') + glob.glob('_posts/*.markdown')
    if not list_of_files:
        return None
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

def generate_social_copys(post_content, post_title):
    # Usamos Gemini para analizar el post y redactar los textos
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"""
    Eres un experto Social Media Manager para un blog de literatura, ciencia ficción y tecnología.
    Basándote en el siguiente artículo titulado "{post_title}", redacta propuestas de contenido para redes sociales:

    1. 🧵 **HILO PARA X (TWITTER):** Un hilo enganchante de 3 tuits con hashtags clave.
    2. 📘 **POST PARA FACEBOOK / LINKEDIN:** Un texto persuasivo y atractivo.
    3. ✉️ **BOLETÍN SUBSTACK:** Un párrafo de introducción tentador para invitar a leer el post completo.

    Mantén un tono profesional pero cercano, literario y enfocado en despertar la curiosidad.

    Contenido del artículo:
    {post_content[:3500]}
    """
    response = model.generate_content(prompt)
    return response.text

def send_to_telegram(text, title):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    message = f"🚀 **NUEVA PUBLICACIÓN DETECTADA**\n\n📌 **Título:** {title}\n\n---\n\n{text}"
    
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    latest_post_path = get_latest_post()
    if latest_post_path:
        post = frontmatter.load(latest_post_path)
        title = post.get('title', 'Nuevo Post')
        body = post.content
        
        print(f"Procesando: {title}")
        copys = generate_social_copys(body, title)
        send_to_telegram(copys, title)
        print("Borradores enviados con éxito a Telegram.")
    else:
        print("No se encontraron publicaciones en _posts/")
