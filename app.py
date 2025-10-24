from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head>
        <title>TimmyApp is Live</title>
        <style>
          body {
            background: radial-gradient(circle at 20% 20%, #ff4fd8 0%, #4a007a 60%, #000000 100%);
            color: white;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
            height: 100vh;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
          }
          .glow {
            font-size: 1.4rem;
            line-height: 1.5;
            text-shadow: 0 0 8px #ff4fd8, 0 0 16px #ff4fd8, 0 0 32px #a200ff;
          }
          .tag {
            margin-top: 1rem;
            font-size: .8rem;
            opacity: .7;
          }
        </style>
      </head>
      <body>
        <div>
          <div class="glow">
            💜 TimmyApp endpoint responding 💜<br/>
            Purple / pink heartbeat online.
          </div>
          <div class="tag">
            / route served by Flask → gunicorn → Render
          </div>
        </div>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "ok", "source": "TimmyApp Render", "v": 1})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
