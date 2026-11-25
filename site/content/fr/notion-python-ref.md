title: Python et ses résultats
---
Le Python utile à ce cours, à chaque fois avec **ce qu'il affiche**. Les exemples portent sur une bibliothèque. Copiez-en un dans un fichier `essai.py` et lancez `python essai.py`. Perdu ? Voir le [tutoriel officiel](https://docs.python.org/fr/3/tutorial/).

## Valeurs et texte

### `print`, variables, types

`print` affiche une valeur dans le terminal. `type` donne sa nature : `str` (texte), `int` (entier), `float` (décimal), `bool` (vrai/faux).

```python
city = "Toulouse"
year = 2027
print(city, year)
print(type(city), type(year))
```

**Ce que vous voyez**

```text
Toulouse 2027
<class 'str'> <class 'int'>
```

### les f-strings

Un texte contenant des valeurs : `f` devant le guillemet, la valeur entre `{ }`.

```python
title = "Emma"
share = 94.9812
print(f"{title} is lent")
print(f"{share:.1f} %")
```

**Ce que vous voyez**

```text
Emma is lent
95.0 %
```

### `strip`, `upper`, `int`, `float`

Nettoyer un texte et le convertir en nombre. Un texte lu dans un fichier est toujours un `str`.

```python
raw = "  fr "
print(raw.strip().upper())
print(int("2025") + 1)
print(float("94.98"))
```

**Ce que vous voyez**

```text
FR
2026
94.98
```

## Collections et boucles

### les listes

Une suite ordonnée de valeurs. Les positions commencent à 0.

```python
years = [2023, 2024]
years.append(2025)
print(years)
print(years[0], years[-1], len(years))
```

**Ce que vous voyez**

```text
[2023, 2024, 2025]
2023 2025 3
```

### les dictionnaires

Des couples clé → valeur. `get` donne une valeur par défaut quand la clé manque.

```python
book = {"title": "Emma", "pages": 400}
print(book["title"])
print(book.get("author", "unknown"))
```

**Ce que vous voyez**

```text
Emma
unknown
```

### `for` et `if`

Répéter pour chaque élément, et n'agir que si un test est vrai.

```python
books = [{"title": "Emma", "pages": 400},
         {"title": "Dune", "pages": 600}]
for book in books:
    if book["pages"] > 500:
        print(book["title"])
```

**Ce que vous voyez**

```text
Dune
```

### les listes en compréhension

Construire une nouvelle liste en une ligne.

```python
books = [{"title": "Emma", "pages": 400},
         {"title": "Dune", "pages": 600}]
titles = [b["title"] for b in books if b["pages"] > 500]
print(titles)
```

**Ce que vous voyez**

```text
['Dune']
```

### `min`, `max`, `sum`, `sorted`

Calculer sur une liste. `key=lambda b: ...` dit quoi comparer.

```python
books = [{"title": "Emma", "pages": 400},
         {"title": "Dune", "pages": 600}]
print(max(books, key=lambda b: b["pages"]))
print(sum(b["pages"] for b in books) / len(books))
print(sorted([3, 1, 2]))
```

**Ce que vous voyez**

```text
{'title': 'Dune', 'pages': 600}
500.0
[1, 2, 3]
```

### `"\n".join`

Assembler plusieurs textes, un par ligne.

```python
lines = ["Emma  1815", "Dracula  1897"]
print("\n".join(lines))
```

**Ce que vous voyez**

```text
Emma  1815
Dracula  1897
```

## Fonctions et modules

### `def` et `return`

Une fonction a un nom, reçoit des valeurs et renvoie un résultat avec `return`. Sans `return`, on obtient `None`.

```python
def average(values):
    return sum(values) / len(values)

print(average([10, 20]))
```

**Ce que vous voyez**

```text
15.0
```

### `import`

Utiliser le code d'un module (un fichier de fonctions toutes prêtes).

```python
import math
from pathlib import Path

print(math.floor(94.98))
print(Path("data/books.csv").name)
```

**Ce que vous voyez**

```text
94
books.csv
```

### `if __name__ == "__main__":`

Le bloc s'exécute quand vous lancez le fichier vous-même, pas quand un autre fichier l'importe.

```python
if __name__ == "__main__":
    print("started directly")
```

**Ce que vous voyez**

```text
started directly
```

## Fichiers et données

### écrire et lire un fichier texte

`open` avec `"w"` écrit (et efface l'ancien contenu), sans, il lit. `with` referme le fichier.

```python
with open("note.txt", "w", encoding="utf-8") as f:
    f.write("Hello")
with open("note.txt", encoding="utf-8") as f:
    print(f.read())
```

**Ce que vous voyez**

```text
Hello
```

### les fichiers CSV

`csv.DictReader` donne un dictionnaire par ligne, `csv.DictWriter` les écrit.

```python
import csv

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "year"])
    writer.writeheader()
    writer.writerow({"title": "Emma", "year": 1815})

with open("books.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row)
```

**Ce que vous voyez**

```text
{'title': 'Emma', 'year': '1815'}
```

### les fichiers JSON

`json.dump` écrit une valeur Python dans un fichier, `json.load` la relit. `dumps` donne le texte.

```python
import json

book = {"title": "Emma", "lent": True, "note": None}
with open("book.json", "w", encoding="utf-8") as f:
    json.dump(book, f)
print(json.dumps(book))
with open("book.json", encoding="utf-8") as f:
    print(json.load(f)["title"])
```

**Ce que vous voyez**

```text
{"title": "Emma", "lent": true, "note": null}
Emma
```

## Lire un message d'erreur

Lisez d'abord la **dernière ligne** : elle nomme l'erreur. Les lignes au-dessus disent où. Messages obtenus avec Python 3.13 (d'autres versions peuvent les formuler autrement).

### `SyntaxError`

Une faute d'écriture : un `:`, une parenthèse ou un guillemet manque. Regarder la ligne indiquée et la précédente.

```python
for x in [1, 2]
    print(x)
```

```text
  File "ex.py", line 1
    for x in [1, 2]
                   ^
SyntaxError: expected ':'
```

### `IndentationError`

Les espaces en début de ligne sont faux.

```python
if True:
print("a")
```

```text
  File "ex.py", line 2
    print("a")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 1
```

### `NameError`

Un nom qui n'existe pas : orthographe, ou `import` oublié.

```python
titel = "Emma"
print(title)
```

```text
NameError: name 'title' is not defined
```

### `KeyError`

Le dictionnaire n'a pas cette clé : affichez-le pour voir les vraies clés.

```python
book = {"title": "Emma"}
print(book["Title"])
```

```text
KeyError: 'Title'
```

### `TypeError`

Deux natures de valeurs incompatibles, souvent texte et nombre.

```python
print("2025" + 1)
```

```text
TypeError: can only concatenate str (not "int") to str
```

### `ValueError`

Le bon type mais une valeur impossible.

```python
print(float("n/a"))
```

```text
ValueError: could not convert string to float: 'n/a'
```

### `FileNotFoundError`

Le fichier n'est pas là où vous le pensez : vérifiez le dossier du terminal.

```python
open("data/missing.csv")
```

```text
FileNotFoundError: [Errno 2] No such file or directory: 'data/missing.csv'
```

- [Toutes les notions](notions.html)
