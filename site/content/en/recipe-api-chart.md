title: A JSON API and its chart
---
**When to use it:** The page asks the server and redraws without reloading.

## Files

`app.py`

```python
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
LOANS = [{"branch": "NORTH", "month": "Jan", "loans": 120},
         {"branch": "NORTH", "month": "Feb", "loans": 95},
         {"branch": "SOUTH", "month": "Jan", "loans": 70}]


@app.route("/")
def home():
    return render_template("chart.html")


@app.route("/api/loans")
def api_loans():
    branch = request.args.get("branch", "NORTH").upper()
    rows = [r for r in LOANS if r["branch"] == branch]
    if not rows:
        return jsonify(error="Unknown branch"), 404
    return jsonify(rows)


if __name__ == "__main__":
    app.run(debug=True)
```

`templates/chart.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>City library</title>
</head>
<body>
  <main>
    <h1>Loans</h1>
    <label for="branch">Branch</label>
    <input id="branch" value="north">
    <button id="load" type="button">Show</button>
    <p id="message"></p>
    <canvas id="chart" aria-label="Loans per month" role="img"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.6.2/dist/chart.umd.min.js"></script>
    <script src="/static/chart.js"></script>
  </main>
</body>
</html>
```

`static/chart.js`

```javascript
let chart = null;

function load() {
  const branch = document.getElementById("branch").value;
  fetch("/api/loans?branch=" + encodeURIComponent(branch))
    .then(response => response.json())
    .then(rows => {
      const message = document.getElementById("message");
      if (rows.error) {
        message.textContent = rows.error;
        return;
      }
      message.textContent = "";
      if (chart) {
        chart.destroy();
      }
      chart = new Chart(document.getElementById("chart"), {
        type: "bar",
        data: {
          labels: rows.map(row => row.month),
          datasets: [{ label: "Loans", data: rows.map(row => row.loans) }]
        }
      });
    });
}

document.getElementById("load").addEventListener("click", load);
load();
```

## Run

```text
python app.py
```

**You should see:** `south` redraws one bar; `east` shows `Unknown branch`.

## Adapt it

Change the data, the route, the parameter and the two properties of the chart.

- Notions: [JSON API](notion-api.html) · [fetch: asking for data](notion-fetch.html) · [Changing the page from JavaScript](notion-dom.html) · [Charts with Chart.js](notion-chartjs.html)
- [All recipes](recipes.html)
