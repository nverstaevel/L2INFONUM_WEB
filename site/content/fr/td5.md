title: TD5 · Flask : routes et réponses
---
**Vendredi 5 février 2027 · 3 heures.** Fichiers de départ : [`td5`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td5).

## Objectif

Faire tourner une première application Flask avec des routes renvoyant du texte, du HTML et du JSON.

**Vous avez réussi si** cinq adresses répondent, avec les bons codes d'état.

| Fourni | À vous |
|---|---|
| `app.py` avec une route, `templates/base.html`, `static/style.css` | les cinq `TODO` |

## Avant la séance

- [ ] J'ai relu [CM5](cm5.html).
- [ ] Python et mon environnement virtuel fonctionnent.

## Étape 1 · Installer et lancer (30 min)

Un *framework web* est une bibliothèque qui prend en charge le travail répétitif d'un serveur. Dans `td5`, créez l'environnement ([installation](setup.html)), puis :

```
python -m pip install -r requirements.txt
python app.py
```

**Point de contrôle :** <http://127.0.0.1:5000/> dit bonjour.


## Étape 2 · Routes (35 min)

Une *route* associe une adresse à une fonction Python. Ajoutez `/about`.

**Point de contrôle :** `/about` affiche du HTML.

<details><summary>Indice 1</summary><p>`@app.route("/about")` juste au-dessus de la fonction.</p></details>

## Étape 3 · JSON et paramètre d'URL (40 min)

Ajoutez `/api/info` avec `jsonify`, puis `/country/<code>`.

**Point de contrôle :** `/country/fr` affiche `FR`.

<details><summary>Indice 1</summary><p>La fonction reçoit `code` en argument.</p></details>
<details><summary>Indice 2</summary><p>Renvoyer directement une saisie est risqué : utilisez un gabarit avec `{{ code }}` (copiez `base.html`).</p></details>

## Étape 4 · Gabarits (45 min)

Un *gabarit* est un fichier HTML avec des trous `{{ nom }}` remplis par `render_template`. Créez `templates/index.html` à partir de `base.html`.

**Point de contrôle :** la page d'accueil est stylée et son titre vient de Python.

<details><summary>Indice 1</summary><p>`render_template("index.html", title="…")`</p></details>

## Étape 5 · Codes d'état (20 min)

Ajoutez `/teapot` avec le code 418 et observez-le dans l'onglet Réseau.

**Point de contrôle :** vous voyez 200, 404 et 418.

<details><summary>Indice 1</summary><p>`return "message", 418`</p></details>

## Extensions

1. Ajoutez `/count` : nombre de lignes du fichier nettoyé.
2. Personnalisez la page 404 avec `@app.errorhandler(404)`.
