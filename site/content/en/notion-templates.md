title: Templates and static files
---
A **template** is an HTML file in `templates/` with holes `{{ name }}` filled by `render_template`. In this course: no loop or condition in templates, Python prepares the text. CSS, JavaScript and images go in `static/`.

## Example

```python
# app.py
return render_template("shop.html", city="Toulouse")

# templates/shop.html
# <link rel="stylesheet" href="/static/style.css">
# <h1>Shops in {{ city }}</h1>
```

## What you see

```text
<link rel="stylesheet" href="/static/style.css">
<h1>Shops in Toulouse</h1>
```

## Common mistakes

- `TemplateNotFound`: folder not called exactly `templates`.
- The value not passed to `render_template`: the hole stays empty.

## Go further

- Lecture: [CM5](cm5.html)
- Recipes: [A Flask app with a template](recipe-flask-app.html)
- Labs using it: [TD5](td5.html), [TD6](td6.html), [TD8](td8.html), [TD9](td9.html)
- [Flask, with its result](notion-flask-ref.html)
- [All notions](notions.html)
