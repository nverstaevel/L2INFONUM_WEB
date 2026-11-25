title: Download a file
---
**When to use it:** Get a data file from the web with Python.

## Files

`get_file.py`

```python
from pathlib import Path

import requests

URL = "https://raw.githubusercontent.com/pallets/flask/main/README.md"   # any file address
OUTPUT = Path("data/flask_readme.md")

response = requests.get(URL, timeout=60)
if response.status_code != 200:
    raise SystemExit(f"Failed: status {response.status_code}")
OUTPUT.parent.mkdir(exist_ok=True)
OUTPUT.write_bytes(response.content)
print("Saved", OUTPUT)
```

## Run

```text
python get_file.py
```

**You should see:** The file appears in the folder `data`.

## Adapt it

Change the address and the file name. Check the licence.

- Notions: [HTTP: requests, responses, status codes](notion-http.html) · [Reading and writing files](notion-python-files.html) · [Open data and licences](notion-open-data.html)
- [All recipes](recipes.html)
