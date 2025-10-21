// Whodunnit reveal
document.getElementById("reveal").addEventListener("click", () => {
  const who = document.getElementById("who").value;
  const verdict = document.getElementById("verdict");
  if(!who){ verdict.textContent = "Pick a suspect, Detective."; return; }

  const lines = {
    dee: "Coach Dee? Possible — strong legs for the ladder. But no glitter paw prints in the weight room.",
    jasmine: "Jasmine has keys, yes — but she hates funnel cake. Motive weak.",
    buck: "Uncle Buck night-fishes… and smells like it. But those paw prints? Not his style.",
    reggie: "Reggie the Dog 😎 — glitter paws, donut leverage, and ‘ten-four’ on the audio. Case closed, Chief."
  };
  verdict.textContent = lines[who] || "Hmm… inconclusive.";
});

// Riddle checks
document.querySelectorAll('.card select').forEach(sel=>{
  sel.addEventListener('change', e=>{
    const a = e.target.dataset.answer;
    const out = e.target.parentElement.querySelector('.result');
    if(!e.target.value){ out.textContent = ""; return; }
    if(e.target.value === a){
      out.innerHTML = "<span class='correct'>✅ Correct!</span>";
    }else{
      out.innerHTML = "<span class='wrong'>❌ Not quite — try again.</span>";
    }
  });
});
