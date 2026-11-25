title: Compute figures and save them as JSON
---
**When to use it:** Summarise a list of rows.

## Files

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

## Run

```text
python summary.py
```

**You should see:** `summary.json` contains `"average": 356.7`.

## Adapt it

Replace `books` by the rows read from your file.

- Notions: [Comprehensions, min, max, sorted](notion-list-tools.html) · [JSON](notion-json.html) · [Lists of dictionaries](notion-lists-dicts.html)
- [All recipes](recipes.html)
