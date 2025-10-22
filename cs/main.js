// Bubble background (no external libs, smooth on iPhone)
(function () {
  var c = document.getElementById("bubble-canvas");
  if (!c) return;
  var ctx = c.getContext("2d");
  var bubbles = [];
  var w, h, dpr = Math.max(1, window.devicePixelRatio || 1);

  function resize() {
    w = window.innerWidth; h = window.innerHeight;
    c.width = Math.floor(w * dpr);
    c.height = Math.floor(h * dpr);
    c.style.width = w + "px";
    c.style.height = h + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  window.addEventListener("resize", resize);
  resize();

  function spawn() {
    var r = 6 + Math.random() * 24;
    bubbles.push({
      x: Math.random() * w,
      y: h + r + Math.random() * h * 0.2,
      r: r,
      vy: -0.4 - Math.random() * 0.7,
      vx: (Math.random() - 0.5) * 0.3,
      alpha: 0.3 + Math.random() * 0.4
    });
    if (bubbles.length > 120) bubbles.shift();
  }

  function tick() {
    ctx.clearRect(0, 0, w, h);
    // soft glow backdrop to amplify purple/pink
    var grd = ctx.createRadialGradient(w*0.2, h*0.1, 0, w*0.2, h*0.1, Math.max(w,h)*0.6);
    grd.addColorStop(0, "rgba(255,158,252,0.08)");
    grd.addColorStop(1, "rgba(0,0,0,0)");
    ctx.fillStyle = grd;
    ctx.fillRect(0,0,w,h);

    for (var i=0;i<bubbles.length;i++){
      var b = bubbles[i];
      b.x += b.vx;
      b.y += b.vy;
      if (b.y + b.r < -20) {
        bubbles.splice(i, 1); i--; continue;
      }
      ctx.beginPath();
      ctx.arc(b.x, b.y, b.r, 0, Math.PI*2);
      ctx.closePath();
      ctx.fillStyle = "rgba(255, 158, 252, " + b.alpha + ")";
      ctx.fill();
      ctx.lineWidth = 1;
      ctx.strokeStyle = "rgba(179, 136, 255, 0.6)";
      ctx.stroke();
    }
    if (Math.random() < 0.6) spawn();
    requestAnimationFrame(tick);
  }
  tick();
})();
