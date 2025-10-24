from flask import Flask, request, jsonify, render_template

# This is the Flask application object that Gunicorn / Render needs
app = Flask(__name__)

# Example route for testing
@app.route("/", methods=["GET"])
def index():
    # You can return HTML or JSON here.
    # If you have templates, you can do: return render_template("index.html")
    return "Hello from Render 👋 Flask is alive."

# Example API route
@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify({
        "message": "You posted this",
        "you_sent": data
    })

# This block only runs when you do `python app.py` locally.
# On Render/Gunicorn this block is ignored and gunicorn will import `app` instead.
if __name__ == "__main__":
    # Render will inject PORT env var, but locally we default to 5000
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
