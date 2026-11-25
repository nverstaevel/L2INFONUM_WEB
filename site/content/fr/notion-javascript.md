title: Bases de JavaScript
---
**JavaScript** est le langage de programmation des pages web. `const` (non réaffecté) et `let` (modifiable). Un **tableau** ressemble à une liste, un **objet** à un dictionnaire lu avec un point. `map` transforme chaque élément. Les accolades remplacent l'indentation.

## Exemple

```javascript
const books = [{ title: "Emma", pages: 400 }];
const titles = books.map(book => book.title);
if (titles.length > 0) {
  console.log(titles[0]);
}
```

## Erreurs fréquentes

- Les majuscules comptent : `textContent` et non `textcontent`.
- Une virgule oubliée entre deux propriétés d'un objet.

## Pour aller plus loin

- Cours : [CM4](cm4.html)
- Recettes : [Un graphique à partir d'un fichier JSON](recipe-chart-from-json.html)
- TD qui l'utilisent : [TD4](td4.html)
- [Toutes les notions](notions.html)
