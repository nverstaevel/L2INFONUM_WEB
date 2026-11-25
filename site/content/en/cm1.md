title: CM1 · Web, open data and Python files
---
**Tuesday 5 January 2027.**

## Objectives

After this lecture you can:

1. describe what happens when a browser requests a page;
2. judge whether a dataset can be reused;
3. tell CSV, JSON and an API apart;
4. read a CSV file and write a JSON file in Python.

<!--plan-->
## The question

**How do we get data from the web and use it?**

1. How the web works
2. Open data
3. Python on a data file
<!--/plan-->

## Slides

[PDF](cm1-en.pdf)

{{slides:cm1:en}}

<!--lab-->
## For Friday

TD1: set up Python, download and clean the Eurostat file, compute figures.

- Notions: [Terminal and virtual environment](notion-terminal-venv.html), [HTTP: requests, responses, status codes](notion-http.html), [Reading and writing files](notion-python-files.html), [CSV files](notion-csv.html), [Open data and licences](notion-open-data.html), [Lists of dictionaries](notion-lists-dicts.html), [Comprehensions, min, max, sorted](notion-list-tools.html), [JSON](notion-json.html)
- Recipes: [Set up a project](recipe-venv.html), [Download a file](recipe-download.html), [Filter a CSV file](recipe-clean-csv.html), [Compute figures and save them as JSON](recipe-stats-json.html)
<!--/lab-->

## Check yourself

<details><summary>Who sends the first message: the client or the server?</summary><p>The client. A web server only answers requests.</p></details>
<details><summary>What does status code 404 mean?</summary><p>The resource was not found.</p></details>
<details><summary>A dataset states no licence. May you put it on your website?</summary><p>Do not assume so. Ask the owner or choose another dataset.</p></details>
<details><summary>What type is a value read from a CSV file?</summary><p>Text (a string). Convert it with <code>int()</code> or <code>float()</code>.</p></details>

Next: [TD1](td1.html).
