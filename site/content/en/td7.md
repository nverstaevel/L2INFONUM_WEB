title: TD7 · A JSON API consumed by a chart
---
**Friday 26 February 2027 · 3 hours.** Starter files: [`td7`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td7).

## Goal

Serve filtered data as JSON and draw it with a chart that updates.

**You have succeeded if** choosing another country redraws the chart without reloading the page.

| Provided | Your job |
|---|---|
| `app.py`, `templates/chart.html`, working `static/chart.js` | the four `TODO` |

## Before the session

- [ ] I have read [CM7](cm7.html).
- [ ] My clean CSV is in `data/`.

## Step 1 · Observe (25 min)

Run the app. Open the Network tab, reload, click `data?country=FR` and read the response.

**Checkpoint:** you can say who sends the request.


## Step 2 · Filter by country (35 min)

Complete the route so that only one country is returned.

**Checkpoint:** the chart changes when you type `DE`.

<details><summary>Hint 1</summary><p>A list comprehension: `[r for r in DATA if ...]`.</p></details>

## Step 3 · Year parameter (35 min)

Accept `?year=2022`.

**Checkpoint:** `/api/data?country=FR&year=2022` returns one row.

<details><summary>Hint 1</summary><p>`request.args.get("year", type=int)` gives `None` if absent.</p></details>

## Step 4 · Errors (45 min)

Return a JSON error with status 404, and show the message in the page.

**Checkpoint:** typing `ZZ` shows a message; the console has no red uncaught error.

<details><summary>Hint 1</summary><p>`return jsonify(error="..."), 404`</p></details>
<details><summary>Hint 2</summary><p>In JavaScript test `rows.error`, then `return`.</p></details>

## Step 5 · Debug (40 min)

Break the route address in `chart.js` on purpose. Find the error with the console and the Network tab, then fix it.

**Checkpoint:** you can describe your method in three lines.


## Extensions

1. Add a second country to compare.
2. Replace the text field with a `select`.
3. Choose the chart type from the page.
