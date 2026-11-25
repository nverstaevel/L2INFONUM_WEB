title: TD4 · Data visualisation with Chart.js
---
**Friday 29 January 2027 · 3 hours.** Starter files: folder [`td4`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td4).

## Goal

Turn your TD1 results into a chart, with a few lines of JavaScript (the programming language of web pages). The code already works: you **adapt** it.

**You have succeeded if**: a chart of your country, with a title and the source, and five `[OK]`.

| Step | You do | Time |
|---|---|---|
| 1 | Start a local server | 25 min |
| 2 | Try JavaScript | 35 min |
| 3 | Use your data | 25 min |
| 4 | Adapt the chart | 55 min |
| 5 | Read it critically | 20 min |

## Notions used in this lab

Open them when you need them: each one is a short page. The links are repeated at the step where you need them.

- [Local server](notion-local-server.html)
- [JavaScript basics](notion-javascript.html)
- [Developer tools](notion-devtools.html)
- [fetch: asking for data](notion-fetch.html)
- [JSON](notion-json.html)
- [Charts with Chart.js](notion-chartjs.html)
- [Changing the page from JavaScript](notion-dom.html)
- [Choosing and reading a chart](notion-honest-charts.html)

**Ready-made examples:** [A chart from a JSON file](recipe-chart-from-json.html)

## Before the session

- [ ] I have read [CM4](cm4.html).
- [ ] I have my `summary.json` from TD1 (a sample is provided).

## How to work

1. Do the steps **in order**.
2. Write your code only where you see `TODO`. Its number is the number in this sheet.
3. After each part, **save** (`Ctrl+S`, or `Cmd+S` on a Mac) and run the checker in a terminal (**Terminal → New Terminal** in VS Code):

```text
python check.py
```

On macOS or Linux, outside a virtual environment, type `python3`. `[OK]` means the part works, `[  ]` means not yet. The checker does not replace looking at your page in the browser.

## Step 1 · Start a local server (25 min)

<p class="refs" markdown="1">**Notion:** [Local server](notion-local-server.html)</p>

A page opened by double-click is not allowed to read other files. A **server** is a program that sends files to the browser. Python has a small one.

Open the folder `td4` in VS Code, open a terminal and run (`python3` on macOS or Linux):

```text
python -m http.server
```

Leave this terminal open. In the browser, go to `http://localhost:8000/chart.html` (`localhost` means "this computer").

**Check.** You see a line chart. To run `check.py`, open a **second** terminal.

<details markdown="1"><summary>Stuck?</summary>

`Address already in use`: run `python -m http.server 8001` and use `localhost:8001`. Error 404: the server was not started in the folder `td4`. Stop it with `Ctrl+C`.

</details>

## Step 2 · Try JavaScript (35 min)

<p class="refs" markdown="1">**Notion:** [JavaScript basics](notion-javascript.html), [Developer tools](notion-devtools.html)</p>

The **console** is a place to type JavaScript: press `F12`, tab **Console**. Type each block, press Enter, and **guess the result before**.

### 2A · Variables

```javascript
const city = "Toulouse";    // const: cannot be changed
let people = 500000;        // let: can be changed
people = people + 1;
console.log(city, people);  // like print()
```

### 2B · Arrays and objects

An **array** is like a Python list. An **object** is like a dictionary, read with a dot.

```javascript
const months = ["Jan", "Feb"];
console.log(months.length, months[0]);

const book = { title: "Emma", pages: 400 };
console.log(book.title);
```

### 2C · map

`map` builds a new array by transforming each item. `x => x.pages` means "for each x, take x.pages".

```javascript
const books = [{ title: "Emma", pages: 400 }, { title: "Dune", pages: 600 }];
console.log(books.map(b => b.pages));    // Python: [b["pages"] for b in books]
```

**Check.** Write the line that gives the two titles. Show it to your neighbour.

<details markdown="1"><summary>Stuck?</summary>

Same line as above, with `b.title`.

</details>

## Step 3 · Use your data (25 min)

<p class="refs" markdown="1">**Notion:** [fetch: asking for data](notion-fetch.html), [JSON](notion-json.html) · **Recipe:** [A chart from a JSON file](recipe-chart-from-json.html)</p>

**Your turn.** Copy **your** `summary.json` (made in TD1, folder `td1/data`) over `td4/data/summary.json`. Reload the page with `Ctrl+F5` (`Cmd+Shift+R` on a Mac). Then read `chart.js` and its comments, line by line.

**Check.** `3` is `[OK]`. In the **Network** tab (`F12`), reload: `summary.json` has the status 200.

## Step 4 · Adapt the chart (55 min)

<p class="refs" markdown="1">**Notion:** [Charts with Chart.js](notion-chartjs.html) · **Recipe:** [A chart from a JSON file](recipe-chart-from-json.html)</p>

Change one thing, save, reload, look. If the chart disappears, read the red message in the console.

### 4A · Bars

**Your turn.** Change the type of chart from `line` to `bar`.

### 4B · A title with the country

<p class="refs" markdown="1">**Notion:** [Changing the page from JavaScript](notion-dom.html)</p>

**Example** (another subject: adapt it, do not copy it as it is).

```javascript
document.getElementById("shop-name").textContent = "Shop of " + data.city;
// finds the element with id="shop-name" and replaces its text
```

**Your turn.** The title of `chart.html` has `id="title"`. Under `TODO 4B`, write a title that ends with `summary.country`.

### 4C · The vertical axis

**Example** (another subject: adapt it, do not copy it as it is).

```javascript
new Chart(canvas, {
  type: "bar",
  data: myData,      // a comma between data and options
  options: { scales: { y: { min: 10, max: 50 } } }
});
```

**Your turn.** Make your axis go from 0 to 100. Do not forget the **comma** before `options`.

**Check.** `4A`, `4B`, `4C` `[OK]` and the three changes are visible.

<details markdown="1"><summary>Stuck?</summary>

Blank page after 4C? The console says `Unexpected identifier` when a comma is missing: it goes just after the `}` that closes `data`.

</details>

## Step 5 · Read the chart critically (20 min)

<p class="refs" markdown="1">**Notion:** [Choosing and reading a chart](notion-honest-charts.html)</p>

**Your turn.** Create `notes.txt` in `td4` and write at least 30 words:

1. Remove the `min` and `max` for a moment and look. Put them back. Which chart would you show to a manager, and why?
2. Which year is missing for some countries (look at 2020)? Does the chart make it visible?

**Check.** Five `[OK]`.

## If you finish early (optional)

1. Add a second series (another country) in `datasets`.
2. Use your TD3 stylesheet.
3. Compare minimum, average and maximum with three bars.
