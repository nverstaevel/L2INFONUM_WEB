title: TD3 · Mise en forme et mise en page adaptative
---
**Vendredi 22 janvier 2027 · 3 heures.** Fichiers de départ : [`td3`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td3).

## Objectif

Mettre en forme la page du TD2 et la rendre confortable sur téléphone et sur ordinateur.

**Vous avez réussi si** à 375 px de large rien ne dépasse, et sur grand écran la navigation tient sur une ligne.

| Fourni | À vous |
|---|---|
| squelette `style.css` | la feuille de style |

## Avant la séance

- [ ] J'ai relu [CM3](cm3.html).
- [ ] Ma page du TD2 est valide.

## Étape 1 · Lier et style de base (30 min)

Copiez `style.css` à côté de la page et ajoutez dans `<head>` :

```
<link rel="stylesheet" href="style.css">
```

**Point de contrôle :** changer la couleur de `body` modifie la page.


## Étape 2 · Modèle de boîte (35 min)

Chaque élément est une boîte : contenu, *padding* (intérieur), bordure, *margin* (extérieur). Centrez `main` et limitez sa largeur.

**Point de contrôle :** `main` est centré sur grand écran.

<details><summary>Indice 1</summary><p>`max-width` avec `margin: 0 auto;`</p></details>

## Étape 3 · Navigation Flexbox (35 min)

*Flexbox* place les enfants d'une boîte en ligne ou en colonne.

**Point de contrôle :** les liens sont côte à côte, sans puces.

<details><summary>Indice 1</summary><p>`nav ul { display: flex; gap: 1rem; list-style: none; }`</p></details>

## Étape 4 · Tableau et formulaire (35 min)

Mettez en forme le tableau et espacez les champs.

**Point de contrôle :** les bordures sont simples et l'en-tête ressort.

<details><summary>Indice 1</summary><p>`border-collapse: collapse;`</p></details>

## Étape 5 · Adaptatif (35 min)

Une *media query* applique des règles sous condition. Simulez un téléphone avec la barre d'appareils des outils de développement.

**Point de contrôle :** à 375 px le menu et le formulaire sont verticaux.

<details><summary>Indice 1</summary><p>`@media (max-width: 600px) { ... }`</p></details>

## Extensions

1. Ajoutez des styles `:hover` et `:focus`.
2. Mettez en évidence une ligne avec une classe.
3. Vérifiez le contraste de vos couleurs.
