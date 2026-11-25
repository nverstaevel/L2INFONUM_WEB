title: A Flask app with a template
---
**When to use it:** Serve your first pages.

## Files

`app.py`

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", city="Toulouse")


if __name__ == "__main__":
    app.run(debug=True)
```

`templates/home.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>City library</title>
</head>
<body>
  <main>
    <h1>Library of {{ city }}</h1>
  </main>
</body>
</html>
```

## Run

```text
python app.py
# then open http://127.0.0.1:5000/
```

**You should see:** The page shows `Library of Toulouse`.

## Adapt it

Add one route and one template per page.

- Notions: [Flask and routes](notion-flask-routes.html) · [Templates and static files](notion-templates.html)
- [All recipes](recipes.html)
