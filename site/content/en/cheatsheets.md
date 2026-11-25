title: Cheat sheets
---

All results and error messages: [Python, with its result](notion-python-ref.html) · [Flask, with its result](notion-flask-ref.html) · [HTML tags](notion-html-tags.html).

## Python

```
name = "Emma"; pages = 400                 # str, int
print(f"{name}: {pages} pages")
books = [{"title": "Emma", "pages": 400}]  # list of dictionaries
for book in books:
    if book["pages"] > 300:
        print(book["title"])
long_titles = [b["title"] for b in books if b["pages"] > 300]
shortest = min(books, key=lambda b: b["pages"])
def average(values):
    return sum(values) / len(values)
import csv, json
with open("books.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))          # values are text: int(row["pages"])
with open("out.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, indent=2)
```

## HTML

```
<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>Title</title>
  <link rel="stylesheet" href="style.css"></head>
<body>
  <header><h1>Title</h1><nav><ul><li><a href="#a">Link</a></li></ul></nav></header>
  <main>
    <section id="a"><h2>Part</h2><p>Text</p><ul><li>Item</li></ul>
      <figure><img src="x.svg" alt="Description"><figcaption>Credit</figcaption></figure>
      <p><strong>Important</strong> and <em>stressed</em></p>
      <table><caption>Caption</caption>
        <thead><tr><th>Year</th><th>Value</th></tr></thead>
        <tbody><tr><td>2025</td><td>94.98</td></tr></tbody></table>
      <form action="/search" method="get">
        <label for="c">Country</label>
        <select id="c" name="country"><option value="FR">France</option></select>
        <label for="y">Year</label><input id="y" name="year" type="number" required>
        <button type="submit">Show</button>
      </form>
    </section>
  </main>
  <footer>Source</footer>
</body>
</html>
```

## CSS

```
p { }          /* element */
.note { }      /* class="note" */
#about { }     /* id="about" */
nav a { }      /* a inside nav */
a:hover { }    /* state */
/* specificity: id > class > element; same weight: last rule wins */

.box { width: 300px; padding: 10px; border: 2px solid; margin: 20px; }
/* visible width = 300 + 2*10 + 2*2 = 324px (box-sizing: content-box) */
* { box-sizing: border-box; }   /* then width includes padding and border */

.row { display: flex; flex-direction: row; gap: 1rem;
       justify-content: space-between;  /* main axis */
       align-items: center;             /* cross axis */
       flex-wrap: wrap; }
@media (max-width: 600px) { .row { flex-direction: column; } }
```

## JavaScript, fetch, Chart.js

```
const n = 3;                 // variable that is not reassigned
let total = 0;               // variable that changes
const list = [1, 2, 3];      // array
const obj = { year: 2025 };  // object: obj.year
const years = list.map(x => 2020 + x);
if (obj.year === 2025) { console.log("yes"); }
document.getElementById("title").textContent = "New title";
button.addEventListener("click", load);
fetch("/api/data?country=FR")
  .then(response => response.json())
  .then(rows => { console.log(rows); });
new Chart(canvas, { type: "line",
  data: { labels: [2024, 2025], datasets: [{ label: "%", data: [94.14, 94.98] }] } });
```

## Flask

```
from flask import Flask, jsonify, render_template, request, session
app = Flask(__name__)
app.secret_key = "change-me"            # needed for sessions

@app.route("/country/<code>")           # URL parameter
def country(code):
    return render_template("country.html", code=code)   # {{ code }}

@app.route("/search")                   # /search?country=FR&year=2022
def search():
    country = request.args.get("country", "")
    year = request.args.get("year", type=int)
    return jsonify(country=country, year=year)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form.get("name", "")
        session["names"] = session.get("names", []) + [name]
    return ", ".join(session.get("names", [])), 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run(debug=True)                 # debug only on your computer
```

## Status codes

| Code | Meaning |
|---|---|
| 200 | OK |
| 302 | redirect |
| 400 | bad request |
| 404 | not found |
| 405 | method not allowed |
| 500 | server error |

References: [MDN](https://developer.mozilla.org), [Flask](https://flask.palletsprojects.com), [Chart.js](https://www.chartjs.org/docs/latest/).
