title: CM6 · Flask 2: parameters, forms, sessions
---
**9 February 2027.**

## Objectives

1. read URL and query parameters
2. handle GET and POST forms
3. keep simple state in a session
4. show values safely with {{ variable }}

<!--plan-->
## The question

**How do we answer a visitor's request?**

1. Reading the request and the data
2. Forms and memory
3. Safety
<!--/plan-->

## Slides

[PDF](cm6-en.pdf)

{{slides:cm6:en}}

<!--lab-->
## For Friday

TD6: search, filter and favourites.

- Notions: [Lists of dictionaries](notion-lists-dicts.html), [Templates and static files](notion-templates.html), [URL parameters and query strings](notion-url-parameters.html), [Forms](notion-html-forms.html), [GET and POST](notion-get-post.html), [Sessions and cookies](notion-sessions.html), [Input checking and escaping](notion-safety.html)
- Recipes: [Set up a project](recipe-venv.html), [A search form](recipe-search-form.html), [Remember a list with a session](recipe-session-list.html)
<!--/lab-->

## Check yourself

<details><summary>Which object reads ?year=2022?</summary><p>request.args.</p></details>
<details><summary>Which object reads a POST form?</summary><p>request.form.</p></details>
<details><summary>What is needed to use session?</summary><p>app.secret_key.</p></details>
<details><summary>Why keep escaping on?</summary><p>So that user input is never run as code in the page.</p></details>

Next: [TD6](td6.html).
