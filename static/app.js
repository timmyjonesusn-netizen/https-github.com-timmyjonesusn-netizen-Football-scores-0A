// ===== Blue & White Bubbles: fewer, brighter, relaxed drift =====
(function(){
  const cvs = document.getElementById('bubbles');
  if(!cvs) return;
  const ctx = cvs.getContext('2d');
  let W, H, bubbles, raf;

  // Accents: ~20% blue, ~10% white. Purple stays in CSS background.
  const COLORS = ['#ffffff', '#dfeeff', '#cfe1ff', '#99c3ff']; // white + blues
  const COUNT  = 14;  // fewer bubbles
  const MAX_R  = 26;  // larger, brighter
  const SPEED  = 0.45;

  function resize(){
    W = cvs.width  = window.innerWidth;
    H = cvs.height = window.innerHeight;
  }
  function makeBubble(){
    const r = Math.random()*(MAX_R-8)+8;
    return {
      x: Math.random()*W,
      y: Math.random()*H,
      r,
      vy: 0.12 + Math.random()*SPEED*0.6,   // relaxed rise
      vx: (Math.random()-.5)*0.15,          // gentle drift
      c: COLORS[(Math.random()*COLORS.length)|0],
      a: .35 + Math.random()*.25            // brighter alpha
    };
  }
  function init(){ bubbles = Array.from({length: COUNT}, makeBubble); }
  function tick(){
    ctx.clearRect(0,0,W,H);
    for(const b of bubbles){
      b.y -= b.vy; b.x += b.vx;
      if(b.y + b.r < -10){ b.y = H + b.r + 10; b.x = Math.random()*W; }
      const grad = ctx.createRadialGradient(b.x, b.y, b.r*0.1, b.x, b.y, b.r);
      grad.addColorStop(0, b.c);
      grad.addColorStop(1, 'rgba(255,255,255,0)');
      ctx.globalAlpha = b.a;
      ctx.beginPath(); ctx.arc(b.x, b.y, b.r, 0, Math.PI*2);
      ctx.fillStyle = grad; ctx.fill();
    }
    ctx.globalAlpha = 1;
    raf = requestAnimationFrame(tick);
  }
  window.addEventListener('resize', resize);
  resize(); init(); tick();
})();

// ===== Weather traffic lights (safe global) =====
// Expected (optional) markup:
// <div id="wx-data" data-wind-mph="17" data-has-alert="false"></div>
(function(){
  const dataEl = document.getElementById('wx-data');
  if(!dataEl) return;
  const wind = Number(dataEl.dataset.windMph || 0);
  const hasAlert = (dataEl.dataset.hasAlert || 'false') === 'true';

  let state = 'green';
  if (hasAlert || wind >= 40) state = 'red';
  else if (wind >= 20) state = 'yellow';

  const on = id => { const el = document.getElementById(id); el && el.classList.add('on'); };
  if (state === 'red') on('sig-red');
  else if (state === 'yellow') on('sig-yellow');
  else on('sig-green');

  const text = document.getElementById('wx-text');
  if(text){
    const msg = hasAlert ? '⚠️ Alert in effect' :
                state==='red' ? `High winds (${wind} mph)` :
                state==='yellow' ? `Breezy (${wind} mph)` :
                `Calm (${wind} mph)`;
    text.textContent = msg;
  }
})();

// ===== Robot button stub (wire to your assistant when ready) =====
(function(){
  const fab = document.getElementById('robotFab');
  if(!fab) return;
  fab.addEventListener('click', () => {
    // Replace with your robot action (modal/route/etc.)
    alert("Robot ready for service 🤖");
  });
})();
