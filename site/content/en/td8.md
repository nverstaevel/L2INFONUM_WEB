title: TD8 · Mini-project 1: scope and data
---
**Friday 5 March 2027 · 3 hours.** Starter files: [`project`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/project).

## Goal

Alone or in pairs, choose a question and a dataset, clean the data and design the routes.

**You have succeeded if** at the checkpoint you show clean data and a table of routes.

| Provided | Your job |
|---|---|
| project template: `app.py`, `base.html`, `style.css`, `README.md` | everything specific to your question |

## Before the session

- [ ] I have thought of two possible topics.

## Step 1 · Question and dataset (40 min)

Write one question a manager could ask. Check the licence before anything else.

**Checkpoint:** question, source and licence are in the README.


## Step 2 · Load and clean (70 min)

Adapt your TD1 scripts. Look at the columns and codes first.

**Checkpoint:** a clean CSV with a few clear columns.

<details><summary>Hint 1</summary><p>Other datasets have other dimension columns: keep one value per country and year.</p></details>

## Step 3 · Design (35 min)

Draw the pages on paper and fill the routes table.

**Checkpoint:** 3 routes or more, one JSON with a parameter.


## Step 4 · Checkpoint 1 (35 min)

Short review (not graded): dataset, scope, loading, routes. Meanwhile, write the first route.

**Checkpoint:** feedback noted.


## Minimum requirements

- A dataset under an open licence, loaded and cleaned with Python.
- At least 3 Flask routes, including 1 JSON route with a parameter.
- At least 1 form or filter that changes what is displayed.
- At least 1 Chart.js chart fed by the JSON route through `fetch`.
- Hand-written HTML and CSS, responsive, with a shared navigation bar (`base.html` copied into each page).
- A README: data source, licence, how to run, main routes, AI help received.

## Safe datasets (Eurostat)

| Code | Content |
|---|---|
| [`tipsun20`](https://ec.europa.eu/eurostat/databrowser/view/tipsun20/default/table?lang=en) | Unemployment rate, annual (several age groups: filter `age`) |
| [`sdg_07_40`](https://ec.europa.eu/eurostat/databrowser/view/sdg_07_40/default/table?lang=en) | Share of renewable energy (several sectors: filter `nrg_bal`) |
| [`sdg_11_60`](https://ec.europa.eu/eurostat/databrowser/view/sdg_11_60/default/table?lang=en) | Recycling rate of municipal waste |
| [`sdg_08_10`](https://ec.europa.eu/eurostat/databrowser/view/sdg_08_10/default/table?lang=en) | Real GDP per capita (two units: filter `unit`) |

Checked on 25 November 2026. Download address: replace `tin00028` in the TD1 address with the code. Reuse with attribution ([notice](https://ec.europa.eu/eurostat/help/copyright-notice)). Other portals: [data.gouv.fr](https://www.data.gouv.fr), [Toulouse Métropole](https://data.toulouse-metropole.fr), [data.europa.eu](https://data.europa.eu).
