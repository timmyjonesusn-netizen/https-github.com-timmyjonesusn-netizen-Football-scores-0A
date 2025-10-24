from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

# --- simple home route ---
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_msg = request.form.get("message", "")
        reply = f"You said: {user_msg}"
    else:
        reply = None

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8" />
      <title>Timmy1</title>
      <style>
        body {
          background-color: #0a0a0a;
          color: #fff;
          font-family: system-ui, -apple-system, BlinkMacSystemFont,
                       "Inter", Roboto, "Segoe UI", sans-serif;
          min-height: 100vh;
          margin: 0;
          display: flex;
          align-items: center;
          justify-content: center;
        }
        .chat-card {
          background: #1a1a1a;
          border: 1px solid #333;
          border-radius: 16px;
          padding: 24px;
          width: min(400px, 90vw);
          box-shadow: 0 30px 80px rgba(0,0,0,0.8);
        }
        h1 {
          font-size: 1rem;
          font-weight: 600;
          color: #8b5cf6;
          margin: 0 0 1rem 0;
          display: flex;
          align-items: center;
          gap: 0.5rem;
        }
        .dot {
          width:8px;
          height:8px;
          border-radius:50%;
          background:#10b981;
          box-shadow:0 0 8px #10b981;
        }
        label {
          color:#888;
          font-size:0.8rem;
        }
        input[type="text"] {
          width:100%;
          background:#0f0f0f;
          border:1px solid #333;
          border-radius:8px;
          color:#fff;
          padding:10px 12px;
          font-size:0.9rem;
          outline:none;
        }
        input[type="text"]:focus {
          border-color:#8b5cf6;
          box-shadow:0 0 6px #8b5cf6;
        }
        button {
          background:#8b5cf6;
          border:none;
          border-radius:8px;
          padding:10px 12px;
          font-size:0.9rem;
          font-weight:600;
          cursor:pointer;
          color:#fff;
          margin-top:12px;
          width:100%;
        }
        .reply-box {
          background:#0f0f0f;
          border:1px solid #333;
          border-radius:8px;
          padding:12px;
          color:#fff;
          margin-top:16px;
          font-size:0.85rem;
          line-height:1.4;
          white-space:pre-wrap;
        }

        /* highlight changes (vibrant) vs unchanged (dim) */
        .changed   { color:#22c55e; font-weight:600; }   /* green glow idea */
        .unchanged { color:#666;    font-weight:400; }

      </style>
    </head>
    <body>
      <div class="chat-card">
        <h1>
          <span class="dot"></span>
          Timmy1 · live
        </h1>

        <form method="POST">
          <label for="msgInput">Send a message</label>
          <input id="msgInput" name="message" type="text"
                 placeholder="Talk to Timmy1..." autocomplete="off" />
          <button type="submit">Send</button>
        </form>

        {% if reply %}
          <div class="reply-box">
            <div><span class="unchanged">Timmy1 heard: </span>
                 <span class="changed">{{ reply }}</span>
            </div>
          </div>
        {% endif %}
      </div>
    </body>
    </html>
    """, reply=reply)

# health check for Render
@app.route("/healthz")
def healthz():
    return {"status": "ok"}, 200

# local dev only
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
