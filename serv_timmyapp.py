# serv_timmyapp.py — Flask app factory for Render
from flask import Flask, render_template, make_response, Response
from datetime import datetime

APP_NAME = "TimmyApp"

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="/static")

    # Basic home
    @app.route("/")
    def home():
        return render_template("index.html", app_name=APP_NAME, now=datetime.utcnow())

    # Health check for Render
    @app.route("/health")
    def health():
        return {"status": "ok", "app": APP_NAME, "utc": datetime.utcnow().isoformat()}

    # Minimal service worker (optional)
    @app.route("/service-worker.js")
    def sw():
        js = (
            "self.addEventListener('install',e=>self.skipWaiting());"
            "self.addEventListener('activate',e=>self.clients.claim());"
            "self.addEventListener('fetch',e=>{e.respondWith(fetch(e.request)"
            ".catch(()=>new Response('Offline',{status:200})));});"
        )
        resp = make_response(js)
        resp.headers["Content-Type"] = "application/javascript"
        return resp

    # Friendly errors
    @app.errorhandler(404)
    def not_found(_e):
        return Response("404 — Not Found", 404)

    @app.errorhandler(500)
    def server_error(_e):
        return Response("500 — Server Error", 500)

    # Static caching headers (safe defaults)
    @app.after_request
    def add_headers(resp):
        if resp.cache_control.max_age is None:
            resp.cache_control.max_age = 3600
        return resp

    return app
