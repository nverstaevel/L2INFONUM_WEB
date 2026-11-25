title: Mémoriser une liste avec une session
---
**Quand l'utiliser :** Favoris ou panier, avec un formulaire POST.

## Fichiers

`app.py`

```python
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "change-me"
KNOWN = ["Emma", "Dracula", "Persuasion"]


@app.route("/", methods=["GET", "POST"])
def basket():
    items = session.get("basket", [])
    if request.method == "POST":
        if request.form.get("action") == "clear":
            items = []
        else:
            title = request.form.get("title", "").strip().capitalize()
            if title in KNOWN and title not in items:
                items = items + [title]
        session["basket"] = items
    text = ", ".join(items) if items else "none"
    return render_template("basket.html", items=text)


if __name__ == "__main__":
    app.run(debug=True)
```

`templates/basket.html`

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
    <h1>My books</h1>
    <p>{{ items }}</p>
    <form action="/" method="post">
      <label for="title">Title</label>
      <input id="title" name="title" required>
      <button type="submit">Add</button>
    </form>
    <form action="/" method="post">
      <button type="submit" name="action" value="clear">Empty</button>
    </form>
  </main>
</body>
</html>
```

## Lancer

```text
python app.py
```

<details markdown="1"><summary>La sortie, ou ce que répond le serveur</summary>

```text
GET /  ->  200
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>City library</title>
</head>
<body>
  <main>
    <h1>My books</h1>
    <p>none</p>
    <form action="/" method="post">
      <label for="title">Title</label>
      <input id="title" name="title" required>
      <button type="submit">Add</button>
    </form>
    <form action="/" method="post">
      <button type="submit" name="action" value="clear">Empty</button>
    </form>
  </main>
</body>
</html>

POST /  data={'title': 'emma'}  ->  200
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>City library</title>
</head>
<body>
  <main>
    <h1>My books</h1>
    <p>Emma</p>
    <form action="/" method="post">
      <label for="title">Title</label>
      <input id="title" name="title" required>
      <button type="submit">Add</button>
    </form>
    <form action="/" method="post">
      <button type="submit" name="action" value="clear">Empty</button>
    </form>
  </main>
</body>
</html>

GET /  ->  200
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>City library</title>
</head>
<body>
  <main>
    <h1>My books</h1>
    <p>Emma</p>
    <form action="/" method="post">
      <label for="title">Title</label>
      <input id="title" name="title" required>
      <button type="submit">Add</button>
    </form>
    <form action="/" method="post">
      <button type="submit" name="action" value="clear">Empty</button>
    </form>
  </main>
</body>
</html>
```

</details>

**Vous devez voir :** Ajoutez `emma`, rechargez : `Emma` est toujours là. `Empty` l'enlève.

## À adapter

Changez les valeurs connues et les noms.

- Notions : [GET et POST](notion-get-post.html) · [Sessions et cookies](notion-sessions.html) · [Contrôle des saisies et échappement](notion-safety.html)
- [Toutes les recettes](recipes.html)
