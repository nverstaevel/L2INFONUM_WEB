title: Modifier la page en JavaScript
---
Le navigateur garde la page comme un arbre d'objets (le **DOM**). `document.getElementById` trouve un élément, `textContent` change son texte, `value` lit un champ, `addEventListener` réagit à un clic.

## Exemple

```javascript
const button = document.getElementById("hello");
button.addEventListener("click", () => {
  document.getElementById("message").textContent = "Hello";
});
```

## Erreurs fréquentes

- L'`id` en JavaScript diffère de celui du HTML : le résultat est `null`.
- Utiliser `textContent`, pas `innerHTML`, pour des données ou une saisie.

## Pour aller plus loin

- Cours : [CM4](cm4.html)
- Recettes : [Une API JSON et son graphique](recipe-api-chart.html)
- TD qui l'utilisent : [TD4](td4.html), [TD7](td7.html)
- [Toutes les notions](notions.html)
