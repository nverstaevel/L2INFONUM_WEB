title: GET and POST
---
**GET** asks for information; the data is in the address. **POST** sends data that changes something on the server; the data is in the body of the request. Flask reads GET with `request.args`, POST with `request.form`.

## Example

```python
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        item = request.form.get("item", "")
    return render_template("add.html")
```

## What you see

```text
GET /add  ->  200
<p>Add an item</p>

POST /add  data={'item': 'apple'}  ->  200
<p>Add an item</p>

DELETE /add  ->  405
```

## Common mistakes

- Error 405: `methods` is missing.
- `request.args` used for a POST form.

## Go further

- Lecture: [CM6](cm6.html)
- Recipes: [Remember a list with a session](recipe-session-list.html)
- Labs using it: [TD6](td6.html)
- [Flask, with its result](notion-flask-ref.html)
- [All notions](notions.html)
