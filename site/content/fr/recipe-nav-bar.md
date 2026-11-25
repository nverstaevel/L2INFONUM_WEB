title: Barre de navigation adaptative
---
**Quand l'utiliser :** Un menu en ligne sur ordinateur, en colonne sur téléphone.

## Fichiers

`menu.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Menu</title>
  <link rel="stylesheet" href="menu.css">
</head>
<body>
  <nav>
    <ul>
      <li><a href="#">Home</a></li>
      <li><a href="#">Books</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>
</body>
</html>
```

`menu.css`

```css
body { margin: 0; font-family: system-ui, sans-serif; }
nav { background: #14213d; padding: 1rem; }
nav ul { display: flex; gap: 1.5rem; list-style: none; margin: 0; padding: 0; }
nav a { color: white; }
nav a:hover, nav a:focus { text-decoration: none; }

@media (max-width: 600px) {
  nav ul { flex-direction: column; gap: 0.5rem; }
}
```

## Lancer

```text
# double-click menu.html
```

**Vous devez voir :** À 375px de large, les liens sont les uns sous les autres.

## À adapter

Changez les liens et les couleurs.

- Notions : [Flexbox](notion-css-flexbox.html) · [Mise en page adaptative et media queries](notion-css-media.html)
- [Toutes les recettes](recipes.html)
