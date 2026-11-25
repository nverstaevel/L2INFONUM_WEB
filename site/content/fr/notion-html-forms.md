title: Formulaires
---
Un **formulaire** recueille une saisie et l'envoie. `action` est l'adresse, `method` vaut `get` ou `post`. Chaque champ a un `name` (envoyé au serveur) et un `label` relié par `for` = `id`.

## Exemple

```html
<form action="/search" method="get">
  <label for="author">Author</label>
  <input id="author" name="author">
  <button type="submit">Search</button>
</form>
```

## Erreurs fréquentes

- Un champ sans `name` n'est pas envoyé.
- `for` et `id` différents.

## Pour aller plus loin

- Cours : [CM2](cm2.html)
- Recettes : [Un tableau et un formulaire](recipe-table-form.html) · [Un formulaire de recherche](recipe-search-form.html)
- TD qui l'utilisent : [TD2](td2.html), [TD6](td6.html), [TD9](td9.html)
- [Toutes les notions](notions.html)
