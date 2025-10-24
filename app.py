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
            --panel-bg: rgba(30, 0, 60, 0.25);           /* more transparent glass */
            --panel-border: rgba(255, 0, 255, 0.4);
            --panel-glow1: rgba(255,0,255,0.3);          /* soft outer glow */
            --panel-glow2: rgba(120,0,180,0.25);         /* violet halo */
            --panel-inner: rgba(255,0,255,0.15);         /* inner inset glow */

            --track-bg: rgba(255,255,255,0.05);          /* lighter tiles */
            --track-border: rgba(255,255,255,0.12);

            --text-main: #ffffff;
            --text-soft: #dcdcdc;
            --text-dim: #a7a7a7;
            --halo-strong: rgba(255,0,255,0.7);
            --halo-soft: rgba(255,0,255,0.4);

            --legal-text: #8a8a8a;
          }

          /* PAGE BACKGROUND
             lighter purple wash, subtle bloom, not blacked out
          */
          body {
            margin: 0;
            min-height: 100vh;
            background:
              radial-gradient(
                circle at 20% 15%,
                rgba(255,160,255,0.45) 0%,
                rgba(60,0,80,0.6) 40%,
                rgba(15,0,25,1) 80%
              ),
              radial-gradient(
                circle at 60% 120%,
                rgba(180,0,255,0.22) 0%,
                rgba(0,0,0,0) 80%
              );
            background-color: #1e0038;

            display: flex;
            align-items: flex-start;
            justify-content: center;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Inter", Roboto, sans-serif;
            color: var(--text-main);
            overflow: hidden;
            position: relative;
            padding: 2rem 1rem 4rem;
          }

          /* FLOATING BUBBLES
             - brighter
             - more visible through glass
             - slow vertical drift loop
          */
          .bubble {
            position: absolute;
            border-radius: 50%;
            filter: blur(8px);
            opacity: 0.5;
            animation: drift var(--speed) linear infinite;
            box-shadow: 0 0 30px currentColor, 0 0 80px currentColor;
            mix-blend-mode: screen;
            pointer-events: none;
            z-index: 1; /* sits BEHIND the card */
          }

          .bubble.purple {
            color: rgba(255, 0, 255, 0.55);
            background: radial-gradient(
              circle,
              rgba(255,0,255,0.4) 0%,
              rgba(0,0,0,0) 70%
            );
          }

          .bubble.blue {
            color: rgba(80, 140, 255, 0.55);
            background: radial-gradient(
              circle,
              rgba(80,140,255,0.4) 0%,
              rgba(0,0,0,0) 70%
            );
          }

          .bubble.white {
            color: rgba(255,255,255,0.6);
            background: radial-gradient(
              circle,
              rgba(255,255,255,0.5) 0%,
              rgba(0,0,0,0) 70%
            );
          }

          /* slow upward drift */
          @keyframes drift {
            0%   { transform: translateY(100px) scale(1);   opacity: 0.2; }
            50%  { transform: translateY(-80px) scale(1.1); opacity: 0.55; }
            100% { transform: translateY(100px) scale(1);   opacity: 0.2; }
          }

          /* bubble placement & speed */
          .b1 { --speed: 11s; width: 180px; height:180px; top: 10%; left: 8%;  }
          .b2 { --speed: 15s; width: 140px; height:140px; top: 25%; right:12%; }
          .b3 { --speed: 19s; width: 240px; height:240px; bottom:15%; left:5%; }
          .b4 { --speed: 23s; width: 110px; height:110px; bottom:20%; right:18%; }
          .b5 { --speed: 27s; width: 80px;  height:80px;  top: 60%; left: 60%; }

          /* MAIN GLASS CARD
             - more transparent
             - glow ring
             - sit ABOVE bubbles
          */
          .card {
            position: relative;
            width: 100%;
            max-width: 480px;

            background: var(--panel-bg); /* thinner glass now */
            border: 1px solid var(--panel-border);

            box-shadow:
              0 0 25px var(--panel-glow1),
              0 0 60px var(--panel-glow2),
              0 40px 100px rgba(0,0,0,0.9),
              inset 0 0 40px var(--panel-inner);

            border-radius: 24px;
            padding: 1.5rem 1rem 1rem;
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            text-align: left;
            z-index: 10; /* sits ABOVE bubbles */
          }

          .hub-title {
            font-size: 1.4rem;
            font-weight: 600;
            line-height: 1.6rem;
            color: var(--text-main);
            text-shadow:
              0 0 8px var(--halo-strong),
              0 0 20px var(--halo-strong),
              0 0 40px var(--halo-soft);
            margin-bottom: .75rem;
          }

          .hub-desc {
            font-size: .95rem;
            font-weight: 400;
            color: var(--text-soft);
            line-height: 1.4rem;
            margin-bottom: 1.25rem;
          }

          .playlist-header {
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--text-main);
            line-height: 1.3rem;
            margin-bottom: .4rem;
          }

          .playlist-sub {
            font-size: .85rem;
            font-weight: 400;
            color: var(--text-dim);
            line-height: 1.2rem;
            margin-bottom: .9rem;
          }

          /* OUTER LIST BOX AROUND TRACKS
             - lighter
             - more see-through so bubbles bleed through
          */
          .playlist-box {
            background: rgba(0,0,0,0.15);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            padding: .75rem .75rem;
            box-shadow:
              0 30px 60px rgba(0,0,0,0.9),
              0 0 40px rgba(255,0,255,0.25);
          }

          /* EACH PLAYLIST TILE / LINK */
          .track {
            display: block;
            text-decoration: none;
            background: var(--track-bg);
            border: 1px solid var(--track-border);
            border-radius: 14px;
            padding: .9rem .9rem;
            margin-bottom: .8rem;
            color: var(--text-main);
            box-shadow:
              0 20px 40px rgba(0,0,0,0.9),
              0 0 20px rgba(255,0,255,0.25);
          }

          .track:last-child {
            margin-bottom: 0;
          }

          .track-title {
            font-size: 1.05rem;
            font-weight: 500;
            color: var(--text-main);
            line-height: 1.3rem;
            text-shadow:
              0 0 6px rgba(255,0,255,0.8),
              0 0 20px rgba(255,0,255,0.5);
            margin-bottom: .3rem;
          }

          .track-desc {
            font-size: .85rem;
            line-height: 1.3rem;
            color: var(--text-soft);
          }

          .legal-note {
            font-size: .75rem;
            color: var(--legal-text);
            text-align: center;
            margin-top: 1.25rem;
            line-height: 1.1rem;
          }
        </style>
      </head>

      <body>

        <!-- BUBBLES BEHIND -->
        <div class="bubble purple b1"></div>
        <div class="bubble purple b2"></div>
        <div class="bubble blue   b3"></div>
        <div class="bubble white  b4"></div>
        <div class="bubble blue   b5"></div>

        <!-- MAIN CARD -->
        <div class="card">
          <div class="hub-title">
            TimmyApp Music Hub 💜
          </div>

          <div class="hub-desc">
            Royalty-friendly vibe tracks for creators.<br/>
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
            <a class="track" href="#" target="_blank" rel="noopener">
              <div class="track-title">Midnight Neon Cruise</div>
              <div class="track-desc">dreamy synth / slow drift / safe for socials</div>
            </a>

            <!-- PLAYLIST 2 -->
            <a class="track" href="#" target="_blank" rel="noopener">
              <div class="track-title">Southern Heatwave</div>
              <div class="track-desc">swagger beat / outlaw country trap / creator-safe</div>
            </a>

            <!-- PLAYLIST 3 -->
            <a class="track" href="#" target="_blank" rel="noopener">
              <div class="track-title">Halo Pulse</div>
              <div class="track-desc">angel pads / uplight energy / intro & outro friendly</div>
            </a>

            <!-- PLAYLIST 4 -->
            <a class="track" href="#" target="_blank" rel="noopener">
              <div class="track-title">Purple Drive</div>
              <div class="track-desc">midtempo glide / neon ride / safe for ads</div>
            </a>

            <!-- PLAYLIST 5 -->
            <a class="track" href="#" target="_blank" rel="noopener">
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
