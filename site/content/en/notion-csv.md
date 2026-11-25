title: CSV files
---
A **CSV** file is a table written as text: one line per row, values separated by commas, column names on the first line. Python's `csv` module reads each row as a dictionary. **Everything read is text**: convert numbers.

## Example

```python
import csv

with open("books.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print(rows[0]["title"])
```

## Common mistakes

- `"10" > "9"` is False: texts are not compared like numbers. Use `int` or `float`.
- Forgetting `newline=""` (empty lines on Windows).

## Go further

- Lecture: [CM1](cm1.html)
- Recipes: [Filter a CSV file](recipe-clean-csv.html)
- Labs using it: [TD1](td1.html), [TD8](td8.html)
- [All notions](notions.html)
