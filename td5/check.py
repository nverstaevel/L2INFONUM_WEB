"""TD5: check your work. Run `python check.py` from the td5 folder (virtual environment active).
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


def check(name, test):
    try:
        ok = test()
    except Exception as error:  # show the problem and go on with the next check
        print(f"[  ] {name}  ->  {type(error).__name__}: {error}")
        return
    print(f"[OK] {name}" if ok else f"[  ] {name}")


def index_template():
    text = Path("templates/index.html").read_text(encoding="utf-8").replace(" ", "")
    return "{{title}}" in text and 'href="/about"' in text


def home_page():
    r = client.get("/")
    return r.status_code == 200 and "<html" in r.text and "{{" not in r.text


def country_page():
    r = client.get("/country/fr")
    return r.status_code == 200 and "<html" in r.text and "FR" in r.text


check("2A /about answers with an h1", lambda: "<h1" in client.get("/about").text and client.get("/about").status_code == 200)
check("3A /api/info returns JSON", lambda: {"source", "unit", "licence"} <= set(client.get("/api/info").get_json()))
check("4A templates/index.html with {{ title }}", index_template)
check("4B / uses the template", home_page)
check("5A templates/country.html with {{ code }}",
      lambda: "{{code}}" in Path("templates/country.html").read_text(encoding="utf-8").replace(" ", ""))
check("5B /country/fr shows FR", country_page)
check("6A /teapot has the status code 418", lambda: client.get("/teapot").status_code == 418)
