title: TD2 · Une page statique présentant un jeu de données
---
**Vendredi 15 janvier 2027 · 3 heures.** Fichiers de départ : dossier [`td2`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td2).

## Objectif

Écrire une page web qui présente vos données Eurostat, avec un formulaire. **Gardez cette page :** le TD3 l'embellit.

**Vous avez réussi si** : `python check.py` affiche quinze `[OK]` et le validateur ne signale aucune erreur.

| Étape | Vous faites | Durée |
|---|---|---|
| 1 | Ouvrir les fichiers | 15 min |
| 2 | Construire la structure | 30 min |
| 3 | Ajouter texte, lien et image | 35 min |
| 4 | Faire un tableau | 40 min |
| 5 | Faire un formulaire | 35 min |
| 6 | Pied de page et validation | 25 min |

## Notions mobilisées dans ce TD

Ouvrez-les quand vous en avez besoin : chacune est une page courte. Les liens sont rappelés à l'étape concernée.

- [Éléments et attributs HTML](notion-html-elements.html)
- [Structure, balises sémantiques, validation](notion-html-structure.html)
- [Listes, liens, images, accessibilité](notion-html-links-images.html)
- [Tableaux](notion-html-tables.html)
- [Formulaires](notion-html-forms.html)

**Exemples clés en main :** [Une page HTML complète](recipe-page-skeleton.html) · [Un tableau et un formulaire](recipe-table-form.html)

## Avant la séance

- [ ] J'ai relu le [CM2](cm2.html).
- [ ] J'ai mon `internet_use_clean.csv` du TD1.

## Comment travailler

1. Faites les étapes **dans l'ordre**.
2. Écrivez uniquement là où vous voyez `TODO`. Son numéro est celui de ce sujet.
3. Après chaque partie, **enregistrez** (`Ctrl+S`, ou `Cmd+S` sur Mac) et lancez le vérificateur dans un terminal (**Terminal → New Terminal** dans VS Code) :

```text
python check.py
```

Sur macOS ou Linux, hors environnement virtuel, tapez `python3`. `[OK]` : la partie fonctionne ; `[  ]` : pas encore. Le vérificateur ne remplace pas un coup d'œil à votre page dans le navigateur.

## Rappel de cinq minutes

HTML décrit une page avec des **éléments**. Un élément a une **balise** ouvrante, un contenu et une balise fermante. Un **attribut** ajoute une information dans la balise ouvrante. Les éléments s'emboîtent : on ferme d'abord celui de l'intérieur. Indentez de 2 espaces pour voir qui contient qui.

```html
<p>Read <a href="books.html">our books</a>.</p>
<!-- p = paragraph · a = link · href = attribute · this line is a comment -->
```

## Étape 1 · Ouvrir les fichiers (15 min)

<p class="refs" markdown="1">**Notion :** [Éléments et attributs HTML](notion-html-elements.html)</p>

1. Ouvrez le dossier `td2` dans VS Code (**File → Open Folder**).
2. Ouvrez aussi `index.html` dans le navigateur : double-cliquez dessus dans l'explorateur de fichiers.
3. Dans le terminal de VS Code, lancez `python check.py`.

Ensuite : modifiez dans VS Code, **enregistrez**, puis **rechargez** le navigateur (`F5`).

**Vérification.** La page est vide et le vérificateur montre beaucoup de `[  ]`. C'est normal.

## Étape 2 · Construire la structure (30 min)

<p class="refs" markdown="1">**Notion :** [Structure, balises sémantiques, validation](notion-html-structure.html) · **Recette :** [Une page HTML complète](recipe-page-skeleton.html)</p>

### 2A · Le titre de l'onglet

**À vous.** Remplacez `TODO 2A: page title` (entre `<title>` et `</title>`) par un titre sur l'usage d'Internet.

**Vérification.** Le titre apparaît sur l'onglet du navigateur.

### 2B · L'en-tête

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```html
<header>
  <h1>My local library</h1>
</header>
```

**À vous.** Écrivez votre en-tête sous `TODO 2B`. Une page n'a qu'**un seul** `h1`, son titre principal.

### 2C · La navigation

<p class="refs" markdown="1">**Notion :** [Listes, liens, images, accessibilité](notion-html-links-images.html) · **Recette :** [Une page HTML complète](recipe-page-skeleton.html)</p>

`nav` contient le menu. `ul` est une liste et `li` un élément de liste. Un lien vers `#books` saute à l'élément qui porte `id="books"` dans la même page.

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```html
<nav>
  <ul>
    <li><a href="#books">Books</a></li>
    <li><a href="#hours">Opening hours</a></li>
  </ul>
</nav>
```

**À vous.** **Dans** votre `header`, ajoutez trois liens vers `#about`, `#figures` et `#search`.

**Vérification.** `2A`, `2B`, `2C` sont `[OK]`. Les liens ne font rien encore : leurs cibles n'existent pas.

## Étape 3 · Texte, lien et image (35 min)

<p class="refs" markdown="1">**Notion :** [Listes, liens, images, accessibilité](notion-html-links-images.html) · **Recette :** [Une page HTML complète](recipe-page-skeleton.html)</p>

### 3A · Une section

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```html
<section id="books">
  <h2>Our books</h2>
  <p>The library lends novels and comics.</p>
</section>
```

**À vous.** Sous `TODO 3A`, faites une section avec `id="about"`, un `h2` et un paragraphe qui dit ce que mesurent vos données. **Écrivez 3B, 3C et 3D dans cette section**, avant `</section>`.

### 3B · Une liste

**À vous.** Ajoutez une liste (`ul` et `li`, comme en 2C sans les liens) avec trois éléments : le producteur, l'unité, la fréquence de publication.

### 3C · Un lien vers un autre site

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```html
<p><a href="https://www.toulouse.fr">Visit the city website</a></p>
```

**À vous.** Faites un lien vers le jeu de données. Le texte du lien doit dire où il mène (pas « cliquez ici »). Adresse :

```text
https://ec.europa.eu/eurostat/databrowser/view/tin00028/default/table
```

### 3D · Une image

`img` n'a pas de balise fermante. `alt` décrit l'image pour les personnes qui ne la voient pas.

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```html
<img src="images/library.jpg" alt="Shelves full of books" width="320" height="180">
```

**À vous.** Affichez `images/network.svg` avec votre propre texte `alt`.

**Vérification.** `3A` à `3D` sont `[OK]`, le lien ouvre Eurostat et vous voyez l'image.

<details markdown="1"><summary>Bloqué ?</summary>

Pas d'image ? Le chemin doit être exactement `images/network.svg`. `[  ] 3B` ? Votre liste doit être avant `</section>`.

</details>

## Étape 4 · Un tableau (40 min)

<p class="refs" markdown="1">**Notion :** [Tableaux](notion-html-tables.html) · **Recette :** [Un tableau et un formulaire](recipe-table-form.html)</p>

| Balise | Sens |
|---|---|
| `table` | le tableau |
| `caption` | son titre |
| `thead` / `tbody` | partie en-tête / partie données |
| `tr` | une ligne |
| `th` / `td` | cellule d'en-tête / de données |

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

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

### 4A · Section, tableau, légende

**À vous.** Faites une section avec `id="figures"`, un `h2` et une `table` avec une `caption` nommant le pays et les années.

### 4B · Ligne d'en-tête

**À vous.** Ajoutez un `thead` avec deux cellules `th` : année et part (%).

### 4C · Lignes de données

**À vous.** Ajoutez un `tbody` avec **au moins 5 lignes**. Prenez les chiffres de votre pays dans `internet_use_clean.csv`. Écrivez une ligne, vérifiez dans le navigateur, puis recopiez-la.

**Vérification.** `4A` à `4C` sont `[OK]`. Le tableau n'a pas de bordures : le CSS les ajoutera au TD3.

## Étape 5 · Un formulaire (35 min)

<p class="refs" markdown="1">**Notion :** [Formulaires](notion-html-forms.html) · **Recette :** [Un tableau et un formulaire](recipe-table-form.html)</p>

Un **formulaire** recueille ce que saisit le visiteur. `name` est le nom sous lequel la valeur est envoyée. Un `label` est le texte d'un champ : son `for` est égal à l'`id` du champ.

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

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

### 5A · Section et formulaire

**À vous.** Section avec `id="search"`, un `h2` et un `form` vide avec `action="#search"` et `method="get"`. Écrivez 5B à 5D dans le formulaire.

### 5B · Les pays

**À vous.** Un `label` et un `select` nommé `country` avec au moins trois pays. La `value` est le code (`FR`), le texte est le nom.

### 5C · L'année

**À vous.** Un `label` et un champ nombre nommé `year`, avec `min`, `max` et `required`.

### 5D · Le bouton

**À vous.** Ajoutez un `button` de type `submit`.

**Vérification.** Remplissez et cliquez. La barre d'adresse affiche `?country=…&year=…`. Il ne se passe rien d'autre : Flask répondra en semaine 6.

<details markdown="1"><summary>Bloqué ?</summary>

`[  ] 5B` ou `5C` ? Comparez le `for` du label avec l'`id` du champ : ils doivent être identiques. Le champ a aussi besoin d'un `name`.

</details>

## Étape 6 · Pied de page et validation (25 min)

### 6A · Pied de page

**À vous.** Ajoutez un `footer` avec un paragraphe citant la source (Eurostat, tin00028).

### 6B · Valider

<p class="refs" markdown="1">**Notion :** [Structure, balises sémantiques, validation](notion-html-structure.html)</p>

Un **validateur** cherche les erreurs dans votre HTML. Ouvrez le [validateur du W3C](https://validator.w3.org/#validate_by_input), collez tout votre fichier, cliquez sur **Check**. Corrigez la **première** erreur, relancez.

**Vérification.** Quinze `[OK]` et aucune erreur dans le validateur.

## Si vous avez fini (facultatif)

1. Ajoutez un second tableau pour un autre pays.
2. Ajoutez des boutons radio et une case à cocher au formulaire.
3. Ajoutez une seconde page et liez les deux.
