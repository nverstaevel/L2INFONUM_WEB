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

## What you see

<div class="preview"><p><strong>Live result: the code really runs</strong></p><iframe sandbox="allow-scripts" title="Live result: the code really runs" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&#10;&#10;&lt;script&gt;&#10;const FILES = {&quot;data/books.json&quot;: &quot;[{\&quot;title\&quot;: \&quot;Emma\&quot;}]&quot;};&#10;window.fetch = url =&gt; Promise.resolve(new Response(FILES[url] || &#x27;Not found&#x27;, {status: url in FILES ? 200 : 404}));&#10;console.log = value =&gt; { document.body.textContent = &#x27;console: &#x27; + JSON.stringify(value); };&#10;fetch(&quot;data/books.json&quot;)&#10;  .then(response =&gt; response.json())&#10;  .then(books =&gt; {&#10;    console.log(books);&#10;  });&#10;&lt;/script&gt;" style="height:60px"></iframe></div>

## Common mistakes

- Using the data outside `then`: it has not arrived yet.
- Page opened by double-click: `fetch` is blocked.

## Go further

- Lecture: [CM4](cm4.html)
- Recipes: [A chart from a JSON file](recipe-chart-from-json.html) · [A JSON API and its chart](recipe-api-chart.html)
- Labs using it: [TD4](td4.html), [TD7](td7.html), [TD9](td9.html)
- [JavaScript, with its result](notion-js-ref.html)
- [All notions](notions.html)
