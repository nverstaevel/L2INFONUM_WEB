title: TD3 · Styling and responsive layout
---
**Friday 22 January 2027 · 3 hours.** Starter files: [`td3`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td3).

## Goal

Style your TD2 page and make it comfortable on a phone and on a computer.

**You have succeeded if** at 375 px wide nothing overflows, and on a wide screen the navigation is on one line.

| Provided | Your job |
|---|---|
| `style.css` skeleton | the stylesheet |

## Before the session

- [ ] I have read [CM3](cm3.html).
- [ ] My TD2 page is valid.

## Step 1 · Link and base style (30 min)

Copy `style.css` next to your page and add in `<head>`:

```
<link rel="stylesheet" href="style.css">
```

**Checkpoint:** changing the `body` colour changes the page.


## Step 2 · Box model (35 min)

Each element is a box: content, *padding* (inside), border, *margin* (outside). Centre `main` and give it a maximum width.

**Checkpoint:** `main` is centred on a wide screen.

<details><summary>Hint 1</summary><p>`max-width` with `margin: 0 auto;`</p></details>

## Step 3 · Flexbox navigation (35 min)

*Flexbox* places the children of a box in a row or a column.

**Checkpoint:** links are side by side without bullets.

<details><summary>Hint 1</summary><p>`nav ul { display: flex; gap: 1rem; list-style: none; }`</p></details>

## Step 4 · Table and form (35 min)

Style the table and space the form fields.

**Checkpoint:** borders are single and the header stands out.

<details><summary>Hint 1</summary><p>`border-collapse: collapse;`</p></details>

## Step 5 · Responsive (35 min)

A *media query* applies rules only under a condition. Use the device toolbar of the developer tools to simulate a phone.

**Checkpoint:** at 375 px the menu and form are vertical.

<details><summary>Hint 1</summary><p>`@media (max-width: 600px) { ... }`</p></details>

## Extensions

1. Add `:hover` and `:focus` styles.
2. Use a class to highlight one table row.
3. Check the colour contrast of your page.
