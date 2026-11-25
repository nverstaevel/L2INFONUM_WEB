title: Les balises HTML et leur résultat
---
Chaque balise du cours : à quoi elle sert, le code, et **ce que le navigateur affiche** sans CSS. Les exemples portent sur une bibliothèque. Référence complète : [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements) (en anglais).

## La page

### `html`, `head`, `body`

Le squelette de toute page. `head` contient les informations sur la page : `meta` (jeu de caractères), `title` (nom de l'onglet), `link` (feuille de style). `body` contient ce qui s'affiche.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>City library</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <p>Only the body is shown.</p>
</body>
</html>
```

### `header`, `nav`, `main`, `section`, `footer`

Balises **sémantiques** : elles disent ce qu'est chaque partie. Elles changent peu l'apparence.

```html
<header>
  <h1>City library</h1>
  <nav><a href="#books">Books</a></nav>
</header>
<main>
  <section id="books">
    <h2>Books</h2>
    <p>We lend novels.</p>
  </section>
</main>
<footer>Source: city library.</footer>
```

### `div`

Une boîte sans signification, pour regrouper des éléments (style ou JavaScript). Préférez une balise sémantique quand il y en a une.

```html
<div>
  <p>Two paragraphs</p>
  <p>in the same box.</p>
</div>
```

## Texte et listes

### `h1`, `h2`, `h3`, `p`

Les titres, par niveau, et les paragraphes. Un seul `h1` par page.

```html
<h1>City library</h1>
<h2>Books</h2>
<h3>Novels</h3>
<p>We lend novels for three weeks.</p>
```

### `strong`, `em`

`strong` marque ce qui est important (affiché en gras), `em` un mot sur lequel on insiste (italique). On les choisit pour le sens, pas pour l'apparence.

```html
<p><strong>Closed on Monday.</strong> Loans last <em>three</em> weeks.</p>
```

### `ul`, `ol`, `li`

Liste à puces (`ul`) ou numérotée (`ol`). Chaque élément est un `li`.

```html
<ul>
  <li>Novels</li>
  <li>Comics</li>
</ul>
<ol>
  <li>Choose a book</li>
  <li>Show your card</li>
</ol>
```

### `pre`

Texte affiché tel qu'écrit, avec ses espaces et retours à la ligne.

```html
<pre>Emma     1815
Dracula  1897</pre>
```

## Liens et images

### `a`

Un lien. `href` dit où il mène : un autre site, un autre fichier, ou `#id` dans la même page. Le texte doit dire où l'on va.

```html
<p><a href="https://www.toulouse.fr">The city of Toulouse</a> ·
<a href="about.html">About us</a></p>
```

### `img`

Une image. Pas de balise fermante. `src` est le chemin du fichier, `alt` le texte lu quand on ne voit pas l'image. `width` et `height` réservent sa place pendant le chargement.

```html
<img src="images/library.jpg" alt="Three shelves of books" width="320" height="180">
```

### `figure`, `figcaption`

Une image (ou un tableau, un graphique) avec sa légende. La légende est le bon endroit pour le **crédit** : auteur, licence et source.

```html
<figure>
  <img src="images/library.jpg" alt="Three shelves of books" width="320" height="180">
  <figcaption>Our shelves. Drawing: course team.</figcaption>
</figure>
```

## Tableaux

### `table`, `caption`, `thead`, `tbody`, `tr`, `th`, `td`

`caption` est le titre, `tr` une ligne, `th` une cellule d'en-tête, `td` une cellule de données. Le navigateur ne trace pas de bordure : c'est le rôle du CSS.

```html
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
```

## Formulaires

### `form`, `label`, `input`, `button`

Un **formulaire** envoie la saisie du visiteur. `name` est la clé envoyée ; `label for` désigne l'`id` du champ.

```html
<form action="/search" method="get">
  <label for="author">Author</label>
  <input id="author" name="author">
  <label for="year">Year</label>
  <input id="year" name="year" type="number">
  <button type="submit">Search</button>
</form>
```

### `select`, `option`

Une liste déroulante. `value` est ce qui est envoyé, le texte entre les balises ce qui est affiché.

```html
<label for="genre">Genre</label>
<select id="genre" name="genre">
  <option value="novel">Novel</option>
  <option value="comic">Comic</option>
</select>
```

### `input type="radio"`, `input type="checkbox"`

Boutons radio : un seul choix parmi ceux de même `name`. Case à cocher : oui ou non.

```html
<label><input type="radio" name="lang" value="fr" checked> French</label>
<label><input type="radio" name="lang" value="en"> English</label>
<label><input type="checkbox" name="new"> New books only</label>
```

## Pour JavaScript (CM4)

### `script`, `canvas`

`script` charge ou contient du JavaScript. `canvas` est une zone de dessin vide : Chart.js y trace le graphique. Pas d'aperçu ici.

```html
<canvas id="chart"></canvas>
<script src="chart.js"></script>
```

- [Toutes les notions](notions.html)
