title: TD5 · Flask : routes et réponses
---
**Vendredi 5 février 2027 · 3 heures.** Fichiers de départ : dossier [`td5`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td5).

## Objectif

Faire tourner votre première application avec Flask, un paquet Python qui répond aux requêtes web.

**Vous avez réussi si** : `python check.py` affiche six `[OK]`.

| Étape | Vous faites | Durée |
|---|---|---|
| 1 | Installer et lancer | 30 min |
| 2 | Une première route | 25 min |
| 3 | Renvoyer du JSON | 25 min |
| 4 | Un gabarit | 45 min |
| 5 | Une valeur dans l'adresse | 35 min |
| 6 | Codes d'état | 10 min |

## Notions mobilisées dans ce TD

Ouvrez-les quand vous en avez besoin : chacune est une page courte. Les liens sont rappelés à l'étape concernée.

- [Terminal et environnement virtuel](notion-terminal-venv.html)
- [Serveur local](notion-local-server.html)
- [Flask et les routes](notion-flask-routes.html)
- [JSON](notion-json.html)
- [API JSON](notion-api.html)
- [Gabarits et fichiers statiques](notion-templates.html)
- [Paramètres d'URL et chaîne de requête](notion-url-parameters.html)
- [Contrôle des saisies et échappement](notion-safety.html)
- [HTTP : requêtes, réponses, codes d'état](notion-http.html)
- [Outils de développement](notion-devtools.html)
- **[Flask et ses résultats](notion-flask-ref.html)**

**Exemples clés en main :** [Installer un projet](recipe-venv.html) · [Une application Flask avec un gabarit](recipe-flask-app.html)

## Avant la séance

- [ ] J'ai relu le [CM5](cm5.html).

## Comment travailler

1. Faites les étapes **dans l'ordre**.
2. Écrivez uniquement là où vous voyez `TODO`. Son numéro est celui de ce sujet.
3. Après chaque partie, **enregistrez** (`Ctrl+S`, ou `Cmd+S` sur Mac) et lancez le vérificateur dans un terminal (**Terminal → New Terminal** dans VS Code) :

```text
python check.py
```

Sur macOS ou Linux, hors environnement virtuel, tapez `python3`. `[OK]` : la partie fonctionne ; `[  ]` : pas encore. Le vérificateur ne remplace pas un coup d'œil à votre page dans le navigateur.

## Étape 1 · Installer et lancer (30 min)

<p class="refs" markdown="1">**Notion :** [Terminal et environnement virtuel](notion-terminal-venv.html), [Serveur local](notion-local-server.html) · **Recette :** [Installer un projet](recipe-venv.html)</p>

1. Ouvrez le dossier `td5` dans VS Code et un terminal.
2. Créez l'environnement (voir le [guide d'installation](setup.html) en cas d'échec).

Windows :

```text
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS / Linux :

```text
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Lancez l'application :

```text
python app.py
```

Ouvrez `http://127.0.0.1:5000/` (`127.0.0.1` signifie « cet ordinateur »). Laissez ce terminal tourner : `Ctrl+C` l'arrête. Lancez `check.py` dans un **second** terminal, après y avoir aussi activé l'environnement. L'application redémarre toute seule quand vous enregistrez un fichier `.py`.

**Vérification.** Le navigateur dit `Hello, web!` et `check.py` montre six `[  ]`.

## Étape 2 · Une première route (25 min)

<p class="refs" markdown="1">**Notion :** [Flask et les routes](notion-flask-routes.html) · **Recette :** [Une application Flask avec un gabarit](recipe-flask-app.html)</p>

Une **route** relie une adresse à une fonction Python. La ligne qui commence par `@` est un **décorateur** : il s'applique à la fonction juste en dessous. Ce que la fonction renvoie est envoyé au navigateur. Lisez la route `/` dans `app.py`.

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```python
@app.route("/contact")
def contact():
    return "<h1>Contact</h1><p>Write to the library.</p>"
```

### 2A · /about

**À vous.** Sous `TODO 2A`, écrivez la route `/about` : elle renvoie un `h1` et un paragraphe citant le jeu `tin00028`. Deux fonctions ne peuvent pas avoir le même nom.

**Vérification.** `http://127.0.0.1:5000/about` affiche votre texte et `2A` est `[OK]`.

## Étape 3 · Renvoyer du JSON (25 min)

<p class="refs" markdown="1">**Notion :** [JSON](notion-json.html), [API JSON](notion-api.html)</p>

Le **JSON** est de la donnée écrite en texte. Les programmes le lisent plus facilement que du HTML. `jsonify` le fabrique.

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```python
@app.route("/api/library")
def library():
    return jsonify(name="City library", books=1200)
```

### 3A · /api/info

**À vous.** Écrivez `/api/info` avec trois clés : `source`, `unit`, `licence`.

**Vérification.** Le navigateur affiche les trois clés ; `3A` est `[OK]`.

## Étape 4 · Un gabarit (45 min)

<p class="refs" markdown="1">**Notion :** [Gabarits et fichiers statiques](notion-templates.html) · **Recette :** [Une application Flask avec un gabarit](recipe-flask-app.html)</p>

Écrire une page entière dans Python est pénible. Un **gabarit** (*template*) est un fichier HTML, dans le dossier `templates`, avec des trous écrits `{{ nom }}`. `render_template` les remplit.

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```python
# in app.py
return render_template("shop.html", city="Toulouse", number=3)
```

```html
<!-- in templates/shop.html -->
<h1>Shops in {{ city }}</h1>
<p>{{ number }} shops</p>
```

### 4A · Créer index.html

**À vous.** Copiez `templates/base.html` et nommez la copie `templates/index.html`. Dans la copie, remplacez le texte du `h1` par `{{ title }}`.

### 4B · L'utiliser

**À vous.** Dans la fonction `home`, remplacez le texte renvoyé par un `render_template` de `index.html`, en donnant une valeur à `title`.

**Vérification.** La page d'accueil a le menu, les couleurs et votre titre. `4A`, `4B` `[OK]`.

<details markdown="1"><summary>Bloqué ?</summary>

`return render_template("index.html", title="…")`. Une erreur `TemplateNotFound` signifie que le nom du dossier ou du fichier est mal écrit.

</details>

## Étape 5 · Une valeur dans l'adresse (35 min)

<p class="refs" markdown="1">**Notion :** [Paramètres d'URL et chaîne de requête](notion-url-parameters.html), [Contrôle des saisies et échappement](notion-safety.html)</p>

Une partie de l'adresse écrite `<nom>` est donnée à la fonction comme argument.

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```python
@app.route("/book/<title>")
def book(title):
    return render_template("book.html", title=title.capitalize())
```

### 5A · Créer country.html

**À vous.** Copiez `base.html` en `templates/country.html`. Faites afficher `{{ code }}` par le `h1`.

### 5B · La route

**À vous.** Écrivez `/country/<code>` : elle rend `country.html` avec le code en **majuscules** (`.upper()`).

**Vérification.** `/country/fr` affiche `FR`, `/country/es` affiche `ES`. `5A`, `5B` `[OK]`.

Pourquoi un gabarit et pas `return code` ? `{{ }}` affiche ce qu'a saisi le visiteur comme du simple texte : personne ne peut glisser de code dans votre page.

## Étape 6 · Codes d'état (10 min)

<p class="refs" markdown="1">**Notion :** [HTTP : requêtes, réponses, codes d'état](notion-http.html), [Outils de développement](notion-devtools.html)</p>

Toute réponse a un numéro : 200 succès, 404 introuvable, 405 méthode non autorisée, 500 erreur dans votre code.

**À vous.** Ouvrez l'onglet **Réseau** (`F12`). Rechargez `/about`, puis visitez `/nothing`. Quel code lisez-vous à chaque fois ?

**Vérification.** Vous lisez 200, puis 404. `check.py` affiche six `[OK]`.

## Quand ça ne marche pas

| Vous voyez | Regardez |
|---|---|
| `app.py cannot be loaded` | la **dernière** ligne du message : la ligne du fichier et le type d'erreur |
| `Not Found` (404) | l'orthographe de l'adresse dans `@app.route` |
| `Method Not Allowed` (405) | `methods=[...]` dans la route |
| `Internal Server Error` (500) | le terminal où tourne `app.py` : lisez la dernière ligne |

## Si vous avez fini (facultatif)

1. Ajoutez `/count` : le nombre de lignes de votre fichier nettoyé (copiez-le dans `td5/data`).
2. Personnalisez la page 404 avec `@app.errorhandler(404)`.
3. Choisissez vous-même un code : une route `/teapot` qui renvoie `"No coffee here", 418`.
