# app.py
from flask import Flask, render_template

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    @app.get("/")
    def home():
        # If you don’t have templates/index.html yet, replace with: return "Hello Timmy!"
        return render_template("index.html")

    @app.get("/healthz")
    def healthz():
        return "ok", 200

    return app   # <-- this return is critical
