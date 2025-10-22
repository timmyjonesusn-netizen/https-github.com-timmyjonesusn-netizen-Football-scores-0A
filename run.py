# run.py — add-only shim so gunicorn "run:app" works
from app import app  # expects you already have app.py with a Flask app named "app"

# Optional: local run helper (won't affect Render)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
