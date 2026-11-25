title: fetch : demander des données
---
`fetch` envoie une requête depuis la page sans la recharger. La réponse arrive plus tard : chaque `then` dit quoi faire à son arrivée. Un 404 n'arrête pas `fetch` : testez le contenu.

## Exemple

```javascript
fetch("data/books.json")
  .then(response => response.json())
  .then(books => {
    console.log(books);
  });
```

## Erreurs fréquentes

- Utiliser les données hors du `then` : elles ne sont pas encore arrivées.
- Page ouverte par double-clic : `fetch` est bloqué.

## Pour aller plus loin

- Cours : [CM4](cm4.html)
- Recettes : [Un graphique à partir d'un fichier JSON](recipe-chart-from-json.html) · [Une API JSON et son graphique](recipe-api-chart.html)
- TD qui l'utilisent : [TD4](td4.html), [TD7](td7.html), [TD9](td9.html)
- [Toutes les notions](notions.html)
