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
});
