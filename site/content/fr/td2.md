title: TD2 · Une page statique présentant un jeu de données
---
**Vendredi 15 janvier 2027 · 3 heures.** Fichiers de départ : [`td2`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td2).

## Objectif

Écrire une page HTML5 valide et sémantique qui présente les données Eurostat, avec un formulaire.

**Vous avez réussi si** la page passe le [validateur W3C](https://validator.w3.org/#validate_by_input) sans erreur.

| Fourni | À vous |
|---|---|
| squelette `index.html`, `images/network.svg` | les six `TODO` |

## Avant la séance

- [ ] J'ai relu [CM2](cm2.html).
- [ ] J'ai mon `internet_use_clean.csv` du TD1.

## Étape 1 · Structure (30 min)

Une *balise* indique le rôle d'un contenu. Complétez le titre, puis `header` avec `h1` et une liste `nav` de liens internes.

**Point de contrôle :** la page s'ouvre dans le navigateur, avec un seul `h1`.

<details><summary>Indice 1</summary><p>`<a href="#about">` jumps to the element with `id="about"`.</p></details>

## Étape 2 · Texte, liens, image (35 min)

Ajoutez une `section` avec un paragraphe, une liste, un lien vers le jeu de données et l'image. L'*attribut* `alt` décrit l'image pour qui ne la voit pas.

**Point de contrôle :** le lien fonctionne et l'image a un texte `alt`.


## Étape 3 · Tableau (45 min)

Présentez au moins 5 lignes de votre fichier nettoyé.

**Point de contrôle :** le tableau a un `caption`, un `thead` et des cellules `th`.

<details><summary>Indice 1</summary><p>`<tr>` est une ligne, `<th>` une cellule d'en-tête, `<td>` une cellule de données.</p></details>

## Étape 4 · Formulaire (40 min)

Un *formulaire* recueille une saisie. Ajoutez une liste de pays et un champ année avec un bouton. Il n'est pas encore traité : Flask s'en chargera en semaine 6.

**Point de contrôle :** chaque champ a un `label`, et après le clic l'adresse affiche `?country=…&year=…`.

<details><summary>Indice 1</summary><p>`<label for="year">` goes with `<input id="year" name="year">`.</p></details>
<details><summary>Indice 2</summary><p>Utilisez `type="number"` avec `min`, `max` et `required`.</p></details>

## Étape 5 · Valider (15 min)

Collez votre code dans le validateur W3C et corrigez les erreurs.

**Point de contrôle :** aucune erreur.


## Extensions

1. Ajoutez un second tableau pour un autre pays.
2. Ajoutez des boutons radio et une case à cocher.
3. Ajoutez une seconde page et liez les deux.
