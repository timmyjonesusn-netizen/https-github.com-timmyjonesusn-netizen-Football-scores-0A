# serv_timmyapp.py — SINGLE FILE, NO STATIC FOLDERS NEEDED
from flask import Flask, Response

HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>TimmyApp — Purple-Pink Glow</title>
  <meta name="theme-color" content="#7b2cff">
  <style>
    *{box-sizing:border-box;margin:0;padding:0}
    html,body{height:100%;background:
      radial-gradient(1200px 800px at 20% 10%, rgba(255,105,180,.25), transparent 60%),
      radial-gradient(900px 700px at 80% 80%, rgba(147,112,219,.25), transparent 60%),
      #0c0320;
      color:#fff;font-family:-apple-system,system-ui,Segoe UI,Roboto,Arial,sans-serif;
      overflow:hidden}
    #bubbles{position:fixed;inset:0;z-index:0}
    .wrap{position:relative;z-index:1;max-width:960px;margin:7vh auto;padding:24px;text-align:center}
    h1{font-size:48px;letter-spacing:.5px;text-shadow:0 0 18px rgba(255,105,180,.6),0 0 36px rgba(147,112,219,.5)}
    .tag{margin-top:8px;opacity:.9}
    .cards{margin:28px auto 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;width:100%}
    .card{display:block;padding:16px;border-radius:14px;background:rgba(255,255,255,.06);
      border:1px solid rgba(255,255,255,.12);backdrop-filter:blur(6px);text-decoration:none;color:#fff;
      transition:transform .2s ease, box-shadow .2s ease, background .2s ease;
      box-shadow:0 8px 28px rgba(123,44,255,.16), inset 0 0 0 1px rgba(255,255,255,.06)}
    .card h2{font-size:20px;margin-bottom:6px}
    .card p{font-size:14px;opacity:.92}
    .card:hover{transform:translateY(-4px);box-shadow:0 18px 44px rgba(255,105,180,.28);background:rgba(255,255,255,.10)}
    footer{margin-top:26px;opacity:.85;font-size:13px}
  </style>
</head>
<body>
  <canvas id="bubbles" aria-hidden="true"></canvas>
  <main class="wrap">
    <h1>TimmyApp</h1>
    <p class="tag">purple + pink holographic goodness — if it’s not glowing, it’s not going.</p>

    <section class="cards">
      <a class="card" href="https://suno.com/playlist/2ec04889-1c23-4e2d-9c27-8a2b6475da4b" target="_blank" rel="noopener">
        <h2>Creator Playlist A</h2><p>Royalty-friendly vibes for reels.</p>
      </a>
      <a class="card" href="https://suno.com/playlist/e95ddd12-7e37-43e2-b3e0-fe342085a19f" target="_blank" rel="noopener">
        <h2>Creator Playlist B</h2><p>Energy up, strikes down.</p>
      </a>
      <a class="card" href="https://suno.com/playlist/2e2eefa6-6828-40ba-bf5b-02bf338e3243" target="_blank" rel="noopener">
        <h2>Creator Playlist C</h2><p>No copyright drama—just flow.</p>
      </a>
    </section>

    <footer><span>Share: <strong>https://timmyapp.onrender.com/</strong></span></footer>
  </main>

  <script>
    // Neon bubbles (no libs)
    const c=document.getElementById('bubbles'),x=c.getContext('2d');
    let W,H,B=[];
    function size(){W=c.width=innerWidth;H=c.height=innerHeight}
    addEventListener('resize',size); size();

    function bubble(){
      const r=6+Math.random()*18;
      return {x:Math.random()*W,y:H+r+Math.random()*H*.4,r,
              vy:.6+Math.random()*1.6,
              sway:(Math.random()*1.5+.5)*(Math.random()<.5?-1:1),
              hue:280+Math.random()*80};
    }
    for(let i=0;i<60;i++)B.push(bubble());

    (function loop(){
      x.clearRect(0,0,W,H);
      for(const b of B){
        b.y-=b.vy;
        b.x+=Math.sin((Date.now()/600+b.y/80))*(b.sway*.08);
        const g=x.createRadialGradient(b.x,b.y,b.r*.2,b.x,b.y,b.r);
        g.addColorStop(0,`hsla(${b.hue},90%,70%,.95)`);
        g.addColorStop(1,`hsla(${b.hue},90%,50%,.06)`);
        x.beginPath(); x.fillStyle=g; x.arc(b.x,b.y,b.r,0,Math.PI*2); x.fill();
        if(b.y<-b.r-10) Object.assign(b,bubble(),{y:H+b.r+Math.random()*H*.3});
      }
      requestAnimationFrame(loop);
    })();
  </script>
</body>
</html>"""

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return Response(HTML, mimetype="text/html")

    @app.route("/health")
    def health():
        return "ok", 200

    return app
