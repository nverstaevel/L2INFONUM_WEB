title: TD5 · Flask: routes and responses
---
**Friday 5 February 2027 · 3 hours.** Starter files: [`td5`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td5).

## Goal

Run your first Flask application with several routes returning text, HTML and JSON.

**You have succeeded if** five addresses answer, with the right status codes.

| Provided | Your job |
|---|---|
| `app.py` with one route, `templates/base.html`, `static/style.css` | the five `TODO` |

## Before the session

- [ ] I have read [CM5](cm5.html).
- [ ] Python and my virtual environment work.

## Step 1 · Install and run (30 min)

A *web framework* is a library that does the repetitive work of a web server. In `td5`, create the environment ([setup](setup.html)), then:

```
python -m pip install -r requirements.txt
python app.py
```

**Checkpoint:** <http://127.0.0.1:5000/> says Hello.


## Step 2 · Routes (35 min)

A *route* links an address to a Python function. Add `/about`.

**Checkpoint:** `/about` shows HTML.

<details><summary>Hint 1</summary><p>`@app.route("/about")` just above the function.</p></details>

## Step 3 · JSON and URL parameter (40 min)

Add `/api/info` with `jsonify`, then `/country/<code>`.

**Checkpoint:** `/country/fr` shows `FR`.

<details><summary>Hint 1</summary><p>The function receives `code` as an argument.</p></details>
<details><summary>Hint 2</summary><p>Returning plain text with user input is risky: use a template with `{{ code }}` (copy `base.html`).</p></details>

## Step 4 · Templates (45 min)

A *template* is an HTML file with holes `{{ name }}` filled by `render_template`. Create `templates/index.html` from `base.html`.

**Checkpoint:** the home page is styled and its title comes from Python.

<details><summary>Hint 1</summary><p>`render_template("index.html", title="…")`</p></details>

## Step 5 · Status codes (20 min)

Add `/teapot` with code 418 and observe it in the Network tab.

**Checkpoint:** you see 200, 404 and 418.

<details><summary>Hint 1</summary><p>`return "message", 418`</p></details>

## Extensions

1. Add `/count` that shows the number of rows of your clean file.
2. Add a custom page for errors 404 with `@app.errorhandler(404)`.
