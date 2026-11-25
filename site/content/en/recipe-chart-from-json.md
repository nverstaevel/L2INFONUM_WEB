title: A chart from a JSON file
---
**When to use it:** Draw data saved by Python.

## Files

`books.json`

```json
[{"month": "Jan", "loans": 120}, {"month": "Feb", "loans": 95}, {"month": "Mar", "loans": 140}]
```

`chart.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Loans</title>
</head>
<body>
  <h1>Books lent</h1>
  <canvas id="chart" aria-label="Books lent per month" role="img"></canvas>
  <p>Source: city library.</p>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.6.2/dist/chart.umd.min.js"></script>
  <script src="chart.js"></script>
</body>
</html>
```

`chart.js`

```javascript
fetch("books.json")
  .then(response => response.json())
  .then(rows => {
    new Chart(document.getElementById("chart"), {
      type: "bar",
      data: {
        labels: rows.map(row => row.month),
        datasets: [{ label: "Loans", data: rows.map(row => row.loans) }]
      },
      options: { scales: { y: { min: 0 } } }
    });
  });
```

## What you see

<div class="preview"><p><strong>Live result: the code really runs</strong></p><iframe sandbox="allow-scripts" title="Live result: the code really runs" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;div style=&quot;max-width:30rem&quot;&gt;&lt;canvas id=&quot;chart&quot;&gt;&lt;/canvas&gt;&lt;/div&gt;&#10;&lt;script src=&quot;https://cdn.jsdelivr.net/npm/chart.js@4.6.2/dist/chart.umd.min.js&quot;&gt;&lt;/script&gt;&#10;&lt;script&gt;&#10;const FILES = {&quot;books.json&quot;: &quot;[{\&quot;month\&quot;: \&quot;Jan\&quot;, \&quot;loans\&quot;: 120}, {\&quot;month\&quot;: \&quot;Feb\&quot;, \&quot;loans\&quot;: 95}, {\&quot;month\&quot;: \&quot;Mar\&quot;, \&quot;loans\&quot;: 140}]\n&quot;};&#10;window.fetch = url =&gt; Promise.resolve(new Response(FILES[url] || &#x27;Not found&#x27;, {status: url in FILES ? 200 : 404}));&#10;fetch(&quot;books.json&quot;)&#10;  .then(response =&gt; response.json())&#10;  .then(rows =&gt; {&#10;    new Chart(document.getElementById(&quot;chart&quot;), {&#10;      type: &quot;bar&quot;,&#10;      data: {&#10;        labels: rows.map(row =&gt; row.month),&#10;        datasets: [{ label: &quot;Loans&quot;, data: rows.map(row =&gt; row.loans) }]&#10;      },&#10;      options: { scales: { y: { min: 0 } } }&#10;    });&#10;  });&#10;&#10;&lt;/script&gt;" style="height:270px"></iframe></div>

## Run

```text
python -m http.server
# then open http://localhost:8000/chart.html
```

**You should see:** Three bars appear.

## Adapt it

Change the file name, the two properties (`month`, `loans`) and the type.

- Notions: [Local server](notion-local-server.html) · [fetch: asking for data](notion-fetch.html) · [Charts with Chart.js](notion-chartjs.html) · [JavaScript basics](notion-javascript.html)
- [All recipes](recipes.html)
