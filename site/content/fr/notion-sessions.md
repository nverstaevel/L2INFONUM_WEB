title: Sessions et cookies
---
HTTP oublie tout entre deux requêtes. Une **session** mémorise des données pour un visiteur, dans un **cookie** (petit texte conservé par le navigateur). Elle est signée avec `app.secret_key` : lisible mais non modifiable. Pas de secret dedans.

## Exemple

```python
app.secret_key = "change-me"

items = session.get("basket", [])
session["basket"] = items + ["apple"]    # assign a new list
```

## Erreurs fréquentes

- `items.append(...)` seul peut ne pas être enregistré : réaffecter `session[...]`.
- `RuntimeError` : `secret_key` manque.

## Pour aller plus loin

- Cours : [CM6](cm6.html)
- Recettes : [Mémoriser une liste avec une session](recipe-session-list.html)
- TD qui l'utilisent : [TD6](td6.html)
- [Toutes les notions](notions.html)
