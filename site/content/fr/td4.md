title: TD4 · Visualisation avec Chart.js
---
**Vendredi 29 janvier 2027 · 3 heures.** Fichiers de départ : dossier [`td4`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td4).

## Objectif

Transformer les résultats du TD1 en graphique avec quelques lignes de JavaScript (le langage de programmation des pages web). Le code fonctionne déjà : vous l'**adaptez**.

**Vous avez réussi si** : un graphique de votre pays, avec titre et source, et cinq `[OK]`.

| Étape | Vous faites | Durée |
|---|---|---|
| 1 | Lancer un serveur local | 25 min |
| 2 | Essayer JavaScript | 35 min |
| 3 | Utiliser vos données | 25 min |
| 4 | Adapter le graphique | 55 min |
| 5 | Le lire avec esprit critique | 20 min |

## Notions mobilisées dans ce TD

Ouvrez-les quand vous en avez besoin : chacune est une page courte. Les liens sont rappelés à l'étape concernée.

- [Serveur local](notion-local-server.html)
- [Bases de JavaScript](notion-javascript.html)
- [Outils de développement](notion-devtools.html)
- [fetch : demander des données](notion-fetch.html)
- [JSON](notion-json.html)
- [Graphiques avec Chart.js](notion-chartjs.html)
- [Modifier la page en JavaScript](notion-dom.html)
- [Choisir et lire un graphique](notion-honest-charts.html)

**Exemples clés en main :** [Un graphique à partir d'un fichier JSON](recipe-chart-from-json.html)

## Avant la séance

- [ ] J'ai relu le [CM4](cm4.html).
- [ ] J'ai mon `summary.json` du TD1 (un exemple est fourni).

## Comment travailler

1. Faites les étapes **dans l'ordre**.
2. Écrivez uniquement là où vous voyez `TODO`. Son numéro est celui de ce sujet.
3. Après chaque partie, **enregistrez** (`Ctrl+S`, ou `Cmd+S` sur Mac) et lancez le vérificateur dans un terminal (**Terminal → New Terminal** dans VS Code) :

```text
python check.py
```

Sur macOS ou Linux, hors environnement virtuel, tapez `python3`. `[OK]` : la partie fonctionne ; `[  ]` : pas encore. Le vérificateur ne remplace pas un coup d'œil à votre page dans le navigateur.

## Étape 1 · Lancer un serveur local (25 min)

<p class="refs" markdown="1">**Notion :** [Serveur local](notion-local-server.html)</p>

Une page ouverte par double-clic n'a pas le droit de lire d'autres fichiers. Un **serveur** est un programme qui envoie des fichiers au navigateur. Python en a un petit.

Ouvrez le dossier `td4` dans VS Code, ouvrez un terminal et lancez (`python3` sur macOS ou Linux) :

```text
python -m http.server
```

Laissez ce terminal ouvert. Dans le navigateur, allez sur `http://localhost:8000/chart.html` (`localhost` signifie « cet ordinateur »).

**Vérification.** Vous voyez une courbe. Pour lancer `check.py`, ouvrez un **second** terminal.

<details markdown="1"><summary>Bloqué ?</summary>

`Address already in use` : lancez `python -m http.server 8001` et utilisez `localhost:8001`. Erreur 404 : le serveur n'a pas été lancé dans le dossier `td4`. On l'arrête avec `Ctrl+C`.

</details>

## Étape 2 · Essayer JavaScript (35 min)

<p class="refs" markdown="1">**Notion :** [Bases de JavaScript](notion-javascript.html), [Outils de développement](notion-devtools.html)</p>

La **console** permet de taper du JavaScript : `F12`, onglet **Console**. Tapez chaque bloc, validez, et **devinez le résultat avant**.

### 2A · Variables

```javascript
const city = "Toulouse";    // const: cannot be changed
let people = 500000;        // let: can be changed
people = people + 1;
console.log(city, people);  // like print()
```

### 2B · Tableaux et objets

Un **tableau** ressemble à une liste Python. Un **objet** ressemble à un dictionnaire, lu avec un point.

```javascript
const months = ["Jan", "Feb"];
console.log(months.length, months[0]);

const book = { title: "Emma", pages: 400 };
console.log(book.title);
```

### 2C · map

`map` construit un nouveau tableau en transformant chaque élément. `x => x.pages` signifie « pour chaque x, prendre x.pages ».

```javascript
const books = [{ title: "Emma", pages: 400 }, { title: "Dune", pages: 600 }];
console.log(books.map(b => b.pages));    // Python: [b["pages"] for b in books]
```

**Vérification.** Écrivez la ligne qui donne les deux titres. Montrez-la à votre voisin.

<details markdown="1"><summary>Bloqué ?</summary>

La même ligne que ci-dessus, avec `b.title`.

</details>

## Étape 3 · Utiliser vos données (25 min)

<p class="refs" markdown="1">**Notion :** [fetch : demander des données](notion-fetch.html), [JSON](notion-json.html) · **Recette :** [Un graphique à partir d'un fichier JSON](recipe-chart-from-json.html)</p>

**À vous.** Copiez **votre** `summary.json` (créé au TD1, dossier `td1/data`) à la place de `td4/data/summary.json`. Rechargez avec `Ctrl+F5` (`Cmd+Shift+R` sur Mac). Puis lisez `chart.js` et ses commentaires, ligne par ligne.

**Vérification.** `3` est `[OK]`. Dans l'onglet **Réseau** (`F12`), rechargez : `summary.json` a le code 200.

## Étape 4 · Adapter le graphique (55 min)

<p class="refs" markdown="1">**Notion :** [Graphiques avec Chart.js](notion-chartjs.html) · **Recette :** [Un graphique à partir d'un fichier JSON](recipe-chart-from-json.html)</p>

Changez une chose, enregistrez, rechargez, regardez. Si le graphique disparaît, lisez le message rouge dans la console.

### 4A · Des barres

**À vous.** Changez le type de graphique de `line` à `bar`.

### 4B · Un titre avec le pays

<p class="refs" markdown="1">**Notion :** [Modifier la page en JavaScript](notion-dom.html)</p>

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```javascript
document.getElementById("shop-name").textContent = "Shop of " + data.city;
// finds the element with id="shop-name" and replaces its text
```

**À vous.** Le titre de `chart.html` a `id="title"`. Sous `TODO 4B`, écrivez un titre qui se termine par `summary.country`.

### 4C · L'axe vertical

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```javascript
new Chart(canvas, {
  type: "bar",
  data: myData,      // a comma between data and options
  options: { scales: { y: { min: 10, max: 50 } } }
});
```

**À vous.** Faites aller votre axe de 0 à 100. N'oubliez pas la **virgule** avant `options`.

**Vérification.** `4A`, `4B`, `4C` `[OK]` et les trois changements sont visibles.

<details markdown="1"><summary>Bloqué ?</summary>

Page vide après 4C ? La console dit `Unexpected identifier` quand il manque une virgule : elle se place juste après la `}` qui ferme `data`.

</details>

## Étape 5 · Lire le graphique avec esprit critique (20 min)

<p class="refs" markdown="1">**Notion :** [Choisir et lire un graphique](notion-honest-charts.html)</p>

**À vous.** Créez `notes.txt` dans `td4` et écrivez au moins 30 mots :

1. Enlevez un instant `min` et `max` et observez. Remettez-les. Quel graphique montreriez-vous à un manager, et pourquoi ?
2. Quelle année manque pour certains pays (regardez 2020) ? Le graphique le rend-il visible ?

**Vérification.** Cinq `[OK]`.

## Si vous avez fini (facultatif)

1. Ajoutez une seconde série (autre pays) dans `datasets`.
2. Utilisez votre feuille de style du TD3.
3. Comparez minimum, moyenne et maximum avec trois barres.
