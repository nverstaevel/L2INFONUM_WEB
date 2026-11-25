title: CM6 · Flask 2 : paramètres, formulaires, sessions
---
**9 février 2027.**

## Objectifs

1. lire paramètres d’URL et de requête
2. traiter des formulaires GET et POST
3. conserver un état simple en session
4. afficher sans risque avec {{ variable }}

<!--plan-->
## La question

**Comment répondre à la demande d'un visiteur ?**

1. Lire la demande et les données
2. Formulaires et mémoire
3. La sécurité
<!--/plan-->

## Diapositives

[PDF](cm6-fr.pdf)

{{slides:cm6:fr}}

<!--lab-->
## Pour vendredi

TD6 : recherche, filtre et favoris.

- Notions : [Listes de dictionnaires](notion-lists-dicts.html), [Gabarits et fichiers statiques](notion-templates.html), [Paramètres d'URL et chaîne de requête](notion-url-parameters.html), [Formulaires](notion-html-forms.html), [GET et POST](notion-get-post.html), [Sessions et cookies](notion-sessions.html), [Contrôle des saisies et échappement](notion-safety.html)
- Recettes : [Installer un projet](recipe-venv.html), [Un formulaire de recherche](recipe-search-form.html), [Mémoriser une liste avec une session](recipe-session-list.html)
<!--/lab-->

## Vérifiez vos acquis

<details><summary>Quel objet lit ?year=2022 ?</summary><p>request.args.</p></details>
<details><summary>Quel objet lit un formulaire POST ?</summary><p>request.form.</p></details>
<details><summary>Que faut-il pour utiliser session ?</summary><p>app.secret_key.</p></details>
<details><summary>Pourquoi garder l’échappement ?</summary><p>Pour qu’une saisie ne soit jamais exécutée comme du code.</p></details>

Ensuite : [TD6](td6.html).
