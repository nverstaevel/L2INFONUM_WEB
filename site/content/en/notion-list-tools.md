title: Comprehensions, min, max, sorted
---
A **list comprehension** builds a list in one line. `min`, `max` and `sorted` accept a `key`: a small function (`lambda`) that says what to compare.

## Example

```python
books = [{"title": "Emma", "pages": 400}, {"title": "Dune", "pages": 600}]
long_ones = [b for b in books if b["pages"] > 500]
shortest = min(books, key=lambda b: b["pages"])
by_size = sorted(books, key=lambda b: b["pages"], reverse=True)
average = sum(b["pages"] for b in books) / len(books)
```

## Common mistakes

- `min` of an empty list raises an error: check the filter first.

## Go further

- Lecture: [CM1](cm1.html)
- Recipes: [Compute figures and save them as JSON](recipe-stats-json.html)
- Labs using it: [TD1](td1.html), [TD7](td7.html)
- [All notions](notions.html)
