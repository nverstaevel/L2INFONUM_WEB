title: TD2 · A static page about a dataset
---
**Friday 15 January 2027 · 3 hours.** Starter files: [`td2`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td2).

## Goal

Write a valid, semantic HTML5 page that presents the Eurostat data, with a form.

**You have succeeded if** the page passes the [W3C validator](https://validator.w3.org/#validate_by_input) with no error.

| Provided | Your job |
|---|---|
| `index.html` skeleton, `images/network.svg` | the six `TODO` |

## Before the session

- [ ] I have read [CM2](cm2.html).
- [ ] I have my `internet_use_clean.csv` from TD1.

## Step 1 · Structure (30 min)

A *tag* marks the role of a piece of content. Fill the title, then `header` with `h1` and a `nav` list of internal links.

**Checkpoint:** the page opens in the browser, one `h1` only.

<details><summary>Hint 1</summary><p>`<a href="#about">` jumps to the element with `id="about"`.</p></details>

## Step 2 · Text, links, image (35 min)

Add a `section` with a paragraph, a list, a link to the dataset and the image. The `alt` *attribute* describes an image for people who cannot see it.

**Checkpoint:** the link works and the image has an `alt` text.


## Step 3 · Table (45 min)

Show at least 5 rows of your clean file.

**Checkpoint:** the table has a `caption`, a `thead` and `th` cells.

<details><summary>Hint 1</summary><p>`<tr>` is a row, `<th>` a header cell, `<td>` a data cell.</p></details>

## Step 4 · Form (40 min)

A *form* collects input. Add a country list and a year field with a button. It sends nothing useful yet: Flask will answer it in week 6.

**Checkpoint:** each field has a `label`, and after clicking the button the address shows `?country=…&year=…`.

<details><summary>Hint 1</summary><p>`<label for="year">` goes with `<input id="year" name="year">`.</p></details>
<details><summary>Hint 2</summary><p>Use `type="number"` with `min` and `max`, and `required`.</p></details>

## Step 5 · Validate (15 min)

Paste your code in the W3C validator and fix the errors.

**Checkpoint:** no error.


## Extensions

1. Add a second table for another country.
2. Add radio buttons and a checkbox to the form.
3. Add a second page and link the two.
