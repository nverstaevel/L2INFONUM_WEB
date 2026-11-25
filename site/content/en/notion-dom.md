title: Changing the page from JavaScript
---
The browser keeps the page as a tree of objects (the **DOM**). `document.getElementById` finds an element, `textContent` changes its text, `value` reads a field, `addEventListener` reacts to a click.

## Example

```javascript
const button = document.getElementById("hello");
button.addEventListener("click", () => {
  document.getElementById("message").textContent = "Hello";
});
```

## Common mistakes

- The `id` in JavaScript differs from the one in HTML: the result is `null`.
- Use `textContent`, not `innerHTML`, for data and input.

## Go further

- Lecture: [CM4](cm4.html)
- Recipes: [A JSON API and its chart](recipe-api-chart.html)
- Labs using it: [TD4](td4.html), [TD7](td7.html)
- [All notions](notions.html)
