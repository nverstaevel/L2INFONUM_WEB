title: TD9 · Mini-project 2: pages, filters, charts
---
**Friday 12 March 2027 · 3 hours.** Starter files: folder [`project`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/project).

## Goal

Build the pages, the filter and the first chart.

**You have succeeded if**: the main path works, from the home page to the chart.

| Step | You do | Time |
|---|---|---|
| 1 | Pages | 45 min |
| 2 | Form or filter | 45 min |
| 3 | JSON route and chart | 60 min |
| 4 | Review | 30 min |

## Notions used in this lab

Open them when you need them: each one is a short page. The links are repeated at the step where you need them.

- [Templates and static files](notion-templates.html)
- [Flexbox](notion-css-flexbox.html)
- [URL parameters and query strings](notion-url-parameters.html)
- [Forms](notion-html-forms.html)
- [JSON API](notion-api.html)
- [fetch: asking for data](notion-fetch.html)
- [Charts with Chart.js](notion-chartjs.html)
- [Debugging](notion-debugging.html)

**Ready-made examples:** [A Flask app with a template](recipe-flask-app.html) · [Responsive navigation bar](recipe-nav-bar.html) · [A search form](recipe-search-form.html) · [A JSON API and its chart](recipe-api-chart.html)

## Before the session

- [ ] The remarks of checkpoint 1 are dealt with.

## How to work

Tick each box when it is done (your browser remembers it). Do not start the next part before reaching the **milestone**. Make a copy of your folder after each milestone.

## Step 1 · Pages (45 min)

<p class="refs" markdown="1">**Notion:** [Templates and static files](notion-templates.html), [Flexbox](notion-css-flexbox.html) · **Recipe:** [A Flask app with a template](recipe-flask-app.html), [Responsive navigation bar](recipe-nav-bar.html)</p>

- [ ] For each page: copy `base.html`, rename it, change the titles.
- [ ] Write one route per page (TD5, step 4).
- [ ] Update the links of the menu **in every file**.
- [ ] Add your TD3 rules to `static/style.css`.

**Milestone.** Every link of the menu works.

## Step 2 · Form or filter (45 min)

<p class="refs" markdown="1">**Notion:** [URL parameters and query strings](notion-url-parameters.html), [Forms](notion-html-forms.html) · **Recipe:** [A search form](recipe-search-form.html)</p>

- [ ] Copy the search route and template of TD6.
- [ ] Add `request` to the line `from flask import ...`.
- [ ] Adapt the field names and the test of the loop.
- [ ] Test a normal value, an unknown value and an empty field.

**Milestone.** The display changes with the input and nothing crashes.

## Step 3 · JSON route and chart (60 min)

<p class="refs" markdown="1">**Notion:** [JSON API](notion-api.html), [fetch: asking for data](notion-fetch.html), [Charts with Chart.js](notion-chartjs.html), [Debugging](notion-debugging.html) · **Recipe:** [A JSON API and its chart](recipe-api-chart.html)</p>

- [ ] Copy `api_data` from TD7.
- [ ] Add `jsonify` to the line `from flask import ...`.
- [ ] Test the JSON address **alone** in the browser.
- [ ] Copy `chart.html` to `templates` and `chart.js` to `static`; add the route of the page.
- [ ] Change the title, the label and the type of chart.
- [ ] Check the console: no red message.

**Milestone.** The chart changes when the parameter changes.

## Step 4 · Review (30 min)

- [ ] **Checkpoint 2** (not graded): show pages, filter and chart.
- [ ] Write the list of what remains, most important first.

**Milestone.** You have your list.

## Minimum requirements

| Requirement | Seen in |
|---|---|
| A dataset under an open licence, loaded and cleaned with Python | TD1 |
| At least 3 Flask routes, including 1 JSON route with a parameter | TD5, TD7 |
| At least 1 form or filter that changes what is shown | TD6 |
| At least 1 Chart.js chart fed by the JSON route with `fetch` | TD4, TD7 |
| Hand-written, responsive HTML and CSS, same navigation on every page (`base.html` copied) | TD2, TD3 |
| A README: source, licence, how to run, main routes, help received from AI | TD8 |
