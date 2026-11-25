title: A search form
---
**When to use it:** Filter data with a GET form.

## Files

`app.py`

```python
from flask import Flask, render_template, request

app = Flask(__name__)
BOOKS = [{"title": "Emma", "author": "AUSTEN"},
         {"title": "Dracula", "author": "STOKER"}]


@app.route("/")
def search():
    author = request.args.get("author", "").strip().upper()
    lines = []
    for book in BOOKS:
        if author == "" or book["author"] == author:
            lines.append(book["title"])
    results = "\n".join(lines) if lines else "No result."
    return render_template("search.html", author=author, results=results)


if __name__ == "__main__":
    app.run(debug=True)
```

`templates/search.html`

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
    <h1>Search</h1>
    <form action="/" method="get">
      <label for="author">Author</label>
      <input id="author" name="author" value="{{ author }}">
      <button type="submit">Search</button>
    </form>
    <pre>{{ results }}</pre>
  </main>
</body>
</html>
```

## Run

```text
python app.py
```

<details markdown="1"><summary>The output, or what the server answers</summary>

```text
GET /?author=stoker  ->  200
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>City library</title>
</head>
<body>
  <main>
    <h1>Search</h1>
    <form action="/" method="get">
      <label for="author">Author</label>
      <input id="author" name="author" value="STOKER">
      <button type="submit">Search</button>
    </form>
    <pre>Dracula</pre>
  </main>
</body>
</html>

GET /?author=zzz  ->  200
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>City library</title>
</head>
<body>
  <main>
    <h1>Search</h1>
    <form action="/" method="get">
      <label for="author">Author</label>
      <input id="author" name="author" value="ZZZ">
      <button type="submit">Search</button>
    </form>
    <pre>No result.</pre>
  </main>
</body>
</html>
```

</details>

**You should see:** `stoker` shows only Dracula; `zzz` shows `No result.`

## Adapt it

Replace `BOOKS` by your data and `author` by your field.

- Notions: [URL parameters and query strings](notion-url-parameters.html) · [Forms](notion-html-forms.html) · [Input checking and escaping](notion-safety.html)
- [All recipes](recipes.html)
