title: JSON
---
Le **JSON** est un format texte pour les listes et dictionnaires, utilisé partout sur le web. Il ressemble à Python, avec `true`, `false`, `null` et uniquement des guillemets doubles.

## Exemple

```python
import json

book = {"title": "Emma", "pages": 400, "lent": True}
with open("book.json", "w", encoding="utf-8") as f:
    json.dump(book, f, indent=2)
with open("book.json", encoding="utf-8") as f:
    print(json.load(f)["title"])
```

## Ce que vous voyez

```text
Emma
```

## Erreurs fréquentes

- Un fichier JSON écrit à la main avec une virgule après le dernier élément est invalide.

## Pour aller plus loin

- Cours : [CM1](cm1.html)
- Recettes : [Calculer des chiffres et les enregistrer en JSON](recipe-stats-json.html)
- TD qui l'utilisent : [TD1](td1.html), [TD4](td4.html), [TD5](td5.html)
- [Python et ses résultats](notion-python-ref.html)
- [Toutes les notions](notions.html)
