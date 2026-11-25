title: HTML tags, with their result
---
Each tag of the course: what it is for, the code, and **what the browser shows** with no CSS. The examples are about a library. Full reference: [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements).

## The page

### `html`, `head`, `body`

The skeleton of every page. `head` holds information about the page: `meta` (character set), `title` (name of the tab), `link` (stylesheet). `body` holds what is shown.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>City library</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <p>Only the body is shown.</p>
</body>
</html>
```

### `header`, `nav`, `main`, `section`, `footer`

**Semantic** tags: they say what each part is. They do not change much how the page looks.

```html
<header>
  <h1>City library</h1>
  <nav><a href="#books">Books</a></nav>
</header>
<main>
  <section id="books">
    <h2>Books</h2>
    <p>We lend novels.</p>
  </section>
</main>
<footer>Source: city library.</footer>
```

### `div`

A box with no meaning, used to group elements (for style or JavaScript). Prefer a semantic tag when one fits.

```html
<div>
  <p>Two paragraphs</p>
  <p>in the same box.</p>
</div>
```

## Text and lists

### `h1`, `h2`, `h3`, `p`

Headings, by level, and paragraphs. One `h1` per page.

```html
<h1>City library</h1>
<h2>Books</h2>
<h3>Novels</h3>
<p>We lend novels for three weeks.</p>
```

### `strong`, `em`

`strong` marks something important (shown in bold), `em` a stressed word (shown in italics). Choose them for the meaning, not for the look.

```html
<p><strong>Closed on Monday.</strong> Loans last <em>three</em> weeks.</p>
```

### `ul`, `ol`, `li`

A list with bullets (`ul`) or numbers (`ol`). Each item is a `li`.

```html
<ul>
  <li>Novels</li>
  <li>Comics</li>
</ul>
<ol>
  <li>Choose a book</li>
  <li>Show your card</li>
</ol>
```

### `pre`

Text shown exactly as written, with its spaces and line breaks.

```html
<pre>Emma     1815
Dracula  1897</pre>
```

## Links and images

### `a`

A link. `href` says where it goes: another site, another file, or `#id` in the same page. Write a text that says where it goes.

```html
<p><a href="https://www.toulouse.fr">The city of Toulouse</a> ·
<a href="about.html">About us</a></p>
```

### `img`

An image. It has no closing tag. `src` is the path of the file, `alt` the text read when the image cannot be seen. `width` and `height` keep its place while it loads.

```html
<img src="images/library.jpg" alt="Three shelves of books" width="320" height="180">
```

### `figure`, `figcaption`

An image (or a table, a chart) with its caption. The caption is a good place for the **credit**: author, licence and source.

```html
<figure>
  <img src="images/library.jpg" alt="Three shelves of books" width="320" height="180">
  <figcaption>Our shelves. Drawing: course team.</figcaption>
</figure>
```

## Tables

### `table`, `caption`, `thead`, `tbody`, `tr`, `th`, `td`

`caption` is the title, `tr` a row, `th` a header cell, `td` a data cell. The browser draws no border: that is the job of CSS.

```html
<table>
  <caption>Books lent per month</caption>
  <thead>
    <tr><th scope="col">Month</th><th scope="col">Books</th></tr>
  </thead>
  <tbody>
    <tr><td>January</td><td>120</td></tr>
    <tr><td>February</td><td>95</td></tr>
  </tbody>
</table>
```

## Forms

### `form`, `label`, `input`, `button`

A **form** sends what the visitor types. `name` is the key that is sent; `label for` points to the `id` of the field.

```html
<form action="/search" method="get">
  <label for="author">Author</label>
  <input id="author" name="author">
  <label for="year">Year</label>
  <input id="year" name="year" type="number">
  <button type="submit">Search</button>
</form>
```

### `select`, `option`

A drop-down list. `value` is what is sent, the text between the tags is what is shown.

```html
<label for="genre">Genre</label>
<select id="genre" name="genre">
  <option value="novel">Novel</option>
  <option value="comic">Comic</option>
</select>
```

### `input type="radio"`, `input type="checkbox"`

Radio buttons: one choice among those with the same `name`. Checkbox: yes or no.

```html
<label><input type="radio" name="lang" value="fr" checked> French</label>
<label><input type="radio" name="lang" value="en"> English</label>
<label><input type="checkbox" name="new"> New books only</label>
```

## For JavaScript (CM4)

### `script`, `canvas`

`script` loads or contains JavaScript. `canvas` is an empty drawing area: Chart.js draws the chart in it. No preview here.

```html
<canvas id="chart"></canvas>
<script src="chart.js"></script>
```

- [All notions](notions.html)
