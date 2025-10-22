(() => {
  const c = document.getElementById('bubbles');
  const ctx = c.getContext('2d');
  let W, H, dpr;
  const bubbles = [];
  const N = 35;

  function resize() {
    dpr = window.devicePixelRatio || 1;
    W = c.width = innerWidth * dpr;
    H = c.height = innerHeight * dpr;
    c.style.width = innerWidth + "px";
    c.style.height = innerHeight + "px";
  }
  window.addEventListener('resize', resize);
  resize();

  function rand(a,b){return a+Math.random()*(b-a);}
  function newB() {
    const r = rand(10,60)*dpr;
    return {
      x: rand(r, W-r),
      y: rand(r, H-r),
      r,
      vx: rand(-0.1,0.1)*dpr,
      vy: -rand(0.2,0.8)*dpr,
      hue: rand(285,320),
      alpha: rand(0.15,0.35)
    };
  }
  for(let i=0;i<N;i++) bubbles.push(newB());

  function draw(b){
    const g = ctx.createRadialGradient(b.x,b.y,b.r*0.1,b.x,b.y,b.r);
    g.addColorStop(0,`hsla(${b.hue},80%,70%,${b.alpha})`);
    g.addColorStop(1,`hsla(${b.hue},80%,20%,0)`);
    ctx.fillStyle=g;
    ctx.beginPath();
    ctx.arc(b.x,b.y,b.r,0,Math.PI*2);
    ctx.fill();
  }

  function step(){
    ctx.clearRect(0,0,W,H);
    for(const b of bubbles){
      b.x+=b.vx; b.y+=b.vy;
      if(b.y+b.r<0){Object.assign(b,newB(),{y:H+b.r});}
      if(b.x-b.r<0||b.x+b.r>W) b.vx*=-1;
      draw(b);
    }
    requestAnimationFrame(step);
  }
  step();
})();
