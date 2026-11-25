title: TD8 · Mini-projet 1 : cadrage et données
---
**Vendredi 5 mars 2027 · 3 heures.** Fichiers de départ : [`project`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/project).

## Objectif

Seul ou en binôme, choisir une question et un jeu de données, nettoyer et concevoir les routes.

**Vous avez réussi si** au point d'étape vous montrez des données propres et un tableau des routes.

| Fourni | À vous |
|---|---|
| gabarit de projet : `app.py`, `base.html`, `style.css`, `README.md` | tout ce qui est propre à votre question |

## Avant la séance

- [ ] J'ai réfléchi à deux sujets possibles.

## Étape 1 · Question et données (40 min)

Formulez une question qu'un manager pourrait poser. Vérifiez d'abord la licence.

**Point de contrôle :** question, source et licence sont dans le README.


## Étape 2 · Charger et nettoyer (70 min)

Adaptez vos scripts du TD1. Regardez d'abord colonnes et codes.

**Point de contrôle :** un CSV propre aux colonnes claires.

<details><summary>Indice 1</summary><p>D'autres jeux ont d'autres dimensions : gardez une valeur par pays et par année.</p></details>

## Étape 3 · Concevoir (35 min)

Dessinez les pages sur papier et remplissez le tableau des routes.

**Point de contrôle :** au moins 3 routes, dont une JSON paramétrée.


## Étape 4 · Point d'étape 1 (35 min)

Courte revue (non notée) : données, périmètre, chargement, routes. En attendant, écrivez la première route.

**Point de contrôle :** retours notés.


## Exigences minimales

- Un jeu de données sous licence ouverte, chargé et nettoyé avec Python.
- Au moins 3 routes Flask, dont 1 route JSON avec paramètre.
- Au moins 1 formulaire ou filtre qui change l'affichage.
- Au moins 1 graphique Chart.js alimenté par la route JSON via `fetch`.
- HTML et CSS écrits à la main, adaptatifs, avec une barre de navigation commune (`base.html` copié dans chaque page).
- Un README : source, licence, lancement, routes principales, aide d'IA reçue.

## Jeux de données sûrs (Eurostat)

| Code | Contenu |
|---|---|
| [`tipsun20`](https://ec.europa.eu/eurostat/databrowser/view/tipsun20/default/table?lang=fr) | Taux de chômage annuel (plusieurs âges : filtrer `age`) |
| [`sdg_07_40`](https://ec.europa.eu/eurostat/databrowser/view/sdg_07_40/default/table?lang=fr) | Part des énergies renouvelables (plusieurs secteurs : filtrer `nrg_bal`) |
| [`sdg_11_60`](https://ec.europa.eu/eurostat/databrowser/view/sdg_11_60/default/table?lang=fr) | Taux de recyclage des déchets municipaux |
| [`sdg_08_10`](https://ec.europa.eu/eurostat/databrowser/view/sdg_08_10/default/table?lang=fr) | PIB réel par habitant (deux unités : filtrer `unit`) |

Vérifiés le 25 novembre 2026. Adresse de téléchargement : remplacez `tin00028` par le code dans l'adresse du TD1. Réutilisation avec attribution ([notice](https://ec.europa.eu/eurostat/fr/help/copyright-notice)). Autres portails : [data.gouv.fr](https://www.data.gouv.fr), [Toulouse Métropole](https://data.toulouse-metropole.fr), [data.europa.eu](https://data.europa.eu).
