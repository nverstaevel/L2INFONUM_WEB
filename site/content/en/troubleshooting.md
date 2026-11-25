title: Troubleshooting
---
Read the **last line** of a Python error, and the **first red line** of the browser console.

| Problem | What to try |
|---|---|
| `python` not found | use `py` (Windows) or `python3` |
| `ModuleNotFoundError` | activate the environment, then `pip install` |
| `FileNotFoundError: data/…` | run from the folder that contains `data` |
| Chart empty, error about CORS | you opened the file by double-click: start `python -m http.server` |
| `TemplateNotFound` | the file must be in `templates/` |
| CSS not applied in Flask | file in `static/`, link `/static/style.css` |
| 404 on my route | check spelling; save the file; restart the server |
| 405 Method Not Allowed | add `methods=["GET", "POST"]` |
| `RuntimeError … secret key` | set `app.secret_key` |
| Port 5000 already in use | stop the other server, or `app.run(debug=True, port=5001)` |
| Changes not visible | reload with Ctrl+Shift+R (Cmd+Shift+R) |

A Python error you do not understand? See the examples in [Read an error message](notion-python-ref.html#read-an-error-message).
