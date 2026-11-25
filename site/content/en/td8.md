title: TD8 · Mini-project 1: scope and data
---
**Friday 5 March 2027 · 3 hours.** Starter files: folder [`project`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/project).

## Goal

Alone or in pairs: choose a question and a dataset, clean the data, plan the pages.

**You have succeeded if**: you show a clean CSV file and a table of routes.

| Step | You do | Time |
|---|---|---|
| 1 | Question and dataset | 40 min |
| 2 | Load and clean | 75 min |
| 3 | Plan the pages | 30 min |
| 4 | First route and review | 35 min |

## Before the session

- [ ] I have thought of two possible topics.

## How to work

Tick each box when it is done (your browser remembers it). Do not start the next part before reaching the **milestone**. Make a copy of your folder after each milestone.

## Step 1 · Question and dataset (40 min)

A good question compares or follows something over time. Example: *How has the share of renewable energy changed in my country and in two others?*

Unsure? Take one of these Eurostat datasets (checked on 25 November 2026):

| Code | Content | Filter to apply |
|---|---|---|
| [`tipsun20`](https://ec.europa.eu/eurostat/databrowser/view/tipsun20/default/table?lang=en) | Annual unemployment rate | one `age`, for example `Y15-74` |
| [`sdg_07_40`](https://ec.europa.eu/eurostat/databrowser/view/sdg_07_40/default/table?lang=en) | Share of renewable energy | one `nrg_bal`, for example `REN` |
| [`sdg_11_60`](https://ec.europa.eu/eurostat/databrowser/view/sdg_11_60/default/table?lang=en) | Recycling rate of municipal waste | none |
| [`sdg_08_10`](https://ec.europa.eu/eurostat/databrowser/view/sdg_08_10/default/table?lang=en) | Real GDP per capita | one `unit` |

Reuse is allowed with attribution ([notice](https://ec.europa.eu/eurostat/help/copyright-notice)). Other portals: [data.gouv.fr](https://www.data.gouv.fr), [Toulouse Métropole](https://data.toulouse-metropole.fr), [data.europa.eu](https://data.europa.eu).

- [ ] Copy the folder `project` and rename it with your names.
- [ ] Write the question in `README.md`.
- [ ] Write the source, the producer and the **licence** (no licence: change dataset).

**Milestone.** Question, source and licence are in the README.

## Step 2 · Load and clean (75 min)

Reuse your three TD1 scripts. For a Eurostat dataset, only the address changes (replace `tin00028` by your code), then the filters.

- [ ] Copy `download.py` and `clean.py` into your project; change the address and file names.
- [ ] Run the download and open the file: read the column names.
- [ ] Remove the test on `indic_is` if your file has no such column.
- [ ] Add your filter (table above).
- [ ] Check: only one row per country and year.

**Example** (another subject: adapt it, do not copy it as it is).

```python
if row["age"] != "Y15-74":   # keep one value of a column
    continue
```

<details markdown="1"><summary>Stuck?</summary>

Print the different values of a column: `print(set(row["age"] for row in rows))`.

</details>

**Milestone.** A clean CSV file `country,year,value` in the folder `data`.

## Step 3 · Plan the pages (30 min)

- [ ] Draw each page on paper.
- [ ] Fill the table of routes of the README (at least 3, one JSON with a parameter).
- [ ] Decide who does what.

**Example** (another subject: adapt it, do not copy it as it is).

```text
| Route                  | Method | What it does                |
| /                      | GET    | presents the question       |
| /search                | GET    | filter by country           |
| /api/data?country=FR   | GET    | JSON used by the chart      |
```

**Milestone.** The table of routes is complete.

## Step 4 · First route and review (35 min)

- [ ] Copy `load_data` from TD6 and show the number of rows on the home page.
- [ ] **Checkpoint 1** (short review, not graded): show your data and your routes.
- [ ] Write the teacher's remarks.

**Milestone.** The application runs and loads your data.

## Minimum requirements

| Requirement | Seen in |
|---|---|
| A dataset under an open licence, loaded and cleaned with Python | TD1 |
| At least 3 Flask routes, including 1 JSON route with a parameter | TD5, TD7 |
| At least 1 form or filter that changes what is shown | TD6 |
| At least 1 Chart.js chart fed by the JSON route with `fetch` | TD4, TD7 |
| Hand-written, responsive HTML and CSS, same navigation on every page (`base.html` copied) | TD2, TD3 |
| A README: source, licence, how to run, main routes, help received from AI | TD8 |
