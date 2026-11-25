"""TD7: check your work. Run `python check.py` from the td7 folder (virtual environment active).
Do not modify this file."""
import logging
from pathlib import Path

try:
    import app as student
except Exception as error:  # a mistake in app.py: show it and stop
    raise SystemExit(f"app.py cannot be loaded -> {type(error).__name__}: {error}")

student.app.logger.disabled = True   # keep the output short
logging.getLogger("flask.app").disabled = True
client = student.app.test_client()

student.DATA = [{"country": "FR", "year": 2024, "value": 90.5},   # small test data
                {"country": "FR", "year": 2025, "value": 91.75},
                {"country": "ES", "year": 2024, "value": 70.25}]


def check(name, test):
    try:
        ok = test()
    except Exception as error:  # show the problem and go on with the next check
        print(f"[  ] {name}  ->  {type(error).__name__}: {error}")
        return
    print(f"[OK] {name}" if ok else f"[  ] {name}")


def rows(address):
    return [(r["country"], r["year"]) for r in client.get(address).get_json()]


def message_in_page():
    code = "".join(line.split("//")[0] for line in Path("static/chart.js").read_text(encoding="utf-8").splitlines(True))
    return "rows.error" in code and "textContent" in code and "return" in code


check("2A only the requested country", lambda: rows("/api/data?country=es") == [("ES", 2024)])
check("3A the year filter", lambda: rows("/api/data?country=FR&year=2025") == [("FR", 2025)]
      and len(rows("/api/data?country=FR")) == 2)
check("4A unknown request: 404 and a JSON error", lambda: client.get("/api/data?country=ZZ").status_code == 404
      and "error" in client.get("/api/data?country=ZZ").get_json())
check("4B chart.js shows the error in the page", message_in_page)
check("5  notes.txt written", lambda: len(Path("notes.txt").read_text(encoding="utf-8").split()) >= 20)
