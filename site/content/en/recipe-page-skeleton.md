title: A complete HTML page
---
**When to use it:** Start any page.

## Files

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

## Run

```text
# double-click index.html
```

**You should see:** The validator reports no error.

## Adapt it

Change titles, links and sections.

- Notions: [HTML elements and attributes](notion-html-elements.html) · [Page structure, semantic tags, validation](notion-html-structure.html) · [Lists, links, images, accessibility](notion-html-links-images.html)
- [All recipes](recipes.html)
