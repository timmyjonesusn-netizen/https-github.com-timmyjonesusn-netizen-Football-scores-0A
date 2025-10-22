from flask import Flask, render_template, make_response, request
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

APP_NAME = "TimmyApp"

def cache_control(resp, seconds):
    resp.headers["Cache-Control"] = f"public, max-age={seconds}"
    return resp

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    @app.after_request
    def add_common_headers(resp):
        # make sure index.html isn't cached while you're iterating on iPhone
        if request.path in ("/", "/index", "/index.html"):
            resp.headers["Cache-Control"] = "no-store"
        resp.headers["X-Frame-Options"] = "SAMEORIGIN"
        return resp

    @app.route("/")
    def home():
        base_url = request.url_root.rstrip("/")
        ver = datetime.utcnow().strftime("%Y%m%d%H%M")  # cache-busting
        return render_template("index.html",
                               app_name=APP_NAME,
                               base_url=base_url,
                               v=ver)

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
        return cache_control(resp, 3600)

    # Dynamic OG/Twitter preview image (1200x630)
    @app.route("/og.png")
    def og_image():
        W, H = 1200, 630
        im = Image.new("RGB", (W, H), "#120216")
        d = ImageDraw.Draw(im)
        # gradient
        for y in range(H):
            r = int(18 + 120 * (y / H)); g = 0; b = int(60 + 195 * (y / H))
            d.line([(0, y), (W, y)], fill=(r, g, b))
        # neon ring
        d.ellipse([180, 60, 1020, 600], outline=(255, 0, 170), width=12)
        # text
        try:
            t1 = ImageFont.truetype("DejaVuSans-Bold.ttf", 92)
            t2 = ImageFont.truetype("DejaVuSans.ttf", 42)
        except:
            t1 = t2 = ImageFont.load_default()
        title = f"{APP_NAME} is LIVE"
        sub = "Purple-pink glow, floating bubbles, and good vibes."
        tw = d.textlength(title, font=t1)
        sw = d.textlength(sub, font=t2)
        d.text(((W-tw)//2, 200), title, font=t1, fill=(255,255,255))
        d.text(((W-sw)//2, 330), sub, font=t2, fill=(245,210,255))
        buf = BytesIO(); im.save(buf, "PNG"); buf.seek(0)
        resp = make_response(buf.read())
        resp.headers["Content-Type"] = "image/png"
        return cache_control(resp, 86400)

    return app
