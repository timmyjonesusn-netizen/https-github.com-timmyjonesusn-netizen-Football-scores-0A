# serv_timmyapp.py
from flask import Flask, render_template, make_response

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates", static_url_path="/static")

    # ---------- PAGES (endpoints must match template links) ----------
    @app.route("/", endpoint="home")
    def home():
        return render_template("home.html")

    @app.route("/music", endpoint="music")
    def music():
        return render_template("music.html")

    @app.route("/weather", endpoint="weather")
    def weather():
        return render_template("weather.html")

    @app.route("/whodunnit", endpoint="whodunnit")
    def whodunnit():
        return render_template("whodunnit.html")

    # ---------- Service worker (optional) ----------
    @app.route("/service-worker.js", endpoint="service_worker")
    def service_worker():
        js = (
            "self.addEventListener('install', e=>{self.skipWaiting();});"
            "self.addEventListener('activate', e=>{clients.claim();});"
            "self.addEventListener('fetch', e=>{"
            "  e.respondWith(fetch(e.request).catch(()=>new Response('Offline',{status:200,headers:{'Content-Type':'text/plain'}})));"
            "});"
        )
        resp = make_response(js)
        resp.headers["Content-Type"] = "application/javascript"
        return resp

    return app
