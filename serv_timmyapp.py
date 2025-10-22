# serv_timmyapp.py — Flask app (no f-strings)
import os
from datetime import datetime
from flask import Flask, send_from_directory, make_response

APP_NAME = "TimmyApp"

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="/static")

    @app.route("/")
    def root():
        # Tiny HTML to prove it’s alive even if templates fail
        html = (
            "<!doctype html><meta charset='utf-8'/>"
            "<title>TimmyApp</title>"
            "<link rel='stylesheet' href='/static/style.css'/>"
            "<div class='wrap'>"
            "<h1>TimmyApp is live ✅</h1>"
            "<p>Deployed at: " + datetime.utcnow().isoformat() + "Z</p>"
            "<p><a class='btn' href='/home'>Go to Home</a></p>"
            "</div>"
        )
        resp = make_response(html, 200)
        resp.headers["Content-Type"] = "text/html; charset=utf-8"
        return resp

    @app.route("/home")
    def home():
        return send_from_directory("static", "index.html")

    @app.route("/healthz")
    def healthz():
        return "ok", 200

    # Optional service worker (kept super simple)
    @app.route("/service-worker.js")
    def sw():
        js = (
            "self.addEventListener('install', e=>self.skipWaiting());"
            "self.addEventListener('activate', e=>self.clients.claim());"
            "self.addEventListener('fetch', e=>{e.respondWith(fetch(e.request).catch(()=>new Response('Offline',{status:200})));});"
        )
        resp = make_response(js, 200)
        resp.headers["Content-Type"] = "application/javascript; charset=utf-8"
        return resp

    return app

# Local debug runner (Render will NOT use this — it uses Procfile)
if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
 
