<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>TimmyApp</title>

<style>
    /* ===============================
       GLOBAL PAGE BACKGROUND
       =============================== */
    :root {
        --bg-main-start: rgb(20, 0, 30);
        --bg-main-end: rgb(60, 0, 80);
        --pulse-color: rgba(255, 0, 128, 0.4);
        --text-main: #fff;
        --accent-pink: rgb(255, 0, 170);
        --card-bg: rgba(0,0,0,0.4);
        --card-border: rgba(255,0,255,0.4);
        --radius-lg: 18px;
        --radius-md: 12px;
        --radius-sm: 8px;
        --shadow-card: 0 0 24px rgba(255,0,200,0.4);
        --shadow-strong: 0 0 32px rgba(255,0,255,0.75);
        --tap-highlight: rgba(255,0,200,0.2);
        --bubble-max-size: 200px;
    }

    * {
        box-sizing: border-box;
        -webkit-tap-highlight-color: transparent;
        margin: 0;
        padding: 0;
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, "Inter", "Roboto", sans-serif;
        color: var(--text-main);
        background: radial-gradient(circle at 20% 20%, rgb(90,0,120) 0%, rgb(20,0,30) 60%) fixed,
                    radial-gradient(circle at 80% 80%, rgb(255,0,128,0.2) 0%, rgba(0,0,0,0) 70%) fixed,
                    linear-gradient(160deg, var(--bg-main-start) 0%, var(--bg-main-end) 100%) fixed;
        background-blend-mode: screen, normal, normal;
        min-height: 100vh;
        position: relative;
        overflow-x: hidden;
        overflow-y: auto;
        animation: bgPulse 4s ease-in-out infinite;
    }

    /* slow "heartbeat" glow */
    @keyframes bgPulse {
        0%   { box-shadow: 0 0 60px 20px var(--pulse-color) inset; }
        50%  { box-shadow: 0 0 10px 2px rgba(0,0,0,0.8) inset; }
        100% { box-shadow: 0 0 60px 20px var(--pulse-color) inset; }
    }

    /* layout wrapper so content sits above bubbles */
    .app-shell {
        position: relative;
        z-index: 10;
        max-width: 480px;
        margin: 0 auto;
        padding: 24px 16px 80px;
        display: flex;
        flex-direction: column;
        gap: 24px;
    }

    /* ===============================
       HEADER / TITLE AREA
       =============================== */
    .hero-card {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: var(--radius-lg);
        padding: 16px 20px;
        box-shadow: var(--shadow-card);
        backdrop-filter: blur(10px);
    }

    .app-title {
        font-size: 1.4rem;
        font-weight: 600;
        line-height: 1.2;
        display: flex;
        align-items: center;
        gap: 8px;
        color: #fff;
        text-shadow: 0 0 8px rgba(255,0,255,0.8);
    }

    .title-glow-dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        box-shadow: 0 0 12px rgba(255,0,255,0.9), 0 0 32px rgba(255,0,255,0.6);
        background: radial-gradient(circle,
            rgba(255,0,255,1) 0%,
            rgba(255,0,255,0.3) 60%,
            rgba(0,0,0,0) 80%
        );
        flex-shrink: 0;
    }

    .tagline {
        margin-top: 6px;
        font-size: 0.9rem;
        line-height: 1.4;
        color: rgba(255,255,255,0.8);
    }

    /* ===============================
       MUSIC / PLAYLISTS SECTION
       =============================== */
    .section-card {
        background: var(--card-bg);
        border: 1px solid rgba(0, 200, 255, 0.4);
        border-radius: var(--radius-lg);
        box-shadow: 0 0 20px rgba(0,200,255,0.35);
        padding: 16px 20px;
        backdrop-filter: blur(10px);
    }

    .section-head {
        font-size: 1rem;
        font-weight: 600;
        color: #fff;
        text-shadow: 0 0 8px rgba(0,200,255,0.8);
        margin-bottom: 8px;
        display: flex;
        flex-wrap: wrap;
        align-items: baseline;
        justify-content: space-between;
        row-gap: 4px;
    }

    .section-head span.note {
        font-size: 0.7rem;
        font-weight: 500;
        color: rgba(255,255,255,0.7);
    }

    .playlist-list {
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .playlist-item {
        background: rgba(0,0,0,0.45);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: var(--radius-md);
        padding: 12px 14px;
        box-shadow: 0 0 12px rgba(0,0,0,0.8), 0 0 20px rgba(0,200,255,0.3);
    }

    .playlist-label {
        font-size: 0.8rem;
        font-weight: 600;
        color: var(--accent-pink);
        text-shadow: 0 0 10px rgba(255,0,170,0.8), 0 0 24px rgba(255,0,170,0.5);
        margin-bottom: 4px;
        display: block;
    }

    .playlist-link {
        display: inline-block;
        font-size: 0.9rem;
        font-weight: 500;
        line-height: 1.3;
        color: #fff;
        text-decoration: none;
        word-break: break-word;
        border-radius: var(--radius-sm);
        padding: 6px 8px;
        background: rgba(255,0,170,0.08);
        border: 1px solid rgba(255,0,170,0.4);
        box-shadow: 0 0 16px rgba(255,0,170,0.6);
    }

    .playlist-link:active {
        background: rgba(255,0,170,0.22);
        box-shadow: 0 0 24px rgba(255,0,170,0.9);
    }

    /* ===============================
       DAILY STORY / HOLOGRAPHIC BLURB
       (placeholder content block, you can edit text in HTML)
       =============================== */
    .story-card {
        background: rgba(30,0,40,0.5);
        border: 1px solid rgba(255,0,255,0.5);
        border-radius: var(--radius-lg);
        padding: 16px 20px;
        box-shadow: var(--shadow-strong);
        backdrop-filter: blur(12px);
        color: #fff;
    }

    .story-headline {
        font-size: 1rem;
        font-weight: 600;
        color: #fff;
        text-shadow: 0 0 10px rgba(255,0,255,0.9);
        margin-bottom: 8px;
    }

    .story-text {
        font-size: 0.9rem;
        line-height: 1.4;
        color: rgba(255,255,255,0.9);
    }

    /* ===============================
       FLOATING BUBBLES LAYER
       =============================== */

    .bubbles-layer {
        position: fixed;
        inset: 0;
        overflow: hidden;
        z-index: 1; /* UNDER content but ABOVE background */
        pointer-events: none; /* bubbles should NOT block taps */
    }

    .bubble {
        position: absolute;
        border-radius: 50%;
        filter: blur(0px);
        opacity: 0.9;
        animation-name: drift;
        animation-timing-function: linear;
        animation-iteration-count: infinite;
        mix-blend-mode: screen;
        /* each bubble instance gets its own custom props below */
    }

    /* PURPLE bubble glow */
    .bubble.purple {
        color: rgba(255, 0, 255, 0.85);
        background: radial-gradient(
            circle,
            rgba(255, 0, 255, 0.7) 0%,
            rgba(255, 0, 255, 0.25) 40%,
            rgba(255, 0, 255, 0.05) 70%,
            transparent 100%
        );
        box-shadow: 0 0 20px rgba(255, 0, 255, 0.8);
    }

    /* BLUE bubble glow */
    .bubble.blue {
        color: rgba(80, 140, 255, 0.85);
        background: radial-gradient(
            circle,
            rgba(80, 140, 255, 0.7) 0%,
            rgba(80, 140, 255, 0.25) 40%,
            rgba(80, 140, 255, 0.05) 70%,
            transparent 100%
        );
        box-shadow: 0 0 20px rgba(80, 140, 255, 0.8);
    }

    /* WHITE bubble glow */
    .bubble.white {
        color: rgba(255, 255, 255, 0.9);
        background: radial-gradient(
            circle,
            rgba(255, 255, 255, 0.8) 0%,
            rgba(255, 255, 255, 0.3) 40%,
            rgba(255, 255, 255, 0.05) 70%,
            transparent 100%
        );
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.7);
    }

    /* slow upward float + slight sway + spin */
    @keyframes drift {
        0% {
            transform: translateY(100px) translateX(0) rotate(0deg) scale(1);
        }
        50% {
            transform: translateY(-80px) translateX(-20px) rotate(180deg) scale(1.07);
        }
        100% {
            transform: translateY(100px) translateX(0) rotate(360deg) scale(1);
        }
    }

    /* We'll assign size/pos/speed via inline style in JS */

    /* ===============================
       FOOTER / CREDIT
       =============================== */
    .footer {
        text-align: center;
        font-size: 0.7rem;
        color: rgba(255,255,255,0.5);
        line-height: 1.4;
        padding-bottom: 32px;
    }

    .footer span.brand {
        color: var(--accent-pink);
        text-shadow: 0 0 10px rgba(255,0,170,0.8);
        font-weight: 600;
    }

    /* iPhone safe-area breathing room on modern devices */
    @supports(padding:max(0px)) {
        body {
            padding-bottom: max(0px, env(safe-area-inset-bottom));
        }
        .app-shell {
            padding-bottom: max(80px, calc(env(safe-area-inset-bottom) + 40px));
        }
    }
</style>
</head>

<body>

    <!-- BUBBLES BACKGROUND LAYER -->
    <div class="bubbles-layer" id="bubbles-layer">
        <!-- bubbles get injected by JS -->
    </div>

    <!-- APP CONTENT -->
    <main class="app-shell">

        <!-- HERO / TITLE CARD -->
        <section class="hero-card">
            <div class="app-title">
                <div class="title-glow-dot"></div>
                <div>TimmyApp • Creator Mode</div>
            </div>
            <p class="tagline">
                Royalty-free vibe station. Neon sky. Local stories. No strikes, no drama —
                just press play and glow.
            </p>
        </section>

        <!-- MUSIC / PLAYLISTS -->
        <section class="section-card">
            <div class="section-head">
                <div>Playlists for Creators</div>
                <span class="note">No copyright. Use in background.</span>
            </div>

            <div class="playlist-list">

                <div class="playlist-item">
                    <span class="playlist-label">Playlist 1</span>
                    <a class="playlist-link"
                       href="https://suno.com/playlist/2ec04889-1c23-4e2d-9c27-8a2b6475da4b"
                       target="_blank" rel="noopener noreferrer">
                       suno.com/playlist/2ec04889...
                    </a>
                </div>

                <div class="playlist-item">
                    <span class="playlist-label">Song / Track</span>
                    <a class="playlist-link"
                       href="https://suno.com/song/c0943681-4a5f-48f0-9e18-5c8bf5b24e8d"
                       target="_blank" rel="noopener noreferrer">
                       suno.com/song/c0943681...
                    </a>
                </div>

                <div class="playlist-item">
                    <span class="playlist-label">Medicine Bag Inspo</span>
                    <a class="playlist-link"
                       href="https://www.nativecrafts.us/medicine-bags-c-164.html"
                       target="_blank" rel="noopener noreferrer">
                       nativecrafts.us/medicine-bags...
                    </a>
                </div>

                <div class="playlist-item">
                    <span class="playlist-label">Playlist 4</span>
                    <a class="playlist-link"
                       href="https://suno.com/playlist/01b65a04-d231-4574-bbb6-713997ca5b44"
                       target="_blank" rel="noopener noreferrer">
                       suno.com/playlist/01b65a04...
                    </a>
                </div>

                <div class="playlist-item">
                    <span class="playlist-label">Playlist 5</span>
                    <a class="playlist-link"
                       href="https://suno.com/playlist/457d7e00-938e-4bf0-bd59-f070729200df"
                       target="_blank" rel="noopener noreferrer">
                       suno.com/playlist/457d7e00...
                    </a>
                </div>

            </div>
        </section>

        <!-- DAILY STORY / HOLOGRAPHIC CARD -->
        <section class="story-card">
            <div class="story-headline">
                Daily Story • Hologram Drop
            </div>
            <div class="story-text">
                Tonight in the glow dome: creators get free beats, Ragland gets a signal,
                and the Yeti says “we broadcasting now.” Keep scrolling tomorrow —
                this box updates every day.
            </div>
        </section>

        <!-- FOOTER -->
        <footer class="footer">
            <div><span class="brand">TimmyApp</span> — live beta</div>
            <div>All vibes are community safe-use / creator friendly.</div>
        </footer>

    </main>

<script>
/*
   BUBBLE GENERATOR
   We create a handful of bubbles with random:
   - size
   - start position
   - animation duration (speed)
   - delay (desync motion)

   They float with the @keyframes drift and never block taps.
*/

(function makeBubbles() {
    const layer = document.getElementById('bubbles-layer');

    // you can tune how many / which colors here:
    const bubbleConfigs = [
        { colorClass: 'purple', count: 4 },
        { colorClass: 'blue',   count: 3 },
        { colorClass: 'white',  count: 2 }
    ];

    const vw = window.innerWidth;
    const vh = window.innerHeight;

    bubbleConfigs.forEach(cfg => {
        for (let i = 0; i < cfg.count; i++) {
            const bub = document.createElement('div');
            bub.className = 'bubble ' + cfg.colorClass;

            // random size 60px - 200px
            const size = Math.floor(60 + Math.random() * 140);

            // random horizontal start %
            const leftPx = Math.floor(Math.random() * vw);

            // random vertical base (so they don't all start same height)
            const topPx = Math.floor(Math.random() * vh);

            // random duration (slower feels floaty). between 10s and 22s
            const duration = (10 + Math.random() * 12).toFixed(2) + 's';

            // random delay so they don't sync
            const delay = (-Math.random() * 10).toFixed(2) + 's';

            bub.style.width = size + 'px';
            bub.style.height = size + 'px';
            bub.style.left = leftPx + 'px';
            bub.style.top = topPx + 'px';
            bub.style.opacity = 0.8 + Math.random() * 0.2;

            bub.style.animationDuration = duration;
            bub.style.animationDelay = delay;

            layer.appendChild(bub);
        }
    });
})();
</script>

</body>
</html>
