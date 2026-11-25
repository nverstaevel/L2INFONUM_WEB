title: TD1 · Python, files and open data
---
**Friday 8 January 2027 · 3 hours.** Starter files: folder `td1` of the [repository](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td1).

## Goal

You will download real data from Eurostat (the statistics office of the European Union), clean it and compute a few figures. **Keep your files:** the next labs use them.

| Step | Script (a file of Python code) | It produces | Time |
|---|---|---|---|
| 1 | none: set up | a working environment | 25 min |
| 2 | `download.py` | `data/internet_use.csv` | 25 min |
| 3 | none: read the data | `notes.txt` | 20 min |
| 4 | `clean.py` | `data/internet_use_clean.csv` | 55 min |
| 5 | `stats.py` | `data/summary.json` | 45 min |

## How to work

1. Do the steps **in order**. Each one needs the previous one.
2. Write your code only where you see `TODO`. The number of the `TODO` is the number in this sheet.
3. After each part, **save** the file (`Ctrl+S`, or `Cmd+S` on a Mac) and run the checker:
```text
python check.py
```
`[OK]` means that the part works. `[  ]` means not yet: read the message after the arrow. It is normal to see many `[  ]` at the start.

## Five-minute reminder

A table of data is a **list of dictionaries**: one dictionary per row, one **key** per column.
```python
rows = [{"city": "Toulouse", "inhabitants": "500000"},
        {"city": "Paris", "inhabitants": "2100000"}]

for row in rows:
    number = int(row["inhabitants"])   # "500000" (text) -> 500000 (number)
    if number > 1000000:
        print(row["city"])             # Paris
```
## Step 1 · Set up (25 min)

A **terminal** is a window where you type commands. A **virtual environment** is a private set of Python packages (code written by other people) for one project.

1. On the [course repository](https://github.com/nverstaevel/L2INFONUM_WEB), click **Code → Download ZIP**, then unzip the file.
2. In VS Code: **File → Open Folder**, choose the folder `td1` (not the whole course folder).
3. **Terminal → New Terminal**.
4. Type these commands one by one, pressing Enter after each.

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

**Check.** The line where you type starts with `(.venv)`, and `python check.py` shows eight lines with `[  ]`.
<details markdown="1"><summary>Stuck?</summary>

See the table of common problems in the [setup guide](setup.html).

</details>

## Step 2 · Download (25 min)

`requests` is a package that asks a web server for a page or a file, like a browser does. Open `download.py`.

### 2A · The address

Put this address between the quotation marks of `URL = ""`:
```text
https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/tin00028?format=SDMX-CSV&compress=false
```

### 2B · Did it work?

The server answers with a **status code**, a number: 200 means success.

**Example** (another subject: do not copy it as it is).
```python
import requests

answer = requests.get("https://www.python.org", timeout=60)
print(answer.status_code)          # 200
if answer.status_code != 200:
    raise SystemExit("It failed")  # stops the script
```

**Your turn.** In `download.py` the answer is called `response`. Under `TODO 2B`, stop the script if its status code is not 200.
<details markdown="1"><summary>Stuck?</summary>

Two lines. The first starts with `if response.` and ends with `:`. The second is indented (4 spaces) and starts with `raise SystemExit(`.

</details>

### 2C · Save the file

**Example** (another subject: do not copy it as it is).
```python
from pathlib import Path

Path("hello.txt").write_bytes(b"Hello")   # b"..." is a piece of bytes
print("Done")
```

**Your turn.** `OUTPUT` is already a `Path`, and `content` already holds the bytes. Write `content` into `OUTPUT` (one line), then print a message (one line). Run:
```text
python download.py
python check.py
```

**Check.** `Step 2` shows `[OK]` and you can open `data/internet_use.csv`.
<details markdown="1"><summary>Stuck?</summary>

`OUTPUT.write_bytes(...)`: what goes between the brackets? If the message is a connection error, check the address and your Internet access.

</details>

## Step 3 · Read the data (20 min)

A **CSV** file is a table written as text: one row per line, columns separated by commas. The first line gives the column names. Open `data/internet_use.csv` in VS Code, create a file `notes.txt` and answer:

1. Copy the first line. How many columns are there?
2. Find a line for France (`FR`). Which column holds the year? Which one holds the figure?
3. Search (`Ctrl+F`) for `EU27`. Is it a country?
4. Look at the column `indic_is`. Do you see several different values? We keep only `I_IU3`: people who used the Internet in the last 3 months.
5. Read the [Eurostat copyright notice](https://ec.europa.eu/eurostat/help/copyright-notice). What must you write when you reuse the data?

## Step 4 · Clean (55 min)

**Cleaning** means keeping only what we need, with the right types. Open `clean.py`. It has three **functions** (named blocks of code). A function gives its result back with `return`.

### 4A · Read the file · `load_rows`

**Example** (another subject: do not copy it as it is).
```python
import csv

with open("cities.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print(rows[0])    # {'city': 'Toulouse', 'inhabitants': '500000'}
```

**Your turn.** Write the same thing inside `load_rows`, but open the file given by `path` and `return` the list. `python check.py` → `Step 4A` `[OK]`.
<details markdown="1"><summary>Stuck?</summary>

Three lines inside the function: `with open(path, ...) as f:`, then, indented, `return list(...)`. Keep `newline=""` and `encoding="utf-8"`.

</details>

### 4B · Filter the rows · `clean_rows`

**Example** (another subject: do not copy it as it is).
```python
result = []
for row in rows:
    if row["city"] == "Paris":      # != means "is different from"
        continue                    # go directly to the next row
    result.append({"name": row["city"],
                   "people": int(row["inhabitants"])})
```

Write inside the `for` loop, **one test at a time**:

| TODO | Skip the row if… | Words to use |
|---|---|---|
| 4B-1 | the column `indic_is` is different from `INDICATOR` | `!=`, `continue` |
| 4B-2 | `geo` does not have 2 letters, **or** is in the list `AGGREGATES` | `len(...)`, `or`, `in` |
| 4B-3 | `OBS_VALUE` is the empty text `""` | `==` |
| 4B-4 | (no skip) add a dictionary with the keys `country`, `year`, `value` | `append`, `int`, `float` |

`country` comes from the column `geo`, `year` from `TIME_PERIOD` (a whole number), `value` from `OBS_VALUE` (a decimal number). Delete the line `pass`.

**Check.** `Step 4B` `[OK]`.
<details markdown="1"><summary>Stuck? 4B-1</summary>

`if row["indic_is"] ... INDICATOR:` then, indented, `continue`.

</details>

<details markdown="1"><summary>Stuck? 4B-2</summary>

`if len(row["geo"]) != 2 or row["geo"] in ...:`

</details>

<details markdown="1"><summary>Stuck? 4B-4</summary>

`cleaned.append({"country": row[...], "year": int(row[...]), "value": ...})`

</details>

### 4C · Write the clean file · `save_rows`

**Example** (another subject: do not copy it as it is).
```python
with open("copy.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "people"])
    writer.writeheader()      # first line: name,people
    writer.writerows(result)  # one line per dictionary
```

**Your turn.** Do the same in `save_rows`: the file is `path`, the three column names are `country`, `year`, `value`, and the data is `rows`. Then run:
```text
python clean.py
python check.py
```

**Check.** `clean.py` prints the number of rows read and kept. `data/internet_use_clean.csv` starts with `country,year,value` and does not contain `EU27_2020`.
<details markdown="1"><summary>Stuck?</summary>

`0 rows kept`? Check the spelling of the column names and the indentation: `append` must be inside the `for` loop, and `return cleaned` outside.

</details>

## Step 5 · Statistics (45 min)

Open `stats.py`.

### 5A · Read the clean file · `load_clean`

As in 4A, but a CSV file only contains text: convert `year` to `int` and `value` to `float`. This short form builds a list in one go (a **list comprehension**):
```python
rows = [{"name": r["name"], "people": int(r["people"])}
        for r in csv.DictReader(f)]      # inside a "with open(...) as f:" block
```

**Your turn.** The dictionaries must have the keys `country`, `year`, `value`. **Check:** `Step 5A` `[OK]`.

### 5B · Latest year · `summarise`

**Example** (another subject: do not copy it as it is).
```python
cities = [{"name": "A", "people": 10}, {"name": "B", "people": 30}]

biggest = max(c["people"] for c in cities)                # 30
only_big = [c for c in cities if c["people"] == biggest]  # [{'name': 'B', ...}]
smallest = min(cities, key=lambda c: c["people"])         # the whole dictionary of A
average = sum(c["people"] for c in cities) / len(cities)  # 20.0
round(3.14159, 2)                                         # 3.14
```

**Your turn**, in this order. Print each variable to check it before going on.

1. `latest`: the biggest year in `rows`.
2. `current`: only the rows of that year.
3. `lowest` and `highest`: the rows of `current` with the smallest and the biggest `value`.
4. `average`: the average `value` of `current`.
5. Return a dictionary with the keys `year`, `countries` (how many rows in `current`), `average` (2 decimals), `lowest`, `highest`.
<details markdown="1"><summary>Stuck?</summary>

Replace `c` by `r`, `cities` by `rows` or `current`, and `"people"` by `"year"` or `"value"`. For `highest`, `max` works like `min`. The last line starts with `return {"year": latest, "countries": len(current),`.

</details>

*This is a simple average of countries. It is not the EU figure, which takes population into account.*

### 5C · One country over time · `history`

**Example** (another subject: do not copy it as it is).
```python
points = [{"year": c["year"], "people": c["people"]}
          for c in rows if c["name"] == "A"]
points = sorted(points, key=lambda p: p["year"])   # oldest first
```

**Your turn.** Return the list of `{"year", "value"}` of the rows whose `country` is `country`, oldest first. At the top of the file, you may change `MY_COUNTRY` (France is `FR`, Spain `ES`, Italy `IT`, Germany `DE`).
<details markdown="1"><summary>Stuck?</summary>

`if r["country"] == country`, then `return sorted(points, key=...)`.

</details>

### 5D · Save as JSON

**JSON** is a text format for lists and dictionaries, used a lot on the web.

**Example** (another subject: do not copy it as it is).
```python
import json

with open("city.json", "w", encoding="utf-8") as f:
    json.dump({"name": "A", "people": 10}, f, indent=2)
```

**Your turn.** Under `TODO 5D`, write `result` into the file `OUTPUT`. Then run:
```text
python stats.py
python check.py
```

**Check.** Eight `[OK]`. Compare the last value of your country with the [Eurostat table](https://ec.europa.eu/eurostat/databrowser/view/tin00028/default/table?lang=en).

## If you finish early (optional)

1. Print the 5 countries with the highest value in the latest year. Start with `sorted(current, key=..., reverse=True)`, then keep `[:5]`.
2. Ask for the country code with `input()` instead of `MY_COUNTRY`.
3. Add a dictionary of country names (`{"FR": "France"}`) and print the name. Greece is `EL`.

## Source

Eurostat, dataset `tin00028`. Reuse is allowed if you name the source and say what you changed.
