title: TD5 · Flask: routes and responses
---
**Friday 5 February 2027 · 3 hours.** Starter files: folder [`td5`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td5).

## Goal

Run your first application with Flask, a Python package that answers web requests.

**You have succeeded if**: `python check.py` shows seven `[OK]`.

| Step | You do | Time |
|---|---|---|
| 1 | Install and run | 30 min |
| 2 | A first route | 25 min |
| 3 | Return JSON | 25 min |
| 4 | A template | 45 min |
| 5 | A value in the address | 35 min |
| 6 | Status codes | 20 min |

## Notions used in this lab

Open them when you need them: each one is a short page. The links are repeated at the step where you need them.

- [Terminal and virtual environment](notion-terminal-venv.html)
- [Local server](notion-local-server.html)
- [Flask and routes](notion-flask-routes.html)
- [JSON](notion-json.html)
- [JSON API](notion-api.html)
- [Templates and static files](notion-templates.html)
- [URL parameters and query strings](notion-url-parameters.html)
- [Input checking and escaping](notion-safety.html)
- [HTTP: requests, responses, status codes](notion-http.html)
- [Developer tools](notion-devtools.html)

**Ready-made examples:** [Set up a project](recipe-venv.html) · [A Flask app with a template](recipe-flask-app.html)

## Before the session

- [ ] I have read [CM5](cm5.html).

## How to work

1. Do the steps **in order**.
2. Write your code only where you see `TODO`. Its number is the number in this sheet.
3. After each part, **save** (`Ctrl+S`, or `Cmd+S` on a Mac) and run the checker in a terminal (**Terminal → New Terminal** in VS Code):

```text
python check.py
```

On macOS or Linux, outside a virtual environment, type `python3`. `[OK]` means the part works, `[  ]` means not yet. The checker does not replace looking at your page in the browser.

## Step 1 · Install and run (30 min)

<p class="refs" markdown="1">**Notion:** [Terminal and virtual environment](notion-terminal-venv.html), [Local server](notion-local-server.html) · **Recipe:** [Set up a project](recipe-venv.html)</p>

1. Open the folder `td5` in VS Code and a terminal.
2. Create the environment (see the [setup guide](setup.html) if it fails).

Windows:

```text
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS / Linux:

```text
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Start the application:

```text
python app.py
```

Open `http://127.0.0.1:5000/` (`127.0.0.1` means "this computer"). Leave this terminal running: `Ctrl+C` stops it. Run `check.py` in a **second** terminal, after activating the environment there too. The application restarts by itself when you save a `.py` file.

**Check.** The browser says `Hello, web!` and `check.py` shows seven `[  ]`.

## Step 2 · A first route (25 min)

<p class="refs" markdown="1">**Notion:** [Flask and routes](notion-flask-routes.html) · **Recipe:** [A Flask app with a template](recipe-flask-app.html)</p>

A **route** links an address to a Python function. The line starting with `@` is a **decorator**: it applies to the function just below. What the function returns is sent to the browser. Read the route `/` in `app.py`.

**Example** (another subject: adapt it, do not copy it as it is).

```python
@app.route("/contact")
def contact():
    return "<h1>Contact</h1><p>Write to the library.</p>"
```

### 2A · /about

**Your turn.** Under `TODO 2A`, write the route `/about`: it returns an `h1` and a paragraph naming the dataset `tin00028`. Two functions cannot have the same name.

**Check.** `http://127.0.0.1:5000/about` shows your text and `2A` is `[OK]`.

## Step 3 · Return JSON (25 min)

<p class="refs" markdown="1">**Notion:** [JSON](notion-json.html), [JSON API](notion-api.html)</p>

**JSON** is data written as text. Programs read it more easily than HTML. `jsonify` makes it.

**Example** (another subject: adapt it, do not copy it as it is).

```python
@app.route("/api/library")
def library():
    return jsonify(name="City library", books=1200)
```

### 3A · /api/info

**Your turn.** Write `/api/info` with three keys: `source`, `unit`, `licence`.

**Check.** The browser shows the three keys; `3A` is `[OK]`.

## Step 4 · A template (45 min)

<p class="refs" markdown="1">**Notion:** [Templates and static files](notion-templates.html) · **Recipe:** [A Flask app with a template](recipe-flask-app.html)</p>

Writing a whole page inside Python is painful. A **template** is an HTML file, in the folder `templates`, with holes written `{{ name }}`. `render_template` fills them.

**Example** (another subject: adapt it, do not copy it as it is).

```python
# in app.py
return render_template("shop.html", city="Toulouse", number=3)
```

```html
<!-- in templates/shop.html -->
<h1>Shops in {{ city }}</h1>
<p>{{ number }} shops</p>
```

### 4A · Create index.html

**Your turn.** Copy `templates/base.html` and name the copy `templates/index.html`. In the copy, replace the text of `h1` by `{{ title }}`.

### 4B · Use it

**Your turn.** In the function `home`, replace the returned text by a `render_template` of `index.html`, giving a value to `title`.

**Check.** The home page has the menu, the colours and your title. `4A`, `4B` `[OK]`.

<details markdown="1"><summary>Stuck?</summary>

`return render_template("index.html", title="…")`. An error `TemplateNotFound` means that the folder or file name is misspelled.

</details>

## Step 5 · A value in the address (35 min)

<p class="refs" markdown="1">**Notion:** [URL parameters and query strings](notion-url-parameters.html), [Input checking and escaping](notion-safety.html)</p>

A part of the address written `<name>` is given to the function as an argument.

**Example** (another subject: adapt it, do not copy it as it is).

```python
@app.route("/book/<title>")
def book(title):
    return render_template("book.html", title=title.capitalize())
```

### 5A · Create country.html

**Your turn.** Copy `base.html` to `templates/country.html`. Make the `h1` show `{{ code }}`.

### 5B · The route

**Your turn.** Write `/country/<code>`: it renders `country.html` with the code in **capital letters** (`.upper()`).

**Check.** `/country/fr` shows `FR`, `/country/es` shows `ES`. `5A`, `5B` `[OK]`.

Why a template and not `return code`? `{{ }}` shows what the visitor typed as plain text, so nobody can slip code into your page.

## Step 6 · Status codes (20 min)

<p class="refs" markdown="1">**Notion:** [HTTP: requests, responses, status codes](notion-http.html), [Developer tools](notion-devtools.html)</p>

Every answer has a number: 200 success, 404 not found, 500 error in your code. You can choose it by returning two values.

**Example** (another subject: adapt it, do not copy it as it is).

```python
return "This book is gone", 410
```

### 6A · /teapot

**Your turn.** Write `/teapot`, which returns a message with the code 418.

**Check.** In the **Network** tab (`F12`), reload `/teapot`: you read 418. Visit `/nothing`: 404. Seven `[OK]`.

## When something fails

| You see | Look at |
|---|---|
| `app.py cannot be loaded` | the **last** line of the message: the file line and the kind of error |
| `Not Found` (404) | the spelling of the address in `@app.route` |
| `Method Not Allowed` (405) | `methods=[...]` in the route |
| `Internal Server Error` (500) | the terminal where `app.py` runs: read the last line |

## If you finish early (optional)

1. Add `/count`: the number of lines of your clean file (copy it into `td5/data`).
2. Customise the 404 page with `@app.errorhandler(404)`.
