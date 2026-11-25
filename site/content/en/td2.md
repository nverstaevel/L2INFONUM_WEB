title: TD2 · A static page presenting a dataset
---
**Friday 15 January 2027 · 3 hours.** Starter files: folder [`td2`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td2).

## Goal

Write a web page that presents your Eurostat data, with a form. **Keep this page:** TD3 makes it beautiful.

**You have succeeded if**: `python check.py` shows fifteen `[OK]` and the validator reports no error.

| Step | You do | Time |
|---|---|---|
| 1 | Open the files | 15 min |
| 2 | Build the structure | 30 min |
| 3 | Add text, link and image | 35 min |
| 4 | Make a table | 40 min |
| 5 | Make a form | 35 min |
| 6 | Footer and validation | 25 min |

## Before the session

- [ ] I have read [CM2](cm2.html).
- [ ] I have my `internet_use_clean.csv` from TD1.

## How to work

1. Do the steps **in order**.
2. Write your code only where you see `TODO`. Its number is the number in this sheet.
3. After each part, **save** (`Ctrl+S`, or `Cmd+S` on a Mac) and run the checker in a terminal (**Terminal → New Terminal** in VS Code):

```text
python check.py
```

On macOS or Linux, outside a virtual environment, type `python3`. `[OK]` means the part works, `[  ]` means not yet. The checker does not replace looking at your page in the browser.

## Five-minute reminder

HTML describes a page with **elements**. An element has an opening **tag**, some content and a closing tag. An **attribute** adds information inside the opening tag. Elements go inside one another: close the inner one first. Indent by 2 spaces to see who is inside whom.

```html
<p>Read <a href="books.html">our books</a>.</p>
<!-- p = paragraph · a = link · href = attribute · this line is a comment -->
```

## Step 1 · Open the files (15 min)

1. Open the folder `td2` in VS Code (**File → Open Folder**).
2. Open `index.html` in your browser too: double-click it in your file explorer.
3. In the VS Code terminal, run `python check.py`.

From now on: edit in VS Code, **save**, then **reload** the browser (`F5`).

**Check.** The page is empty and the checker shows many `[  ]`. That is normal.

## Step 2 · Build the structure (30 min)

### 2A · The page title

**Your turn.** Replace `TODO 2A: page title` (between `<title>` and `</title>`) by a title about Internet use.

**Check.** The title appears on the browser tab.

### 2B · The header

**Example** (another subject: adapt it, do not copy it as it is).

```html
<header>
  <h1>My local library</h1>
</header>
```

**Your turn.** Write your header under `TODO 2B`. A page has only **one** `h1`, its main title.

### 2C · The navigation

`nav` holds the menu. `ul` is a list and `li` one item. A link to `#books` jumps to the element with `id="books"` in the same page.

**Example** (another subject: adapt it, do not copy it as it is).

```html
<nav>
  <ul>
    <li><a href="#books">Books</a></li>
    <li><a href="#hours">Opening hours</a></li>
  </ul>
</nav>
```

**Your turn.** **Inside** your `header`, add three links to `#about`, `#figures` and `#search`.

**Check.** `2A`, `2B`, `2C` are `[OK]`. The links do nothing yet: their targets do not exist.

## Step 3 · Text, link and image (35 min)

### 3A · A section

**Example** (another subject: adapt it, do not copy it as it is).

```html
<section id="books">
  <h2>Our books</h2>
  <p>The library lends novels and comics.</p>
</section>
```

**Your turn.** Under `TODO 3A`, make a section with `id="about"`, an `h2` and one paragraph that says what your data measures. **Write 3B, 3C and 3D inside this section**, before `</section>`.

### 3B · A list

**Your turn.** Add a list (`ul` and `li`, as in 2C without links) with three items: the producer, the unit, how often the data is published.

### 3C · A link to another site

**Example** (another subject: adapt it, do not copy it as it is).

```html
<p><a href="https://www.toulouse.fr">Visit the city website</a></p>
```

**Your turn.** Link to the dataset. The text of the link must say where it goes (not "click here"). Address:

```text
https://ec.europa.eu/eurostat/databrowser/view/tin00028/default/table
```

### 3D · An image

`img` has no closing tag. `alt` describes the image for people who cannot see it.

**Example** (another subject: adapt it, do not copy it as it is).

```html
<img src="images/library.jpg" alt="Shelves full of books" width="320" height="180">
```

**Your turn.** Show `images/network.svg` with your own `alt` text.

**Check.** `3A` to `3D` are `[OK]`, the link opens Eurostat and you see the picture.

<details markdown="1"><summary>Stuck?</summary>

No picture? The path must be exactly `images/network.svg`. `[  ] 3B`? Your list must be before `</section>`.

</details>

## Step 4 · A table (40 min)

| Tag | Meaning |
|---|---|
| `table` | the table |
| `caption` | its title |
| `thead` / `tbody` | header part / data part |
| `tr` | one row |
| `th` / `td` | header cell / data cell |

**Example** (another subject: adapt it, do not copy it as it is).

```html
<section id="loans">
  <h2>Loans</h2>
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
</section>
```

### 4A · Section, table, caption

**Your turn.** Make a section with `id="figures"`, an `h2`, and a `table` with a `caption` naming the country and the years.

### 4B · Header row

**Your turn.** Add a `thead` with two `th` cells: year and share (%).

### 4C · Data rows

**Your turn.** Add a `tbody` with **at least 5 rows**. Take the figures of your country in `internet_use_clean.csv`. Write one row, check it in the browser, then copy it.

**Check.** `4A` to `4C` are `[OK]`. The table has no borders: CSS adds them in TD3.

## Step 5 · A form (35 min)

A **form** collects what the visitor types. `name` is the name under which the value is sent. A `label` is the text of a field: its `for` equals the field's `id`.

**Example** (another subject: adapt it, do not copy it as it is).

```html
<form action="#loans" method="get">
  <label for="genre">Genre</label>
  <select id="genre" name="genre">
    <option value="novel">Novel</option>
    <option value="comic">Comic</option>
  </select>

  <label for="age">Your age</label>
  <input id="age" name="age" type="number" min="3" max="110" required>

  <button type="submit">Send</button>
</form>
```

### 5A · Section and form

**Your turn.** Section with `id="search"`, an `h2`, and an empty `form` with `action="#search"` and `method="get"`. Write 5B to 5D inside the form.

### 5B · Countries

**Your turn.** A `label` and a `select` named `country` with at least three countries. The `value` is the code (`FR`), the text is the name.

### 5C · Year

**Your turn.** A `label` and a number field named `year`, with `min`, `max` and `required`.

### 5D · Button

**Your turn.** Add a `button` of type `submit`.

**Check.** Fill the form and click. The address bar shows `?country=…&year=…`. Nothing else happens: Flask will answer in week 6.

<details markdown="1"><summary>Stuck?</summary>

`[  ] 5B` or `5C`? Compare `for` on the label with `id` on the field: they must be identical. The field also needs `name`.

</details>

## Step 6 · Footer and validation (25 min)

### 6A · Footer

**Your turn.** Add a `footer` with a paragraph naming the source (Eurostat, tin00028).

### 6B · Validate

A **validator** looks for mistakes in your HTML. Open the [W3C validator](https://validator.w3.org/#validate_by_input), paste your whole file, click **Check**. Fix the **first** error, check again.

**Check.** Fifteen `[OK]` and no error in the validator.

## If you finish early (optional)

1. Add a second table for another country.
2. Add radio buttons and a checkbox to the form.
3. Add a second page and link the two.
