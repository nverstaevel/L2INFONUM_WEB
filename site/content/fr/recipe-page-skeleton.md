title: Une page HTML complète
---
**Quand l'utiliser :** Démarrer une page.

## Fichiers

`index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>City library</title>
</head>
<body>
  <header>
    <h1>City library</h1>
    <nav>
      <ul>
        <li><a href="#books">Books</a></li>
        <li><a href="https://www.toulouse.fr">The city</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <section id="books">
      <h2>Books</h2>
      <p>We lend novels.</p>
    </section>
  </main>
  <footer>
    <p>Source: city library.</p>
  </footer>
</body>
</html>
```

## Lancer

```text
# double-click index.html
```

**Vous devez voir :** Le validateur ne signale aucune erreur.

## À adapter

Changez titres, liens et sections.

- Notions : [Éléments et attributs HTML](notion-html-elements.html) · [Structure, balises sémantiques, validation](notion-html-structure.html) · [Listes, liens, images, accessibilité](notion-html-links-images.html)
- [Toutes les recettes](recipes.html)
