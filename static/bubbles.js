// Minimal, smooth, random-speed bubbles (performance-friendly)
(function () {
  const c = document.getElementById('bubbles');
  const x = c.getContext('2d');
  let W, H, B = [];

  function resize() {
    W = c.width = window.innerWidth;
    H = c.height = window.innerHeight;
  }
  window.addEventListener('resize', resize);
  resize();

  function spawn() {
    const n = 24; // bubble count
    B = new Array(n).fill(0).map(() => ({
      x: Math.random() * W,
      y: H + Math.random() * H,
      r: 4 + Math.random() * 18,
      s: 0.4 + Math.random() * 1.6, // speed
      drift: (Math.random() * 0.6) - 0.3,
      a: 0.15 + Math.random() * 0.35
    }));
  }
  spawn();

  function tick() {
    x.clearRect(0, 0, W, H);
    for (const b of B) {
      b.y -= b.s;
      b.x += b.drift;
      if (b.y + b.r < -20) { // recycle to bottom
        b.y = H + 20;
        b.x = Math.random() * W;
      }
      x.beginPath();
      const g = x.createRadialGradient(b.x, b.y, 0, b.x, b.y, b.r);
      g.addColorStop(0, 'rgba(255,79,216,' + (b.a + 0.25) + ')'); // pink glow core
      g.addColorStop(1, 'rgba(255,255,255,0)');
      x.fillStyle = g;
      x.arc(b.x, b.y, b.r, 0, Math.PI * 2);
      x.fill();
    }
    requestAnimationFrame(tick);
  }
  tick();
})();
