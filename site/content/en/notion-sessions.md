title: Sessions and cookies
---
HTTP forgets everything between two requests. A **session** remembers data for one visitor, stored in a **cookie** (a small text kept by the browser). It is signed with `app.secret_key`: readable but not modifiable. No secrets in it.

## Example

```python
app.secret_key = "change-me"

items = session.get("basket", [])
session["basket"] = items + ["apple"]    # assign a new list
```

## Common mistakes

- `items.append(...)` alone may not be saved: assign `session[...]` again.
- `RuntimeError`: `secret_key` is missing.

## Go further

- Lecture: [CM6](cm6.html)
- Recipes: [Remember a list with a session](recipe-session-list.html)
- Labs using it: [TD6](td6.html)
- [All notions](notions.html)
