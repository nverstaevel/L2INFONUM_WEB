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

## What you see

<div class="preview"><p><strong>Live result: the code really runs</strong></p><iframe sandbox="allow-scripts" title="Live result: the code really runs" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;div style=&quot;max-width:30rem&quot;&gt;&lt;canvas id=&quot;chart&quot;&gt;&lt;/canvas&gt;&lt;/div&gt;&#10;&lt;script src=&quot;https://cdn.jsdelivr.net/npm/chart.js@4.6.2/dist/chart.umd.min.js&quot;&gt;&lt;/script&gt;&#10;&lt;script&gt;&#10;new Chart(document.getElementById(&quot;chart&quot;), {&#10;  type: &quot;bar&quot;,&#10;  data: { labels: [&quot;Jan&quot;, &quot;Feb&quot;], datasets: [{ label: &quot;Books&quot;, data: [120, 95] }] },&#10;  options: { scales: { y: { min: 0 } } }&#10;});&#10;&lt;/script&gt;" style="height:270px"></iframe></div>

## Common mistakes

- Chart.js loaded after your script: `Chart is not defined`.
- Drawing twice in the same canvas: call `destroy()` first.

## Go further

- Lecture: [CM4](cm4.html)
- Recipes: [A chart from a JSON file](recipe-chart-from-json.html) · [A JSON API and its chart](recipe-api-chart.html)
- Labs using it: [TD4](td4.html), [TD9](td9.html)
- [JavaScript, with its result](notion-js-ref.html)
- [All notions](notions.html)
