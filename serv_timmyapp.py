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

    @app.route("/service-worker.js")
    def service_worker():
        js = (
            "self.addEventListener('install',e=>self.skipWaiting());"
            "self.addEventListener('activate',e=>clients.claim());"
            "self.addEventListener('fetch',e=>{e.respondWith(fetch(e.request)"
            ".catch(()=>new Response('Offline',{status:200})))});"
        )
        resp = make_response(js)
        resp.headers["Content-Type"] = "application/javascript"
        return resp

    # dynamic Open Graph preview image
    @app.route("/og.png")
    def og_image():
        W, H = 1200, 630
        img = Image.new("RGB", (W, H), "#120216")
        d = ImageDraw.Draw(img)
        for y in range(H):
            r = int(18 + 120 * (y / H))
            g = 0
            b = int(60 + 195 * (y / H))
            d.line([(0, y), (W, y)], fill=(r, g, b))
        d.ellipse([200, 60, 1000, 620], outline=(255, 0, 170), width=12)
        try:
            f1 = ImageFont.truetype("DejaVuSans-Bold.ttf", 92)
            f2 = ImageFont.truetype("DejaVuSans.ttf", 42)
        except:
            f1 = f2 = ImageFont.load_default()
        title = f"{APP_NAME} is LIVE"
        sub = "Purple-pink glow, floating bubbles, and good vibes."
        tw = d.textlength(title, font=f1)
        sw = d.textlength(sub, font=f2)
        d.text(((W - tw)/2, 200), title, font=f1, fill=(255, 255, 255))
        d.text(((W - sw)/2, 330), sub, font=f2, fill=(255, 180, 255))
        buf = BytesIO()
        img.save(buf, "PNG")
        buf.seek(0)
        resp = make_response(buf.read())
        resp.headers["Content-Type"] = "image/png"
        resp.headers["Cache-Control"] = "public, max-age=86400"
        return resp

    return app
