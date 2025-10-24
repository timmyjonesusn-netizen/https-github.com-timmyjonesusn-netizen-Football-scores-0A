# app.py
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# --- Root route ---
@app.route("/")
def home():
    return "TimmyApp is awake 👋", 200


# --- Health check route (for Render or uptime pingers) ---
@app.route("/health")
def health():
    return jsonify(status="ok", message="Service running"), 200


# --- Example API route ---
@app.route("/api/echo", methods=["POST"])
def echo():
    """Simple test route that echoes back JSON sent by client."""
    data = request.get_json(silent=True) or {}
    return jsonify(received=data, message="Echo success!"), 200


# --- Optional: keep-alive ping logs ---
@app.before_request
def log_ping():
    if request.path == "/health":
        print("✅ Health ping received.")


# --- Run locally ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
