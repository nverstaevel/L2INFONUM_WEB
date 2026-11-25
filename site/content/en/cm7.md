title: CM7 · Flask 3: the back-end as a JSON API
---
**23 February 2027.**

## Objectives

1. separate the back-end that serves data from the front-end that shows it
2. write a filterable JSON route
3. call it with fetch
4. debug with the console and the Network tab

<!--plan-->
## The question

**How do we feed a chart live?**

1. Serving data
2. Showing data
3. Debugging
<!--/plan-->

## Slides

[PDF](cm7-en.pdf)

{{slides:cm7:en}}

<!--lab-->
## For Friday

TD7: a chart fed live by your API.

- Notions: [JSON API](notion-api.html), [fetch: asking for data](notion-fetch.html), [Developer tools](notion-devtools.html), [Comprehensions, min, max, sorted](notion-list-tools.html), [URL parameters and query strings](notion-url-parameters.html), [HTTP: requests, responses, status codes](notion-http.html), [Changing the page from JavaScript](notion-dom.html), [Debugging](notion-debugging.html)
- Recipes: [A JSON API and its chart](recipe-api-chart.html)
<!--/lab-->

## Check yourself

<details><summary>What does jsonify return?</summary><p>A JSON HTTP response.</p></details>
<details><summary>Where do JavaScript files go in Flask?</summary><p>In static/.</p></details>
<details><summary>Which tab shows the status of a fetch?</summary><p>Network.</p></details>
<details><summary>Why destroy the old chart?</summary><p>A canvas can hold only one chart.</p></details>

Next: [TD7](td7.html).
