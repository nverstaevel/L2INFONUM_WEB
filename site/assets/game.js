// "Squash the bug": a small break between two exercises. Plain JavaScript, no library.
addEventListener("DOMContentLoaded", () => {
  const T = {
    en: {
      start: "Start", again: "Play again", empty: "Empty hole", bug: "Bug", gold: "Golden bug", feature: "Feature",
      ready: "Press Start. Squash the bugs, spare the features.",
      go: "Go!",
      hit: ["Squashed.", "It works on my machine now.", "One less ticket.", "Clean commit!"],
      golden: "Golden bug! The one nobody could reproduce. +3",
      oops: ["That was a feature! −2", "The client wanted that one. −2", "You deleted production. −2"],
      end: s => `Time! Score: ${s}. `,
      ranks: [[0, "Rank: the bug was you."], [8, "Rank: intern who reads the error message."],
              [16, "Rank: solid debugger."], [24, "Rank: the whole room calls you for help."]]
    },
    fr: {
      start: "Commencer", again: "Rejouer", empty: "Trou vide", bug: "Bug", gold: "Bug doré", feature: "Fonctionnalité",
      ready: "Appuyez sur Commencer. Écrasez les bugs, épargnez les fonctionnalités.",
      go: "C'est parti !",
      hit: ["Écrasé.", "Maintenant ça marche sur ma machine.", "Un ticket de moins.", "Commit propre !"],
      golden: "Bug doré ! Celui que personne n'arrivait à reproduire. +3",
      oops: ["C'était une fonctionnalité ! −2", "Le client y tenait. −2", "Vous avez effacé la production. −2"],
      end: s => `Terminé ! Score : ${s}. `,
      ranks: [[0, "Grade : le bug, c'était vous."], [8, "Grade : stagiaire qui lit le message d'erreur."],
              [16, "Grade : débogueur solide."], [24, "Grade : toute la salle vous appelle à l'aide."]]
    }
  }[document.documentElement.lang];
  const ICON = { bug: "🐛", gold: "🪲", feature: "✨" };
  const $ = id => document.getElementById(id);
  const holes = [...document.querySelectorAll(".hole")];
  const pick = list => list[Math.floor(Math.random() * list.length)];
  let score = 0, left = 0, clock = null, spawner = null;

  const read = () => { try { return Number(localStorage.getItem("best-bugs")) || 0; } catch (e) { return 0; } };
  const save = v => { try { localStorage.setItem("best-bugs", v); } catch (e) {} };

  function clear(hole) {
    clearTimeout(hole.timer);
    delete hole.dataset.kind;
    hole.querySelector(".thing").textContent = "";
    hole.setAttribute("aria-label", `${hole.dataset.n}: ${T.empty}`);
  }

  function spawn() {
    const calm = $("calm").checked;
    const free = holes.filter(h => !h.dataset.kind);
    if (free.length) {
      const hole = pick(free), r = Math.random();
      const kind = r < 0.1 ? "gold" : r < 0.32 ? "feature" : "bug";
      hole.dataset.kind = kind;
      hole.querySelector(".thing").textContent = ICON[kind];
      hole.setAttribute("aria-label", `${hole.dataset.n}: ${T[kind]}`);
      hole.timer = setTimeout(() => clear(hole), calm ? 2600 : kind === "gold" ? 800 : 1100);
    }
    const wait = calm ? 1300 : 420 + left * 12;       // faster and faster
    spawner = setTimeout(spawn, wait);
  }

  function squash(hole) {
    const kind = hole.dataset.kind;
    if (!left || !kind) return;
    if (kind === "feature") { score -= 2; $("say").textContent = pick(T.oops); }
    else if (kind === "gold") { score += 3; $("say").textContent = T.golden; }
    else { score += 1; $("say").textContent = pick(T.hit); }
    clear(hole);
    hole.querySelector(".thing").textContent = kind === "feature" ? "😱" : "💥";
    hole.timer = setTimeout(() => clear(hole), 250);
    $("score").textContent = score;
  }

  function stop() {
    clearInterval(clock);
    clearTimeout(spawner);
    holes.forEach(clear);
    if (score > read()) save(score);
    $("best").textContent = read();
    const rank = T.ranks.filter(([min]) => score >= min).pop() || T.ranks[0];
    $("say").textContent = T.end(score) + rank[1];
    $("start").textContent = T.again;
    $("start").disabled = false;
  }

  $("start").onclick = () => {
    score = 0; left = 30;
    $("score").textContent = 0; $("time").textContent = left; $("say").textContent = T.go;
    $("start").disabled = true;
    document.querySelector(".game").scrollIntoView({ block: "start" });   // keep the board in view
    spawn();
    clock = setInterval(() => {
      left -= 1;
      $("time").textContent = left;
      if (!left) stop();
    }, 1000);
  };

  holes.forEach((hole, i) => {
    hole.dataset.n = i + 1;
    clear(hole);
    hole.onclick = () => squash(hole);
  });
  addEventListener("keydown", e => {                   // keys 1 to 9
    if (!e.ctrlKey && !e.metaKey && !e.altKey && /^[1-9]$/.test(e.key)) squash(holes[Number(e.key) - 1]);
  });
  $("best").textContent = read();
  $("start").textContent = T.start;
  $("say").textContent = T.ready;
});
