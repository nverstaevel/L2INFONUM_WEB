title: Flask et ses résultats
---
Le Flask utile, à chaque fois avec **ce que répond le serveur**. Chaque exemple a besoin de ces lignes avant lui, et des deux dernières lignes habituelles après. `GET /about  ->  200` signifie : l'adresse demandée, puis le code d'état. Voir aussi la [documentation officielle](https://flask.palletsprojects.com).

```python
from flask import Flask, jsonify, render_template, request, session

app = Flask(__name__)

# ... one example here ...

if __name__ == "__main__":
    app.run(debug=True)     # only on your own computer
```

## Routes et réponses

### `@app.route` et `return`

Une **route** relie une adresse à une fonction Python. Ce que la fonction renvoie part au navigateur.

```python
@app.route("/")
def home():
    return "Hello"
```

**Ce que vous voyez**

```text
GET /  ->  200
Hello

GET /nothing  ->  404
```

### un morceau de l'adresse : `<name>`

Un morceau de l'adresse devient un paramètre de la fonction.

```python
@app.route("/book/<title>")
def book(title):
    return f"Book: {title}"
```

**Ce que vous voyez**

```text
GET /book/Emma  ->  200
Book: Emma
```

### les codes d'état

Ajoutez un nombre après la réponse : 200 par défaut, 404 signifie introuvable.

```python
@app.route("/old")
def old():
    return "This page is gone", 404
```

**Ce que vous voyez**

```text
GET /old  -> 404
This page is gone
```

### `jsonify`

Envoyer des données en JSON, pour un programme ou pour `fetch`.

```python
@app.route("/api/books")
def api_books():
    return jsonify([{"title": "Emma", "year": 1815}])
```

**Ce que vous voyez**

```text
GET /api/books  ->  200
[{"title":"Emma","year":1815}]
```

## Ce que le visiteur envoie

### `request.args` (GET)

Les valeurs après `?` dans l'adresse. Avec `type=int`, une valeur fausse donne la valeur par défaut.

```python
@app.route("/search")
def search():
    author = request.args.get("author", "")
    year = request.args.get("year", 0, type=int)
    return f"author={author} year={year}"
```

**Ce que vous voyez**

```text
GET /search?author=Austen&year=1815  ->  200
author=Austen year=1815

GET /search?year=abc  ->  200
author= year=0
```

### `methods` et `request.form` (POST)

Un formulaire envoyé en `post` se lit dans `request.form`. Une méthode non prévue donne 405.

```python
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        return "received " + request.form.get("title", "")
    return "send me a title"
```

**Ce que vous voyez**

```text
GET /add  ->  200
send me a title

POST /add  data={'title': 'Emma'}  ->  200
received Emma

DELETE /add  ->  405
```

### `session`

La mémoire d'un visiteur, gardée dans un **cookie** signé. Il faut `app.secret_key`. On réaffecte pour enregistrer.

```python
app.secret_key = "change-me"

@app.route("/visit")
def visit():
    session["count"] = session.get("count", 0) + 1
    return f"visit number {session['count']}"
```

**Ce que vous voyez**

```text
GET /visit  ->  200
visit number 1

GET /visit  ->  200
visit number 2

another visitor:
GET /visit  ->  200
visit number 1
```

## Pages et fichiers

### `render_template` et `{{ }}`

Envoyer un fichier HTML du dossier `templates`, dont les trous sont remplis par Python. Flask **échappe** les valeurs : `<` s'affiche, il n'est pas interprété.

```python
@app.route("/hello")
def hello():
    name = request.args.get("name", "world")
    return render_template("hello.html", name=name)
```

`templates/hello.html`

```html
<h1>Hello {{ name }}</h1>
```

**Ce que vous voyez**

```text
GET /hello?name=Ada  ->  200
<h1>Hello Ada</h1>

GET /hello?name=<b>  ->  200
<h1>Hello &lt;b&gt;</h1>
```

### les fichiers statiques

Les fichiers du dossier `static` (CSS, JavaScript, images) sont envoyés tels quels, à l'adresse `/static/...`.

```python
# no route to write
# static/style.css  ->  /static/style.css
```

`static/style.css`

```css
h1 { color: darkred; }
```

**Ce que vous voyez**

```text
GET /static/style.css  -> 200
h1 { color: darkred; }
```

- [Toutes les notions](notions.html)
