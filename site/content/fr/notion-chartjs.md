title: Graphiques avec Chart.js
---
**Chart.js** est une bibliothèque qui dessine des graphiques dans un élément `canvas`. On la charge depuis un **CDN** (serveur public de bibliothèques). On donne un `type`, des `labels` et des `datasets`.

## Exemple

```javascript
new Chart(document.getElementById("chart"), {
  type: "bar",
  data: { labels: ["Jan", "Feb"], datasets: [{ label: "Books", data: [120, 95] }] },
  options: { scales: { y: { min: 0 } } }
});
```

## Erreurs fréquentes

- Chart.js chargé après votre script : `Chart is not defined`.
- Dessiner deux fois dans le même canvas : appeler `destroy()` avant.

## Pour aller plus loin

- Cours : [CM4](cm4.html)
- Recettes : [Un graphique à partir d'un fichier JSON](recipe-chart-from-json.html) · [Une API JSON et son graphique](recipe-api-chart.html)
- TD qui l'utilisent : [TD4](td4.html), [TD9](td9.html)
- [Toutes les notions](notions.html)
