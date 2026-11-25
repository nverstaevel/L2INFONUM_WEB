title: CM5 · Flask 1: routes and responses
---
**2 February 2027.**

## Objectives

1. explain what a web framework does
2. map a URL to a Python function
3. return text, HTML and JSON
4. use the right status code

<!--plan-->
## The question

**How can Python build pages?**

1. A server of your own
2. Routes and answers
3. When it breaks
<!--/plan-->

## Slides

[PDF](cm5-en.pdf)

{{slides:cm5:en}}

<!--lab-->
## For Friday

TD5: your first Flask application.

- Notions: [Terminal and virtual environment](notion-terminal-venv.html), [Local server](notion-local-server.html), [Flask and routes](notion-flask-routes.html), [JSON](notion-json.html), [JSON API](notion-api.html), [Templates and static files](notion-templates.html), [URL parameters and query strings](notion-url-parameters.html), [Input checking and escaping](notion-safety.html), [HTTP: requests, responses, status codes](notion-http.html), [Developer tools](notion-devtools.html)
- Recipes: [Set up a project](recipe-venv.html), [A Flask app with a template](recipe-flask-app.html)
<!--/lab-->

## Check yourself

<details><summary>What links a URL to a function?</summary><p>The @app.route decorator.</p></details>
<details><summary>Which function returns JSON?</summary><p>jsonify.</p></details>
<details><summary>Where do templates go?</summary><p>In the templates folder.</p></details>
<details><summary>What does 500 mean?</summary><p>An error in the server code.</p></details>

Next: [TD5](td5.html).
