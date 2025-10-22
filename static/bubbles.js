// Floating holographic bubbles using canvas (mobile-friendly, battery-light)
(() => {
  const c = document.getElementById('bubbles');
  const ctx = c.getContext('2d', { alpha: true });
  let W, H, dpr;

  const bubbles = [];
  const N = 36;                 // number of bubbles
  const SPEED = 0.25;           // base speed
  const R_MIN = 10, R_MAX = 70; // radius range

  function resize() {
    dpr = window.devicePixelRatio || 1;
    W = c.width = Math.floor(innerWidth * dpr);
    H = c.height = Math.floor(innerHeight * dpr);
    c.style.width = innerWidth + 'px';
    c.style.height = innerHeight + 'px';
  }
  window.addEventListener('resize', resize, { passive: true });
  resize();

  function rand(a, b) { return a + Math.random() * (b - a); }

  function makeBubble() {
    const r = rand(R_MIN, R_MAX) * dpr;
    const x = rand(r, W - r);
    const y = rand(r, H - r);
    const vy = -rand(SPEED * 0.2, SPEED * 1.2) * dpr; // upward drift
    const vx = rand(-0.15, 0.15) * dpr;               // sideways wobble
    const hue = rand(285, 320); // purple-pink band
    const sat = rand(65, 95);
    const alp = rand(0.18, 0.38);
    return { x, y, r, vx, vy, hue, sat, alp, t: rand(0, Math.PI * 2) };
  }

  for (let i = 0; i < N; i++) bubbles.push(makeBubble());

  function drawBubble(b) {
    // outer soft glow
    const g = ctx.createRadialGradient(b.x, b.y, b.r * 0.1, b.x, b.y, b.r);
    g.addColorStop(0, `hsla(${b.hue}, ${b.sat}%, 65%, ${b.alp})`);
    g.addColorStop(1, `hsla(${b.hue}, ${b.sat}%, 10%, 0)`);
    ctx.fillStyle = g;
    ctx.beginPath();
    ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
    ctx.fill();

    // inner highlight
    ctx.beginPath();
    ctx.arc(b.x - b.r * 0.25, b.y - b.r * 0.25, b.r * 0.45, 0, Math.PI * 2);
    ctx.fillStyle = `hsla(${b.hue}, ${b.sat}%, 85%, ${b.alp * 0.65})`;
    ctx.fill();
  }

  function step(ts) {
    ctx.clearRect(0, 0, W, H);
    for (const b of bubbles) {
      // gentle wobble
      b.t += 0.015;
      b.x += b.vx + Math.sin(b.t) * 0.2 * dpr;
      b.y += b.vy + Math.cos(b.t * 0.8) * 0.1 * dpr;

      // wrap to bottom once leaving the top
      if (b.y + b.r < 0) {
        const nb = makeBubble();
        b.x = nb.x; b.y = H + nb.r; b.r = nb.r;
        b.vx = nb.vx; b.vy = nb.vy; b.hue = nb.hue; b.sat = nb.sat; b.alp = nb.alp; b.t = nb.t;
      }

      // keep inside horizontal bounds
      if (b.x - b.r < 0 || b.x + b.r > W) b.vx *= -1;

      drawBubble(b);
    }
    requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
})();
