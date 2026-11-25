"""TD4: check your work. Run `python check.py` from the td4 folder. Do not modify this file."""
import json
import re
from pathlib import Path

JS = re.sub(r"//.*", "", Path("chart.js").read_text(encoding="utf-8"))  # without comments


def check(name, test):
    try:
        ok = test()
    except Exception as error:  # show the problem and go on with the next check
        print(f"[  ] {name}  ->  {type(error).__name__}: {error}")
        return
    print(f"[OK] {name}" if ok else f"[  ] {name}")


def my_data():
    summary = json.loads(Path("data/summary.json").read_text(encoding="utf-8"))
    return bool(summary["country"] and summary["history"])


check("3  data/summary.json readable, with country and history", my_data)
check("4A chart type is bar", lambda: bool(re.search(r"type\s*:\s*[\"']bar", JS)))
check("4B title uses summary.country", lambda: "textContent" in JS and "summary.country" in JS)
check("4C vertical axis from 0 to 100",
      lambda: bool(re.search(r"\bmin\s*:\s*0\b", JS) and re.search(r"\bmax\s*:\s*100\b", JS)))
check("5  notes.txt written", lambda: len(Path("notes.txt").read_text(encoding="utf-8").split()) >= 30)
