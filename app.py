from flask import Flask, jsonify

app = Flask(__name__)

# --- BASIC HOME ROUTE ---
@app.route("/")
def home():
    return """
    <html>
      <head>
        <title>TimmyApp</title>
        <style>
          body {
            background: radial-gradient(circle at 20% 20%, #ff00ff22 0%, #000011 60%);
            color: #fff;
            font-family: system-ui, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            text-align: center;
          }
          .glow {
            font-size: 1.5rem;
            line-height: 2rem;
            color: #fff;
            text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 40px #ff00ff;
          }
          .tag {
            margin-top: 1rem;
            font-size: .9rem;
            color: #bbb;
          }
        </style>
      </head>
      <body>
        <div class="glow">
          TimmyApp is LIVE 💜<br/>
          Flask is running directly with python app.py
        </div>
        <div class="tag">
          no gunicorn. no drama. just vibes.
        </div>
      </body>
    </html>
    """

# --- SIMPLE HEALTH CHECK FOR RENDER LOGS ---
@app.route("/health")
def health():
    return jsonify(status="ok", service="timmyapp"), 200


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    # 0.0.0.0 is REQUIRED on Render so the outside world can see it
    app.run(host="0.0.0.0", port=port, debug=False)
