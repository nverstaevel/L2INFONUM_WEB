title: Page structure, semantic tags, validation
---
`head` holds information about the page, `body` what is shown. **Semantic** tags say what a part is: `header`, `nav`, `main`, `section`, `footer`. One `h1` per page, then `h2`, `h3` in order. The [W3C validator](https://validator.w3.org/#validate_by_input) finds mistakes.

## Example

```html
<header><h1>City library</h1></header>
<main>
  <section id="books">
    <h2>Books</h2>
  </section>
</main>
<footer><p>Source: ...</p></footer>
```

## Common mistakes

- Choosing a heading for its size instead of its level.

## Go further

- Lecture: [CM2](cm2.html)
- Recipes: [A complete HTML page](recipe-page-skeleton.html)
- Labs using it: [TD2](td2.html), [TD10](td10.html)
- [All notions](notions.html)
