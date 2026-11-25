title: CSS et ses résultats
---
Le CSS utilisé dans ce cours, à chaque fois avec **ce qu'affiche le navigateur**. Liez votre feuille de style dans le `head` de la page :

```text
<link rel="stylesheet" href="style.css">
```

Voir aussi la [référence sur MDN](https://developer.mozilla.org/en-US/docs/Web/CSS) (en anglais).

## Choisir quoi habiller (sélecteurs)

### élément

Le nom d'une balise habille tous les éléments de ce type.

```css
p { color: darkred; }
```

```html
<h3>A title</h3>
<p>First paragraph.</p>
<p>Second paragraph.</p>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;p { color: darkred; }&#10;&lt;/style&gt;&#10;&lt;h3&gt;A title&lt;/h3&gt;&#10;&lt;p&gt;First paragraph.&lt;/p&gt;&#10;&lt;p&gt;Second paragraph.&lt;/p&gt;"></iframe></div>

### classe : `.nom`

Tous les éléments qui ont `class="nom"`.

```css
.note { background: gold; }
```

```html
<p class="note">With the class.</p>
<p>Without.</p>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.note { background: gold; }&#10;&lt;/style&gt;&#10;&lt;p class=&quot;note&quot;&gt;With the class.&lt;/p&gt;&#10;&lt;p&gt;Without.&lt;/p&gt;"></iframe></div>

### identifiant : `#nom`

Le seul élément qui a `id="nom"`.

```css
#source { color: grey; }
```

```html
<p>Loans of 2025.</p>
<p id="source">Source: city library.</p>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;#source { color: grey; }&#10;&lt;/style&gt;&#10;&lt;p&gt;Loans of 2025.&lt;/p&gt;&#10;&lt;p id=&quot;source&quot;&gt;Source: city library.&lt;/p&gt;"></iframe></div>

### à l'intérieur : `nav a`

Seulement les liens placés dans `nav`.

```css
nav a { color: green; }
```

```html
<nav><a href="#">In the menu</a></nav>
<p><a href="#">In a paragraph</a></p>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;nav a { color: green; }&#10;&lt;/style&gt;&#10;&lt;nav&gt;&lt;a href=&quot;#&quot;&gt;In the menu&lt;/a&gt;&lt;/nav&gt;&#10;&lt;p&gt;&lt;a href=&quot;#&quot;&gt;In a paragraph&lt;/a&gt;&lt;/p&gt;"></iframe></div>

### état : `:hover`, `:focus`

Quand la souris est dessus, ou atteint avec la touche Tab. Passez la souris sur le lien.

```css
a:hover, a:focus { background: gold; }
```

```html
<p><a href="#">Move the mouse here</a></p>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;a:hover, a:focus { background: gold; }&#10;&lt;/style&gt;&#10;&lt;p&gt;&lt;a href=&quot;#&quot;&gt;Move the mouse here&lt;/a&gt;&lt;/p&gt;"></iframe></div>

### quelle règle gagne ?

**Spécificité** : id l'emporte sur classe, classe sur élément. À égalité, la dernière règle gagne.

```css
#a    { color: orange; }
.note { color: green; }
p     { color: red; }
p     { color: blue; }
```

```html
<p id="a" class="note">id + class + element</p>
<p class="note">class + element</p>
<p>element only</p>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;#a    { color: orange; }&#10;.note { color: green; }&#10;p     { color: red; }&#10;p     { color: blue; }&#10;&lt;/style&gt;&#10;&lt;p id=&quot;a&quot; class=&quot;note&quot;&gt;id + class + element&lt;/p&gt;&#10;&lt;p class=&quot;note&quot;&gt;class + element&lt;/p&gt;&#10;&lt;p&gt;element only&lt;/p&gt;"></iframe></div>

## Couleurs et texte

### `color`, `background`

Couleur du texte et du fond, par son nom ou son code `#rrggbb`.

```css
p { color: #ffffff; background: #14213d; padding: 8px; }
```

```html
<p>White on dark blue.</p>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;p { color: #ffffff; background: #14213d; padding: 8px; }&#10;&lt;/style&gt;&#10;&lt;p&gt;White on dark blue.&lt;/p&gt;"></iframe></div>

### `font-family`, `line-height`

La police (prévoir un remplacement) et l'interligne.

```css
.a { font-family: Arial, sans-serif; }
.b { font-family: Georgia, serif; line-height: 2; }
```

```html
<p class="a">Arial</p>
<p class="b">Georgia,<br>with more space between lines.</p>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.a { font-family: Arial, sans-serif; }&#10;.b { font-family: Georgia, serif; line-height: 2; }&#10;&lt;/style&gt;&#10;&lt;p class=&quot;a&quot;&gt;Arial&lt;/p&gt;&#10;&lt;p class=&quot;b&quot;&gt;Georgia,&lt;br&gt;with more space between lines.&lt;/p&gt;"></iframe></div>

### `text-align`

Aligner le texte à gauche, au centre ou à droite.

```css
h3 { text-align: center; }
p  { text-align: right; }
```

```html
<h3>Centred</h3>
<p>Right</p>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;h3 { text-align: center; }&#10;p  { text-align: right; }&#10;&lt;/style&gt;&#10;&lt;h3&gt;Centred&lt;/h3&gt;&#10;&lt;p&gt;Right&lt;/p&gt;"></iframe></div>

## Le modèle de boîte

### `padding`, `border`, `margin`

**padding** : espace intérieur ; **border** : le trait autour ; **margin** : espace extérieur.

```css
p { padding: 20px; border: 4px solid darkred; margin: 30px; background: #fde; }
```

```html
<p>One box</p>
<p>Another box</p>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;p { padding: 20px; border: 4px solid darkred; margin: 30px; background: #fde; }&#10;&lt;/style&gt;&#10;&lt;p&gt;One box&lt;/p&gt;&#10;&lt;p&gt;Another box&lt;/p&gt;"></iframe></div>

### `width` et `box-sizing`

Par défaut `width` ne compte que le contenu : la première boîte fait 200 + 2×20 + 2×5 = 250px. Avec `border-box`, les 200px comprennent tout.

```css
p  { width: 200px; padding: 20px; border: 5px solid; }
.b { box-sizing: border-box; }
```

```html
<p>content-box: 250px</p>
<p class="b">border-box: 200px</p>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;p  { width: 200px; padding: 20px; border: 5px solid; }&#10;.b { box-sizing: border-box; }&#10;&lt;/style&gt;&#10;&lt;p&gt;content-box: 250px&lt;/p&gt;&#10;&lt;p class=&quot;b&quot;&gt;border-box: 200px&lt;/p&gt;"></iframe></div>

### `max-width` et `margin: 0 auto`

Jamais plus large qu'une valeur, et centré.

```css
main { max-width: 300px; margin: 0 auto; background: #eef2f7; padding: 8px; }
```

```html
<main>A centred column.</main>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;main { max-width: 300px; margin: 0 auto; background: #eef2f7; padding: 8px; }&#10;&lt;/style&gt;&#10;&lt;main&gt;A centred column.&lt;/main&gt;"></iframe></div>

### images qui s'adaptent

Une image ne dépasse jamais de sa boîte.

```css
div { width: 160px; border: 2px dashed grey; }
img { max-width: 100%; height: auto; }
```

```html
<div><img alt="A wide rectangle" src="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='600' height='200'><rect width='600' height='200' fill='teal'/></svg>"></div>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;div { width: 160px; border: 2px dashed grey; }&#10;img { max-width: 100%; height: auto; }&#10;&lt;/style&gt;&#10;&lt;div&gt;&lt;img alt=&quot;A wide rectangle&quot; src=&quot;data:image/svg+xml,&lt;svg xmlns=&#x27;http://www.w3.org/2000/svg&#x27; width=&#x27;600&#x27; height=&#x27;200&#x27;&gt;&lt;rect width=&#x27;600&#x27; height=&#x27;200&#x27; fill=&#x27;teal&#x27;/&gt;&lt;/svg&gt;&quot;&gt;&lt;/div&gt;"></iframe></div>

## Listes et tableaux

### `list-style`

Retirer les puces, pour un menu.

```css
ul { list-style: none; padding: 0; }
```

```html
<ul>
  <li>Home</li>
  <li>Books</li>
  <li>Contact</li>
</ul>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;ul { list-style: none; padding: 0; }&#10;&lt;/style&gt;&#10;&lt;ul&gt;&#10;  &lt;li&gt;Home&lt;/li&gt;&#10;  &lt;li&gt;Books&lt;/li&gt;&#10;  &lt;li&gt;Contact&lt;/li&gt;&#10;&lt;/ul&gt;"></iframe></div>

### `border-collapse`

Un seul trait entre les cellules au lieu de deux.

```css
table { width: 100%; border-collapse: collapse; }
th, td { border: 1px solid grey; padding: 6px; text-align: left; }
th { background: #eef2f7; }
```

```html
<table>
  <tr><th>Title</th><th>Loans</th></tr>
  <tr><td>Emma</td><td>12</td></tr>
</table>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;table { width: 100%; border-collapse: collapse; }&#10;th, td { border: 1px solid grey; padding: 6px; text-align: left; }&#10;th { background: #eef2f7; }&#10;&lt;/style&gt;&#10;&lt;table&gt;&#10;  &lt;tr&gt;&lt;th&gt;Title&lt;/th&gt;&lt;th&gt;Loans&lt;/th&gt;&lt;/tr&gt;&#10;  &lt;tr&gt;&lt;td&gt;Emma&lt;/td&gt;&lt;td&gt;12&lt;/td&gt;&lt;/tr&gt;&#10;&lt;/table&gt;"></iframe></div>

## Mise en page avec Flexbox

### `display: flex` et `gap`

Mettre les enfants d'un élément en ligne, avec un espace entre eux.

```css
.row div { border: 2px solid; padding: 4px 12px; }
.row { display: flex; gap: 1rem; }
```

```html
<div class="row">
  <div>One</div>
  <div>Two</div>
  <div>Three</div>
</div>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.row div { border: 2px solid; padding: 4px 12px; }&#10;.row { display: flex; gap: 1rem; }&#10;&lt;/style&gt;&#10;&lt;div class=&quot;row&quot;&gt;&#10;  &lt;div&gt;One&lt;/div&gt;&#10;  &lt;div&gt;Two&lt;/div&gt;&#10;  &lt;div&gt;Three&lt;/div&gt;&#10;&lt;/div&gt;"></iframe></div>

### `justify-content`

Répartir l'espace libre dans le sens de la ligne.

```css
.row div { border: 2px solid; padding: 4px 12px; }
.row { display: flex; justify-content: space-between; }
```

```html
<div class="row">
  <div>One</div>
  <div>Two</div>
  <div>Three</div>
</div>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.row div { border: 2px solid; padding: 4px 12px; }&#10;.row { display: flex; justify-content: space-between; }&#10;&lt;/style&gt;&#10;&lt;div class=&quot;row&quot;&gt;&#10;  &lt;div&gt;One&lt;/div&gt;&#10;  &lt;div&gt;Two&lt;/div&gt;&#10;  &lt;div&gt;Three&lt;/div&gt;&#10;&lt;/div&gt;"></iframe></div>

### `align-items`

Placer les éléments dans l'autre sens.

```css
.row div { border: 2px solid; padding: 4px 12px; }
.row { display: flex; gap: 1rem; height: 90px; align-items: center; background: #eef2f7; }
```

```html
<div class="row">
  <div>One</div>
  <div>Two</div>
  <div>Three</div>
</div>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.row div { border: 2px solid; padding: 4px 12px; }&#10;.row { display: flex; gap: 1rem; height: 90px; align-items: center; background: #eef2f7; }&#10;&lt;/style&gt;&#10;&lt;div class=&quot;row&quot;&gt;&#10;  &lt;div&gt;One&lt;/div&gt;&#10;  &lt;div&gt;Two&lt;/div&gt;&#10;  &lt;div&gt;Three&lt;/div&gt;&#10;&lt;/div&gt;"></iframe></div>

### `flex-direction: column`

Les uns sous les autres.

```css
.row div { border: 2px solid; padding: 4px 12px; }
.row { display: flex; flex-direction: column; gap: 4px; }
```

```html
<div class="row">
  <div>One</div>
  <div>Two</div>
  <div>Three</div>
</div>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.row div { border: 2px solid; padding: 4px 12px; }&#10;.row { display: flex; flex-direction: column; gap: 4px; }&#10;&lt;/style&gt;&#10;&lt;div class=&quot;row&quot;&gt;&#10;  &lt;div&gt;One&lt;/div&gt;&#10;  &lt;div&gt;Two&lt;/div&gt;&#10;  &lt;div&gt;Three&lt;/div&gt;&#10;&lt;/div&gt;"></iframe></div>

### `flex-wrap`

Passer à la ligne quand la place manque.

```css
.row div { border: 2px solid; padding: 4px 12px; }
.row { display: flex; flex-wrap: wrap; gap: 8px; width: 160px; border: 2px dashed grey; }
```

```html
<div class="row">
  <div>One</div>
  <div>Two</div>
  <div>Three</div>
</div>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.row div { border: 2px solid; padding: 4px 12px; }&#10;.row { display: flex; flex-wrap: wrap; gap: 8px; width: 160px; border: 2px dashed grey; }&#10;&lt;/style&gt;&#10;&lt;div class=&quot;row&quot;&gt;&#10;  &lt;div&gt;One&lt;/div&gt;&#10;  &lt;div&gt;Two&lt;/div&gt;&#10;  &lt;div&gt;Three&lt;/div&gt;&#10;&lt;/div&gt;"></iframe></div>

## Écrans de tailles différentes

### `@media`

Des règles réservées aux écrans étroits. Placez-les à la **fin** du fichier. Sur une vraie page, ajoutez aussi la ligne `viewport` dans le `head`.

```css
.row div { border: 2px solid; padding: 4px 12px; }
.row { display: flex; gap: 1rem; }
@media (max-width: 600px) {
  .row { flex-direction: column; }
}
```

```html
<div class="row">
  <div>One</div>
  <div>Two</div>
  <div>Three</div>
</div>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · pleine largeur (plus de 600px sur ordinateur)</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.row div { border: 2px solid; padding: 4px 12px; }&#10;.row { display: flex; gap: 1rem; }&#10;@media (max-width: 600px) {&#10;  .row { flex-direction: column; }&#10;}&#10;&lt;/style&gt;&#10;&lt;div class=&quot;row&quot;&gt;&#10;  &lt;div&gt;One&lt;/div&gt;&#10;  &lt;div&gt;Two&lt;/div&gt;&#10;  &lt;div&gt;Three&lt;/div&gt;&#10;&lt;/div&gt;"></iframe></div>

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · 320px de large, comme un téléphone</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;.row div { border: 2px solid; padding: 4px 12px; }&#10;.row { display: flex; gap: 1rem; }&#10;@media (max-width: 600px) {&#10;  .row { flex-direction: column; }&#10;}&#10;&lt;/style&gt;&#10;&lt;div class=&quot;row&quot;&gt;&#10;  &lt;div&gt;One&lt;/div&gt;&#10;  &lt;div&gt;Two&lt;/div&gt;&#10;  &lt;div&gt;Three&lt;/div&gt;&#10;&lt;/div&gt;" style="width:320px;max-width:100%"></iframe></div>

## Quand ça ne marche pas

**Rien ne change ?** Ouvrez les outils de développement (F12), choisissez l'élément : une ligne barrée est remplacée ou incomprise.

### un `;` oublié

Les deux lignes sont perdues. CSS n'affiche **aucun message d'erreur**.

```css
p {
  color: red
  background: gold;
}
```

```html
<p>Neither red nor gold.</p>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;p {&#10;  color: red&#10;  background: gold;&#10;}&#10;&lt;/style&gt;&#10;&lt;p&gt;Neither red nor gold.&lt;/p&gt;"></iframe></div>

### un nombre sans unité

`padding: 20` est ignoré : écrivez `20px`.

```css
p { padding: 20; background: gold; }
```

```html
<p>No inner space.</p>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;p { padding: 20; background: gold; }&#10;&lt;/style&gt;&#10;&lt;p&gt;No inner space.&lt;/p&gt;"></iframe></div>

### classe sans le point

`note` désigne une balise nommée note ; une classe s'écrit `.note`.

```css
note { color: red; }
```

```html
<p class="note">Still not red.</p>
```

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;note { color: red; }&#10;&lt;/style&gt;&#10;&lt;p class=&quot;note&quot;&gt;Still not red.&lt;/p&gt;"></iframe></div>

- [Toutes les notions](notions.html)
