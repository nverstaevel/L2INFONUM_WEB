title: Flask, with its result
---
The Flask you need, each time with **what the server answers**. Every example needs these lines before it, and the usual last two lines after it. `GET /about  ->  200` means: the address asked, then the status code. See also the [official documentation](https://flask.palletsprojects.com).

```python
from flask import Flask, jsonify, render_template, request, session

app = Flask(__name__)

# ... one example here ...

if __name__ == "__main__":
    app.run(debug=True)     # only on your own computer
```

## Routes and answers

### `@app.route` and `return`

A **route** links an address to a Python function. What the function returns is sent to the browser.

```python
@app.route("/")
def home():
    return "Hello"
```

**What you see**

```text
GET /  ->  200
Hello

GET /nothing  ->  404
```

### part of the address: `<name>`

A piece of the address becomes a parameter of the function.

```python
@app.route("/book/<title>")
def book(title):
    return f"Book: {title}"
```

**What you see**

```text
GET /book/Emma  ->  200
Book: Emma
```

### status codes

Add a number after the answer: 200 is the default, 404 means not found.

```python
@app.route("/old")
def old():
    return "This page is gone", 404
```

**What you see**

```text
GET /old  -> 404
This page is gone
```

### `jsonify`

Send data as JSON, for a program or for `fetch`.

```python
@app.route("/api/books")
def api_books():
    return jsonify([{"title": "Emma", "year": 1815}])
```

**What you see**

```text
GET /api/books  ->  200
[{"title":"Emma","year":1815}]
```

## What the visitor sends

### `request.args` (GET)

The values after `?` in the address. With `type=int`, a wrong value gives the default.

```python
@app.route("/search")
def search():
    author = request.args.get("author", "")
    year = request.args.get("year", 0, type=int)
    return f"author={author} year={year}"
```

**What you see**

```text
GET /search?author=Austen&year=1815  ->  200
author=Austen year=1815

GET /search?year=abc  ->  200
author= year=0
```

### `methods` and `request.form` (POST)

A form sent with `method="post"` is read in `request.form`. A method that is not listed gives 405.

```python
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        return "received " + request.form.get("title", "")
    return "send me a title"
```

**What you see**

```text
GET /add  ->  200
send me a title

POST /add  data={'title': 'Emma'}  ->  200
received Emma

DELETE /add  ->  405
```

### `session`

Memory for one visitor, kept in a signed **cookie**. It needs `app.secret_key`. Assign a new value to save it.

```python
app.secret_key = "change-me"

@app.route("/visit")
def visit():
    session["count"] = session.get("count", 0) + 1
    return f"visit number {session['count']}"
```

**What you see**

```text
GET /visit  ->  200
visit number 1

GET /visit  ->  200
visit number 2

another visitor:
GET /visit  ->  200
visit number 1
```

## Pages and files

### `render_template` and `{{ }}`

Send an HTML file of the folder `templates`, with holes filled by Python. Flask **escapes** the values: `<` is shown, not interpreted.

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

**What you see**

```text
GET /hello?name=Ada  ->  200
<h1>Hello Ada</h1>

GET /hello?name=<b>  ->  200
<h1>Hello &lt;b&gt;</h1>
```

### static files

Files of the folder `static` (CSS, JavaScript, images) are sent as they are, at the address `/static/...`.

```python
# no route to write
# static/style.css  ->  /static/style.css
```

`static/style.css`

```css
h1 { color: darkred; }
```

**What you see**

```text
GET /static/style.css  -> 200
h1 { color: darkred; }
```

- [All notions](notions.html)
