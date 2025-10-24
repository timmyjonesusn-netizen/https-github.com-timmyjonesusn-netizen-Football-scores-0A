# app.py
from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    # Example config
    app.config["SECRET_KEY"] = "dev-secret"  # replace in real prod

    # Example health route
    @app.route("/", methods=["GET"])
    def index():
        return jsonify({
            "status": "ok",
            "message": "Hello from Render 🐍"
        })

    # You can add more routes here
    @app.route("/ping", methods=["GET"])
    def ping():
        return "pong"

    return app
