"""TD1, step 5: compute simple statistics and save them as JSON."""
import csv
import json

INPUT = "data/internet_use_clean.csv"
OUTPUT = "data/summary.json"
MY_COUNTRY = "FR"              # choose your country code


def load_clean(path):
    """Return the clean file with year as int and value as float."""
    # TODO 5A (then delete the line "return []")
    return []


def summarise(rows):
    """Return the latest year, and the average, lowest and highest value that year."""
    if not rows:                                           # nothing to do before 5A
        return {}
    latest = max(r["year"] for r in rows)                 # given: read these two lines
    current = [r for r in rows if r["year"] == latest]
    # TODO 5B: lowest, highest, average, then the dictionary (delete the line "return {}")
    return {}


def history(rows, country):
    """Return the list of {"year", "value"} for one country, oldest first."""
    # Already written: read it (step 5C).
    points = [{"year": r["year"], "value": r["value"]} for r in rows if r["country"] == country]
    return sorted(points, key=lambda p: p["year"])


if __name__ == "__main__":
    data = load_clean(INPUT)
    result = summarise(data)
    result["country"] = MY_COUNTRY
    result["history"] = history(data, MY_COUNTRY)
    # TODO 5D: write `result` into OUTPUT as JSON
    print(result)
