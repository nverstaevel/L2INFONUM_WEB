title: CSS rules and selectors
---
**CSS** says how elements look. A rule = a **selector** + declarations `property: value;`. `p` targets elements, `.note` a **class**, `#about` an **id**, `nav a` the links inside `nav`. When rules conflict, the most precise selector wins (**specificity**: id > class > element), then the last one.

## Example

```css
body { font-family: system-ui, sans-serif; color: #14213d; }
.note { color: darkblue; }
nav a { color: white; }
```

## Common mistakes

- A missing `;` or `}` breaks the following rules.
- The stylesheet is not linked in `<head>`.

## Go further

- Lecture: [CM3](cm3.html)
- Recipes: [Readable page and tables](recipe-clean-style.html)
- Labs using it: [TD3](td3.html)
- [All notions](notions.html)
