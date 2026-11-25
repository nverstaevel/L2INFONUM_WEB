title: CSS, with its result
---
The CSS used in this course, each time with **what the browser displays**. Link your stylesheet in the `head` of the page:

```text
<link rel="stylesheet" href="style.css">
```

See also the [reference on MDN](https://developer.mozilla.org/en-US/docs/Web/CSS).

## Choose what to style (selectors)

### element

The name of a tag styles every such element.

```css
p { color: darkred; }
```

```html
<h3>A title</h3>
<p>First paragraph.</p>
<p>Second paragraph.</p>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;p { color: darkred; }&#10;&lt;/style&gt;&#10;&lt;h3&gt;A title&lt;/h3&gt;&#10;&lt;p&gt;First paragraph.&lt;/p&gt;&#10;&lt;p&gt;Second paragraph.&lt;/p&gt;"></iframe></div>

### class: `.name`

Every element with `class="name"`.

```css
.note { background: gold; }
```

```html
<p class="note">With the class.</p>
<p>Without.</p>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.note { background: gold; }&#10;&lt;/style&gt;&#10;&lt;p class=&quot;note&quot;&gt;With the class.&lt;/p&gt;&#10;&lt;p&gt;Without.&lt;/p&gt;"></iframe></div>

### identifier: `#name`

The only element with `id="name"`.

```css
#source { color: grey; }
```

```html
<p>Loans of 2025.</p>
<p id="source">Source: city library.</p>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;#source { color: grey; }&#10;&lt;/style&gt;&#10;&lt;p&gt;Loans of 2025.&lt;/p&gt;&#10;&lt;p id=&quot;source&quot;&gt;Source: city library.&lt;/p&gt;"></iframe></div>

### inside another: `nav a`

Only the links inside `nav`.

```css
nav a { color: green; }
```

```html
<nav><a href="#">In the menu</a></nav>
<p><a href="#">In a paragraph</a></p>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;nav a { color: green; }&#10;&lt;/style&gt;&#10;&lt;nav&gt;&lt;a href=&quot;#&quot;&gt;In the menu&lt;/a&gt;&lt;/nav&gt;&#10;&lt;p&gt;&lt;a href=&quot;#&quot;&gt;In a paragraph&lt;/a&gt;&lt;/p&gt;"></iframe></div>

### state: `:hover`, `:focus`

When the mouse is over, or when reached with the Tab key. Move your mouse over the link.

```css
a:hover, a:focus { background: gold; }
```

```html
<p><a href="#">Move the mouse here</a></p>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;a:hover, a:focus { background: gold; }&#10;&lt;/style&gt;&#10;&lt;p&gt;&lt;a href=&quot;#&quot;&gt;Move the mouse here&lt;/a&gt;&lt;/p&gt;"></iframe></div>

### which rule wins?

**Specificity**: id beats class, class beats element. With equal weight, the last rule wins.

```css
#a    { color: orange; }
.note { color: green; }
p     { color: red; }
p     { color: blue; }
```

```html
<p id="a" class="note">id + class + element</p>
<p class="note">class + element</p>
<p>element only</p>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;#a    { color: orange; }&#10;.note { color: green; }&#10;p     { color: red; }&#10;p     { color: blue; }&#10;&lt;/style&gt;&#10;&lt;p id=&quot;a&quot; class=&quot;note&quot;&gt;id + class + element&lt;/p&gt;&#10;&lt;p class=&quot;note&quot;&gt;class + element&lt;/p&gt;&#10;&lt;p&gt;element only&lt;/p&gt;"></iframe></div>

## Colours and text

### `color`, `background`

Colour of the text and of the background, by name or code `#rrggbb`.

```css
p { color: #ffffff; background: #14213d; padding: 8px; }
```

```html
<p>White on dark blue.</p>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;p { color: #ffffff; background: #14213d; padding: 8px; }&#10;&lt;/style&gt;&#10;&lt;p&gt;White on dark blue.&lt;/p&gt;"></iframe></div>

### `font-family`, `line-height`

The font (give a spare one) and the space between lines.

```css
.a { font-family: Arial, sans-serif; }
.b { font-family: Georgia, serif; line-height: 2; }
```

```html
<p class="a">Arial</p>
<p class="b">Georgia,<br>with more space between lines.</p>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.a { font-family: Arial, sans-serif; }&#10;.b { font-family: Georgia, serif; line-height: 2; }&#10;&lt;/style&gt;&#10;&lt;p class=&quot;a&quot;&gt;Arial&lt;/p&gt;&#10;&lt;p class=&quot;b&quot;&gt;Georgia,&lt;br&gt;with more space between lines.&lt;/p&gt;"></iframe></div>

### `text-align`

Align the text left, centre or right.

```css
h3 { text-align: center; }
p  { text-align: right; }
```

```html
<h3>Centred</h3>
<p>Right</p>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;h3 { text-align: center; }&#10;p  { text-align: right; }&#10;&lt;/style&gt;&#10;&lt;h3&gt;Centred&lt;/h3&gt;&#10;&lt;p&gt;Right&lt;/p&gt;"></iframe></div>

## The box model

### `padding`, `border`, `margin`

**padding**: space inside; **border**: the line around; **margin**: space outside.

```css
p { padding: 20px; border: 4px solid darkred; margin: 30px; background: #fde; }
```

```html
<p>One box</p>
<p>Another box</p>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;p { padding: 20px; border: 4px solid darkred; margin: 30px; background: #fde; }&#10;&lt;/style&gt;&#10;&lt;p&gt;One box&lt;/p&gt;&#10;&lt;p&gt;Another box&lt;/p&gt;"></iframe></div>

### `width` and `box-sizing`

By default `width` is the content only: the first box is 200 + 2×20 + 2×5 = 250px wide. With `border-box`, 200px includes everything.

```css
p  { width: 200px; padding: 20px; border: 5px solid; }
.b { box-sizing: border-box; }
```

```html
<p>content-box: 250px</p>
<p class="b">border-box: 200px</p>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;p  { width: 200px; padding: 20px; border: 5px solid; }&#10;.b { box-sizing: border-box; }&#10;&lt;/style&gt;&#10;&lt;p&gt;content-box: 250px&lt;/p&gt;&#10;&lt;p class=&quot;b&quot;&gt;border-box: 200px&lt;/p&gt;"></iframe></div>

### `max-width` and `margin: 0 auto`

Never wider than a value, and centred.

```css
main { max-width: 300px; margin: 0 auto; background: #eef2f7; padding: 8px; }
```

```html
<main>A centred column.</main>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;main { max-width: 300px; margin: 0 auto; background: #eef2f7; padding: 8px; }&#10;&lt;/style&gt;&#10;&lt;main&gt;A centred column.&lt;/main&gt;"></iframe></div>

### responsive images

An image never goes beyond its box.

```css
div { width: 160px; border: 2px dashed grey; }
img { max-width: 100%; height: auto; }
```

```html
<div><img alt="A wide rectangle" src="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='600' height='200'><rect width='600' height='200' fill='teal'/></svg>"></div>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;div { width: 160px; border: 2px dashed grey; }&#10;img { max-width: 100%; height: auto; }&#10;&lt;/style&gt;&#10;&lt;div&gt;&lt;img alt=&quot;A wide rectangle&quot; src=&quot;data:image/svg+xml,&lt;svg xmlns=&#x27;http://www.w3.org/2000/svg&#x27; width=&#x27;600&#x27; height=&#x27;200&#x27;&gt;&lt;rect width=&#x27;600&#x27; height=&#x27;200&#x27; fill=&#x27;teal&#x27;/&gt;&lt;/svg&gt;&quot;&gt;&lt;/div&gt;"></iframe></div>

## Lists and tables

### `list-style`

Remove the bullets, for a menu.

```css
ul { list-style: none; padding: 0; }
```

```html
<ul>
  <li>Home</li>
  <li>Books</li>
  <li>Contact</li>
</ul>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;ul { list-style: none; padding: 0; }&#10;&lt;/style&gt;&#10;&lt;ul&gt;&#10;  &lt;li&gt;Home&lt;/li&gt;&#10;  &lt;li&gt;Books&lt;/li&gt;&#10;  &lt;li&gt;Contact&lt;/li&gt;&#10;&lt;/ul&gt;"></iframe></div>

### `border-collapse`

One line between the cells instead of two.

```css
table { width: 100%; border-collapse: collapse; }
th, td { border: 1px solid grey; padding: 6px; text-align: left; }
th { background: #eef2f7; }
```

```html
<table>
  <tr><th>Title</th><th>Loans</th></tr>
  <tr><td>Emma</td><td>12</td></tr>
</table>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;table { width: 100%; border-collapse: collapse; }&#10;th, td { border: 1px solid grey; padding: 6px; text-align: left; }&#10;th { background: #eef2f7; }&#10;&lt;/style&gt;&#10;&lt;table&gt;&#10;  &lt;tr&gt;&lt;th&gt;Title&lt;/th&gt;&lt;th&gt;Loans&lt;/th&gt;&lt;/tr&gt;&#10;  &lt;tr&gt;&lt;td&gt;Emma&lt;/td&gt;&lt;td&gt;12&lt;/td&gt;&lt;/tr&gt;&#10;&lt;/table&gt;"></iframe></div>

## Layout with Flexbox

### `display: flex` and `gap`

Put the children of an element in a row, with space between them.

```css
.row div { border: 2px solid; padding: 4px 12px; }
.row { display: flex; gap: 1rem; }
```

```html
<div class="row">
  <div>One</div>
  <div>Two</div>
  <div>Three</div>
</div>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.row div { border: 2px solid; padding: 4px 12px; }&#10;.row { display: flex; gap: 1rem; }&#10;&lt;/style&gt;&#10;&lt;div class=&quot;row&quot;&gt;&#10;  &lt;div&gt;One&lt;/div&gt;&#10;  &lt;div&gt;Two&lt;/div&gt;&#10;  &lt;div&gt;Three&lt;/div&gt;&#10;&lt;/div&gt;"></iframe></div>

### `justify-content`

Share the free space along the row.

```css
.row div { border: 2px solid; padding: 4px 12px; }
.row { display: flex; justify-content: space-between; }
```

```html
<div class="row">
  <div>One</div>
  <div>Two</div>
  <div>Three</div>
</div>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.row div { border: 2px solid; padding: 4px 12px; }&#10;.row { display: flex; justify-content: space-between; }&#10;&lt;/style&gt;&#10;&lt;div class=&quot;row&quot;&gt;&#10;  &lt;div&gt;One&lt;/div&gt;&#10;  &lt;div&gt;Two&lt;/div&gt;&#10;  &lt;div&gt;Three&lt;/div&gt;&#10;&lt;/div&gt;"></iframe></div>

### `align-items`

Place the elements across the row.

```css
.row div { border: 2px solid; padding: 4px 12px; }
.row { display: flex; gap: 1rem; height: 90px; align-items: center; background: #eef2f7; }
```

```html
<div class="row">
  <div>One</div>
  <div>Two</div>
  <div>Three</div>
</div>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.row div { border: 2px solid; padding: 4px 12px; }&#10;.row { display: flex; gap: 1rem; height: 90px; align-items: center; background: #eef2f7; }&#10;&lt;/style&gt;&#10;&lt;div class=&quot;row&quot;&gt;&#10;  &lt;div&gt;One&lt;/div&gt;&#10;  &lt;div&gt;Two&lt;/div&gt;&#10;  &lt;div&gt;Three&lt;/div&gt;&#10;&lt;/div&gt;"></iframe></div>

### `flex-direction: column`

One under the other.

```css
.row div { border: 2px solid; padding: 4px 12px; }
.row { display: flex; flex-direction: column; gap: 4px; }
```

```html
<div class="row">
  <div>One</div>
  <div>Two</div>
  <div>Three</div>
</div>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.row div { border: 2px solid; padding: 4px 12px; }&#10;.row { display: flex; flex-direction: column; gap: 4px; }&#10;&lt;/style&gt;&#10;&lt;div class=&quot;row&quot;&gt;&#10;  &lt;div&gt;One&lt;/div&gt;&#10;  &lt;div&gt;Two&lt;/div&gt;&#10;  &lt;div&gt;Three&lt;/div&gt;&#10;&lt;/div&gt;"></iframe></div>

### `flex-wrap`

Go to the next line when there is no room.

```css
.row div { border: 2px solid; padding: 4px 12px; }
.row { display: flex; flex-wrap: wrap; gap: 8px; width: 160px; border: 2px dashed grey; }
```

```html
<div class="row">
  <div>One</div>
  <div>Two</div>
  <div>Three</div>
</div>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.row div { border: 2px solid; padding: 4px 12px; }&#10;.row { display: flex; flex-wrap: wrap; gap: 8px; width: 160px; border: 2px dashed grey; }&#10;&lt;/style&gt;&#10;&lt;div class=&quot;row&quot;&gt;&#10;  &lt;div&gt;One&lt;/div&gt;&#10;  &lt;div&gt;Two&lt;/div&gt;&#10;  &lt;div&gt;Three&lt;/div&gt;&#10;&lt;/div&gt;"></iframe></div>

## Screens of different sizes

### `@media`

Rules that apply only on narrow screens. Put them at the **end** of the file. On a real page also add the `viewport` line in the `head`.

```css
.row div { border: 2px solid; padding: 4px 12px; }
.row { display: flex; gap: 1rem; }
@media (max-width: 600px) {
  .row { flex-direction: column; }
}
```

```html
<div class="row">
  <div>One</div>
  <div>Two</div>
  <div>Three</div>
</div>
```

<div class="preview"><p><strong>Result in the browser</strong> · full width (wider than 600px on a computer)</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.row div { border: 2px solid; padding: 4px 12px; }&#10;.row { display: flex; gap: 1rem; }&#10;@media (max-width: 600px) {&#10;  .row { flex-direction: column; }&#10;}&#10;&lt;/style&gt;&#10;&lt;div class=&quot;row&quot;&gt;&#10;  &lt;div&gt;One&lt;/div&gt;&#10;  &lt;div&gt;Two&lt;/div&gt;&#10;  &lt;div&gt;Three&lt;/div&gt;&#10;&lt;/div&gt;"></iframe></div>

<div class="preview"><p><strong>Result in the browser</strong> · 320px wide, like a phone</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.row div { border: 2px solid; padding: 4px 12px; }&#10;.row { display: flex; gap: 1rem; }&#10;@media (max-width: 600px) {&#10;  .row { flex-direction: column; }&#10;}&#10;&lt;/style&gt;&#10;&lt;div class=&quot;row&quot;&gt;&#10;  &lt;div&gt;One&lt;/div&gt;&#10;  &lt;div&gt;Two&lt;/div&gt;&#10;  &lt;div&gt;Three&lt;/div&gt;&#10;&lt;/div&gt;" style="width:320px;max-width:100%"></iframe></div>

## When it does not work

**Nothing changes?** Open the developer tools (F12), pick the element: a crossed-out line is overridden or not understood.

### a missing `;`

Both lines are lost. CSS shows **no error message**.

```css
p {
  color: red
  background: gold;
}
```

```html
<p>Neither red nor gold.</p>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;p {&#10;  color: red&#10;  background: gold;&#10;}&#10;&lt;/style&gt;&#10;&lt;p&gt;Neither red nor gold.&lt;/p&gt;"></iframe></div>

### a number without unit

`padding: 20` is ignored: write `20px`.

```css
p { padding: 20; background: gold; }
```

```html
<p>No inner space.</p>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;p { padding: 20; background: gold; }&#10;&lt;/style&gt;&#10;&lt;p&gt;No inner space.&lt;/p&gt;"></iframe></div>

### class without the dot

`note` means a tag called note; a class is `.note`.

```css
note { color: red; }
```

```html
<p class="note">Still not red.</p>
```

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;note { color: red; }&#10;&lt;/style&gt;&#10;&lt;p class=&quot;note&quot;&gt;Still not red.&lt;/p&gt;"></iframe></div>

- [All notions](notions.html)
