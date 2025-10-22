# app.py — clean baseline for TimmyApp
# ------------------------------------
from flask import Flask, Response

app = Flask(__name__)

# --- Main route ---
@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>TimmyApp is LIVE</title>
      <style>
        html, body {
          height: 100%%;
          margin: 0;
          font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
          color: #fff;
          display: flex;
          align-items: center;
          justify-content: center;
          flex-direction: column;
          background: radial-gradient(circle at 25%% 20%%, rgba(255,105,180,0.25), transparent 40%%),
                      radial-gradient(circle at 75%% 80%%, rgba(147,112,219,0.25), transparent 45%%),
                      #6a0dad;
          animation: pulse 5s infinite alternate;
        }

        @keyframes pulse {
          0%% { background-color: #6a0dad; }
          50%% { background-color: #8b00ff; }
          100%% { background-color: #6a0dad; }
        }

        h1 { font-size: 2.5em; margin: 0; text-shadow: 0 0 20px rgba(255,255,255,0.4); }
        p { margin-top: 10px; opacity: 0.9; }
      </style>
    </head>
    <body>
      <h1>🟣 TimmyApp is LIVE</h1>
      <p>Purple-pink pulse is strong. Good comms, captain.</p>
    </body>
    </html>
    """
    return Response(html, mimetype="text/html")


# --- Simple health check route ---
@app.route("/health")
def health():
    return "OK", 200
