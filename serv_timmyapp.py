# serv_timmyapp.py
import os
from flask import Flask, send_from_directory, render_template_string

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="/static")

    @app.route("/")
    def home():
        # Serve index.html from repo root
        try:
            return send_from_directory(".", "index.html")
        except Exception:
            return render_template_string("<h1>TimmyApp online</h1>")

    # Optional health check (some platforms ping this)
    @app.route("/healthz")
    def healthz():
        return "ok", 200

    return app
