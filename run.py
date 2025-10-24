# run.py — guaranteed export of `app`
try:
    # Use your real app if available
    from app import create_app   # <- if your main file is app.py
    app = create_app()           # must RETURN a Flask instance
except Exception as e:
    # Fallback so Gunicorn always finds `app`
    from flask import Flask
    app = Flask(__name__)

    @app.get("/")
    def fallback_root():
        return "TimmyApp fallback ✅ — real app failed to load. See /_boot."

    @app.get("/_boot")
    def boot_info():
        return {"import_error": str(e)}, 200
