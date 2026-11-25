title: Responsive design and media queries
---
A **responsive** page adapts to the screen. A **media query** applies rules only under a condition. The `viewport` line in `head` is required on phones.

## Example

```css
/* in head: <meta name="viewport" content="width=device-width, initial-scale=1"> */
@media (max-width: 600px) {
  nav ul { flex-direction: column; }
}
```

## Common mistakes

- The media query placed before the normal rule: the normal rule then wins.

## Go further

- Lecture: [CM3](cm3.html)
- Recipes: [Responsive navigation bar](recipe-nav-bar.html)
- Labs using it: [TD3](td3.html), [TD10](td10.html)
- [All notions](notions.html)
