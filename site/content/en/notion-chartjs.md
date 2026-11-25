title: Charts with Chart.js
---
**Chart.js** is a library that draws charts in a `canvas` element. It is loaded from a **CDN** (a public server of libraries). You give a `type`, `labels` and `datasets`.

## Example

```javascript
new Chart(document.getElementById("chart"), {
  type: "bar",
  data: { labels: ["Jan", "Feb"], datasets: [{ label: "Books", data: [120, 95] }] },
  options: { scales: { y: { min: 0 } } }
});
```

## Common mistakes

- Chart.js loaded after your script: `Chart is not defined`.
- Drawing twice in the same canvas: call `destroy()` first.

## Go further

- Lecture: [CM4](cm4.html)
- Recipes: [A chart from a JSON file](recipe-chart-from-json.html) · [A JSON API and its chart](recipe-api-chart.html)
- Labs using it: [TD4](td4.html), [TD9](td9.html)
- [All notions](notions.html)
