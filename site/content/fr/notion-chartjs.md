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

## Ce que vous voyez

<div class="preview"><p><strong>Résultat en direct : le code s'exécute vraiment</strong></p><iframe sandbox="allow-scripts" title="Résultat en direct : le code s'exécute vraiment" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;div style=&quot;max-width:30rem&quot;&gt;&lt;canvas id=&quot;chart&quot;&gt;&lt;/canvas&gt;&lt;/div&gt;&#10;&lt;script src=&quot;https://cdn.jsdelivr.net/npm/chart.js@4.6.2/dist/chart.umd.min.js&quot;&gt;&lt;/script&gt;&#10;&lt;script&gt;&#10;new Chart(document.getElementById(&quot;chart&quot;), {&#10;  type: &quot;bar&quot;,&#10;  data: { labels: [&quot;Jan&quot;, &quot;Feb&quot;], datasets: [{ label: &quot;Books&quot;, data: [120, 95] }] },&#10;  options: { scales: { y: { min: 0 } } }&#10;});&#10;&lt;/script&gt;" style="height:270px"></iframe></div>

## Erreurs fréquentes

- Chart.js chargé après votre script : `Chart is not defined`.
- Dessiner deux fois dans le même canvas : appeler `destroy()` avant.

## Pour aller plus loin

- Cours : [CM4](cm4.html)
- Recettes : [Un graphique à partir d'un fichier JSON](recipe-chart-from-json.html) · [Une API JSON et son graphique](recipe-api-chart.html)
- TD qui l'utilisent : [TD4](td4.html), [TD9](td9.html)
- [JavaScript et ses résultats](notion-js-ref.html)
- [Toutes les notions](notions.html)
