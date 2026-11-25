title: CM5 · Flask 1 : routes et réponses
---
**2 février 2027.**

## Objectifs

1. expliquer le rôle d’un framework web
2. associer une URL à une fonction Python
3. renvoyer texte, HTML et JSON
4. utiliser le bon code d’état

<!--plan-->
## La question

**Comment faire fabriquer les pages par Python ?**

1. Votre propre serveur
2. Routes et réponses
3. Quand ça casse
<!--/plan-->

## Diapositives

[PDF](cm5-fr.pdf)

{{slides:cm5:fr}}

<!--lab-->
## Pour vendredi

TD5 : votre première application Flask.

- Notions : [Terminal et environnement virtuel](notion-terminal-venv.html), [Serveur local](notion-local-server.html), [Flask et les routes](notion-flask-routes.html), [JSON](notion-json.html), [API JSON](notion-api.html), [Gabarits et fichiers statiques](notion-templates.html), [Paramètres d'URL et chaîne de requête](notion-url-parameters.html), [Contrôle des saisies et échappement](notion-safety.html), [HTTP : requêtes, réponses, codes d'état](notion-http.html), [Outils de développement](notion-devtools.html)
- Recettes : [Installer un projet](recipe-venv.html), [Une application Flask avec un gabarit](recipe-flask-app.html)
<!--/lab-->

## Vérifiez vos acquis

<details><summary>Qu’est-ce qui relie une URL à une fonction ?</summary><p>Le décorateur @app.route.</p></details>
<details><summary>Quelle fonction renvoie du JSON ?</summary><p>jsonify.</p></details>
<details><summary>Où placer les gabarits ?</summary><p>Dans le dossier templates.</p></details>
<details><summary>Que signifie 500 ?</summary><p>Une erreur dans le code serveur.</p></details>

Ensuite : [TD5](td5.html).
