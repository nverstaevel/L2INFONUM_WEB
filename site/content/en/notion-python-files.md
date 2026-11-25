title: Reading and writing files
---
`with open(...) as f:` opens a file and closes it for you. `"r"` reads (default), `"w"` writes and **replaces** the file. `Path` is another way to handle files. Paths are relative to the folder where you run the script.

## Example

```python
from pathlib import Path

Path("data").mkdir(exist_ok=True)          # create a folder
with open("data/hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello")
print(Path("data/hello.txt").read_text(encoding="utf-8"))
```

## What you see

```text
Hello
```

## Common mistakes

- Opening with `"w"` a file you only wanted to read erases it.

## Go further

- Lecture: [CM1](cm1.html)
- Recipes: [Download a file](recipe-download.html) · [Filter a CSV file](recipe-clean-csv.html)
- Labs using it: [TD1](td1.html), [TD8](td8.html)
- [Python, with its result](notion-python-ref.html)
- [All notions](notions.html)
