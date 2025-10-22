# serv_timmyapp.py
from flask import Flask, render_template, make_response
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

APP_NAME = "TimmyApp"

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    @app.route("/")
    def home():
        return render_template("index.html", app_name=APP_NAME, base_url="https://timmyapp.onrender.com")

    @app.route("/health")
    def health():
        return {"status": "ok", "app": APP_NAME}, 200

    # Lightweight service worker
    @app.route("/service-worker.js")
    def service_worker():
        js = (
            "self.addEventListener('install',e=>self.skipWaiting());"
            "self.addEventListener('activate',e=>clients.claim());"
            "self.addEventListener('fetch',e=>{e.respondWith(fetch(e.request)"
            ".catch(()=>new Response('Offline',{status:200})))});"
        )
        resp = make_response(js); resp.headers["Content-Type"] = "application/javascript"
        return resp

    # Dynamic OG/Twitter preview image (1200x630 PNG)
    @app.route("/og.png")
    def og_image():
        W, H = 1200, 630
        img = Image.new("RGB", (W, H), "#120216")
        d = ImageDraw.Draw(img)

        # gradient bars
        for y in range(H):
            r = int(18 + 120 * (y / H)); g = 0; b = int(60 + 195 * (y / H))
            d.line([(0, y), (W, y)], fill=(r, g, b))

        # glow ellipse
        d.ellipse([200, 60, 1000, 620], outline=(255, 0, 170), width=12)

        # fonts (fallback to default if no system fonts)
        try:
            title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 92)
            sub_font   = ImageFont.truetype("DejaVuSans.ttf", 42)
        except:
            title_font = ImageFont.load_default()
            sub_font   = ImageFont.load_default()

        title = f"{APP_NAME} is LIVE"
        sub = "Purple-pink glow, floating bubbles, and good vibes."

        tw, th = d.textbbox((0,0), title, font=title_font)[2:]
        sx, sy = (W - tw)//2, 200
        d.text((sx+2, sy+2), title, font=title_font, fill=(255, 0, 200))
        d.text((sx, sy), title, font=title_font, fill=(255, 255, 255))

        sw, sh = d.textbbox((0,0), sub, font=sub_font)[2:]
        d.text(((W - sw)//2, sy + th + 30), sub, font=sub_font, fill=(240, 220, 255))

        buf = BytesIO(); img.save(buf, format="PNG"); buf.seek(0)
        resp = make_response(buf.read())
        resp.headers["Content-Type"] = "image/png"
        resp.headers["Cache-Control"] = "public, max-age=3600"
        return resp

    return app
