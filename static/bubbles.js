(()=> {
  const c = document.getElementById('bubbles');
  const ctx = c.getContext('2d', { alpha: true });
  let W, H, dpr;
  const N = 36;
  const bubbles = [];

  function resize(){
    dpr = window.devicePixelRatio || 1;
    W = c.width = Math.floor(innerWidth * dpr);
    H = c.height = Math.floor(innerHeight * dpr);
    c.style.width = innerWidth + 'px';
    c.style.height = innerHeight + 'px';
  }
  addEventListener('resize', resize, { passive:true }); resize();

  const RMIN=10, RMAX=70;
  function rnd(a,b){ return a + Math.random()*(b-a); }
  function make(){
    const r = rnd(RMIN,RMAX)*dpr;
    return { x:rnd(r,W-r), y:rnd(r,H-r), r, vx:rnd(-0.12,0.12)*dpr, vy:-rnd(0.2,0.9)*dpr, hue:rnd(285,320), a:rnd(0.15,0.35), t:rnd(0,6.28) };
  }
  for(let i=0;i<N;i++) bubbles.push(make());

  function draw(b){
    const g = ctx.createRadialGradient(b.x,b.y,b.r*0.1,b.x,b.y,b.r);
    g.addColorStop(0,`hsla(${b.hue},80%,70%,${b.a})`);
    g.addColorStop(1,`hsla(${b.hue},80%,20%,0)`);
    ctx.fillStyle=g; ctx.beginPath(); ctx.arc(b.x,b.y,b.r,0,Math.PI*2); ctx.fill();

    ctx.beginPath();
    ctx.arc(b.x-b.r*0.25,b.y-b.r*0.25,b.r*0.45,0,Math.PI*2);
    ctx.fillStyle=`hsla(${b.hue},85%,85%,${b.a*0.6})`; ctx.fill();
  }

  function tick(){
    ctx.clearRect(0,0,W,H);
    for(const b of bubbles){
      b.t += 0.015;
      b.x += b.vx + Math.sin(b.t)*0.2*dpr;
      b.y += b.vy + Math.cos(b.t*0.8)*0.1*dpr;
      if(b.y + b.r < 0){ Object.assign(b, make(), { y: H + b.r }); }
      if(b.x - b.r < 0 || b.x + b.r > W) b.vx *= -1;
      draw(b);
    }
    requestAnimationFrame(tick);
  }
  tick();
})();
