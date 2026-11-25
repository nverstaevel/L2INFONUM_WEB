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

## What you see

<div class="preview"><p><strong>Live result: the code really runs</strong></p><iframe sandbox="allow-scripts" title="Live result: the code really runs" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;button id=&quot;hello&quot;&gt;Say hello&lt;/button&gt;&#10;&lt;p id=&quot;message&quot;&gt;...&lt;/p&gt;&#10;&#10;&lt;script&gt;&#10;const button = document.getElementById(&quot;hello&quot;);&#10;button.addEventListener(&quot;click&quot;, () =&gt; {&#10;  document.getElementById(&quot;message&quot;).textContent = &quot;Hello&quot;;&#10;});&#10;&lt;/script&gt;" style="height:100px"></iframe></div>

## Common mistakes

- The `id` in JavaScript differs from the one in HTML: the result is `null`.
- Use `textContent`, not `innerHTML`, for data and input.

## Go further

- Lecture: [CM4](cm4.html)
- Recipes: [A JSON API and its chart](recipe-api-chart.html)
- Labs using it: [TD4](td4.html), [TD7](td7.html)
- [JavaScript, with its result](notion-js-ref.html)
- [All notions](notions.html)
