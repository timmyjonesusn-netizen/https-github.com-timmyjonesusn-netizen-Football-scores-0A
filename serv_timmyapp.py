from flask import Flask, render_template, make_response, request, jsonify
import os

APP_NAME = "TimmyApp"

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    # ------- LIVE HOME -------
    @app.route("/")
    def home():
        base_url = request.url_root.rstrip("/")
        return render_template("index.html", app_name=APP_NAME, base_url=base_url)

    # ------- HEALTH -------
    @app.route("/health")
    def health():
        return {"status": "ok", "app": APP_NAME}, 200

    # ------- DIAGNOSTIC: shows exactly what Render is serving -------
    @app.route("/__whoami")
    def whoami():
        root = os.getcwd()
        files = sorted(os.listdir(root))
        return jsonify({
            "cwd": root,
            "start_cmd_expected": "gunicorn wsgi:app",
            "template_folder": app.template_folder,
            "static_folder": app.static_folder,
            "root_files": files,
            "routes": sorted([str(r) for r in app.url_map.iter_rules()])
        })

    # tiny service worker (safe)
    @app.route("/service-worker.js")
    def sw():
        js = ("self.addEventListener('install',e=>self.skipWaiting());"
              "self.addEventListener('activate',e=>clients.claim());"
              "self.addEventListener('fetch',e=>{e.respondWith(fetch(e.request)"
              ".catch(()=>new Response('Offline',{status:200})))});")
        resp = make_response(js)
        resp.headers["Content-Type"] = "application/javascript"
        return resp

    return app
