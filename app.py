from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    # ultra-simple payload so you KNOW it's your app
    return jsonify(status="ok", app="TimmyApp", message="Comms up 💜")

@app.get("/healthz")
def health():
    return "ok", 200
