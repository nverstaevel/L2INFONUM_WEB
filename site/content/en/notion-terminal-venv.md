title: Terminal and virtual environment
---
A **terminal** is a window where you type commands. A **package** is code written by others that you can install. A **virtual environment** (`.venv`) is a private set of packages for one project, so that projects do not disturb each other. Create it once, **activate** it in every new terminal.

## Example

```text
cd td5                  # go into a folder
.venv\Scripts\Activate.ps1      # activate (Windows)
source .venv/bin/activate       # activate (macOS, Linux)
python app.py                   # run a script
```

## Common mistakes

- `ModuleNotFoundError`: the environment is not activated (no `(.venv)` at the start of the line).
- `FileNotFoundError`: the terminal is not in the right folder.

## Go further

- Lecture: [CM1](cm1.html)
- Recipes: [Set up a project](recipe-venv.html)
- Labs using it: [TD1](td1.html), [TD5](td5.html)
- [All notions](notions.html)
