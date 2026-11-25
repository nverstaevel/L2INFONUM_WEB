import csv

from flask import Flask, jsonify, render_template, request, session

app = Flask(__name__)


def load_data():
    """Read the clean file produced in TD1."""
    with open("data/internet_use_clean.csv", newline="", encoding="utf-8") as f:
        return [{"country": r["country"], "year": int(r["year"]), "value": float(r["value"])}
                for r in csv.DictReader(f)]


DATA = load_data()


@app.route("/")
def home():
    return render_template("chart.html")


@app.route("/api/data")
def api_data():
    country = request.args.get("country", "FR").upper()
    # TODO 1: keep only the rows of this country
    rows = DATA
    # TODO 2: accept an optional year parameter (?year=2022)
    # TODO 3: return status code 404 with a JSON error when there is no row
    return jsonify(rows)


if __name__ == "__main__":
    app.run(debug=True)
