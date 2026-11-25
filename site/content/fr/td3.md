title: TD3 · Mise en forme et mise en page adaptative
---
**Vendredi 22 janvier 2027 · 3 heures.** Fichiers de départ : dossier [`td3`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td3).

## Objectif

Mettre en forme la page du TD2 pour qu'elle soit confortable sur téléphone et sur ordinateur.

**Vous avez réussi si** : `python check.py` affiche onze `[OK]` et, à la largeur d'un téléphone, rien ne dépasse.

| Étape | Vous faites | Durée |
|---|---|---|
| 1 | Lier la feuille de style | 20 min |
| 2 | Couleurs et polices | 30 min |
| 3 | Boîtes et espacements | 30 min |
| 4 | Navigation avec Flexbox | 30 min |
| 5 | Tableau et formulaire | 40 min |
| 6 | Écrans de téléphone | 30 min |

## Avant la séance

- [ ] J'ai relu le [CM3](cm3.html).
- [ ] Ma page du TD2 est valide. Sinon, je demande une page de départ à l'enseignant.

## Comment travailler

1. Faites les étapes **dans l'ordre**.
2. Écrivez uniquement là où vous voyez `TODO`. Son numéro est celui de ce sujet.
3. Après chaque partie, **enregistrez** (`Ctrl+S`, ou `Cmd+S` sur Mac) et lancez le vérificateur dans un terminal (**Terminal → New Terminal** dans VS Code) :

```text
python check.py
```

Sur macOS ou Linux, hors environnement virtuel, tapez `python3`. `[OK]` : la partie fonctionne ; `[  ]` : pas encore. Le vérificateur ne remplace pas un coup d'œil à votre page dans le navigateur.

## Rappel de cinq minutes

Le CSS dit quelle apparence ont les éléments. Une **règle** a un **sélecteur** (quels éléments) et des **déclarations** (propriété : valeur). Chaque déclaration finit par `;`.

```css
h2 {              /* selector: every h2 */
  color: green;   /* property: value; */
}
nav a { }         /* the links that are inside nav */
th, td { }        /* th and td together */
```

## Étape 1 · Lier la feuille de style (20 min)

1. Copiez `index.html` et le dossier `images` de `td2` dans `td3`.
2. Ouvrez le dossier `td3` dans VS Code et la page dans le navigateur.
3. Dans `index.html`, à l'intérieur de `<head>`, ajoutez :

```html
<link rel="stylesheet" href="style.css">
```

**Vérification.** `1` est `[OK]`.

## Étape 2 · Couleurs et polices (30 min)

### 2A · Toute la page

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```css
h1 {
  font-family: Georgia, serif;
  color: darkred;
  background: #fff4e0;   /* a colour written as a code */
}
```

**À vous.** Pour `body` : mettez `margin: 0;`, `font-family: system-ui, Arial, sans-serif;`, `line-height: 1.5;`, puis choisissez une `color` foncée et un `background` clair.

### 2B · En-tête et pied de page

**À vous.** Donnez à `header, footer` un `background` foncé, une `color` claire et `padding: 1rem;`. `rem` est une unité basée sur la taille du texte.

**Vérification.** `2A` et `2B` sont `[OK]`. Les liens de l'en-tête sont peut-être peu lisibles : l'étape 4 corrige cela.

<details markdown="1"><summary>Bloqué ?</summary>

Rien ne change dans le navigateur ? Vérifiez que les deux fichiers sont enregistrés et que la ligne `link` est exacte. Une `}` oubliée bloque tout ce qui suit.

</details>

## Étape 3 · Boîtes et espacements (30 min)

Chaque élément est une boîte : le contenu, puis le **padding** (espace intérieur), la **border** (bordure), puis la **margin** (espace extérieur).

### 3A · Centrer le contenu

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```css
.card {
  max-width: 20rem;    /* never wider than this */
  margin: 0 auto;      /* 0 above and below, automatic left and right = centred */
  padding: 2rem;
}
```

**À vous.** Centrez `main`, avec une largeur maximale de `60rem` et un padding de `1rem`.

### 3B · Les images ne débordent jamais

**À vous.** Pour `img` : `max-width: 100%;` et `height: auto;`.

**Vérification.** `3A`, `3B` `[OK]`. Sur une fenêtre large, le contenu reste au milieu. Clic droit → **Inspecter** pour voir le dessin de la boîte.

## Étape 4 · Navigation avec Flexbox (30 min)

**Flexbox** place les enfants d'une boîte en ligne. On l'écrit sur le **parent**.

### 4A · La liste en ligne

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```css
.toolbar {
  display: flex;      /* children side by side */
  gap: 2rem;          /* space between them */
}
```

**À vous.** Appliquez-le à `nav ul`, avec un `gap` de `1rem`. Supprimez aussi les puces (`list-style: none;`) et les espaces (`margin: 0;`, `padding: 0;`).

### 4B · Des liens lisibles

**À vous.** Donnez à `nav a` une `color` lisible sur votre en-tête.

**Vérification.** Les trois liens sont sur une ligne, sans puces.

## Étape 5 · Tableau et formulaire (40 min)

### 5A · Une bordure, pas deux

**À vous.** Pour `table` : `width: 100%;` et `border-collapse: collapse;`.

### 5B · Les cellules

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```css
.price {
  border: 1px solid grey;   /* thickness, style, colour */
  padding: 0.5rem;
  text-align: left;
}
```

**À vous.** Donnez à `th, td` une bordure, un padding et `text-align: left;`. Puis, dans une règle à part, un `background` à `th`.

### 5C · Le formulaire

**À vous.** Faites de `form` une boîte flex avec `gap: 0.75rem;`, `flex-wrap: wrap;` (aller à la ligne si besoin) et `align-items: center;`.

**Vérification.** `5A` à `5C` `[OK]` : bordures simples, en-tête visible, champs espacés.

## Étape 6 · Écrans de téléphone (30 min)

Une **media query** applique des règles seulement si une condition est vraie, ici un écran étroit.

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```css
@media (max-width: 600px) {
  .toolbar {
    flex-direction: column;   /* one under the other */
  }
}
```

**À vous.** À la **fin** du fichier, mettez `nav ul` et `form` en colonne sur les écrans jusqu'à 600px. Ajoutez `align-items: stretch;` pour que les champs prennent toute la largeur.

**Vérification.** Appuyez sur `F12`, puis sur l'icône **téléphone et tablette**, et choisissez 375px de large : menu et formulaire sont verticaux, rien ne dépasse. Onze `[OK]`.

<details markdown="1"><summary>Bloqué ?</summary>

Deux sélecteurs peuvent partager une règle : `nav ul, form { … }`. Il y a deux `}` à la fin : une pour la règle, une pour `@media`.

</details>

## Si vous avez fini (facultatif)

1. Ajoutez des styles `:hover` et `:focus` aux liens et boutons.
2. Mettez en évidence une ligne du tableau avec une classe.
3. Vérifiez le contraste de vos couleurs avec les outils de développement.
