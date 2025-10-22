# run.py — minimal, Render-safe Flask app (works out of the box)
from flask import Flask, Response

app = Flask(__name__)

@app.get("/healthz")
def healthz():
    return Response("ok", status=200, mimetype="text/plain")

@app.get("/")
def home():
    # simple page so we can confirm it’s alive
    return """
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>TimmyApp — It’s Alive</title>
        <style>
          html,body{height:100%;margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto;}
          body{display:grid;place-items:center;background:#0b0016;color:#fff;}
          .card{
            padding:24px 28px;border:1px solid #6a00ff55;border-radius:16px;
            background: radial-gradient(1200px 600px at 20% 0%, #ff2fb033 0%, transparent 60%),
                        radial-gradient(800px 400px at 80% 100%, #6a00ff33 0%, transparent 70%),
                        #120022;
            box-shadow:0 8px 40px #0008, inset 0 0 32px #ff2fb022, inset 0 0 64px #6a00ff22;
            text-align:center;
          }
          h1{margin:0 0 8px;font-weight:800;letter-spacing:.5px}
          .ok{opacity:.85;font-size:.95rem}
        </style>
      </head>
      <body>
        <div class="card">
          <h1>TimmyApp is live ✅</h1>
          <div class="ok">If you can see this, the 502 is gone. Try <code>/healthz</code> too.</div>
        </div>
      </body>
    </html>
    """
    
if __name__ == "__main__":
    # local dev only; Render will use Gunicorn via Procfile
    app.run(host="0.0.0.0", port=8080, debug=False)
