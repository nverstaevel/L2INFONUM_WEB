"""TD1: check your work. Run `python check.py` from the td1 folder. Do not modify this file."""
import csv
import json
import tempfile
from pathlib import Path

RAW = [
    {"indic_is": "I_IU3", "geo": "FR", "TIME_PERIOD": "2025", "OBS_VALUE": "90.5"},
    {"indic_is": "OTHER", "geo": "FR", "TIME_PERIOD": "2025", "OBS_VALUE": "10"},
    {"indic_is": "I_IU3", "geo": "EU27_2020", "TIME_PERIOD": "2025", "OBS_VALUE": "92"},
    {"indic_is": "I_IU3", "geo": "EA", "TIME_PERIOD": "2025", "OBS_VALUE": "92"},
    {"indic_is": "I_IU3", "geo": "ES", "TIME_PERIOD": "2025", "OBS_VALUE": ""},
    {"indic_is": "I_IU3", "geo": "ES", "TIME_PERIOD": "2024", "OBS_VALUE": "80"},
]
CLEAN = [
    {"country": "FR", "year": 2025, "value": 90.0},
    {"country": "ES", "year": 2025, "value": 80.0},
    {"country": "FR", "year": 2024, "value": 70.0},
]


def check(name, test):
    try:
        ok = test()
    except Exception as error:  # show the problem and go on with the next check
        print(f"[  ] {name}  ->  {type(error).__name__}: {error}")
        return
    print(f"[OK] {name}" if ok else f"[  ] {name}")


def downloaded():
    with open("data/internet_use.csv", encoding="utf-8-sig") as f:
        header = f.readline().strip().split(",")
    missing = [c for c in ["indic_is", "geo", "TIME_PERIOD", "OBS_VALUE"] if c not in header]
    if missing:
        print("     Columns not found:", missing, "- call your teacher.")
    return not missing


def temp_file():
    return Path(tempfile.mkdtemp()) / "test.csv"


def loads():
    import clean
    path = temp_file()
    path.write_text("geo,OBS_VALUE\nFR,1\nES,2\n", encoding="utf-8")
    return clean.load_rows(path) == [{"geo": "FR", "OBS_VALUE": "1"}, {"geo": "ES", "OBS_VALUE": "2"}]


def cleans():
    import clean
    return clean.clean_rows(RAW) == [{"country": "FR", "year": 2025, "value": 90.5},
                                     {"country": "ES", "year": 2024, "value": 80.0}]


def saves():
    import clean
    path = temp_file()
    clean.save_rows(CLEAN, path)
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    return rows[0] == ["country", "year", "value"] and len(rows) == 4


def reads_clean():
    import stats
    path = temp_file()
    path.write_text("country,year,value\nFR,2025,90.5\n", encoding="utf-8")
    return stats.load_clean(path) == [{"country": "FR", "year": 2025, "value": 90.5}]


def summarises():
    import stats
    r = stats.summarise(CLEAN)
    return (r["year"] == 2025 and r["countries"] == 2 and r["average"] == 85.0
            and r["lowest"]["country"] == "ES" and r["highest"]["country"] == "FR")


def summary_file():
    with open("data/summary.json", encoding="utf-8") as f:
        result = json.load(f)
    return {"year", "average", "lowest", "highest", "country", "history"} <= set(result) and result["history"] != []


check("Step 2  data/internet_use.csv downloaded", downloaded)
check("Step 4A load_rows", loads)
check("Step 4B clean_rows", cleans)
check("Step 4C save_rows", saves)
check("Step 5A load_clean", reads_clean)
check("Step 5B summarise", summarises)
check("Step 5D data/summary.json written", summary_file)
