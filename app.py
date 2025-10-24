from flask import Flask, render_template

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    @app.get("/")
    def home():
        return render_template("index.html")  # or: return "Hello Timmy!"

    return app   # <- do NOT forget this
