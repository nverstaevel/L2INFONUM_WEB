title: TD3 · Styling and responsive layout
---
**Friday 22 January 2027 · 3 hours.** Starter files: folder [`td3`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td3).

## Goal

Style your TD2 page so that it is comfortable on a phone and on a computer.

**You have succeeded if**: `python check.py` shows eleven `[OK]` and, on a phone width, nothing overflows.

| Step | You do | Time |
|---|---|---|
| 1 | Link the stylesheet | 20 min |
| 2 | Colours and fonts | 30 min |
| 3 | Boxes and spacing | 30 min |
| 4 | Navigation with Flexbox | 30 min |
| 5 | Table and form | 40 min |
| 6 | Phone screens | 30 min |

## Before the session

- [ ] I have read [CM3](cm3.html).
- [ ] My TD2 page is valid. If not, ask your teacher for a starting page.

## How to work

1. Do the steps **in order**.
2. Write your code only where you see `TODO`. Its number is the number in this sheet.
3. After each part, **save** (`Ctrl+S`, or `Cmd+S` on a Mac) and run the checker in a terminal (**Terminal → New Terminal** in VS Code):

```text
python check.py
```

On macOS or Linux, outside a virtual environment, type `python3`. `[OK]` means the part works, `[  ]` means not yet. The checker does not replace looking at your page in the browser.

## Five-minute reminder

CSS says how elements look. A **rule** has a **selector** (which elements) and **declarations** (property: value). Each declaration ends with `;`.

```css
h2 {              /* selector: every h2 */
  color: green;   /* property: value; */
}
nav a { }         /* the links that are inside nav */
th, td { }        /* th and td together */
```

## Step 1 · Link the stylesheet (20 min)

1. Copy `index.html` and the folder `images` from `td2` into `td3`.
2. Open the folder `td3` in VS Code and the page in your browser.
3. In `index.html`, inside `<head>`, add:

```html
<link rel="stylesheet" href="style.css">
```

**Check.** `1` is `[OK]`.

## Step 2 · Colours and fonts (30 min)

### 2A · The whole page

**Example** (another subject: adapt it, do not copy it as it is).

```css
h1 {
  font-family: Georgia, serif;
  color: darkred;
  background: #fff4e0;   /* a colour written as a code */
}
```

**Your turn.** For `body`: set `margin: 0;`, `font-family: system-ui, Arial, sans-serif;`, `line-height: 1.5;`, and choose a dark `color` and a light `background`.

### 2B · Header and footer

**Your turn.** Give `header, footer` a dark `background`, a light `color` and `padding: 1rem;`. `rem` is a unit based on the text size.

**Check.** `2A` and `2B` are `[OK]`. The links in the header may be hard to read: step 4 fixes it.

<details markdown="1"><summary>Stuck?</summary>

Nothing changes in the browser? Check that you saved both files and that the `link` line is exact. A missing `}` stops everything after it.

</details>

## Step 3 · Boxes and spacing (30 min)

Every element is a box: the content, then **padding** (space inside), the **border**, then **margin** (space outside).

### 3A · Centre the content

**Example** (another subject: adapt it, do not copy it as it is).

```css
.card {
  max-width: 20rem;    /* never wider than this */
  margin: 0 auto;      /* 0 above and below, automatic left and right = centred */
  padding: 2rem;
}
```

**Your turn.** Centre `main`, with a maximum width of `60rem` and a padding of `1rem`.

### 3B · Images never overflow

**Your turn.** For `img`: `max-width: 100%;` and `height: auto;`.

**Check.** `3A`, `3B` `[OK]`. On a wide window, the content stays in the middle. Right-click → **Inspect** to see the box drawing.

## Step 4 · Navigation with Flexbox (30 min)

**Flexbox** places the children of a box in a row. You write it on the **parent**.

### 4A · The list in a row

**Example** (another subject: adapt it, do not copy it as it is).

```css
.toolbar {
  display: flex;      /* children side by side */
  gap: 2rem;          /* space between them */
}
```

**Your turn.** Apply it to `nav ul`, with a gap of `1rem`. Also remove the bullets (`list-style: none;`) and the spaces (`margin: 0;`, `padding: 0;`).

### 4B · Readable links

**Your turn.** Give `nav a` a `color` that is easy to read on your header.

**Check.** The three links are on one line, without bullets.

## Step 5 · Table and form (40 min)

### 5A · One border, not two

**Your turn.** For `table`: `width: 100%;` and `border-collapse: collapse;`.

### 5B · Cells

**Example** (another subject: adapt it, do not copy it as it is).

```css
.price {
  border: 1px solid grey;   /* thickness, style, colour */
  padding: 0.5rem;
  text-align: left;
}
```

**Your turn.** Give `th, td` a border, a padding and `text-align: left;`. Then, in a separate rule, give `th` a `background`.

### 5C · The form

**Your turn.** Make `form` a flex box with `gap: 0.75rem;`, `flex-wrap: wrap;` (go to the next line if needed) and `align-items: center;`.

**Check.** `5A` to `5C` `[OK]`: simple borders, a visible header row, spaced fields.

## Step 6 · Phone screens (30 min)

A **media query** applies rules only if a condition is true, here a narrow screen.

**Example** (another subject: adapt it, do not copy it as it is).

```css
@media (max-width: 600px) {
  .toolbar {
    flex-direction: column;   /* one under the other */
  }
}
```

**Your turn.** At the **end** of the file, put `nav ul` and `form` in a column on screens up to 600px. Add `align-items: stretch;` so that the fields take the whole width.

**Check.** Press `F12`, then the **phone and tablet** icon, and choose a width of 375px: menu and form are vertical, nothing overflows. Eleven `[OK]`.

<details markdown="1"><summary>Stuck?</summary>

Two selectors can share one rule: `nav ul, form { … }`. There are two `}` at the end: one for the rule, one for `@media`.

</details>

## If you finish early (optional)

1. Add `:hover` and `:focus` styles to links and buttons.
2. Highlight one table row with a class.
3. Check the contrast of your colours with the developer tools.
