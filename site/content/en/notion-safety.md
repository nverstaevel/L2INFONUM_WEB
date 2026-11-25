title: Input checking and escaping
---
Never trust what a visitor sends. **Validate**: expected type, range, known value. **Escaping** shows special characters as text: `{{ value }}` does it for you. Do not switch it off.

## Example

```python
code = request.form.get("code", "").strip().upper()
if code in ["FR", "ES"]:      # known values only
    ...
```

## Common mistakes

- Building HTML by joining text with the visitor's input.

## Go further

- Lecture: [CM6](cm6.html)
- Recipes: [A search form](recipe-search-form.html) · [Remember a list with a session](recipe-session-list.html)
- Labs using it: [TD5](td5.html), [TD6](td6.html)
- [All notions](notions.html)
