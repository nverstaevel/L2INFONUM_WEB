title: JSON API
---
An **API** is a set of addresses that programs use to get data. `jsonify` returns JSON. The **back-end** (server) serves data, the **front-end** (browser) shows it. Return an error message and a status code when there is nothing.

## Example

```python
@app.route("/api/books")
def api_books():
    author = request.args.get("author", "")
    found = [b for b in BOOKS if b["author"] == author]
    if not found:
        return jsonify(error="No book found"), 404
    return jsonify(found)
```

## Common mistakes

- Forgetting `, 404`: the error looks like a success.

## Go further

- Lecture: [CM7](cm7.html)
- Recipes: [A JSON API and its chart](recipe-api-chart.html)
- Labs using it: [TD5](td5.html), [TD7](td7.html), [TD9](td9.html)
- [All notions](notions.html)
