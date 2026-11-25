title: JSON
---
**JSON** is a text format for lists and dictionaries, used everywhere on the web. It looks like Python, with `true`, `false`, `null` and double quotes only.

## Example

```python
import json

book = {"title": "Emma", "pages": 400, "lent": True}
with open("book.json", "w", encoding="utf-8") as f:
    json.dump(book, f, indent=2)
with open("book.json", encoding="utf-8") as f:
    print(json.load(f)["title"])
```

## What you see

```text
Emma
```

## Common mistakes

- A JSON file written by hand with a comma after the last item is invalid.

## Go further

- Lecture: [CM1](cm1.html)
- Recipes: [Compute figures and save them as JSON](recipe-stats-json.html)
- Labs using it: [TD1](td1.html), [TD4](td4.html), [TD5](td5.html)
- [Python, with its result](notion-python-ref.html)
- [All notions](notions.html)
