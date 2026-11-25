title: TD8 · Mini-projet 1 : cadrage et données
---
**Vendredi 5 mars 2027 · 3 heures.** Fichiers de départ : dossier [`project`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/project).

## Objectif

Seul ou en binôme : choisir une question et un jeu de données, nettoyer, prévoir les pages.

**Vous avez réussi si** : vous montrez un fichier CSV propre et un tableau des routes.

| Étape | Vous faites | Durée |
|---|---|---|
| 1 | Question et jeu de données | 40 min |
| 2 | Charger et nettoyer | 75 min |
| 3 | Prévoir les pages | 30 min |
| 4 | Première route et revue | 35 min |

## Notions mobilisées dans ce TD

Ouvrez-les quand vous en avez besoin : chacune est une page courte. Les liens sont rappelés à l'étape concernée.

- [Données ouvertes et licences](notion-open-data.html)
- [Fichiers CSV](notion-csv.html)
- [Lire et écrire des fichiers](notion-python-files.html)
- [README et dossier de projet](notion-readme.html)
- [Flask et les routes](notion-flask-routes.html)
- [Gabarits et fichiers statiques](notion-templates.html)
- [Listes de dictionnaires](notion-lists-dicts.html)
- **[Python et ses résultats](notion-python-ref.html)**
- **[Flask et ses résultats](notion-flask-ref.html)**

**Exemples clés en main :** [Télécharger un fichier](recipe-download.html) · [Filtrer un fichier CSV](recipe-clean-csv.html) · [Un README de projet](recipe-readme.html) · [Une application Flask avec un gabarit](recipe-flask-app.html)

## Avant la séance

- [ ] J'ai réfléchi à deux sujets possibles.
- [ ] J'ai regardé la diapositive sur le dossier du projet et le README dans le [CM8](cm8.html).

## Comment travailler

Cochez chaque case quand c'est fait (le navigateur s'en souvient). Ne commencez pas la partie suivante avant d'avoir atteint le **jalon**. Faites une copie de votre dossier après chaque jalon.

## Étape 1 · Question et jeu de données (40 min)

<p class="refs" markdown="1">**Notion :** [Données ouvertes et licences](notion-open-data.html)</p>

Une bonne question compare ou suit quelque chose dans le temps. Exemple : *Comment la part des énergies renouvelables a-t-elle évolué dans mon pays et dans deux autres ?*

Vous hésitez ? Prenez l'un de ces jeux Eurostat (vérifiés le 25 novembre 2026) :

| Code | Contenu | Filtre à appliquer |
|---|---|---|
| [`tipsun20`](https://ec.europa.eu/eurostat/databrowser/view/tipsun20/default/table?lang=fr) | Taux de chômage annuel | un seul `age`, par exemple `Y15-74` |
| [`sdg_07_40`](https://ec.europa.eu/eurostat/databrowser/view/sdg_07_40/default/table?lang=fr) | Part des énergies renouvelables | un seul `nrg_bal`, par exemple `REN` |
| [`sdg_11_60`](https://ec.europa.eu/eurostat/databrowser/view/sdg_11_60/default/table?lang=fr) | Taux de recyclage des déchets municipaux | aucun |
| [`sdg_08_10`](https://ec.europa.eu/eurostat/databrowser/view/sdg_08_10/default/table?lang=fr) | PIB réel par habitant | une seule `unit` |

Réutilisation avec attribution ([notice](https://ec.europa.eu/eurostat/fr/help/copyright-notice)). Autres portails : [data.gouv.fr](https://www.data.gouv.fr), [Toulouse Métropole](https://data.toulouse-metropole.fr), [data.europa.eu](https://data.europa.eu).

- [ ] Copier le dossier `project` et le renommer à vos noms.
- [ ] Écrire la question dans `README.md`.
- [ ] Noter la source, le producteur et la **licence** (pas de licence : changer de jeu).

**Jalon.** Question, source et licence sont dans le README.

## Étape 2 · Charger et nettoyer (75 min)

<p class="refs" markdown="1">**Notion :** [Fichiers CSV](notion-csv.html), [Lire et écrire des fichiers](notion-python-files.html) · **Recette :** [Télécharger un fichier](recipe-download.html), [Filtrer un fichier CSV](recipe-clean-csv.html)</p>

Réutilisez vos scripts du TD1. Pour un jeu Eurostat, seule l'adresse change (remplacez `tin00028` par votre code), puis les filtres.

- [ ] Copier `download.py` et `clean.py` dans le projet ; changer l'adresse et les noms de fichiers.
- [ ] Lancer le téléchargement et ouvrir le fichier : lire les noms des colonnes.
- [ ] Supprimer le test sur `indic_is` si votre fichier n'a pas cette colonne.
- [ ] Ajouter votre filtre (tableau ci-dessus). D'autres colonnes peuvent aussi en demander un.
- [ ] Vérifier : une seule ligne par pays et par année.

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```python
if row["age"] != "Y15-74":   # keep one value of a column
    continue
```

<details markdown="1"><summary>Bloqué ?</summary>

Affichez les valeurs différentes d'une colonne : `print(set(row["age"] for row in rows))`.

</details>

**Bloqué après 60 minutes ?** Prenez le fichier de secours `project/backup/co2_per_capita.csv` (émissions de CO₂ par personne, déjà nettoyé), copiez-le dans `data` et continuez. Citez-le comme indiqué dans `project/backup/README.md`.

**Jalon.** Un CSV propre `country,year,value` dans le dossier `data`.

## Étape 3 · Prévoir les pages (30 min)

<p class="refs" markdown="1">**Notion :** [README et dossier de projet](notion-readme.html), [Flask et les routes](notion-flask-routes.html) · **Recette :** [Un README de projet](recipe-readme.html)</p>

- [ ] Dessiner chaque page sur papier.
- [ ] Remplir le tableau des routes du README (au moins 3, dont une JSON avec paramètre).
- [ ] Se répartir le travail.

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```text
| Route                  | Method | What it does                |
| /                      | GET    | presents the question       |
| /search                | GET    | filter by country           |
| /api/data?country=FR   | GET    | JSON used by the chart      |
```

**Jalon.** Le tableau des routes est complet.

## Étape 4 · Première route et revue (35 min)

<p class="refs" markdown="1">**Notion :** [Gabarits et fichiers statiques](notion-templates.html), [Listes de dictionnaires](notion-lists-dicts.html) · **Recette :** [Une application Flask avec un gabarit](recipe-flask-app.html)</p>

- [ ] Copier `load_data` du TD6 (ajouter `import csv` en haut) et afficher le nombre de lignes sur l'accueil.
- [ ] **Point d'étape 1** (courte revue, non notée) : montrer les données et les routes.
- [ ] Noter les remarques de l'enseignant.

**Jalon.** L'application tourne et charge vos données.

## Exigences minimales

| Exigence | Vue au |
|---|---|
| Un jeu de données sous licence ouverte, chargé et nettoyé avec Python | TD1 |
| Au moins 3 routes Flask, dont 1 route JSON avec paramètre | TD5, TD7 |
| Au moins 1 formulaire ou filtre qui change l'affichage | TD6 |
| Au moins 1 graphique Chart.js alimenté par la route JSON avec `fetch` | TD4, TD7 |
| HTML et CSS écrits à la main, adaptatifs, même navigation sur chaque page (`base.html` copié) | TD2, TD3 |
| Un README : source, licence, lancement, routes principales, aide d'IA reçue | TD8 |
