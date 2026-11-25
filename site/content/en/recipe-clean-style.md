title: Readable page and tables
---
**When to use it:** A simple stylesheet for any page.

## Files

`style.css`

```css
body { margin: 0; font-family: system-ui, Arial, sans-serif; line-height: 1.5; color: #14213d; }
main { max-width: 50rem; margin: 0 auto; padding: 1rem; }
img { max-width: 100%; height: auto; }
table { width: 100%; border-collapse: collapse; }
th, td { border: 1px solid #cbd5e1; padding: 0.5rem; text-align: left; }
th { background: #eef2f7; }
```

## Run

```text
# in the head of the page:
<link rel="stylesheet" href="style.css">
```

**You should see:** The content is centred and the table has simple borders.

## Adapt it

Choose your colours and widths.

- Notions: [CSS rules and selectors](notion-css-rules.html) · [Box model](notion-css-box.html)
- [All recipes](recipes.html)
