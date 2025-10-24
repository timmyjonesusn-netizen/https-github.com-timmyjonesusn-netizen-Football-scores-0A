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
            --panel-bg: rgba(30, 0, 60, 0.35); /* more transparent now */
            --panel-border: rgba(255, 0, 255, 0.4);
            --panel-glow: rgba(255,0,255,0.5);
            --panel-inner-glow: rgba(120,0,180,0.3);

            --track-bg: rgba(255,255,255,0.05);   /* lighter tiles */
            --track-border: rgba(255,255,255,0.12);

            --text-soft: #dcdcdc;
            --text-dim: #a7a7a7;
            --text-halo: rgba(255,0,255,0.7);
            --text-halo-soft: rgba(255,0,255,0.4);

            --legal-text: #8a8a8a;
          }

          /* PAGE BACKGROUND
             - lighter purple wash instead of almost-black
             - faint bloom toward top-left so it feels lit
          */
          body {
            margin: 0;
            min-height: 100vh;
            background:
              radial-gradient(circle at 20% 15%, rgba(255,140,255,0.35) 0%, rgba(40,0,60,0.6) 40%, rgba(10,0,20,1) 70%),
              radial-gradient(circle at 50% 110%, rgba(255,0,255,0.18) 0%, rgba(0,0,0,0) 70%);
            background-color: #1a002e;

            display: flex;
            align-items: flex-start;
            justify-content: center;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Inter", Roboto, sans-serif;
            color: #fff;
            overflow: hidden;
            position: relative;
            padding: 2rem 1rem 4rem;
          }

          /* FLOATING BUBBLES
             - make them more see-through
             - make them drift upward slowly instead of bobbing
             - keep them under the content (z-index lower than card)
          */
          .bubble {
            position: absolute;
            border-radius: 50%;
            filter: blur(10px);
            opacity: 0.38;
            animation: drift var(--speed) linear infinite;
            box-shadow: 0 0 30px currentColor, 0 0 80px currentColor;
            mix-blend-mode: screen;
            pointer-events: none;
            z-index: 1;
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
            color: rgba(255,255,255,0.55);
            background: radial-gradient(circle, rgba(255,255,255,0.45) 0%, rgba(0,0,0,0) 70%);
          }

          /* upward float, slow, hypnotic */
          @keyframes drift {
            0%   { transform: translateY(40px) translateX(0px) scale(1);   opacity: 0.15; }
            50%  { transform: translateY(-40px) translateX(10px) scale(1.07); opacity: 0.4; }
            100% { transform: translateY(40px) translateX(0px) scale(1);   opacity: 0.15; }
          }

          /* bubble positions/sizing */
          .b1 { --speed: 11s; width: 180px; height:180px; top: 10%; left: 8%;  }
          .b2 { --speed: 15s; width: 140px; height:140px; top: 25%; right:12%; }
          .b3 { --speed: 19s; width: 240px; height:240px; bottom:15%; left:5%; }
          .b4 { --speed: 23s; width: 110px; height:110px; bottom:20%; right:18%; }
          .b5 { --speed: 27s; width: 80px;  height:80px;  top: 60%; left: 60%; }

          /* MAIN PANEL */
          .card {
            position: relative;
            width: 100%;
            max-width: 480px;

            background: var(--panel-bg);
            border: 1px solid var(--panel-border);

            /* Glass look:
               - inner glow
               - outer glow halo in pink/violet
               - softer, not that hard dark slab
            */
            box-shadow:
              0 0 25px var(--panel-glow),
              0 0 60px var(--panel-inner-glow),
              0 40px 100px rgba(0,0,0,0.9),
              inset 0 0 30px rgba(255,0,255,0.25);

            border-radius: 24px;
            padding: 1.5rem 1rem 1rem;
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            text-align: left;
            z-index: 10;
          }

          .hub-title {
            font-size: 1.3rem;
            font-weight: 600;
            line-height: 1.5rem;
            color: #fff;
            text-shadow:
              0 0 8px var(--text-halo),
              0 0 20px var(--text-halo),
              0 0 40px var(--text-halo-soft);
            margin-bottom: .75rem;
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

          .playlist-box {
            border: 1px solid rgba(255,255,255,0.12);
            background: rgba(0,0,0,0.2); /* more see-through than before */
            border-radius: 16px;
            padding: .75rem .75rem;
            box-shadow:
              0 30px 60px rgba(0,0,0,0.9),
              0 0 40px rgba(255,0,255,0.3);
          }

          /* playlist tile (tap area) */
          .track {
            display: block;
            text-decoration: none;
            background: var(--track-bg);
            border: 1px solid var(--track-border);
            border-radius: 12px;
            padding: .8rem .8rem;
            margin-bottom: .7rem;
            color: #fff;
            box-shadow:
              0 20px 40px rgba(0,0,0,0.9),
              0 0 20px rgba(255,0,255,0.25);
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
              0 0 20px rgba(255,0,255,0.5);
            margin-bottom: .25rem;
          }

          .track-desc {
            font-size: .8rem;
            line-height: 1.2rem;
            color: var(--text-soft);
          }

          .legal-note {
            font-size: .7rem;
            color: var(--legal-text);
            text-align: center;
            margin-top: 1rem;
            line-height: 1rem;
          }
        </style>
      </head>

      <body>

        <!-- SOFT FLOAT BUBBLES IN BACK -->
        <div class="bubble purple b1"></div>
        <div class="bubble purple b2"></div>
        <div class="bubble blue   b3"></div>
        <div class="bubble white  b4"></div>
        <div class="bubble blue   b5"></div>

        <!-- GLASS PANEL -->
        <div class="card">
          <div class="hub-title">
            TimmyApp Music Hub 💜
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
