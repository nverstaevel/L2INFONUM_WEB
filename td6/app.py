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


# TODO 1: /search reads ?country=FR with request.args.get and shows the history
# TODO 2: add a year filter that keeps countries above a minimum value (GET form)
# TODO 3: /favourites (GET and POST): add a country code to session["favourites"]
# TODO 4: a button that empties the favourites (POST)


if __name__ == "__main__":
    app.run(debug=True)
