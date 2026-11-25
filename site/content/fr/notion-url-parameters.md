title: Paramètres d'URL et chaîne de requête
---
Deux façons de passer une information dans une adresse : un morceau du chemin (`/book/emma`), capturé avec `<nom>` ; ou la **chaîne de requête** (`/search?author=austen`), lue avec `request.args.get`.

## Exemple

```python
@app.route("/book/<title>")
def book(title): ...

author = request.args.get("author", "")        # "" if missing
year = request.args.get("year", type=int)      # None if missing or not a number
```

## Ce que vous voyez

```text
address: /?author=Austen&year=abc
author = 'Austen'
year   = None
```

## Erreurs fréquentes

- La fonction n'a pas l'argument nommé dans `<...>`.
- Comparer un texte et un nombre : utiliser `type=int`.

## Pour aller plus loin

- Cours : [CM6](cm6.html)
- Recettes : [Un formulaire de recherche](recipe-search-form.html)
- TD qui l'utilisent : [TD5](td5.html), [TD6](td6.html), [TD7](td7.html), [TD9](td9.html)
- [Flask et ses résultats](notion-flask-ref.html)
- [Toutes les notions](notions.html)
