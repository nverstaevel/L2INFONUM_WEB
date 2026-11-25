"""TD1, step 5: compute simple statistics and save them as JSON."""
import csv
import json

INPUT = "data/internet_use_clean.csv"
OUTPUT = "data/summary.json"
MY_COUNTRY = "FR"              # choose your country code


def load_clean(path):
    """Return the clean file with year as int and value as float."""
    # TODO 1
    return []


def summarise(rows):
    """Return the latest year, and the average, lowest and highest value that year."""
    # TODO 2
    return {}


def history(rows, country):
    """Return the list of {"year", "value"} for one country, oldest first."""
    # TODO 3
    return []


if __name__ == "__main__":
    data = load_clean(INPUT)
    result = summarise(data)
    result["country"] = MY_COUNTRY
    result["history"] = history(data, MY_COUNTRY)
    # TODO 4: write `result` into OUTPUT as JSON
    print(result)
