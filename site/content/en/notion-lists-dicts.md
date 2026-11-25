title: Lists of dictionaries
---
A table of data in Python is a **list** (the rows) of **dictionaries** (one row: column name → value). You go through it with a `for` loop.

## Example

```python
books = [{"title": "Emma", "pages": 400},
         {"title": "Dune", "pages": 600}]
for book in books:
    if book["pages"] > 500:
        print(book["title"])
```

## Common mistakes

- `KeyError`: the column name is not exactly the same (capital letters count).
- `return` inside the loop stops at the first row.

## Go further

- Lecture: [CM1](cm1.html)
- Recipes: [Compute figures and save them as JSON](recipe-stats-json.html)
- Labs using it: [TD1](td1.html), [TD6](td6.html), [TD8](td8.html)
- [All notions](notions.html)
