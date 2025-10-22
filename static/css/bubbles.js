// Lightweight canvas bubbles — stable & battery-friendly
(function () {
  const canvas = document.getElementById('bubbles');
  const ctx = canvas.getContext('2d', { alpha: true });

  let W = canvas.width = window.innerWidth;
  let H = canvas.height = window.innerHeight;

  const N = Math.min(80, Math.floor((W * H) / 30000)); // scale to screen
  const bubbles = [];

  function rand(min, max) { return Math.random() * (max - min) + min; }

  for (let i = 0; i < N; i++) {
    bubbles.push({
      x: rand(0, W),
      y: rand(0, H),
      r: rand(6, 22),
      a: rand(0.25, 0.9),
      vx: rand(-0.15, 0.15),
      vy: rand(-0.35, -0.05),  // gentle rise
      hue: rand(260, 320)      // purple → pink
    });
  }

  function resize() {
    W = canvas.width = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }
  window.addEventListener('resize', resize, { passive: true });

  function tick() {
    ctx.clearRect(0, 0, W, H);

    for (const b of bubbles) {
      b.x += b.vx;
      b.y += b.vy;

      // wrap around
      if (b.y + b.r < 0) { b.y = H + b.r; b.x = rand(0, W); }
      if (b.x - b.r > W) b.x = -b.r;
      if (b.x + b.r < 0) b.x = W + b.r;

      const grad = ctx.createRadialGradient(b.x, b.y, 1, b.x, b.y, b.r);
      grad.addColorStop(0, `hsla(${b.hue}, 90%, 70%, ${b.a})`);
      grad.addColorStop(1, `hsla(${b.hue}, 90%, 50%, 0)`);

      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
      ctx.fill();
    }

    requestAnimationFrame(tick);
  }

  tick();
})();
