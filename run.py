from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head><title>TimmyApp</title></head>
      <body style="background-color:black; color:#ff00ff; text-align:center; font-family:Arial;">
        <h1>🔥 TimmyApp is LIVE on Render!</h1>
        <p>Welcome to the matrix, Chief.</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
