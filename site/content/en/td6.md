title: TD6 · Parameters, forms and sessions
---
**Friday 12 February 2027 · 3 hours.** Starter files: [`td6`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td6).

## Goal

Build pages that react to user input: search, filter and a favourites list.

**You have succeeded if** a search by country and minimum value works, and favourites stay after changing page.

| Provided | Your job |
|---|---|
| `app.py` with data loading, `base.html`, `index.html` | two templates and four `TODO` |

## Before the session

- [ ] I have read [CM6](cm6.html).
- [ ] My clean CSV is in `data/`.

## Step 1 · Query string (45 min)

Create `/search`. `request.args.get` reads `?country=FR`. We use no loop in templates: build the lines in Python, join them and show them in a `<pre>` block, which keeps line breaks:

```
results = "\n".join(lines)
# in the template:
<pre>{{ results }}</pre>
```

**Checkpoint:** `/search?country=FR` lists the years.

<details><summary>Hint 1</summary><p>`request.args.get("country", "").strip().upper()`</p></details>

## Step 2 · GET form and filter (45 min)

Add a form with `method="get"` for the country and a minimum value.

**Checkpoint:** changing the minimum changes the list.

<details><summary>Hint 1</summary><p>`request.args.get("minimum", 0, type=float)`</p></details>
<details><summary>Hint 2</summary><p>Handle the case with no result.</p></details>

## Step 3 · POST and session (50 min)

A *session* remembers data for one visitor, in a signed *cookie* (a small text kept by the browser). Create `/favourites` with `methods=["GET", "POST"]`.

**Checkpoint:** a country added is still there after visiting another page.

<details><summary>Hint 1</summary><p>`request.form.get("country")` reads a POST field.</p></details>
<details><summary>Hint 2</summary><p>Assign a new list: `session["favourites"] = codes + [code]`.</p></details>
<details><summary>Hint 3</summary><p>Show it with `", ".join(codes)`.</p></details>

## Step 4 · Check input (25 min)

Accept only codes that exist in the data. Add a button that empties the list.

**Checkpoint:** `ZZ` is not added; searching `<b>` shows the text, not bold.

<details><summary>Hint 1</summary><p>Never disable escaping on user input: `{{ }}` protects you.</p></details>

## Extensions

1. Show the average of the results.
2. Keep the form values after submitting.
3. Redirect after the POST with `redirect`.
