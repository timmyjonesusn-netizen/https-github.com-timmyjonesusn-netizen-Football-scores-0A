(function(){
  const c = document.getElementById('bubbles');
  if(!c) return;
  const dpr = Math.max(1, Math.min(2, window.devicePixelRatio || 1));
  const ctx = c.getContext('2d');
  let W, H, bubbles;

  function resize(){
    W = c.width = Math.floor(innerWidth * dpr);
    H = c.height = Math.floor(innerHeight * dpr);
    c.style.width = innerWidth + 'px';
    c.style.height = innerHeight + 'px';
    spawn();
  }

  function spawn(){
    const n = Math.floor(Math.min(40, Math.max(20, (W*H)/120000)));
    bubbles = Array.from({length:n}, _ => ({
      x: Math.random()*W,
      y: Math.random()*H,
      r: Math.random()*18*dpr + 6*dpr,
      vx: (Math.random()*0.2 - 0.1) * dpr,
      vy: (-Math.random()*0.35 - 0.05) * dpr,
      o: Math.random()*0.5 + 0.25
    }));
  }

  function tick(){
    ctx.clearRect(0,0,W,H);
    for(const b of bubbles){
      b.x += b.vx; b.y += b.vy;
      if(b.y < -40*dpr || b.x < -40*dpr || b.x > W+40*dpr){
        b.x = Math.random()*W; b.y = H + 20*dpr;
      }
      // glow gradient
      const g = ctx.createRadialGradient(b.x, b.y, 0, b.x, b.y, b.r);
      g.addColorStop(0, `rgba(255,255,255,${0.25*b.o})`);
      g.addColorStop(1, `rgba(176,124,255,0)`);
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.arc(b.x, b.y, b.r, 0, Math.PI*2);
      ctx.fill();

      ctx.beginPath();
      ctx.arc(b.x, b.y, b.r*0.6, 0, Math.PI*2);
      ctx.strokeStyle = `rgba(255,107,214,${0.15*b.o})`;
      ctx.lineWidth = 1.2*dpr;
      ctx.stroke();
    }
    requestAnimationFrame(tick);
  }

  window.addEventListener('resize', resize, {passive:true});
  resize();
  tick();
})();
