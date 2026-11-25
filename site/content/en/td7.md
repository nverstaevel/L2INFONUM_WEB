title: TD7 · A JSON API used by a chart
---
**Friday 26 February 2027 · 3 hours.** Starter files: folder [`td7`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td7).

## Goal

Your application sends filtered data as JSON, and the page draws it without reloading. An **API** is a set of addresses that programs use to get data.

**You have succeeded if**: choosing another country redraws the chart, and `check.py` shows five `[OK]`.

| Step | You do | Time |
|---|---|---|
| 1 | Install and observe | 25 min |
| 2 | Filter by country | 30 min |
| 3 | Filter by year | 30 min |
| 4 | Handle errors | 45 min |
| 5 | Debug | 30 min |

## Notions used in this lab

Open them when you need them: each one is a short page. The links are repeated at the step where you need them.

- [JSON API](notion-api.html)
- [fetch: asking for data](notion-fetch.html)
- [Developer tools](notion-devtools.html)
- [Comprehensions, min, max, sorted](notion-list-tools.html)
- [URL parameters and query strings](notion-url-parameters.html)
- [HTTP: requests, responses, status codes](notion-http.html)
- [Changing the page from JavaScript](notion-dom.html)
- [Debugging](notion-debugging.html)
- **[Flask, with its result](notion-flask-ref.html)**
- **[JavaScript, with its result](notion-js-ref.html)**

**Ready-made examples:** [A JSON API and its chart](recipe-api-chart.html)

## Before the session

- [ ] I have read [CM7](cm7.html).
- [ ] I have my clean CSV file from TD1.

## How to work

1. Do the steps **in order**.
2. Write your code only where you see `TODO`. Its number is the number in this sheet.
3. After each part, **save** (`Ctrl+S`, or `Cmd+S` on a Mac) and run the checker in a terminal (**Terminal → New Terminal** in VS Code):

```text
python check.py
```

On macOS or Linux, outside a virtual environment, type `python3`. `[OK]` means the part works, `[  ]` means not yet. The checker does not replace looking at your page in the browser.

## Step 1 · Install and observe (25 min)

<p class="refs" markdown="1">**Notion:** [JSON API](notion-api.html), [fetch: asking for data](notion-fetch.html), [Developer tools](notion-devtools.html) · **Recipe:** [A JSON API and its chart](recipe-api-chart.html)</p>

**Shortcut:** you may reuse the environment of TD6 instead of creating one: `..\td6\.venv\Scripts\Activate.ps1` (Windows) or `source ../td6/.venv/bin/activate` (macOS, Linux). If it fails, create a new one as below.

1. Open the folder `td7` in VS Code and a terminal.
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

In the browser press `F12`, open the **Network** tab and reload. Click the line `data?country=FR`, then **Response**. Read `static/chart.js`: `fetch` asks for an address, then the chart is drawn with the answer.

**Check.** You can say who sends this request (the page or Python?). The chart mixes all countries: that is the next step.

## Step 2 · Filter by country (30 min)

<p class="refs" markdown="1">**Notion:** [JSON API](notion-api.html), [Comprehensions, min, max, sorted](notion-list-tools.html) · **Recipe:** [A JSON API and its chart](recipe-api-chart.html)</p>

**Example** (another subject: adapt it, do not copy it as it is).

```python
author = request.args.get("author", "")
found = [b for b in BOOKS if b["author"] == author]    # keep some items
return jsonify(found)
```

### 2A · One country

**Your turn.** Replace `rows = DATA` by the rows of `country`.

**Check.** Type `ES` in the page and click **Show**: the chart changes. With the sample file (France only), the chart is empty: that is correct. `2A` `[OK]`.

## Step 3 · Filter by year (30 min)

<p class="refs" markdown="1">**Notion:** [URL parameters and query strings](notion-url-parameters.html)</p>

**Example** (another subject: adapt it, do not copy it as it is).

```python
pages = request.args.get("pages", type=int)   # None if absent
if pages is not None:
    found = [b for b in found if b["pages"] == pages]
```

### 3A · Optional year

**Your turn.** Accept `year`. Without it, keep all years.

**Check.** `/api/data?country=FR&year=2024` shows one row. `3A` `[OK]`.

## Step 4 · Handle errors (45 min)

<p class="refs" markdown="1">**Notion:** [HTTP: requests, responses, status codes](notion-http.html), [JSON API](notion-api.html)</p>

### 4A · In Python

**Example** (another subject: adapt it, do not copy it as it is).

```python
if not found:
    return jsonify(error="No book found"), 404
```

**Your turn.** Return a JSON error with the code 404 when there is no row. The key must be `error`.

### 4B · In JavaScript

<p class="refs" markdown="1">**Notion:** [Changing the page from JavaScript](notion-dom.html), [fetch: asking for data](notion-fetch.html) · **Recipe:** [A JSON API and its chart](recipe-api-chart.html)</p>

**Example** (another subject: adapt it, do not copy it as it is).

```javascript
if (books.error) {
  document.getElementById("info").textContent = books.error;
  return;                     // stop here: no chart
}
document.getElementById("info").textContent = "";
```

**Your turn.** Under `TODO 4B` in `static/chart.js`, do the same. The answer is called `rows` and the empty paragraph of the page is `message`.

**Check.** Type `ZZ`: a message appears and the console shows no `Uncaught` error. A 404 line is normal. `4A`, `4B` `[OK]`.

<details markdown="1"><summary>Stuck?</summary>

The old JavaScript may be kept by the browser: reload with `Ctrl+F5` (`Cmd+Shift+R` on a Mac).

</details>

## Step 5 · Debug (30 min)

<p class="refs" markdown="1">**Notion:** [Debugging](notion-debugging.html), [Developer tools](notion-devtools.html)</p>

**Debugging** is finding and fixing a mistake. Practise on purpose:

1. In `chart.js`, change `/api/data` into `/api/dat`. Reload.
2. Open the **Console**: what is the message?
3. Open **Network**: which address failed, with which code?
4. Repair it.
5. Write in `notes.txt` (folder `td7`) where you looked and what you saw, in at least 20 words.

**Check.** The chart works again and five `[OK]`.

## When something fails

| You see | Look at |
|---|---|
| `app.py cannot be loaded` | the **last** line of the message: the file line and the kind of error |
| `Not Found` (404) | the spelling of the address in `@app.route` |
| `Method Not Allowed` (405) | `methods=[...]` in the route |
| `Internal Server Error` (500) | the terminal where `app.py` runs: read the last line |

## If you finish early (optional)

1. Compare with a second country.
2. Replace the field by a `select` list.
3. Choose the type of chart in the page.
4. A silent bug: write `row.values` instead of `row.value`. What happens, and is there a message? Repair it.
