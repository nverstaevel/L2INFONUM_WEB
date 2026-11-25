title: CM3 · CSS: look and layout
---
**19 January 2027.**

## Objectives

1. write selectors and predict which rule wins
2. compute the size of a box
3. arrange elements with Flexbox
4. adapt a page with a media query

<!--plan-->
## The question

**How do we make it readable, on a phone too?**

1. Rules
2. Boxes
3. Layout
<!--/plan-->

## Slides

[PDF](cm3-en.pdf)

{{slides:cm3:en}}

<!--lab-->
## For Friday

TD3: style your page and make it fit a phone.

- Notions: [CSS rules and selectors](notion-css-rules.html), [Box model](notion-css-box.html), [Developer tools](notion-devtools.html), [Flexbox](notion-css-flexbox.html), [Responsive design and media queries](notion-css-media.html)
- Recipes: [Readable page and tables](recipe-clean-style.html), [Responsive navigation bar](recipe-nav-bar.html)
<!--/lab-->

## Check yourself

<details><summary>Which wins: .note or #about?</summary><p>#about: an id weighs more than a class.</p></details>
<details><summary>width 200px, padding 10px, border 1px: visible width?</summary><p>222px with the default box-sizing.</p></details>
<details><summary>Which property starts Flexbox?</summary><p>display: flex on the parent.</p></details>
<details><summary>What does @media (max-width: 600px) mean?</summary><p>Rules for screens of 600px or less.</p></details>

Next: [TD3](td3.html).
