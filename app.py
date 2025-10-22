# === DIAGNOSTIC: ADD-ONLY COLOR CHECK ===
try:
    from flask import Response, render_template_string
except Exception:
    # If already imported earlier, this won't run—totally fine.
    pass

@app.route("/color")
def _timmy_color_probe():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Timmy Color Probe</title>
      <style>
        html, body { height:100%; margin:0; }
        body {
          /* deep purple base + subtle glow */
          background: radial-gradient(circle at 30% 20%, rgba(255,105,180,0.18), transparent 40%),
                      radial-gradient(circle at 70% 80%, rgba(147,112,219,0.25), transparent 45%),
                      #6a0dad;
          color: #fff;
          font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
          display: flex; align-items: center; justify-content: center;
        }
        h1 { letter-spacing: .5px; text-shadow: 0 0 18px rgba(255,255,255,.25); }
        .tag { margin-top:.5rem; opacity:.85; font-size:0.95rem; }
      </style>
    </head>
    <body>
      <div style="text-align:center">
        <h1>🟣 Timmy Comms Online</h1>
        <div class="tag">/color route — add-only probe</div>
      </div>
    </body>
    </html>
    """
    return Response(html, mimetype="text/html")

@app.route("/health")
def _timmy_health():
    return "OK", 200

@app.route("/debug-headers")
def _timmy_debug_headers():
    # quick sanity: see headers Render sends back
    items = [f"{k}: {v}" for k, v in sorted(dict(getattr(request, 'headers', {})).items())]
    return Response("<pre>" + "\n".join(items) + "</pre>", mimetype="text/html")
