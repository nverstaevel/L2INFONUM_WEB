title: Local server
---
A **server** is a program that waits for requests and sends back answers. A **local** server runs on your own computer, at the address `localhost` or `127.0.0.1`. The number after `:` is the **port**, the door the server listens to.

## Example

```text
python -m http.server        # serves the files of the folder: http://localhost:8000
python app.py                # Flask server: http://127.0.0.1:5000
Ctrl+C                       # stops the server
```

## Common mistakes

- Opening the file by double-click instead of using the server address.
- Starting the server in the wrong folder (404).

## Go further

- Lecture: [CM4](cm4.html)
- Recipes: [A chart from a JSON file](recipe-chart-from-json.html)
- Labs using it: [TD4](td4.html), [TD5](td5.html)
- [All notions](notions.html)
