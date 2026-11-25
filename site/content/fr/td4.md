title: TD4 · Visualisation avec Chart.js
---
**Vendredi 29 janvier 2027 · 3 heures.** Fichiers de départ : [`td4`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td4).

## Objectif

Afficher les résultats du TD1 sous forme de graphiques avec quelques lignes de JavaScript.

**Vous avez réussi si** la page montre un graphique de votre pays, avec un titre et la source.

| Fourni | À vous |
|---|---|
| `chart.html` et `chart.js` fonctionnels, exemple `data/summary.json` | adapter données, étiquettes et type |

## Avant la séance

- [ ] J'ai relu [CM4](cm4.html).
- [ ] J'ai mon `summary.json` du TD1.

## Étape 1 · Servir la page (20 min)

Un navigateur interdit à une page ouverte par double-clic de lire d'autres fichiers. Lancez un petit serveur local **dans le dossier `td4`**, puis ouvrez <http://localhost:8000/chart.html> :

```
python -m http.server
```

**Point de contrôle :** le graphique d'exemple apparaît.

<details><summary>Indice 1</summary><p>Utilisez `python3` sur macOS ou Linux. Arrêtez avec Ctrl+C.</p></details>

## Étape 2 · Échauffement JavaScript (40 min)

Ouvrez la *console* (outils de développement) et essayez :

```
const years = [2023, 2024];
const point = { year: 2025, value: 94.98 };
console.log(years.length, point.value);
console.log(years.map(y => y + 1));
```

**Point de contrôle :** vous savez expliquer chaque ligne.


## Étape 3 · Vos données (30 min)

Remplacez `data/summary.json` par le vôtre. Lisez `chart.js` ligne par ligne.

**Point de contrôle :** le graphique montre votre pays.

<details><summary>Indice 1</summary><p>L'onglet *Réseau* montre si `summary.json` a été chargé (code 200).</p></details>

## Étape 4 · Adapter (50 min)

Passez au type `bar`, écrivez le pays dans le titre, réglez l'axe vertical de 0 à 100.

**Point de contrôle :** les trois changements sont visibles.

<details><summary>Indice 1</summary><p>`options: { scales: { y: { min: 0, max: 100 } } }`</p></details>

## Étape 5 · Lire de façon critique (40 min)

Comparez la courbe à axe automatique et à axe partant de 0. Dans `notes.txt`, écrivez laquelle vous montreriez à un manager et pourquoi. Notez ce qui se passe en 2020.

**Point de contrôle :** deux courts paragraphes.


## Extensions

1. Ajoutez une seconde série (autre pays).
2. Appliquez votre feuille de style du TD3.
3. Comparez minimum, moyenne et maximum en barres.
