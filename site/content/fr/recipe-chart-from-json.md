title: Un graphique à partir d'un fichier JSON
---
**Quand l'utiliser :** Tracer des données enregistrées par Python.

## Fichiers

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

## Lancer

```text
python -m http.server
# then open http://localhost:8000/chart.html
```

**Vous devez voir :** Trois barres apparaissent.

## À adapter

Changez le nom du fichier, les deux propriétés (`month`, `loans`) et le type.

- Notions : [Serveur local](notion-local-server.html) · [fetch : demander des données](notion-fetch.html) · [Graphiques avec Chart.js](notion-chartjs.html) · [Bases de JavaScript](notion-javascript.html)
- [Toutes les recettes](recipes.html)
