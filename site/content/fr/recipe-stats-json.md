title: Calculer des chiffres et les enregistrer en JSON
---
**Quand l'utiliser :** Résumer une liste de lignes.

## Fichiers

`summary.py`

```python
import json

books = [{"title": "Emma", "pages": 400},
         {"title": "Dracula", "pages": 420},
         {"title": "Persuasion", "pages": 250}]

result = {
    "count": len(books),
    "average": round(sum(b["pages"] for b in books) / len(books), 1),
    "longest": max(books, key=lambda b: b["pages"]),
    "titles": sorted(b["title"] for b in books),
}

with open("summary.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)
print(result)
```

## Lancer

```text
python summary.py
```

<details markdown="1"><summary>La sortie, ou ce que répond le serveur</summary>

```text
{'count': 3, 'average': 356.7, 'longest': {'title': 'Dracula', 'pages': 420}, 'titles': ['Dracula', 'Emma', 'Persuasion']}
```

</details>

**Vous devez voir :** `summary.json` contient `"average": 356.7`.

## À adapter

Remplacez `books` par les lignes lues dans votre fichier.

- Notions : [Compréhensions, min, max, sorted](notion-list-tools.html) · [JSON](notion-json.html) · [Listes de dictionnaires](notion-lists-dicts.html)
- [Toutes les recettes](recipes.html)
