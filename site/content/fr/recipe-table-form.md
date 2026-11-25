title: Un tableau et un formulaire
---
**Quand l'utiliser :** Montrer des données et demander un choix.

## Fichiers

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

## Lancer

```text
# double-click loans.html
```

**Vous devez voir :** Après un clic, l'adresse finit par `?genre=…&year=…`.

## À adapter

Changez colonnes, lignes et champs.

- Notions : [Tableaux](notion-html-tables.html) · [Formulaires](notion-html-forms.html)
- [Toutes les recettes](recipes.html)
