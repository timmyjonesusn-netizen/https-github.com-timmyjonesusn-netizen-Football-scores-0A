from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head>
        <title>TimmyApp Music Hub</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />

        <style>
          /* Page background: deep purple fading lighter toward the top */
          body {
            margin: 0;
            min-height: 100vh;
            background: radial-gradient(
              circle at 20% 20%,
              rgba(180, 120, 220, 0.35) 0%,
              rgba(20, 0, 40, 1) 60%
            );
            background-color: #0a0014;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Inter", Roboto, sans-serif;
            color: #fff;
            overflow: hidden;
            position: relative;
          }

          /* Bubble base style */
          .bubble {
            position: absolute;
            border-radius: 50%;
            filter: blur(8px);
            opacity: 0.45;
            animation: floaty var(--speed) linear infinite;
            box-shadow: 0 0 20px currentColor, 0 0 60px currentColor;
          }

          /* Different bubble colors */
          .bubble.purple { color: rgba(255, 0, 255, 0.5); background: radial-gradient(circle, rgba(255,0,255,0.4) 0%, rgba(0,0,0,0) 70%); }
          .bubble.blue   { color: rgba(80, 140, 255, 0.5); background: radial-gradient(circle, rgba(80,140,255,0.35) 0%, rgba(0,0,0,0) 70%); }
          .bubble.white  { color: rgba(255,255,255,0.6);   background: radial-gradient(circle, rgba(255,255,255,0.5) 0%, rgba(0,0,0,0) 70%); }

          /* gentle drifting animation */
          @keyframes floaty {
            0%   { transform: translateY(0px) translateX(0px) scale(1); }
            50%  { transform: translateY(-40px) translateX(10px) scale(1.07); }
            100% { transform: translateY(0px) translateX(0px) scale(1); }
          }

          /* center card */
          .card {
            position: relative;
            width: 90%;
            max-width: 400px;
            background: rgba(20, 0, 40, 0.6);
            border: 1px solid rgba(255, 0, 255, 0.3);
            box-shadow:
              0 0 20px rgba(255,0,255,0.4),
              0 0 60px rgba(120,0,180,0.3),
              0 30px 80px rgba(0,0,0,0.9);
            border-radius: 20px;
            padding: 1.5rem 1.25rem 1rem;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            text-align: center;
            z-index: 10;
          }

          .title {
            font-size: 1.1rem;
            font-weight: 600;
            line-height: 1.4rem;
            color: #fff;
            text-shadow:
              0 0 8px #ff00ff,
              0 0 16px #ff00ff,
              0 0 32px #ff00ff;
            margin-bottom: .5rem;
          }

          .subtitle {
            font-size: .8rem;
            font-weight: 400;
            color: #bfbfbf;
            line-height: 1.2rem;
            margin-bottom: 1rem;
          }

          /* playlist section */
          .playlist-box {
            background: rgba(0,0,0,0.4);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 14px;
            padding: .75rem 1rem;
            text-align: left;
            box-shadow: 0 20px 40px rgba(0,0,0,0.8);
          }

          .playlist-header {
            font-size: .8rem;
            font-weight: 600;
            color: #fff;
            margin-bottom: .5rem;
            display: flex;
            flex-direction: column;
          }

          .playlist-header span.small-note {
            color: #9d9d9d;
            font-size: .7rem;
            font-weight: 400;
            line-height: 1rem;
          }

          .track {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 10px;
            padding: .6rem .75rem;
            margin-bottom: .5rem;
            color: #fff;
            font-size: .8rem;
            line-height: 1.1rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.9);
            display: flex;
            flex-direction: column;
          }

          .track:last-child {
            margin-bottom: 0;
          }

          .track-title {
            color: #fff;
            font-weight: 500;
            text-shadow:
              0 0 6px rgba(255,0,255,0.8),
              0 0 16px rgba(255,0,255,0.5);
          }

          .track-desc {
            font-size: .7rem;
            color: #9d9d9d;
          }

          /* footer note under playlist */
          .legal-note {
            font-size: .65rem;
            color: #6f6f6f;
            text-align: center;
            margin-top: 1rem;
            line-height: .9rem;
          }

          /* place & size bubbles */
          /* tweak these positions/sizes for the vibe */
          .b1 { --speed: 7s; width: 160px; height:160px; top:5%; left:10%; }
          .b2 { --speed:11s; width:120px; height:120px; top:20%; right:15%; }
          .b3 { --speed:14s; width:200px; height:200px; bottom:10%; left:5%; }
          .b4 { --speed:18s; width:90px;  height:90px;  bottom:15%; right:20%; }
          .b5 { --speed:22s; width:60px;  height:60px;  top:55%; left:55%; }

          /* make sure bubbles sit behind the card */
          .bubble { z-index: 1; mix-blend-mode: screen; }
        </style>
      </head>

      <body>

        <!-- floating bubbles -->
        <div class="bubble purple b1"></div>
        <div class="bubble purple b2"></div>
        <div class="bubble blue   b3"></div>
        <div class="bubble white  b4"></div>
        <div class="bubble blue   b5"></div>

        <!-- center card -->
        <div class="card">
          <div class="title">
            TimmyApp Music Hub 💜
          </div>
          <div class="subtitle">
            Royalty-friendly vibe tracks for creators.<br/>
            Use for background, reels, shorts.
          </div>

          <div class="playlist-box">
            <div class="playlist-header">
              <span>Today’s Featured Playlist</span>
              <span class="small-note">Hand-picked for mood & flow</span>
            </div>

            <!-- Example tracks. We'll swap with real Suno playlist links next. -->
            <div class="track">
              <div class="track-title">Midnight Neon Cruise</div>
              <div class="track-desc">dreamy synth / slow drift / safe for socials</div>
            </div>

            <div class="track">
              <div class="track-title">Southern Heatwave</div>
              <div class="track-desc">swagger beat / outlaw country trap / creator-safe</div>
            </div>

            <div class="track">
              <div class="track-title">Halo Pulse</div>
              <div class="track-desc">angel pads / uplight energy / intro & outro friendly</div>
            </div>

          </div>

          <div class="legal-note">
            no copyright strikes.<br/>
            you can post this.
          </div>
        </div>

      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="ok", service="timmyapp"), 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
