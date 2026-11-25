title: CM7 · Flask 3 : le back-end comme API JSON
---
**23 février 2027.**

## Objectifs

1. séparer le back-end qui sert les données du front-end qui les affiche
2. écrire une route JSON filtrable
3. l’appeler avec fetch
4. déboguer avec la console et l’onglet Réseau

<!--plan-->
## La question

**Comment alimenter un graphique en direct ?**

1. Servir les données
2. Afficher les données
3. Déboguer
<!--/plan-->

## Diapositives

[PDF](cm7-fr.pdf)

{{slides:cm7:fr}}

<!--lab-->
## Pour vendredi

TD7 : un graphique alimenté en direct par votre API.

- Notions : [API JSON](notion-api.html), [fetch : demander des données](notion-fetch.html), [Outils de développement](notion-devtools.html), [Compréhensions, min, max, sorted](notion-list-tools.html), [Paramètres d'URL et chaîne de requête](notion-url-parameters.html), [HTTP : requêtes, réponses, codes d'état](notion-http.html), [Modifier la page en JavaScript](notion-dom.html), [Déboguer](notion-debugging.html)
- Recettes : [Une API JSON et son graphique](recipe-api-chart.html)
<!--/lab-->

## Vérifiez vos acquis

<details><summary>Que renvoie jsonify ?</summary><p>Une réponse HTTP en JSON.</p></details>
<details><summary>Où placer le JavaScript avec Flask ?</summary><p>Dans static/.</p></details>
<details><summary>Quel onglet montre le code d’un fetch ?</summary><p>Réseau.</p></details>
<details><summary>Pourquoi détruire l’ancien graphique ?</summary><p>Un canvas ne porte qu’un graphique.</p></details>

Ensuite : [TD7](td7.html).
