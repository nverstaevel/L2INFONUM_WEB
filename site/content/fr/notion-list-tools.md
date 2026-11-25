title: Compréhensions, min, max, sorted
---
Une **liste en compréhension** construit une liste en une ligne. `min`, `max` et `sorted` acceptent une `key` : une petite fonction (`lambda`) qui dit quoi comparer.

## Exemple

```python
books = [{"title": "Emma", "pages": 400}, {"title": "Dune", "pages": 600}]
long_ones = [b for b in books if b["pages"] > 500]
shortest = min(books, key=lambda b: b["pages"])
by_size = sorted(books, key=lambda b: b["pages"], reverse=True)
average = sum(b["pages"] for b in books) / len(books)
```

## Erreurs fréquentes

- `min` d'une liste vide provoque une erreur : vérifiez d'abord le filtre.

## Pour aller plus loin

- Cours : [CM1](cm1.html)
- Recettes : [Calculer des chiffres et les enregistrer en JSON](recipe-stats-json.html)
- TD qui l'utilisent : [TD1](td1.html), [TD7](td7.html)
- [Toutes les notions](notions.html)
