import csv

from flask import Flask, jsonify, render_template, request, session

app = Flask(__name__)


def load_data():
    """Read the clean file produced in TD1."""
    with open("data/internet_use_clean.csv", newline="", encoding="utf-8") as f:
        return [{"country": r["country"], "year": int(r["year"]), "value": float(r["value"])}
                for r in csv.DictReader(f)]


DATA = load_data()
app.secret_key = "change-me"   # signs the session cookie


@app.route("/")
def home():
    return render_template("index.html", count=len(DATA))


# TODO 2B: the route /search (read the country)
#   TODO 2C: build the text `results`
#   TODO 3B: also read the minimum value
#   TODO 3C: a message when there is no result

# TODO 4B: the route /favourites (GET and POST)
#   TODO 4C: keep the list in session["favourites"]
#   TODO 5A: accept only known country codes
#   TODO 5B: empty the list


if __name__ == "__main__":   # keep this block at the END of the file
    app.run(debug=True)
