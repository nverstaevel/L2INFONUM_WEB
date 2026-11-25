const store = {
  get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
  set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
};
const root = document.documentElement;
root.dataset.theme = store.get("theme") || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
addEventListener("DOMContentLoaded", () => {
  document.getElementById("theme").onclick = () => {
    root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
    store.set("theme", root.dataset.theme);
  };
  // progress boxes: same key in both languages
  document.querySelectorAll("main input[type=checkbox]").forEach((box, i) => {
    const key = "done:" + location.pathname.split("/").pop() + ":" + i;
    box.checked = store.get(key) === "1";
    box.onchange = () => store.set(key, box.checked ? "1" : "0");
  });
  const fit = () => document.querySelectorAll(".frame").forEach(f => {
    f.firstElementChild.style.transform = `scale(${f.clientWidth / 1920})`;
  });
  addEventListener("resize", fit);
  fit();
  // phone: scroll the one-line menu to the current section
  const here = document.querySelector(".menu a[aria-current]");
  if (here) {
    const strip = here.closest(".bar");
    strip.scrollLeft = here.getBoundingClientRect().left - strip.getBoundingClientRect().left - 40;
  }
  const up = document.querySelector(".to-top");
  const show = () => { up.hidden = scrollY < 600; };
  addEventListener("scroll", show, { passive: true });
  show();
  // left menu: highlight the current section; folded on narrow screens
  const toc = document.querySelector(".toc details");
  if (!toc) return;
  const narrow = matchMedia("(max-width: 760px)");
  const adapt = () => { toc.open = !narrow.matches; };
  narrow.addEventListener("change", adapt);
  adapt();
  const links = [...toc.querySelectorAll("a")];
  links.forEach(a => a.addEventListener("click", () => { if (narrow.matches) toc.open = false; }));
  const heading = a => document.getElementById(decodeURIComponent(a.hash.slice(1)));
  const mark = () => {
    let current = links[0];
    links.forEach(a => { if (heading(a).getBoundingClientRect().top < 140) current = a; });
    links.forEach(a => a === current ? a.setAttribute("aria-current", "true") : a.removeAttribute("aria-current"));
    const box = toc.parentElement, top = current.offsetTop;  // keep the active entry visible
    if (!narrow.matches && (top < box.scrollTop || top > box.scrollTop + box.clientHeight - 40)) box.scrollTop = top - 80;
  };
  addEventListener("scroll", mark, { passive: true });
  mark();
});
