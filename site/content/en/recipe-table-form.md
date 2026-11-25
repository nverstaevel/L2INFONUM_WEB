title: A table and a form
---
**When to use it:** Show data and ask for a choice.

## Files

`loans.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Loans</title>
</head>
<body>
  <main>
    <h1>Loans</h1>
    <table>
      <caption>Books lent per month</caption>
      <thead><tr><th scope="col">Month</th><th scope="col">Books</th></tr></thead>
      <tbody>
        <tr><td>January</td><td>120</td></tr>
        <tr><td>February</td><td>95</td></tr>
      </tbody>
    </table>
    <form action="#" method="get">
      <label for="genre">Genre</label>
      <select id="genre" name="genre">
        <option value="novel">Novel</option>
        <option value="comic">Comic</option>
      </select>
      <label for="year">Year</label>
      <input id="year" name="year" type="number" min="2000" max="2030" required>
      <button type="submit">Show</button>
    </form>
  </main>
</body>
</html>
```

## Run

```text
# double-click loans.html
```

**You should see:** After clicking, the address ends with `?genre=…&year=…`.

## Adapt it

Change the columns, rows and fields.

- Notions: [Tables](notion-html-tables.html) · [Forms](notion-html-forms.html)
- [All recipes](recipes.html)
