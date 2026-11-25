title: TD6 · Parameters, forms and sessions
---
**Friday 12 February 2027 · 3 hours.** Starter files: folder [`td6`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td6).

## Goal

Build pages that react to what the visitor types: a search, a filter and a list of favourites.

**You have succeeded if**: `python check.py` shows six `[OK]`.

| Step | You do | Time |
|---|---|---|
| 1 | Install and look | 15 min |
| 2 | Search by country | 40 min |
| 3 | Form and filter | 25 min |
| 4 | Favourites | 40 min |
| 5 | Check the input | 15 min |

## Notions used in this lab

Open them when you need them: each one is a short page. The links are repeated at the step where you need them.

- [Lists of dictionaries](notion-lists-dicts.html)
- [Templates and static files](notion-templates.html)
- [URL parameters and query strings](notion-url-parameters.html)
- [Forms](notion-html-forms.html)
- [GET and POST](notion-get-post.html)
- [Sessions and cookies](notion-sessions.html)
- [Input checking and escaping](notion-safety.html)
- **[Flask, with its result](notion-flask-ref.html)**
- **[Python, with its result](notion-python-ref.html)**

**Ready-made examples:** [Set up a project](recipe-venv.html) · [A search form](recipe-search-form.html) · [Remember a list with a session](recipe-session-list.html)

## Before the session

- [ ] I have read [CM6](cm6.html).
- [ ] I have my clean CSV file from TD1.

## How to work

1. Do the steps **in order**.
2. Write your code only where you see `TODO`. Its number is the number in this sheet.
3. After each part, **save** (`Ctrl+S`, or `Cmd+S` on a Mac) and run the checker in a terminal (**Terminal → New Terminal** in VS Code):

```text
python check.py
```

On macOS or Linux, outside a virtual environment, type `python3`. `[OK]` means the part works, `[  ]` means not yet. The checker does not replace looking at your page in the browser.

## Five-minute reminder

`DATA` is a list of dictionaries with the keys `country`, `year`, `value`. In this course a template only contains `{{ name }}`: no loop. So **Python builds the text**, and the template shows it.

## Step 1 · Install and look (15 min)

<p class="refs" markdown="1">**Notion:** [Lists of dictionaries](notion-lists-dicts.html), [Templates and static files](notion-templates.html) · **Recipe:** [Set up a project](recipe-venv.html)</p>

1. Open the folder `td6` in VS Code and a terminal.
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

Then copy **your** `internet_use_clean.csv` (made in TD1) into the folder `data`. No file? Copy the one in the folder `sample`: it only contains France.

Start the application:

```text
python app.py
```

Open `http://127.0.0.1:5000/` (`127.0.0.1` means "this computer"). Leave this terminal running: `Ctrl+C` stops it. Run `check.py` in a **second** terminal, after activating the environment there too. The application restarts by itself when you save a `.py` file.

**Check.** The home page says how many rows are loaded.

## Step 2 · Search by country (40 min)

<p class="refs" markdown="1">**Notion:** [URL parameters and query strings](notion-url-parameters.html) · **Recipe:** [A search form](recipe-search-form.html)</p>

### 2A · Read the template

The pages are **already written**: you only write Python. Open `templates/search.html`.

**Your turn.** Find the three holes `{{ ... }}` and write their names on paper: your route must give a value to each. `<pre>` keeps the line breaks.

### 2B · Read the address

In `/search?country=FR`, the part after `?` is the **query string**. `request.args.get` reads it. The second argument is the value used when it is missing.

**Example** (another subject: adapt it, do not copy it as it is).

```python
@app.route("/books")
def books():
    author = request.args.get("author", "").strip().upper()   # strip: no spaces
    return render_template("books.html", results=author)
```

**Your turn.** Write the route `/search`: read `country` the same way and, for now, show it in `results`. Test `/search?country=fr`: you read `FR`.

### 2C · Build the lines

**Example** (another subject: adapt it, do not copy it as it is).

```python
lines = []
for book in BOOKS:
    if author == "" or book["author"] == author:
        lines.append(f"{book['title']}  {book['year']}")
results = "\n".join(lines)      # one line under the other
```

**Your turn.** Build `results` from `DATA`: keep the rows of the country (all rows if `country` is empty), one line with country, year and value.

**Check.** `/search?country=FR` lists the years of France. `2B-2C` `[OK]`.

<details markdown="1"><summary>Stuck?</summary>

Inside an `f"..."` text use single quotes: `{row['year']}`. The `return` must be **after** the loop, not inside it.

</details>

## Step 3 · Form and filter (25 min)

<p class="refs" markdown="1">**Notion:** [Forms](notion-html-forms.html), [URL parameters and query strings](notion-url-parameters.html) · **Recipe:** [A search form](recipe-search-form.html)</p>

### 3A · Read the form

**Your turn.** In `search.html`, read the `form`. Which address does it call (`action`)? What are the `name`s of the two fields? Fill the form, click, and compare with the address bar.

### 3B · The minimum value

**Example** (another subject: adapt it, do not copy it as it is).

```python
maximum = request.args.get("pages", 1000, type=int)   # converted to a number
# then, in the test of the loop:   ... and book["pages"] <= maximum
```

**Your turn.** Read `minimum` as a decimal number (`type=float`, default 0) and keep only the rows whose value is at least this. Put brackets around the country test: `(... or ...) and ...`.

### 3C · No result, and keep the values

**Your turn.** If `lines` is empty, `results` must be exactly `No result.`. Then give `country` and `minimum` to `render_template`: the template already shows them in the fields.

**Check.** Search with several values: the list changes and the fields keep what you typed. `3B`, `3C` `[OK]`.

<details markdown="1"><summary>Stuck?</summary>

`if not lines:` is true when the list is empty.

</details>

## Step 4 · Favourites (40 min)

<p class="refs" markdown="1">**Notion:** [GET and POST](notion-get-post.html), [Sessions and cookies](notion-sessions.html) · **Recipe:** [Remember a list with a session](recipe-session-list.html)</p>

**GET** asks for a page. **POST** sends data that changes something. A **session** remembers data for one visitor between pages, in a **cookie** (a small text kept by the browser).

### 4A · Read the template

**Your turn.** Open `templates/favourites.html`. Note the `method` of the form, the `name` of the field and the name of the hole `{{ ... }}`.

### 4B · The route

**Example** (another subject: adapt it, do not copy it as it is).

```python
@app.route("/basket", methods=["GET", "POST"])
def basket():
    if request.method == "POST":
        item = request.form.get("item", "").strip().upper()   # form, not args
        print("received", item)                              # look in the terminal
    return render_template("basket.html", items="nothing yet")
```

**Your turn.** Write `/favourites` the same way: read `country`, print it, show `none` for now.

### 4C · Remember

**Example** (another subject: adapt it, do not copy it as it is).

```python
items = session.get("basket", [])          # the list, empty the first time
if request.method == "POST":
    ...
    if item and item not in items:
        items = items + [item]              # a NEW list
        session["basket"] = items           # saved
text = ", ".join(items) if items else "none"
```

**Your turn.** Do the same with `session["favourites"]` and give the text to the template under the name `favourites`.

**Check.** Add `FR`, go to another page, come back: it is still there. `4B`, `4C` `[OK]`.

## Step 5 · Check the input (15 min)

<p class="refs" markdown="1">**Notion:** [Input checking and escaping](notion-safety.html) · **Recipe:** [Remember a list with a session](recipe-session-list.html)</p>

A visitor can type anything. Always check.

### 5A · Known codes only

**Example** (another subject: adapt it, do not copy it as it is).

```python
known = any(book["author"] == author for book in BOOKS)   # True if at least one
```

**Your turn.** Add the country only if it exists in `DATA`.

**Check.** `ZZ` is not added; six `[OK]`. In the search field, type `<b>`: it is shown as text, not as bold.

## When something fails

| You see | Look at |
|---|---|
| `app.py cannot be loaded` | the **last** line of the message: the file line and the kind of error |
| `Not Found` (404) | the spelling of the address in `@app.route` |
| `Method Not Allowed` (405) | `methods=[...]` in the route |
| `Internal Server Error` (500) | the terminal where `app.py` runs: read the last line |

## Going further (optional)

### Empty the list

Add this second form to `favourites.html`. The `name` and `value` of a button are sent when it is clicked.

```html
<form action="/favourites" method="post">
  <button type="submit" name="action" value="clear">Empty the list</button>
</form>
```

In the route, if `request.form.get("action")` is `"clear"`, the list becomes empty and is saved in the session.

### Work on the templates

1. Add a field `year` to the form of `search.html`, with its `{{ year }}`, and filter with it.
2. Rebuild `search.html` yourself from `base.html`.

### And also

1. Show the average of the results.
2. After a POST, redirect with `redirect`.
