title: CM6 · Flask 2 : paramètres, formulaires, sessions
---
**9 février 2027.**

## Objectifs

1. lire paramètres d’URL et de requête
2. traiter des formulaires GET et POST
3. conserver un état simple en session
4. afficher sans risque avec {{ variable }}

## Diapositives

[PDF](cm6-fr.pdf)

{{slides:cm6:fr}}

## Vérifiez vos acquis

<details><summary>Quel objet lit ?year=2022 ?</summary><p>request.args.</p></details>
<details><summary>Quel objet lit un formulaire POST ?</summary><p>request.form.</p></details>
<details><summary>Que faut-il pour utiliser session ?</summary><p>app.secret_key.</p></details>
<details><summary>Pourquoi garder l’échappement ?</summary><p>Pour qu’une saisie ne soit jamais exécutée comme du code.</p></details>

Ensuite : [TD6](td6.html).
