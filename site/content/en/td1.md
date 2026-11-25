title: TD1 · Python, files and open data
---
**Friday 8 January 2027 · 3 hours.** Starter files: folder `td1` of the [repository](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td1).

## Goal

Download a real Eurostat dataset, clean it and compute simple statistics. **Keep your files:** they are reused in the next labs.

**You have succeeded if** `data/internet_use_clean.csv` has the header `country,year,value`, contains only countries, and `data/summary.json` gives the latest year and the history of your country.

| Provided | Your job |
|---|---|
| three script skeletons, `requirements.txt` | the `TODO` lines |

## Before the session

- [ ] I have read [CM1](cm1.html).
- [ ] Python and VS Code are installed ([setup guide](setup.html)).

## Step 1 · Environment (30 min)

Follow part 3 of the [setup guide](setup.html) inside the `td1` folder.

**Checkpoint:** `(.venv)` is shown and `import requests` works.

<details><summary>Need help?</summary><p>Look at the Troubleshooting table of the setup guide.</p></details>

## Step 2 · Download (30 min)

`requests` is a package that sends HTTP requests from Python. Complete `download.py`. The address is:

```
https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/tin00028?format=SDMX-CSV&compress=false
```

Run `python download.py`.

**Checkpoint:** `data/internet_use.csv` exists and opens as text.

<details><summary>Hint 1</summary><p>A <em>status code</em> of 200 means success. It is in <code>response.status_code</code>.</p></details>
<details><summary>Hint 2</summary><p><code>OUTPUT.write_bytes(...)</code> writes bytes (raw file content) into a file.</p></details>

## Step 3 · Explore (30 min)

Open the file in VS Code. Answer in a file `notes.txt`:

1. What are the column names?
2. What do `geo`, `TIME_PERIOD` and `OBS_VALUE` contain?
3. Find a `geo` code that is not a country.
4. Is every year present for every country?
5. Who produced the data, and what must you do to reuse it? ([Eurostat copyright notice](https://ec.europa.eu/eurostat/help/copyright-notice))

**Checkpoint:** five answers.

## Step 4 · Clean (45 min)

Complete `clean.py`. Keep rows where `indic_is` is `I_IU3` (used the internet in the last 3 months), `geo` is a country and `OBS_VALUE` is not empty.

**Checkpoint:** the script prints the number of rows read and kept, and the clean file has no `EU27_2020`.

<details><summary>Hint 1</summary><p><code>csv.DictReader</code> gives one dictionary per row.</p></details>
<details><summary>Hint 2</summary><p><code>continue</code> jumps to the next row of a loop.</p></details>
<details><summary>Hint 3</summary><p><code>csv.DictWriter</code> needs <code>fieldnames</code>, then <code>writeheader()</code> and <code>writerows()</code>.</p></details>

## Step 5 · Statistics (45 min)

Complete `stats.py`: for the latest year, the average, lowest and highest value; then the history of your country. Save everything in `data/summary.json`.

*The average is a simple mean of countries. It is not the EU figure, which takes population into account.*

**Checkpoint:** compare your country's latest value with the [Eurostat table](https://ec.europa.eu/eurostat/databrowser/view/tin00028/default/table?lang=en).

<details><summary>Hint 1</summary><p><code>max(r["year"] for r in rows)</code> gives the latest year.</p></details>
<details><summary>Hint 2</summary><p><code>min(rows, key=lambda r: r["value"])</code> returns the whole row.</p></details>
<details><summary>Hint 3</summary><p><code>json.dump(result, f, indent=2)</code></p></details>

## Extensions

1. Print the top 5 countries of the latest year.
2. For each country, compute the change since 2015. Handle countries with no 2015 value.
3. Add a dictionary of country names (`"FR": "France"`). Note that Greece is `EL`.
4. Ask the country code with `input()`.

## Source

Eurostat, dataset `tin00028`. Reuse allowed with the source acknowledged. Say when you have modified the data.
