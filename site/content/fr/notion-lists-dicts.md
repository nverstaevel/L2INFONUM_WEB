title: Listes de dictionnaires
---
En Python, un tableau de données est une **liste** (les lignes) de **dictionnaires** (une ligne : nom de colonne → valeur). On le parcourt avec une boucle `for`.

## Exemple

```python
books = [{"title": "Emma", "pages": 400},
         {"title": "Dune", "pages": 600}]
for book in books:
    if book["pages"] > 500:
        print(book["title"])
```

## Erreurs fréquentes

- `KeyError` : le nom de colonne n'est pas exactement le même (les majuscules comptent).
- Un `return` dans la boucle s'arrête à la première ligne.

## Pour aller plus loin

- Cours : [CM1](cm1.html)
- Recettes : [Calculer des chiffres et les enregistrer en JSON](recipe-stats-json.html)
- TD qui l'utilisent : [TD1](td1.html), [TD6](td6.html), [TD8](td8.html)
- [Toutes les notions](notions.html)
