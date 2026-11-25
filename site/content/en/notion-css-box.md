title: Box model
---
Every element is a box: content, **padding** (inside), **border**, **margin** (outside). By default, visible width = width + padding + border. `box-sizing: border-box` includes them in `width`.

## Example

```css
main {
  max-width: 60rem;     /* never wider */
  margin: 0 auto;       /* centred */
  padding: 1rem;        /* inner space */
}
img { max-width: 100%; height: auto; }
```

## Common mistakes

- Using `width` where `max-width` is needed: the page overflows on a phone.

## Go further

- Lecture: [CM3](cm3.html)
- Recipes: [Readable page and tables](recipe-clean-style.html)
- Labs using it: [TD3](td3.html)
- [All notions](notions.html)
