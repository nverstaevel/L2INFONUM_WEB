title: Set up a project
---
**When to use it:** Start any Python project.

## Files

`requirements.txt`

```text
flask
requests
```

## Run

```text
# Windows
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

**You should see:** The line starts with `(.venv)`.

## Adapt it

Keep only the packages you need.

- Notions: [Terminal and virtual environment](notion-terminal-venv.html)
- [All recipes](recipes.html)
