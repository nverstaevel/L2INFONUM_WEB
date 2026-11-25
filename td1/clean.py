"""TD1, step 4: keep only the rows we need and write a clean CSV file."""
import csv

INPUT = "data/internet_use.csv"
OUTPUT = "data/internet_use_clean.csv"
INDICATOR = "I_IU3"            # used the internet in the last 3 months
AGGREGATES = ["EA", "EU"]      # two-letter codes that are not countries


def load_rows(path):
    """Return the CSV file as a list of dictionaries."""
    # TODO 4A (then delete the line "return []")
    return []


def clean_rows(rows):
    """Return a list of {"country": str, "year": int, "value": float}."""
    cleaned = []
    for row in rows:
        # TODO 4B-1: skip the row if indic_is is not INDICATOR
        # TODO 4B-2: skip it if geo is not a country (length is not 2, or in AGGREGATES)
        # TODO 4B-3: skip it if OBS_VALUE is empty
        # TODO 4B-4: append a dictionary with the right types
        pass  # delete this line when you add your code
    return cleaned


def save_rows(rows, path):
    """Write the cleaned rows, with the header country,year,value."""
    # TODO 4C: use csv.DictWriter
    pass


if __name__ == "__main__":
    raw = load_rows(INPUT)
    clean = clean_rows(raw)
    save_rows(clean, OUTPUT)
    print(len(raw), "rows read,", len(clean), "rows kept")
