from flask import Flask, render_template, make_response, request

APP_NAME = "TimmyApp"

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    @app.route("/")
    def home():
        base_url = request.url_root.rstrip("/")
        return render_template("index.html", app_name=APP_NAME, base_url=base_url)

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

    return app
