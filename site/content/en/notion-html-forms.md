title: Forms
---
A **form** collects input and sends it. `action` is the address, `method` is `get` or `post`. Each field has a `name` (sent to the server) and a `label` linked by `for` = `id`.

## Example

```html
<form action="/search" method="get">
  <label for="author">Author</label>
  <input id="author" name="author">
  <button type="submit">Search</button>
</form>
```

## Common mistakes

- A field without `name` is not sent at all.
- `for` and `id` that differ.

## Go further

- Lecture: [CM2](cm2.html)
- Recipes: [A table and a form](recipe-table-form.html) · [A search form](recipe-search-form.html)
- Labs using it: [TD2](td2.html), [TD6](td6.html), [TD9](td9.html)
- [All notions](notions.html)
