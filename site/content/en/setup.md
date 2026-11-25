title: Setup guide
---
Do this **before TD1** if you use your own computer.

## 1. Install

1. [Python 3](https://www.python.org/downloads/). On Windows, tick *Add Python to PATH*.
2. [Visual Studio Code](https://code.visualstudio.com/) and its *Python* extension.
3. A recent browser (Firefox or Chrome) with developer tools.

## 2. Get the course files

Each lab sheet has a button **Download the starter files (ZIP)**. Create one folder for the course (for example `web-course`), download the ZIP of the lab and **unzip it there** (on Windows: right-click → *Extract All*; do not work inside the ZIP). Keep all labs side by side: `web-course/td1`, `web-course/td2`… If a lab folder already contains your work, do not overwrite it. Everything is also on the [course repository](https://github.com/nverstaevel/L2INFONUM_WEB).

## 3. Create a virtual environment

A *virtual environment* is a private set of Python packages for one project. A *terminal* is a window where you type commands. In VS Code, open the `td1` folder, then **Terminal → New Terminal**.

Windows (PowerShell):

```
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS or Linux:

```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

**Check:** your prompt starts with `(.venv)` and `python -c "import requests; print(requests.__version__)"` prints a number.

From TD5 each folder has its own `requirements.txt` (Flask): repeat part 3 in that folder. More help: [Troubleshooting](troubleshooting.html).

## Common problems

| Problem | What to try |
|---|---|
| `python` is not recognised (Windows) | use `py` instead, or reinstall with *Add Python to PATH* |
| PowerShell refuses to run `Activate.ps1` | use a *Command Prompt* terminal and run `.venv\Scripts\activate.bat` |
| `ModuleNotFoundError: requests` | the environment is not activated: activate it, then install again |
| `FileNotFoundError: data/…` | run the script from the `td1` folder |
