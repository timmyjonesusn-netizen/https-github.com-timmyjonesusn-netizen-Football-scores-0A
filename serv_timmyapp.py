# serv_timmyapp.py
from flask import Flask, render_template, send_from_directory, make_response
import os

APP_NAME = "TimmyApp"

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    @app.route("/")
    def home():
        # Load the real front-end (no more plain text)
        return render_template("index.html", app_name=APP_NAME)

    @app.route("/health")
    def health():
        return {"status": "ok", "app": APP_NAME}, 200

    # (Optional) simple service worker for offline "it works"
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

    return app
