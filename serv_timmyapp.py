# serv_timmyapp.py — Flask app (no f-strings)
from flask import Flask, render_template, make_response, send_from_directory
import os

APP_NAME = "TimmyApp"

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="/static", template_folder="templates")

    @app.route("/")
    def home():
        return render_template("home.html", app_name=APP_NAME)

    @app.route("/music")
    def music():
        # You already have templates/music.html
        return render_template("music.html", app_name=APP_NAME)

    @app.route("/riddles")
    def riddles():
        return render_template("riddles.html", app_name=APP_NAME)

    @app.route("/whodunnit")
    def whodunnit():
        return render_template("whodunnit.html", app_name=APP_NAME)

    # Minimal service worker to avoid offline crashes (no f-string)
    @app.route("/service-worker.js")
    def service_worker():
        js = (
            "self.addEventListener('install', e=>{self.skipWaiting();});\n"
            "self.addEventListener('activate', e=>{self.clients.claim();});\n"
            "self.addEventListener('fetch', e=>{e.respondWith(fetch(e.request).catch(()=>new Response('Offline',"
            "{status:200,headers:{'Content-Type':'text/plain'}})));});"
        )
        resp = make_response(js)
        resp.headers["Content-Type"] = "application/javascript"
        return resp

    # Fallback for a robots file (optional)
    @app.route("/robots.txt")
    def robots():
        txt = "User-agent: *\nAllow: /\n"
        resp = make_response(txt)
        resp.headers["Content-Type"] = "text/plain"
        return resp

    return app
