title: Une application Flask avec un gabarit
---
**Quand l'utiliser :** Servir vos premières pages.

## Fichiers

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

## Lancer

```text
python app.py
# then open http://127.0.0.1:5000/
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
    <h1>Library of Toulouse</h1>
  </main>
</body>
</html>
```

</details>

**Vous devez voir :** La page affiche `Library of Toulouse`.

## À adapter

Ajoutez une route et un gabarit par page.

- Notions : [Flask et les routes](notion-flask-routes.html) · [Gabarits et fichiers statiques](notion-templates.html)
- [Toutes les recettes](recipes.html)
