# run.py exists ONLY so gunicorn can do `gunicorn run:app`
# It just imports the Flask app from app.py and exposes it as `app`.

from app import app

# Optional: allow `python run.py` to also work locally
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
