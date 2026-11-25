title: Responsive navigation bar
---
**When to use it:** A menu in a row on a computer, in a column on a phone.

## Files

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

## Run

```text
# double-click menu.html
```

**You should see:** At 375px wide, the links are one under the other.

## Adapt it

Change the links and colours.

- Notions: [Flexbox](notion-css-flexbox.html) · [Responsive design and media queries](notion-css-media.html)
- [All recipes](recipes.html)
