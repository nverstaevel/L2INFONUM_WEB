title: Filtrer un fichier CSV
---
**Quand l'utiliser :** Garder certaines lignes et colonnes, avec les bons types.

## Fichiers

`books.csv`

```text
title,author,year,pages
Emma,Austen,1815,400
Dracula,Stoker,1897,420
Persuasion,Austen,1817,250
```

`filter_books.py`

```python
import csv

with open("books.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

kept = []
for row in rows:
    if row["pages"] == "":          # skip missing values
        continue
    if row["author"] != "Austen":   # keep one author
        continue
    kept.append({"title": row["title"], "pages": int(row["pages"])})

with open("austen.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "pages"])
    writer.writeheader()
    writer.writerows(kept)
print(len(rows), "rows read,", len(kept), "kept")
```

## Lancer

```text
python filter_books.py
```

<details markdown="1"><summary>La sortie, ou ce que répond le serveur</summary>

```text
3 rows read, 2 kept
```

</details>

**Vous devez voir :** Le script affiche `3 rows read, 2 kept`.

## À adapter

Changez les noms de fichiers, de colonnes et les tests.

- Notions : [Fichiers CSV](notion-csv.html) · [Listes de dictionnaires](notion-lists-dicts.html) · [Lire et écrire des fichiers](notion-python-files.html)
- [Toutes les recettes](recipes.html)
