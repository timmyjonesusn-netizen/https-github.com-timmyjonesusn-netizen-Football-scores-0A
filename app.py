from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head>
        <title>TimmyApp Music Hub 💜</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />

        <style>
          :root {
            --bg-deep: #0a0014;
            --bg-soft: rgba(180, 120, 220, 0.35);
            --panel-bg: rgba(20, 0, 40, 0.6);
            --panel-border: rgba(255, 0, 255, 0.3);
            --panel-shadow1: rgba(255,0,255,0.4);
            --panel-shadow2: rgba(120,0,180,0.3);
            --panel-shadow3: rgba(0,0,0,0.9);
            --track-bg: rgba(255,255,255,0.03);
            --track-border: rgba(255,255,255,0.07);
            --text-dim: #9d9d9d;
            --text-soft: #bfbfbf;
            --text-darker: #6f6f6f;
          }

          /* PAGE BACKGROUND */
          body {
            margin: 0;
            min-height: 100vh;
            background:
              radial-gradient(circle at 20% 20%, var(--bg-soft) 0%, rgba(20,0,40,1) 60%),
              radial-gradient(circle at 50% 110%, rgba(255,0,255,0.15) 0%, rgba(0,0,0,0) 70%);
            background-color: var(--bg-deep);

            display: flex;
            align-items: flex-start;
            justify-content: center;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Inter", Roboto, sans-serif;
            color: #fff;
            overflow: hidden;
            position: relative;
            padding: 2rem 1rem 4rem;
          }

          /* FLOATING BUBBLES */
          .bubble {
            position: absolute;
            border-radius: 50%;
            filter: blur(8px);
            opacity: 0.45;
            animation: floaty var(--speed) linear infinite;
            box-shadow: 0 0 20px currentColor, 0 0 60px currentColor;
            mix-blend-mode: screen;
            pointer-events: none;
          }

          .bubble.purple {
            color: rgba(255, 0, 255, 0.5);
            background: radial-gradient(circle, rgba(255,0,255,0.4) 0%, rgba(0,0,0,0) 70%);
          }

          .bubble.blue {
            color: rgba(80, 140, 255, 0.5);
            background: radial-gradient(circle, rgba(80,140,255,0.35) 0%, rgba(0,0,0,0) 70%);
          }

          .bubble.white {
            color: rgba(255,255,255,0.6);
            background: radial-gradient(circle, rgba(255,255,255,0.5) 0%, rgba(0,0,0,0) 70%);
          }

          @keyframes floaty {
            0%   { transform: translateY(0px) translateX(0px) scale(1); }
            50%  { transform: translateY(-40px) translateX(10px) scale(1.07); }
            100% { transform: translateY(0px) translateX(0px) scale(1); }
          }

          /* bubble positions/sizing */
          .b1 { --speed: 7s;  width: 160px; height:160px; top: 5%;   left: 8%;  }
          .b2 { --speed: 11s; width: 120px; height:120px; top: 18%;  right:12%; }
          .b3 { --speed: 14s; width: 220px; height:220px; bottom:12%; left:4%; }
          .b4 { --speed: 18s; width: 90px;  height:90px;  bottom:18%; right:18%; }
          .b5 { --speed: 22s; width: 60px;  height:60px;  top: 60%;   left: 60%; }

          /* MAIN PANEL ("CARD") */
          .card {
            position: relative;
            width: 100%;
            max-width: 460px;
            background: var(--panel-bg);
            border: 1px solid var(--panel-border);
            box-shadow:
              0 0 20px var(--panel-shadow1),
              0 0 60px var(--panel-shadow2),
              0 30px 80px var(--panel-shadow3);
            border-radius: 20px;
            padding: 1.5rem 1rem 1rem;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            text-align: left;
            z-index: 10;
            border-bottom-left-radius: 25px;
            border-bottom-right-radius: 25px;
            border-top-left-radius: 25px;
            border-top-right-radius: 25px;

            /* subtle outer glow line at bottom */
            box-shadow:
              0 0 20px rgba(255,0,255,0.4),
              0 0 60px rgba(120,0,180,0.3),
              0 30px 80px rgba(0,0,0,0.9),
              0 0 30px rgba(255,0,255,0.4) inset;
          }

          .hub-title {
            font-size: 1.3rem;
            font-weight: 600;
            line-height: 1.5rem;
            color: #fff;
            text-shadow:
              0 0 8px #ff00ff,
              0 0 16px #ff00ff,
              0 0 32px #ff00ff;
            margin-bottom: .75rem;
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: .4rem;
          }

          .hub-desc {
            font-size: .9rem;
            font-weight: 400;
            color: var(--text-soft);
            line-height: 1.3rem;
            margin-bottom: 1.25rem;
          }

          .playlist-header {
            font-size: .95rem;
            font-weight: 600;
            color: #fff;
            line-height: 1.2rem;
            margin-bottom: .4rem;
          }

          .playlist-sub {
            font-size: .8rem;
            font-weight: 400;
            color: var(--text-dim);
            line-height: 1.1rem;
            margin-bottom: .75rem;
          }

          /* playlist list container */
          .playlist-box {
            border: 1px solid rgba(255,255,255,0.08);
            background: rgba(0,0,0,0.35);
            border-radius: 14px;
            padding: .75rem .75rem;
            box-shadow: 0 20px 40px rgba(0,0,0,0.8);
          }

          /* individual playlist tile (clickable) */
          .track {
            display: block;
            text-decoration: none;
            background: var(--track-bg);
            border: 1px solid var(--track-border);
            border-radius: 12px;
            padding: .7rem .8rem;
            margin-bottom: .6rem;
            color: #fff;
            box-shadow: 0 10px 30px rgba(0,0,0,0.9);
          }

          .track:last-child {
            margin-bottom: 0;
          }

          .track-title {
            font-size: 1rem;
            font-weight: 500;
            color: #fff;
            line-height: 1.2rem;
            text-shadow:
              0 0 6px rgba(255,0,255,0.8),
              0 0 16px rgba(255,0,255,0.5);
            margin-bottom: .25rem;
          }

          .track-desc {
            font-size: .8rem;
            line-height: 1.1rem;
            color: var(--text-soft);
          }

          .legal-note {
            font-size: .7rem;
            color: var(--text-darker);
            text-align: center;
            margin-top: 1rem;
            line-height: 1rem;
          }

        </style>
      </head>

      <body>

        <!-- BUBBLES -->
        <div class="bubble purple b1"></div>
        <div class="bubble purple b2"></div>
        <div class="bubble blue   b3"></div>
        <div class="bubble white  b4"></div>
        <div class="bubble blue   b5"></div>

        <!-- MAIN CONTENT CARD -->
        <div class="card">
          <div class="hub-title">
            <div>TimmyApp Music Hub 💜</div>
          </div>

          <div class="hub-desc">
            Royalty-friendly vibe tracks for creators.
            Use for background, reels, shorts.
          </div>

          <div class="playlist-header">
            Today’s Featured Playlist
          </div>
          <div class="playlist-sub">
            Hand-picked for mood & flow
          </div>

          <div class="playlist-box">

            <!-- PLAYLIST 1 -->
            <a class="track" href="#midnight-neon" target="_blank" rel="noopener">
              <div class="track-title">Midnight Neon Cruise</div>
              <div class="track-desc">dreamy synth / slow drift / safe for socials</div>
            </a>

            <!-- PLAYLIST 2 -->
            <a class="track" href="#southern-heatwave" target="_blank" rel="noopener">
              <div class="track-title">Southern Heatwave</div>
              <div class="track-desc">swagger beat / outlaw country trap / creator-safe</div>
            </a>

            <!-- PLAYLIST 3 -->
            <a class="track" href="#halo-pulse" target="_blank" rel="noopener">
              <div class="track-title">Halo Pulse</div>
              <div class="track-desc">angel pads / uplight energy / intro & outro friendly</div>
            </a>

            <!-- PLAYLIST 4 -->
            <a class="track" href="#purple-drive" target="_blank" rel="noopener">
              <div class="track-title">Purple Drive</div>
              <div class="track-desc">midtempo glide / neon ride / safe for ads</div>
            </a>

            <!-- PLAYLIST 5 -->
            <a class="track" href="#yeti-stomp" target="_blank" rel="noopener">
              <div class="track-title">Yeti Stomp</div>
              <div class="track-desc">heavy bass / crowd hype / walk-in energy</div>
            </a>

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
