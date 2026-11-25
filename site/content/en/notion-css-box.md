title: Box model
---
Every element is a box: content, **padding** (inside), **border**, **margin** (outside). By default, visible width = width + padding + border. `box-sizing: border-box` includes them in `width`.

## Example

```css
main {
  max-width: 60rem;     /* never wider */
  margin: 0 auto;       /* centred */
  padding: 1rem;        /* inner space */
}
img { max-width: 100%; height: auto; }
```

## What you see

<div class="preview"><p><strong>Result in the browser</strong> · links are inactive here</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;main {&#10;  max-width: 60rem;     /* never wider */&#10;  margin: 0 auto;       /* centred */&#10;  padding: 1rem;        /* inner space */&#10;}&#10;img { max-width: 100%; height: auto; }&#10;main { background: #eef2f7; }&#10;&lt;/style&gt;&#10;&lt;main&gt;&lt;p&gt;The content of main, never wider than 60rem, centred, with inner space.&lt;/p&gt;&lt;/main&gt;"></iframe></div>

## Common mistakes

- Using `width` where `max-width` is needed: the page overflows on a phone.

## Go further

- Lecture: [CM3](cm3.html)
- Recipes: [Readable page and tables](recipe-clean-style.html)
- Labs using it: [TD3](td3.html)
- [CSS, with its result](notion-css-ref.html)
- [All notions](notions.html)
