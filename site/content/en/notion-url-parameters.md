title: URL parameters and query strings
---
Two ways to give information in an address: a part of the path (`/book/emma`), captured with `<name>`; or the **query string** (`/search?author=austen`), read with `request.args.get`.

## Example

```python
@app.route("/book/<title>")
def book(title): ...

author = request.args.get("author", "")        # "" if missing
year = request.args.get("year", type=int)      # None if missing or not a number
```

## Common mistakes

- The function lacks the argument named in `<...>`.
- Comparing a text with a number: use `type=int`.

## Go further

- Lecture: [CM6](cm6.html)
- Recipes: [A search form](recipe-search-form.html)
- Labs using it: [TD5](td5.html), [TD6](td6.html), [TD7](td7.html), [TD9](td9.html)
- [All notions](notions.html)
