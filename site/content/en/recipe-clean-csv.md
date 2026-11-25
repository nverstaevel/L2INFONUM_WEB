title: Filter a CSV file
---
**When to use it:** Keep some rows and columns, with the right types.

## Files

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

## Run

```text
python filter_books.py
```

**You should see:** It prints `3 rows read, 2 kept`.

## Adapt it

Change the file names, the column names and the tests.

- Notions: [CSV files](notion-csv.html) · [Lists of dictionaries](notion-lists-dicts.html) · [Reading and writing files](notion-python-files.html)
- [All recipes](recipes.html)
