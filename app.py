from flask import Flask, jsonify
app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(status="ok", app="TimmyApp", message="Comms up 💜")

@app.get("/healthz")
def health():
    return "ok", 200
