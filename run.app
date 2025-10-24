# run.py
from app import create_app

# Gunicorn will import THIS variable below: run:app
app = create_app()

# Local dev entrypoint (not used by Gunicorn on Render)
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    # You can turn off debug in prod, but for local it's nice to have
    app.run(host="0.0.0.0", port=port, debug=True)
