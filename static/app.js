// Simple floating bubbles on a full-screen canvas (no external libs)
const canvas = document.getElementById('bubbles');
const ctx = canvas.getContext('2d');

let W, H, bubbles = [];

function resize() {
  W = canvas.width = window.innerWidth;
  H = canvas.height = window.innerHeight;
}
window.addEventListener('resize', resize);
resize();

function makeBubble() {
  const r = 6 + Math.random()*18;
  return {
    x: Math.random()*W,
    y: H + r + Math.random()*H*0.4,
    r,
    vy: 0.6 + Math.random()*1.6,
    sway: (Math.random()*1.5 + 0.5) * (Math.random() < 0.5 ? -1 : 1),
    hue: 280 + Math.random()*80 // purple-pink range
  };
}

for (let i = 0; i < 60; i++) bubbles.push(makeBubble());

function tick() {
  ctx.clearRect(0, 0, W, H);

  for (const b of bubbles) {
    b.y -= b.vy;
    b.x += Math.sin((Date.now()/600 + b.y/80)) * (b.sway*0.08);

    const g = ctx.createRadialGradient(b.x, b.y, b.r*0.2, b.x, b.y, b.r);
    g.addColorStop(0, `hsla(${b.hue}, 90%, 70%, .95)`);
    g.addColorStop(1, `hsla(${b.hue}, 90%, 50%, .05)`);

    ctx.beginPath();
    ctx.fillStyle = g;
    ctx.arc(b.x, b.y, b.r, 0, Math.PI*2);
    ctx.fill();

    if (b.y < -b.r - 10) {
      Object.assign(b, makeBubble(), { y: H + b.r + Math.random()*H*0.3 });
    }
  }

  requestAnimationFrame(tick);
}
tick();
