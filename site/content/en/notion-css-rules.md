title: CSS rules and selectors
---
**CSS** says how elements look. A rule = a **selector** + declarations `property: value;`. `p` targets elements, `.note` a **class**, `#about` an **id**, `nav a` the links inside `nav`. When rules conflict, the most precise selector wins (**specificity**: id > class > element), then the last one.

## Example

```css
body { font-family: system-ui, sans-serif; color: #14213d; }
.note { color: darkblue; }
nav a { color: white; }
```

## What you see

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;body { font-family: system-ui, sans-serif; color: #14213d; }&#10;.note { color: darkblue; }&#10;nav a { color: white; }&#10;nav { background: #14213d; padding: 8px; }&#10;&lt;/style&gt;&#10;&lt;nav&gt;&lt;a href=&quot;#&quot;&gt;A link in nav (white)&lt;/a&gt;&lt;/nav&gt;&#10;&lt;p class=&quot;note&quot;&gt;A paragraph with class=&quot;note&quot;.&lt;/p&gt;&#10;&lt;p&gt;A paragraph.&lt;/p&gt;"></iframe></div>

## Common mistakes

- A missing `;` or `}` breaks the following rules.
- The stylesheet is not linked in `<head>`.

## Go further

- Lecture: [CM3](cm3.html)
- Recipes: [Readable page and tables](recipe-clean-style.html)
- Labs using it: [TD3](td3.html)
- [CSS, with its result](notion-css-ref.html)
- [All notions](notions.html)
