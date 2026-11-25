title: CM6 · Flask 2: parameters, forms, sessions
---
**9 February 2027.**

## Objectives

1. read URL and query parameters
2. handle GET and POST forms
3. keep simple state in a session
4. show values safely with {{ variable }}

## Slides

[PDF](cm6-en.pdf)

{{slides:cm6:en}}

## Check yourself

<details><summary>Which object reads ?year=2022?</summary><p>request.args.</p></details>
<details><summary>Which object reads a POST form?</summary><p>request.form.</p></details>
<details><summary>What is needed to use session?</summary><p>app.secret_key.</p></details>
<details><summary>Why keep escaping on?</summary><p>So that user input is never run as code in the page.</p></details>

Next: [TD6](td6.html).
