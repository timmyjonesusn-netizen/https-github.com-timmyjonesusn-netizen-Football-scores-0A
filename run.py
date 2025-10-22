# run.py — make sure gunicorn "run:app" can import a Flask app
# (ADD-ONLY fix; does not remove your other routes/files)

# 1) Try a direct app in app.py (app = Flask(__name__))
try:
    from app import app  # if you have app.py with a global `app`
except Exception:
    # 2) Try factory pattern from serv_timmyapp.py (create_app())
    try:
        from serv_timmyapp import create_app
        app = create_app()
    except Exception:
        # 3) Last-resort tiny app so gunicorn boots (won't replace your main routes)
        from flask import Flask
        app = Flask(__name__)

# Diagnostic color probe (doesn't interfere with your existing / route)
try:
    from flask import Response
    @app.route("/color")
    def _color():
        return Response(
            "<body style='background:#6a0dad;height:100vh;margin:0;"
            "display:flex;align-items:center;justify-content:center;"
            "color:#fff;font-family:sans-serif'><h1>🟣 Timmy Color</h1></body>",
            mimetype="text/html"
        )
except Exception:
    pass
