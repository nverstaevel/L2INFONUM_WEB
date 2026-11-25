title: JavaScript et ses résultats
---
Le JavaScript utilisé dans ce cours, à chaque fois avec **son résultat**. Placez votre script à la **fin** du `body` ; ouvrez la **console** avec F12 pour voir messages et erreurs.

```text
<script src="page.js"></script>
</body>
```

Votre navigateur peut afficher un peu différemment les tableaux et les objets. Voir aussi la [référence sur MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript) (en anglais).

## Valeurs et tests

### `const`, `let`, `console.log`

`const` pour une variable qu'on ne réaffecte pas, `let` pour une variable qui change. `console.log` est le `print` de JavaScript.

```javascript
const city = "Toulouse";
let people = 500000;
people = people + 1;
console.log(city, people);
```

**Dans la console**

```text
Toulouse 500001
```

### textes et nombres

`+` colle des textes. Un texte doit être converti avant de calculer.

```javascript
console.log("Year " + 2025);
console.log("2025" + 1);
console.log(Number("2025") + 1);
```

**Dans la console**

```text
Year 2025
20251
2026
```

### `if`, `else`, `===`

Le test entre parenthèses, le bloc entre accolades. On compare avec `===`.

```javascript
const pages = 400;
if (pages > 500) {
  console.log("long");
} else {
  console.log("short");
}
console.log(pages === 400);
```

**Dans la console**

```text
short
true
```

## Listes, objets et fonctions

### tableaux

Une liste. Les positions commencent à 0.

```javascript
const months = ["Jan", "Feb"];
console.log(months.length, months[0]);
console.log(months);
```

**Dans la console**

```text
2 Jan
["Jan","Feb"]
```

### objets

Des valeurs nommées, comme un dictionnaire Python. Un nom absent donne `undefined`, sans erreur.

```javascript
const book = { title: "Emma", pages: 400 };
console.log(book.title);
console.log(book.author);
```

**Dans la console**

```text
Emma
undefined
```

### fonctions

`function` avec un nom, ou une flèche `=>` pour une courte.

```javascript
function double(x) {
  return 2 * x;
}
const triple = x => 3 * x;
console.log(double(5), triple(5));
```

**Dans la console**

```text
10 15
```

### `map`

Construire un nouveau tableau, comme une liste en compréhension. C'est ainsi qu'on prépare les données d'un graphique.

```javascript
const books = [{ title: "Emma", pages: 400 }, { title: "Dune", pages: 600 }];
console.log(books.map(b => b.title));
console.log(books.map(b => b.pages));
```

**Dans la console**

```text
["Emma","Dune"]
[400,600]
```

### `encodeURIComponent`

Rendre un texte saisi utilisable dans une adresse.

```javascript
console.log("/api/data?country=" + encodeURIComponent("F R&x"));
```

**Dans la console**

```text
/api/data?country=F%20R%26x
```

## Demander des données : `fetch`

Ici `books.json` contient :

```json
[{"title": "Emma"}, {"title": "Dune"}]
```

`fetch` a besoin d'un serveur (`python -m http.server` ou Flask) : il ne marche pas sur une page ouverte par double-clic.

### demander un fichier JSON

La réponse arrive plus tard : la ligne placée après `fetch` s'affiche **en premier**.

```javascript
fetch("books.json")
  .then(response => response.json())
  .then(books => {
    console.log("received", books.length, "books");
  });
console.log("this line comes first");
```

**Dans la console**

```text
this line comes first
received 2 books
```

### tester la réponse

Une mauvaise adresse n'arrête pas `fetch` : testez `response.ok` ou le contenu.

```javascript
fetch("bokos.json")
  .then(response => {
    console.log(response.status, response.ok);
  });
```

**Dans la console**

```text
404 false
```

## Modifier la page

### changer un texte

`getElementById` trouve l'élément, `textContent` remplace son texte (le HTML n'est pas interprété).

```html
<p id="message">Old text</p>
```

```javascript
document.getElementById("message").textContent = "New text <b>";
```

<div class="preview"><p><strong>Résultat en direct : le code s'exécute vraiment</strong></p><iframe sandbox="allow-scripts" title="Résultat en direct : le code s'exécute vraiment" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;p id=&quot;message&quot;&gt;Old text&lt;/p&gt;&#10;&#10;&lt;script&gt;&#10;document.getElementById(&quot;message&quot;).textContent = &quot;New text &lt;b&gt;&quot;;&#10;&lt;/script&gt;" style="height:60px"></iframe></div>

### réagir à un clic

`addEventListener` exécute une fonction à chaque clic. Essayez le bouton.

```html
<button id="add" type="button">Add a book</button>
<p id="count">0 book</p>
```

```javascript
let total = 0;
document.getElementById("add").addEventListener("click", () => {
  total = total + 1;
  document.getElementById("count").textContent = total + " book(s)";
});
```

<div class="preview"><p><strong>Résultat en direct : le code s'exécute vraiment</strong></p><iframe sandbox="allow-scripts" title="Résultat en direct : le code s'exécute vraiment" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;button id=&quot;add&quot; type=&quot;button&quot;&gt;Add a book&lt;/button&gt;&#10;&lt;p id=&quot;count&quot;&gt;0 book&lt;/p&gt;&#10;&#10;&lt;script&gt;&#10;let total = 0;&#10;document.getElementById(&quot;add&quot;).addEventListener(&quot;click&quot;, () =&gt; {&#10;  total = total + 1;&#10;  document.getElementById(&quot;count&quot;).textContent = total + &quot; book(s)&quot;;&#10;});&#10;&lt;/script&gt;" style="height:100px"></iframe></div>

### lire un champ

`value` est ce que le visiteur a saisi (toujours un texte).

```html
<label for="name">Name</label> <input id="name" value="Ada">
<button id="go" type="button">Greet</button>
<p id="out"></p>
```

```javascript
document.getElementById("go").addEventListener("click", () => {
  const name = document.getElementById("name").value;
  document.getElementById("out").textContent = "Hello " + name;
});
```

<div class="preview"><p><strong>Résultat en direct : le code s'exécute vraiment</strong></p><iframe sandbox="allow-scripts" title="Résultat en direct : le code s'exécute vraiment" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;label for=&quot;name&quot;&gt;Name&lt;/label&gt; &lt;input id=&quot;name&quot; value=&quot;Ada&quot;&gt;&#10;&lt;button id=&quot;go&quot; type=&quot;button&quot;&gt;Greet&lt;/button&gt;&#10;&lt;p id=&quot;out&quot;&gt;&lt;/p&gt;&#10;&#10;&lt;script&gt;&#10;document.getElementById(&quot;go&quot;).addEventListener(&quot;click&quot;, () =&gt; {&#10;  const name = document.getElementById(&quot;name&quot;).value;&#10;  document.getElementById(&quot;out&quot;).textContent = &quot;Hello &quot; + name;&#10;});&#10;&lt;/script&gt;" style="height:110px"></iframe></div>

## Graphiques avec Chart.js

Chargez la bibliothèque **avant** votre script. Les graphiques ci-dessous demandent une connexion internet.

```text
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.6.2/dist/chart.umd.min.js"></script>
<script src="chart.js"></script>
```

```html
<div style="max-width:30rem">
  <canvas id="chart" role="img" aria-label="Books lent per month"></canvas>
</div>
```

### barres

Pour comparer. `labels` et `data` ont la même longueur.

```javascript
new Chart(document.getElementById("chart"), {
  type: "bar",
  data: {
    labels: ["Jan", "Feb", "Mar"],
    datasets: [{ label: "Books lent", data: [120, 95, 140] }]
  }
});
```

<div class="preview"><p><strong>Résultat en direct : le code s'exécute vraiment</strong></p><iframe sandbox="allow-scripts" title="Résultat en direct : le code s'exécute vraiment" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;div style=&quot;max-width:30rem&quot;&gt;&#10;  &lt;canvas id=&quot;chart&quot; role=&quot;img&quot; aria-label=&quot;Books lent per month&quot;&gt;&lt;/canvas&gt;&#10;&lt;/div&gt;&#10;&lt;script src=&quot;https://cdn.jsdelivr.net/npm/chart.js@4.6.2/dist/chart.umd.min.js&quot;&gt;&lt;/script&gt;&#10;&lt;script&gt;&#10;new Chart(document.getElementById(&quot;chart&quot;), {&#10;  type: &quot;bar&quot;,&#10;  data: {&#10;    labels: [&quot;Jan&quot;, &quot;Feb&quot;, &quot;Mar&quot;],&#10;    datasets: [{ label: &quot;Books lent&quot;, data: [120, 95, 140] }]&#10;  }&#10;});&#10;&lt;/script&gt;" style="height:270px"></iframe></div>

### courbe

Pour montrer une évolution.

```javascript
new Chart(document.getElementById("chart"), {
  type: "line",
  data: {
    labels: ["Jan", "Feb", "Mar"],
    datasets: [{ label: "Books lent", data: [120, 95, 140] }]
  }
});
```

<div class="preview"><p><strong>Résultat en direct : le code s'exécute vraiment</strong></p><iframe sandbox="allow-scripts" title="Résultat en direct : le code s'exécute vraiment" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;div style=&quot;max-width:30rem&quot;&gt;&#10;  &lt;canvas id=&quot;chart&quot; role=&quot;img&quot; aria-label=&quot;Books lent per month&quot;&gt;&lt;/canvas&gt;&#10;&lt;/div&gt;&#10;&lt;script src=&quot;https://cdn.jsdelivr.net/npm/chart.js@4.6.2/dist/chart.umd.min.js&quot;&gt;&lt;/script&gt;&#10;&lt;script&gt;&#10;new Chart(document.getElementById(&quot;chart&quot;), {&#10;  type: &quot;line&quot;,&#10;  data: {&#10;    labels: [&quot;Jan&quot;, &quot;Feb&quot;, &quot;Mar&quot;],&#10;    datasets: [{ label: &quot;Books lent&quot;, data: [120, 95, 140] }]&#10;  }&#10;});&#10;&lt;/script&gt;" style="height:270px"></iframe></div>

### l'axe vertical : `options`

Partir de 0 pour des barres honnêtes. Notez la virgule avant `options`.

```javascript
new Chart(document.getElementById("chart"), {
  type: "bar",
  data: {
    labels: ["Jan", "Feb", "Mar"],
    datasets: [{ label: "Books lent", data: [120, 95, 140] }]
  },
  options: { scales: { y: { min: 0, max: 200 } } }
});
```

<div class="preview"><p><strong>Résultat en direct : le code s'exécute vraiment</strong></p><iframe sandbox="allow-scripts" title="Résultat en direct : le code s'exécute vraiment" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;div style=&quot;max-width:30rem&quot;&gt;&#10;  &lt;canvas id=&quot;chart&quot; role=&quot;img&quot; aria-label=&quot;Books lent per month&quot;&gt;&lt;/canvas&gt;&#10;&lt;/div&gt;&#10;&lt;script src=&quot;https://cdn.jsdelivr.net/npm/chart.js@4.6.2/dist/chart.umd.min.js&quot;&gt;&lt;/script&gt;&#10;&lt;script&gt;&#10;new Chart(document.getElementById(&quot;chart&quot;), {&#10;  type: &quot;bar&quot;,&#10;  data: {&#10;    labels: [&quot;Jan&quot;, &quot;Feb&quot;, &quot;Mar&quot;],&#10;    datasets: [{ label: &quot;Books lent&quot;, data: [120, 95, 140] }]&#10;  },&#10;  options: { scales: { y: { min: 0, max: 200 } } }&#10;});&#10;&lt;/script&gt;" style="height:270px"></iframe></div>

### `destroy`

Un canvas ne porte qu'un graphique. Avant de redessiner, supprimez le précédent.

```javascript
let chart = null;
// each time you draw:
if (chart) {
  chart.destroy();
}
chart = new Chart(canvas, settings);
```

## Lire un message d'erreur

Les erreurs apparaissent en rouge dans la console, avec le fichier et la ligne à droite. Messages obtenus avec Chrome (les autres navigateurs les formulent autrement).

### `ReferenceError`

Un nom qui n'existe pas : orthographe.

```javascript
const title = "Emma";
console.log(titel);
```

```text
Uncaught ReferenceError: titel is not defined
```

### `TypeError`: null

L'élément est introuvable : vérifiez l'`id`, et placez `<script>` à la fin du `body`.

```html
<p id="message"></p>
```

```javascript
document.getElementById("mesage").textContent = "Hello";
```

```text
Uncaught TypeError: Cannot set properties of null (setting 'textContent')
```

### `TypeError`: const

Un `const` ne reçoit pas de nouvelle valeur : utilisez `let`.

```javascript
const total = 0;
total = total + 1;
```

```text
Uncaught TypeError: Assignment to constant variable.
```

### `SyntaxError`

Une faute d'écriture : parenthèse, accolade, virgule ou guillemet.

```javascript
console.log("Emma";
```

```text
Uncaught SyntaxError: missing ) after argument list
```

- [Toutes les notions](notions.html)
