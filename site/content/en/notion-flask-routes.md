title: Flask and routes
---
**Flask** is a **web framework**: it receives requests and calls your functions. A **route** links an address to a function with the **decorator** `@app.route`. The function returns the answer.

## Example

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True)     # only on your own computer
```

## What you see

```text
GET /  ->  200
Hello

GET /nothing  ->  404
```

## Common mistakes

- Two functions with the same name.
- A file named `flask.py` hides the library.
- A route written after `app.run`.

## Go further

- Lecture: [CM5](cm5.html)
- Recipes: [A Flask app with a template](recipe-flask-app.html)
- Labs using it: [TD5](td5.html), [TD8](td8.html)
- [Flask, with its result](notion-flask-ref.html)
- [All notions](notions.html)
