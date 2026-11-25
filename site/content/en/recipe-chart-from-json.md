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
