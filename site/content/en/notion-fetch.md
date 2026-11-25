title: fetch: asking for data
---
`fetch` sends a request from the page without reloading it. The answer arrives later: each `then` says what to do when it does. A 404 does not stop `fetch`: test the content.

## Example

```javascript
fetch("data/books.json")
  .then(response => response.json())
  .then(books => {
    console.log(books);
  });
```

## Common mistakes

- Using the data outside `then`: it has not arrived yet.
- Page opened by double-click: `fetch` is blocked.

## Go further

- Lecture: [CM4](cm4.html)
- Recipes: [A chart from a JSON file](recipe-chart-from-json.html) · [A JSON API and its chart](recipe-api-chart.html)
- Labs using it: [TD4](td4.html), [TD7](td7.html), [TD9](td9.html)
- [All notions](notions.html)
