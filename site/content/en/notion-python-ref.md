title: Python, with its result
---
The Python you need in this course, each time with **what it prints**. The examples are about a library. Copy one into a file `try.py` and run `python try.py`. Lost? See the [official tutorial](https://docs.python.org/3/tutorial/).

## Values and text

### `print`, variables, types

`print` shows a value in the terminal. `type` tells what kind of value it is: `str` (text), `int`, `float` (decimal number), `bool`.

```python
city = "Toulouse"
year = 2027
print(city, year)
print(type(city), type(year))
```

**What you see**

```text
Toulouse 2027
<class 'str'> <class 'int'>
```

### f-strings

Text with values inside: put `f` before the quote and the value between `{ }`.

```python
title = "Emma"
share = 94.9812
print(f"{title} is lent")
print(f"{share:.1f} %")
```

**What you see**

```text
Emma is lent
95.0 %
```

### `strip`, `upper`, `int`, `float`

Clean a text and turn it into a number. Text read from a file is always a `str`.

```python
raw = "  fr "
print(raw.strip().upper())
print(int("2025") + 1)
print(float("94.98"))
```

**What you see**

```text
FR
2026
94.98
```

## Collections and loops

### lists

An ordered series of values. Positions start at 0.

```python
years = [2023, 2024]
years.append(2025)
print(years)
print(years[0], years[-1], len(years))
```

**What you see**

```text
[2023, 2024, 2025]
2023 2025 3
```

### dictionaries

Pairs key → value. `get` gives a default value when the key is missing.

```python
book = {"title": "Emma", "pages": 400}
print(book["title"])
print(book.get("author", "unknown"))
```

**What you see**

```text
Emma
unknown
```

### `for` and `if`

Repeat for each element, and do something only when a test is true.

```python
books = [{"title": "Emma", "pages": 400},
         {"title": "Dune", "pages": 600}]
for book in books:
    if book["pages"] > 500:
        print(book["title"])
```

**What you see**

```text
Dune
```

### list comprehensions

Build a new list in one line.

```python
books = [{"title": "Emma", "pages": 400},
         {"title": "Dune", "pages": 600}]
titles = [b["title"] for b in books if b["pages"] > 500]
print(titles)
```

**What you see**

```text
['Dune']
```

### `min`, `max`, `sum`, `sorted`

Compute on a list. `key=lambda b: ...` says what to compare.

```python
books = [{"title": "Emma", "pages": 400},
         {"title": "Dune", "pages": 600}]
print(max(books, key=lambda b: b["pages"]))
print(sum(b["pages"] for b in books) / len(books))
print(sorted([3, 1, 2]))
```

**What you see**

```text
{'title': 'Dune', 'pages': 600}
500.0
[1, 2, 3]
```

### `"\n".join`

Put several texts together, one per line.

```python
lines = ["Emma  1815", "Dracula  1897"]
print("\n".join(lines))
```

**What you see**

```text
Emma  1815
Dracula  1897
```

## Functions and modules

### `def` and `return`

A function has a name, receives values and gives a result back with `return`. Without `return`, you get `None`.

```python
def average(values):
    return sum(values) / len(values)

print(average([10, 20]))
```

**What you see**

```text
15.0
```

### `import`

Use code of a module (a file of ready-made functions).

```python
import math
from pathlib import Path

print(math.floor(94.98))
print(Path("data/books.csv").name)
```

**What you see**

```text
94
books.csv
```

### `if __name__ == "__main__":`

The block runs when you start the file yourself, not when another file imports it.

```python
if __name__ == "__main__":
    print("started directly")
```

**What you see**

```text
started directly
```

## Files and data

### write and read a text file

`open` with `"w"` writes (and erases what was there), without it reads. `with` closes the file for you.

```python
with open("note.txt", "w", encoding="utf-8") as f:
    f.write("Hello")
with open("note.txt", encoding="utf-8") as f:
    print(f.read())
```

**What you see**

```text
Hello
```

### CSV files

`csv.DictReader` gives one dictionary per line, `csv.DictWriter` writes them.

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

**What you see**

```text
{'title': 'Emma', 'year': '1815'}
```

### JSON files

`json.dump` writes a Python value into a file, `json.load` reads it back. `dumps` gives the text.

```python
import json

book = {"title": "Emma", "lent": True, "note": None}
with open("book.json", "w", encoding="utf-8") as f:
    json.dump(book, f)
print(json.dumps(book))
with open("book.json", encoding="utf-8") as f:
    print(json.load(f)["title"])
```

**What you see**

```text
{"title": "Emma", "lent": true, "note": null}
Emma
```

## Read an error message

Read the **last line** first: it names the error. The lines above say where it happened. Messages shown with Python 3.13 (other versions may word them differently).

### `SyntaxError`

A mistake in the writing: a missing `:`, bracket or quote. Look at the line shown and the one before.

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

The spaces at the beginning of a line are wrong.

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

A name that does not exist: spelling, or a missing `import`.

```python
titel = "Emma"
print(title)
```

```text
NameError: name 'title' is not defined
```

### `KeyError`

The dictionary has no such key: print it to see the real keys.

```python
book = {"title": "Emma"}
print(book["Title"])
```

```text
KeyError: 'Title'
```

### `TypeError`

Two kinds of values that do not go together, often text and number.

```python
print("2025" + 1)
```

```text
TypeError: can only concatenate str (not "int") to str
```

### `ValueError`

The right type but an impossible value.

```python
print(float("n/a"))
```

```text
ValueError: could not convert string to float: 'n/a'
```

### `FileNotFoundError`

The file is not where you think: check the folder of your terminal.

```python
open("data/missing.csv")
```

```text
FileNotFoundError: [Errno 2] No such file or directory: 'data/missing.csv'
```

- [All notions](notions.html)
