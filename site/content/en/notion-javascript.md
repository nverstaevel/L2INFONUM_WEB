title: JavaScript basics
---
**JavaScript** is the programming language of web pages. `const` (not reassigned) and `let` (can change). An **array** is like a list, an **object** like a dictionary read with a dot. `map` transforms each item. Braces replace indentation.

## Example

```javascript
const books = [{ title: "Emma", pages: 400 }];
const titles = books.map(book => book.title);
if (titles.length > 0) {
  console.log(titles[0]);
}
```

## Common mistakes

- Capital letters count: `textContent`, not `textcontent`.
- A missing comma between two properties of an object.

## Go further

- Lecture: [CM4](cm4.html)
- Recipes: [A chart from a JSON file](recipe-chart-from-json.html)
- Labs using it: [TD4](td4.html)
- [All notions](notions.html)
