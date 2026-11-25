title: Responsive design and media queries
---
A **responsive** page adapts to the screen. A **media query** applies rules only under a condition. The `viewport` line in `head` is required on phones.

## Example

```css
/* in head: <meta name="viewport" content="width=device-width, initial-scale=1"> */
@media (max-width: 600px) {
  nav ul { flex-direction: column; }
}
```

## What you see

<div class="preview"><p><strong>Result in the browser</strong> · full width (wider than 600px on a computer)</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;nav ul { display: flex; gap: 1rem; list-style: none; padding: 0; }&#10;/* in head: &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt; */&#10;@media (max-width: 600px) {&#10;  nav ul { flex-direction: column; }&#10;}&#10;&lt;/style&gt;&#10;&lt;nav&gt;&lt;ul&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Home&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Books&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Contact&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/nav&gt;"></iframe></div><div class="preview"><p><strong>Result in the browser</strong> · 320px wide, like a phone</p><iframe sandbox="allow-same-origin" title="Result in the browser" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;nav ul { display: flex; gap: 1rem; list-style: none; padding: 0; }&#10;/* in head: &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt; */&#10;@media (max-width: 600px) {&#10;  nav ul { flex-direction: column; }&#10;}&#10;&lt;/style&gt;&#10;&lt;nav&gt;&lt;ul&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Home&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Books&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Contact&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/nav&gt;" style="width:320px;max-width:100%"></iframe></div>

## Common mistakes

- The media query placed before the normal rule: the normal rule then wins.

## Go further

- Lecture: [CM3](cm3.html)
- Recipes: [Responsive navigation bar](recipe-nav-bar.html)
- Labs using it: [TD3](td3.html), [TD10](td10.html)
- [CSS, with its result](notion-css-ref.html)
- [All notions](notions.html)
