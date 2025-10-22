(function(){
  const quiz = document.getElementById('quiz');
  const checkBtn = document.getElementById('check');
  const scoreEl = document.getElementById('score');

  function rand(a,b){ return Math.floor(a + Math.random()*(b-a+1)); }

  function buildExpr(){
    // (a + b) * c - d or a + b * (c - d) style
    const a=rand(2,9), b=rand(2,9), c=rand(2,9), d=rand(1,8);
    const forms = [
      `(${a} + ${b}) * ${c} - ${d}`,
      `${a} + ${b} * (${c} - ${d})`,
      `(${a} * ${b}) + ${c} - ${d}`,
      `${a} * (${b} + ${c}) - ${d}`,
      `${a} + (${b} - ${d}) * ${c}`
    ];
    return forms[rand(0,forms.length-1)];
  }

  function evalSafe(expr){
    // Only digits + ops + spaces + parentheses allowed
    if(!/^[\d\s()+\-*/]+$/.test(expr)) return null;
    // eslint-disable-next-line no-new-func
    return Function(`"use strict";return (${expr});`)();
  }

  const problems = Array.from({length:5}, ()=> buildExpr()).map((expr, i) => {
    const correct = evalSafe(expr);
    // build choices around correct
    const choices = new Set([correct]);
    while(choices.size < 4){
      const delta = rand(-5,5);
      if(delta!==0) choices.add(correct + delta);
    }
    const arr = Array.from(choices).sort(()=>Math.random()-0.5);

    const wrap = document.createElement('div');
    wrap.className = 'tile span-12';
    wrap.innerHTML = `
      <h2>#${i+1} &nbsp;<code>${expr}</code></h2>
      <select data-answer="${correct}">
        ${arr.map(x => `<option value="${x}">${x}</option>`).join('')}
      </select>
    `;
    quiz.appendChild(wrap);
    return wrap;
  });

  checkBtn.addEventListener('click', () => {
    let correct=0;
    problems.forEach(p=>{
      const sel = p.querySelector('select');
      const ans = Number(sel.value);
      const need = Number(sel.dataset.answer);
      if(ans===need){ correct++; p.style.borderColor='rgba(0,255,140,.8)'; }
      else{ p.style.borderColor='rgba(255,60,60,.8)'; }
    });
    scoreEl.textContent = `Score: ${correct}/5`;
  });
})();
