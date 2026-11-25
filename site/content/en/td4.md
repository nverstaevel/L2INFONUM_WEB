title: TD4 · Data visualisation with Chart.js
---
**Friday 29 January 2027 · 3 hours.** Starter files: [`td4`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td4).

## Goal

Display your TD1 results as charts with a few lines of JavaScript.

**You have succeeded if** the page shows a chart of your country, with a title and the source.

| Provided | Your job |
|---|---|
| working `chart.html` and `chart.js`, sample `data/summary.json` | adapt data, labels and chart type |

## Before the session

- [ ] I have read [CM4](cm4.html).
- [ ] I have my `summary.json` from TD1.

## Step 1 · Serve the page (20 min)

A browser refuses to let a page opened by double-click read other files. Start a small local web server **in the `td4` folder**, then open <http://localhost:8000/chart.html>:

```
python -m http.server
```

**Checkpoint:** the sample chart appears.

<details><summary>Hint 1</summary><p>Use `python3` on macOS or Linux. Stop the server with Ctrl+C.</p></details>

## Step 2 · JavaScript warm-up (40 min)

Open the *console* (developer tools) and try:

```
const years = [2023, 2024];
const point = { year: 2025, value: 94.98 };
console.log(years.length, point.value);
console.log(years.map(y => y + 1));
```

**Checkpoint:** you can explain each line.


## Step 3 · Your data (30 min)

Replace `data/summary.json` with yours. Read `chart.js` line by line.

**Checkpoint:** the chart shows your country.

<details><summary>Hint 1</summary><p>The *Network* tab shows whether `summary.json` was loaded (status 200).</p></details>

## Step 4 · Adapt (50 min)

Change the type to `bar`, write the country in the title, set the vertical axis from 0 to 100.

**Checkpoint:** the three changes are visible.

<details><summary>Hint 1</summary><p>`options: { scales: { y: { min: 0, max: 100 } } }`</p></details>

## Step 5 · Read critically (40 min)

Compare the line chart with automatic axis and with an axis from 0. In `notes.txt`, write which one you would show a manager and why. Note what happens in 2020.

**Checkpoint:** two short paragraphs.


## Extensions

1. Add a second dataset (another country).
2. Style the page with your TD3 stylesheet.
3. Draw a bar chart comparing the lowest, average and highest values.
