title: TD9 · Mini-projet 2 : pages, filtres, graphiques
---
**Vendredi 12 mars 2027 · 3 heures.** Fichiers de départ : dossier [`project`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/project).

## Objectif

Construire les pages, le filtre et le premier graphique.

**Vous avez réussi si** : le parcours principal fonctionne, de l'accueil au graphique.

| Étape | Vous faites | Durée |
|---|---|---|
| 1 | Pages | 45 min |
| 2 | Formulaire ou filtre | 45 min |
| 3 | Route JSON et graphique | 60 min |
| 4 | Revue | 30 min |

## Avant la séance

- [ ] Les remarques du point d'étape 1 sont traitées.

## Comment travailler

Cochez chaque case quand c'est fait (le navigateur s'en souvient). Ne commencez pas la partie suivante avant d'avoir atteint le **jalon**. Faites une copie de votre dossier après chaque jalon.

## Étape 1 · Pages (45 min)

- [ ] Pour chaque page : copier `base.html`, le renommer, changer les titres.
- [ ] Écrire une route par page (TD5, étape 4).
- [ ] Mettre à jour les liens du menu **dans chaque fichier**.
- [ ] Ajouter vos règles du TD3 à `static/style.css`.

**Jalon.** Tous les liens du menu fonctionnent.

## Étape 2 · Formulaire ou filtre (45 min)

- [ ] Reprendre la route et le gabarit de recherche du TD6.
- [ ] Adapter les noms des champs et le test de la boucle.
- [ ] Tester une valeur normale, une valeur inconnue et un champ vide.

**Jalon.** L'affichage change avec la saisie et rien ne plante.

## Étape 3 · Route JSON et graphique (60 min)

- [ ] Reprendre `api_data` du TD7.
- [ ] Tester l'adresse JSON **seule** dans le navigateur.
- [ ] Copier `chart.html` dans `templates` et `chart.js` dans `static` ; ajouter la route de la page.
- [ ] Changer le titre, l'étiquette et le type de graphique.
- [ ] Vérifier la console : aucun message rouge.

**Jalon.** Le graphique change quand le paramètre change.

## Étape 4 · Revue (30 min)

- [ ] **Point d'étape 2** (non noté) : montrer pages, filtre et graphique.
- [ ] Écrire la liste de ce qui reste, du plus important au moins important.

**Jalon.** Vous avez votre liste.

## Exigences minimales

| Exigence | Vue au |
|---|---|
| Un jeu de données sous licence ouverte, chargé et nettoyé avec Python | TD1 |
| Au moins 3 routes Flask, dont 1 route JSON avec paramètre | TD5, TD7 |
| Au moins 1 formulaire ou filtre qui change l'affichage | TD6 |
| Au moins 1 graphique Chart.js alimenté par la route JSON avec `fetch` | TD4, TD7 |
| HTML et CSS écrits à la main, adaptatifs, même navigation sur chaque page (`base.html` copié) | TD2, TD3 |
| Un README : source, licence, lancement, routes principales, aide d'IA reçue | TD8 |
