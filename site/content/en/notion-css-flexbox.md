title: Flexbox
---
**Flexbox** places the children of a box in a row or a column. Write `display: flex` on the **parent**. `gap` is the space between children, `justify-content` acts along the row, `align-items` across it.

## Example

```css
nav ul {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  list-style: none;
  padding: 0;
}
```

## Common mistakes

- `display: flex` written on the children instead of the parent.

## Go further

- Lecture: [CM3](cm3.html)
- Recipes: [Responsive navigation bar](recipe-nav-bar.html)
- Labs using it: [TD3](td3.html), [TD9](td9.html)
- [All notions](notions.html)
