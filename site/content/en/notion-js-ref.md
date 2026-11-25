title: JavaScript, with its result
---
The JavaScript used in this course, each time with **its result**. Put your script at the **end** of the `body`; open the **console** with F12 to see messages and errors.

```text
<script src="page.js"></script>
</body>
```

Arrays and objects may be displayed slightly differently by your browser. See also the [reference on MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript).

## Values and tests

### `const`, `let`, `console.log`

`const` for a variable that is not reassigned, `let` for one that changes. `console.log` is the `print` of JavaScript.

```javascript
const city = "Toulouse";
let people = 500000;
people = people + 1;
console.log(city, people);
```

**In the console**

```text
Toulouse 500001
```

### text and numbers

`+` joins texts. A text must be converted before computing.

```javascript
console.log("Year " + 2025);
console.log("2025" + 1);
console.log(Number("2025") + 1);
```

**In the console**

```text
Year 2025
20251
2026
```

### `if`, `else`, `===`

The test is between brackets, the block between braces. Compare with `===`.

```javascript
const pages = 400;
if (pages > 500) {
  console.log("long");
} else {
  console.log("short");
}
console.log(pages === 400);
```

**In the console**

```text
short
true
```

## Lists, objects and functions

### arrays

A list. Positions start at 0.

```javascript
const months = ["Jan", "Feb"];
console.log(months.length, months[0]);
console.log(months);
```

**In the console**

```text
2 Jan
["Jan","Feb"]
```

### objects

Named values, like a Python dictionary. A missing name gives `undefined`, with no error.

```javascript
const book = { title: "Emma", pages: 400 };
console.log(book.title);
console.log(book.author);
```

**In the console**

```text
Emma
undefined
```

### functions

`function` with a name, or an arrow `=>` for a short one.

```javascript
function double(x) {
  return 2 * x;
}
const triple = x => 3 * x;
console.log(double(5), triple(5));
```

**In the console**

```text
10 15
```

### `map`

Build a new array, like a Python list comprehension. This prepares the data of a chart.

```javascript
const books = [{ title: "Emma", pages: 400 }, { title: "Dune", pages: 600 }];
console.log(books.map(b => b.title));
console.log(books.map(b => b.pages));
```

**In the console**

```text
["Emma","Dune"]
[400,600]
```

### `encodeURIComponent`

Make a typed text safe to put in an address.

```javascript
console.log("/api/data?country=" + encodeURIComponent("F R&x"));
```

**In the console**

```text
/api/data?country=F%20R%26x
```

## Ask for data: `fetch`

Here `books.json` contains:

```json
[{"title": "Emma"}, {"title": "Dune"}]
```

`fetch` needs a server (`python -m http.server` or Flask): it does not work on a page opened by double-click.

### ask for a JSON file

The answer arrives later: the line after `fetch` is shown **first**.

```javascript
fetch("books.json")
  .then(response => response.json())
  .then(books => {
    console.log("received", books.length, "books");
  });
console.log("this line comes first");
```

**In the console**

```text
this line comes first
received 2 books
```

### test the answer

A wrong address does not stop `fetch`: test `response.ok` or the content.

```javascript
fetch("bokos.json")
  .then(response => {
    console.log(response.status, response.ok);
  });
```

**In the console**

```text
404 false
```

## Change the page

### change a text

`getElementById` finds the element, `textContent` replaces its text (HTML is not interpreted).

```html
<p id="message">Old text</p>
```

```javascript
document.getElementById("message").textContent = "New text <b>";
```

<div class="preview"><p><strong>Live result: the code really runs</strong></p><iframe sandbox="allow-scripts" title="Live result: the code really runs" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;p id=&quot;message&quot;&gt;Old text&lt;/p&gt;&#10;&#10;&lt;script&gt;&#10;document.getElementById(&quot;message&quot;).textContent = &quot;New text &lt;b&gt;&quot;;&#10;&lt;/script&gt;" style="height:60px"></iframe></div>

### react to a click

`addEventListener` runs a function at each click. Try the button.

```html
<button id="add" type="button">Add a book</button>
<p id="count">0 book</p>
```

```javascript
let total = 0;
document.getElementById("add").addEventListener("click", () => {
  total = total + 1;
  document.getElementById("count").textContent = total + " book(s)";
});
```

<div class="preview"><p><strong>Live result: the code really runs</strong></p><iframe sandbox="allow-scripts" title="Live result: the code really runs" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;button id=&quot;add&quot; type=&quot;button&quot;&gt;Add a book&lt;/button&gt;&#10;&lt;p id=&quot;count&quot;&gt;0 book&lt;/p&gt;&#10;&#10;&lt;script&gt;&#10;let total = 0;&#10;document.getElementById(&quot;add&quot;).addEventListener(&quot;click&quot;, () =&gt; {&#10;  total = total + 1;&#10;  document.getElementById(&quot;count&quot;).textContent = total + &quot; book(s)&quot;;&#10;});&#10;&lt;/script&gt;" style="height:100px"></iframe></div>

### read a field

`value` is what the visitor typed (always a text).

```html
<label for="name">Name</label> <input id="name" value="Ada">
<button id="go" type="button">Greet</button>
<p id="out"></p>
```

```javascript
document.getElementById("go").addEventListener("click", () => {
  const name = document.getElementById("name").value;
  document.getElementById("out").textContent = "Hello " + name;
});
```

<div class="preview"><p><strong>Live result: the code really runs</strong></p><iframe sandbox="allow-scripts" title="Live result: the code really runs" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;label for=&quot;name&quot;&gt;Name&lt;/label&gt; &lt;input id=&quot;name&quot; value=&quot;Ada&quot;&gt;&#10;&lt;button id=&quot;go&quot; type=&quot;button&quot;&gt;Greet&lt;/button&gt;&#10;&lt;p id=&quot;out&quot;&gt;&lt;/p&gt;&#10;&#10;&lt;script&gt;&#10;document.getElementById(&quot;go&quot;).addEventListener(&quot;click&quot;, () =&gt; {&#10;  const name = document.getElementById(&quot;name&quot;).value;&#10;  document.getElementById(&quot;out&quot;).textContent = &quot;Hello &quot; + name;&#10;});&#10;&lt;/script&gt;" style="height:110px"></iframe></div>

## Charts with Chart.js

Load the library **before** your script. The charts below need an internet connection.

```text
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.6.2/dist/chart.umd.min.js"></script>
<script src="chart.js"></script>
```

```html
<div style="max-width:30rem">
  <canvas id="chart" role="img" aria-label="Books lent per month"></canvas>
</div>
```

### bars

To compare. `labels` and `data` must have the same length.

```javascript
new Chart(document.getElementById("chart"), {
  type: "bar",
  data: {
    labels: ["Jan", "Feb", "Mar"],
    datasets: [{ label: "Books lent", data: [120, 95, 140] }]
  }
});
```

<div class="preview"><p><strong>Live result: the code really runs</strong></p><iframe sandbox="allow-scripts" title="Live result: the code really runs" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;div style=&quot;max-width:30rem&quot;&gt;&#10;  &lt;canvas id=&quot;chart&quot; role=&quot;img&quot; aria-label=&quot;Books lent per month&quot;&gt;&lt;/canvas&gt;&#10;&lt;/div&gt;&#10;&lt;script src=&quot;https://cdn.jsdelivr.net/npm/chart.js@4.6.2/dist/chart.umd.min.js&quot;&gt;&lt;/script&gt;&#10;&lt;script&gt;&#10;new Chart(document.getElementById(&quot;chart&quot;), {&#10;  type: &quot;bar&quot;,&#10;  data: {&#10;    labels: [&quot;Jan&quot;, &quot;Feb&quot;, &quot;Mar&quot;],&#10;    datasets: [{ label: &quot;Books lent&quot;, data: [120, 95, 140] }]&#10;  }&#10;});&#10;&lt;/script&gt;" style="height:270px"></iframe></div>

### line

To show a change over time.

```javascript
new Chart(document.getElementById("chart"), {
  type: "line",
  data: {
    labels: ["Jan", "Feb", "Mar"],
    datasets: [{ label: "Books lent", data: [120, 95, 140] }]
  }
});
```

<div class="preview"><p><strong>Live result: the code really runs</strong></p><iframe sandbox="allow-scripts" title="Live result: the code really runs" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;div style=&quot;max-width:30rem&quot;&gt;&#10;  &lt;canvas id=&quot;chart&quot; role=&quot;img&quot; aria-label=&quot;Books lent per month&quot;&gt;&lt;/canvas&gt;&#10;&lt;/div&gt;&#10;&lt;script src=&quot;https://cdn.jsdelivr.net/npm/chart.js@4.6.2/dist/chart.umd.min.js&quot;&gt;&lt;/script&gt;&#10;&lt;script&gt;&#10;new Chart(document.getElementById(&quot;chart&quot;), {&#10;  type: &quot;line&quot;,&#10;  data: {&#10;    labels: [&quot;Jan&quot;, &quot;Feb&quot;, &quot;Mar&quot;],&#10;    datasets: [{ label: &quot;Books lent&quot;, data: [120, 95, 140] }]&#10;  }&#10;});&#10;&lt;/script&gt;" style="height:270px"></iframe></div>

### the vertical axis: `options`

Start at 0 so that bars are honest. Note the comma before `options`.

```javascript
new Chart(document.getElementById("chart"), {
  type: "bar",
  data: {
    labels: ["Jan", "Feb", "Mar"],
    datasets: [{ label: "Books lent", data: [120, 95, 140] }]
  },
  options: { scales: { y: { min: 0, max: 200 } } }
});
```

<div class="preview"><p><strong>Live result: the code really runs</strong></p><iframe sandbox="allow-scripts" title="Live result: the code really runs" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;div style=&quot;max-width:30rem&quot;&gt;&#10;  &lt;canvas id=&quot;chart&quot; role=&quot;img&quot; aria-label=&quot;Books lent per month&quot;&gt;&lt;/canvas&gt;&#10;&lt;/div&gt;&#10;&lt;script src=&quot;https://cdn.jsdelivr.net/npm/chart.js@4.6.2/dist/chart.umd.min.js&quot;&gt;&lt;/script&gt;&#10;&lt;script&gt;&#10;new Chart(document.getElementById(&quot;chart&quot;), {&#10;  type: &quot;bar&quot;,&#10;  data: {&#10;    labels: [&quot;Jan&quot;, &quot;Feb&quot;, &quot;Mar&quot;],&#10;    datasets: [{ label: &quot;Books lent&quot;, data: [120, 95, 140] }]&#10;  },&#10;  options: { scales: { y: { min: 0, max: 200 } } }&#10;});&#10;&lt;/script&gt;" style="height:270px"></iframe></div>

### `destroy`

A canvas holds one chart. Before drawing again, remove the previous one.

```javascript
let chart = null;
// each time you draw:
if (chart) {
  chart.destroy();
}
chart = new Chart(canvas, settings);
```

## Read an error message

Errors appear in red in the console, with the file and line on the right. Messages shown with Chrome (other browsers word them differently).

### `ReferenceError`

A name that does not exist: spelling.

```javascript
const title = "Emma";
console.log(titel);
```

```text
Uncaught ReferenceError: titel is not defined
```

### `TypeError`: null

The element was not found: check the `id`, and put `<script>` at the end of `body`.

```html
<p id="message"></p>
```

```javascript
document.getElementById("mesage").textContent = "Hello";
```

```text
Uncaught TypeError: Cannot set properties of null (setting 'textContent')
```

### `TypeError`: const

A `const` cannot receive a new value: use `let`.

```javascript
const total = 0;
total = total + 1;
```

```text
Uncaught TypeError: Assignment to constant variable.
```

### `SyntaxError`

A mistake in the writing: a bracket, a brace, a comma or a quote.

```javascript
console.log("Emma";
```

```text
Uncaught SyntaxError: missing ) after argument list
```

- [All notions](notions.html)
