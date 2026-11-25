title: Un formulaire de recherche
---
**Quand l'utiliser :** Filtrer des données avec un formulaire GET.

## Fichiers

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

## Lancer

```text
python app.py
```

**Vous devez voir :** `stoker` n'affiche que Dracula ; `zzz` affiche `No result.`

## À adapter

Remplacez `BOOKS` par vos données et `author` par votre champ.

- Notions : [Paramètres d'URL et chaîne de requête](notion-url-parameters.html) · [Formulaires](notion-html-forms.html) · [Contrôle des saisies et échappement](notion-safety.html)
- [Toutes les recettes](recipes.html)
