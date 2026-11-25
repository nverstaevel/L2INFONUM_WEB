"""TD6: check your work. Run `python check.py` from the td6 folder (virtual environment active).
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


def page(address):
    r = client.get(address)
    assert r.status_code == 200, f"status {r.status_code} for {address}"
    return r.text


def add(code):
    client.post("/favourites", data={"country": code})
    with client.session_transaction() as s:
        return s.get("favourites", [])


check("2B-2C /search?country=fr lists France only",
      lambda: "90.5" in page("/search?country=fr") and "70.25" not in page("/search?country=fr"))
check("3B /search?minimum=80 filters all countries",
      lambda: "90.5" in page("/search?minimum=80") and "70.25" not in page("/search?minimum=80")
      and "70.25" in page("/search"))
check("3C message when there is no result", lambda: "No result" in page("/search?country=ZZ"))
check("4B /favourites accepts GET and POST",
      lambda: client.get("/favourites").status_code == 200 and client.post("/favourites", data={"country": "ES"}).status_code == 200)
check("4C added once, in capital letters, and remembered",
      lambda: add("fr").count("FR") == 1 and add("FR").count("FR") == 1 and "FR" in page("/favourites"))
check("5A unknown code refused", lambda: add("fr") != [] and "ZZ" not in add("ZZ"))
