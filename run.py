from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

if __name__ == "__main__":
    # For local testing only; Render uses gunicorn above.
    app.run(host="0.0.0.0", port=5000)
