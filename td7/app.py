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
    rows = DATA   # TODO 2A: keep only the rows of this country
    # TODO 3A: accept an optional year (?year=2024)
    # TODO 4A: error 404 when there is no row
    return jsonify(rows)


if __name__ == "__main__":
    app.run(debug=True)
