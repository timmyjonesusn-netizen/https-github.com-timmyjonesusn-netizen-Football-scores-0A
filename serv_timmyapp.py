# serv_timmyapp.py
from flask import Flask, render_template

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/music")
    def music():
        return render_template("music.html")

    return app
