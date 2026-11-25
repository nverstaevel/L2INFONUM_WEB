title: TD7 · Une API JSON consommée par un graphique
---
**Vendredi 26 février 2027 · 3 heures.** Fichiers de départ : [`td7`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td7).

## Objectif

Servir des données filtrées en JSON et les tracer dans un graphique qui se met à jour.

**Vous avez réussi si** choisir un autre pays redessine le graphique sans recharger la page.

| Fourni | À vous |
|---|---|
| `app.py`, `templates/chart.html`, `static/chart.js` fonctionnel | les quatre `TODO` |

## Avant la séance

- [ ] J'ai relu [CM7](cm7.html).
- [ ] Mon CSV nettoyé est dans `data/`.

## Étape 1 · Observer (25 min)

Lancez l'application. Dans l'onglet Réseau, rechargez, cliquez sur `data?country=FR` et lisez la réponse.

**Point de contrôle :** vous savez dire qui envoie la requête.


## Étape 2 · Filtrer par pays (35 min)

Complétez la route pour ne renvoyer qu'un pays.

**Point de contrôle :** le graphique change quand vous saisissez `DE`.

<details><summary>Indice 1</summary><p>Une liste en compréhension : `[r for r in DATA if ...]`.</p></details>

## Étape 3 · Paramètre année (35 min)

Acceptez `?year=2022`.

**Point de contrôle :** `/api/data?country=FR&year=2022` renvoie une ligne.

<details><summary>Indice 1</summary><p>`request.args.get("year", type=int)` vaut `None` si absent.</p></details>

## Étape 4 · Erreurs (45 min)

Renvoyez une erreur JSON avec le code 404 et affichez le message dans la page.

**Point de contrôle :** saisir `ZZ` affiche un message, sans erreur JavaScript non gérée.

<details><summary>Indice 1</summary><p>`return jsonify(error="..."), 404`</p></details>
<details><summary>Indice 2</summary><p>En JavaScript, testez `rows.error`, puis `return`.</p></details>

## Étape 5 · Déboguer (40 min)

Cassez volontairement l'adresse dans `chart.js`. Trouvez l'erreur avec la console et l'onglet Réseau, puis corrigez.

**Point de contrôle :** vous décrivez votre méthode en trois lignes.


## Extensions

1. Ajoutez un second pays à comparer.
2. Remplacez le champ par une liste `select`.
3. Choisissez le type de graphique dans la page.
