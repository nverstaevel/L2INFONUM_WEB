title: Flexbox
---
**Flexbox** places the children of a box in a row or a column. Write `display: flex` on the **parent**. `gap` is the space between children, `justify-content` acts along the row, `align-items` across it.

## Example

```css
nav ul {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  list-style: none;
  padding: 0;
}
```

## What you see

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;nav ul {&#10;  display: flex;&#10;  gap: 1rem;&#10;  flex-wrap: wrap;&#10;  list-style: none;&#10;  padding: 0;&#10;}&#10;&lt;/style&gt;&#10;&lt;nav&gt;&lt;ul&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Home&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Books&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Contact&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/nav&gt;"></iframe></div>

## Common mistakes

- `display: flex` written on the children instead of the parent.

## Go further

- Lecture: [CM3](cm3.html)
- Recipes: [Responsive navigation bar](recipe-nav-bar.html)
- Labs using it: [TD3](td3.html), [TD9](td9.html)
- [CSS, with its result](notion-css-ref.html)
- [All notions](notions.html)
