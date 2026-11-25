title: TD6 · Paramètres, formulaires et sessions
---
**Vendredi 12 février 2027 · 3 heures.** Fichiers de départ : dossier [`td6`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td6).

## Objectif

Construire des pages qui réagissent à la saisie : une recherche, un filtre et une liste de favoris.

**Vous avez réussi si** : `python check.py` affiche six `[OK]`.

| Étape | Vous faites | Durée |
|---|---|---|
| 1 | Installer et observer | 15 min |
| 2 | Chercher par pays | 40 min |
| 3 | Formulaire et filtre | 25 min |
| 4 | Favoris | 40 min |
| 5 | Vérifier la saisie | 15 min |

## Notions mobilisées dans ce TD

Ouvrez-les quand vous en avez besoin : chacune est une page courte. Les liens sont rappelés à l'étape concernée.

- [Listes de dictionnaires](notion-lists-dicts.html)
- [Gabarits et fichiers statiques](notion-templates.html)
- [Paramètres d'URL et chaîne de requête](notion-url-parameters.html)
- [Formulaires](notion-html-forms.html)
- [GET et POST](notion-get-post.html)
- [Sessions et cookies](notion-sessions.html)
- [Contrôle des saisies et échappement](notion-safety.html)
- **[Flask et ses résultats](notion-flask-ref.html)**
- **[Python et ses résultats](notion-python-ref.html)**

**Exemples clés en main :** [Installer un projet](recipe-venv.html) · [Un formulaire de recherche](recipe-search-form.html) · [Mémoriser une liste avec une session](recipe-session-list.html)

## Avant la séance

- [ ] J'ai relu le [CM6](cm6.html).
- [ ] J'ai mon fichier CSV nettoyé du TD1.

## Comment travailler

1. Faites les étapes **dans l'ordre**.
2. Écrivez uniquement là où vous voyez `TODO`. Son numéro est celui de ce sujet.
3. Après chaque partie, **enregistrez** (`Ctrl+S`, ou `Cmd+S` sur Mac) et lancez le vérificateur dans un terminal (**Terminal → New Terminal** dans VS Code) :

```text
python check.py
```

Sur macOS ou Linux, hors environnement virtuel, tapez `python3`. `[OK]` : la partie fonctionne ; `[  ]` : pas encore. Le vérificateur ne remplace pas un coup d'œil à votre page dans le navigateur.

## Rappel de cinq minutes

`DATA` est une liste de dictionnaires avec les clés `country`, `year`, `value`. Dans ce cours, un gabarit ne contient que des `{{ nom }}` : pas de boucle. C'est donc **Python qui construit le texte**, et le gabarit l'affiche.

## Étape 1 · Installer et observer (15 min)

<p class="refs" markdown="1">**Notion :** [Listes de dictionnaires](notion-lists-dicts.html), [Gabarits et fichiers statiques](notion-templates.html) · **Recette :** [Installer un projet](recipe-venv.html)</p>

1. Ouvrez le dossier `td6` dans VS Code et un terminal.
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

Copiez ensuite **votre** `internet_use_clean.csv` (créé au TD1) dans le dossier `data`. Pas de fichier ? Copiez celui du dossier `sample` : il ne contient que la France.

Lancez l'application :

```text
python app.py
```

Ouvrez `http://127.0.0.1:5000/` (`127.0.0.1` signifie « cet ordinateur »). Laissez ce terminal tourner : `Ctrl+C` l'arrête. Lancez `check.py` dans un **second** terminal, après y avoir aussi activé l'environnement. L'application redémarre toute seule quand vous enregistrez un fichier `.py`.

**Vérification.** La page d'accueil indique le nombre de lignes chargées.

## Étape 2 · Chercher par pays (40 min)

<p class="refs" markdown="1">**Notion :** [Paramètres d'URL et chaîne de requête](notion-url-parameters.html) · **Recette :** [Un formulaire de recherche](recipe-search-form.html)</p>

### 2A · Lire le gabarit

Les pages sont **déjà écrites** : vous n'écrivez que du Python. Ouvrez `templates/search.html`.

**À vous.** Trouvez les trois trous `{{ ... }}` et notez leurs noms sur papier : votre route doit donner une valeur à chacun. `<pre>` conserve les retours à la ligne.

### 2B · Lire l'adresse

Dans `/search?country=FR`, la partie après `?` est la **chaîne de requête**. `request.args.get` la lit. Le second argument est la valeur utilisée si elle manque.

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```python
@app.route("/books")
def books():
    author = request.args.get("author", "").strip().upper()   # strip: no spaces
    return render_template("books.html", results=author)
```

**À vous.** Écrivez la route `/search` : lisez `country` de la même façon et, pour l'instant, affichez-le dans `results`. Testez `/search?country=fr` : vous lisez `FR`.

### 2C · Construire les lignes

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```python
lines = []
for book in BOOKS:
    if author == "" or book["author"] == author:
        lines.append(f"{book['title']}  {book['year']}")
results = "\n".join(lines)      # one line under the other
```

**À vous.** Construisez `results` à partir de `DATA` : gardez les lignes du pays (toutes si `country` est vide), une ligne avec pays, année et valeur.

**Vérification.** `/search?country=FR` liste les années de la France. `2B-2C` `[OK]`.

<details markdown="1"><summary>Bloqué ?</summary>

Dans un texte `f"..."`, utilisez des apostrophes : `{row['year']}`. Le `return` doit être **après** la boucle, pas dedans.

</details>

## Étape 3 · Formulaire et filtre (25 min)

<p class="refs" markdown="1">**Notion :** [Formulaires](notion-html-forms.html), [Paramètres d'URL et chaîne de requête](notion-url-parameters.html) · **Recette :** [Un formulaire de recherche](recipe-search-form.html)</p>

### 3A · Lire le formulaire

**À vous.** Dans `search.html`, lisez le `form`. Quelle adresse appelle-t-il (`action`) ? Quels sont les `name` des deux champs ? Remplissez, cliquez, et comparez avec la barre d'adresse.

### 3B · La valeur minimale

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```python
maximum = request.args.get("pages", 1000, type=int)   # converted to a number
# then, in the test of the loop:   ... and book["pages"] <= maximum
```

**À vous.** Lisez `minimum` comme un nombre à virgule (`type=float`, défaut 0) et ne gardez que les lignes dont la valeur l'atteint. Mettez des parenthèses autour du test du pays : `(... or ...) and ...`.

### 3C · Aucun résultat, et conserver la saisie

**À vous.** Si `lines` est vide, `results` doit être exactement `No result.`. Puis transmettez `country` et `minimum` à `render_template` : le gabarit les affiche déjà dans les champs.

**Vérification.** Cherchez avec plusieurs valeurs : la liste change et les champs gardent votre saisie. `3B`, `3C` `[OK]`.

<details markdown="1"><summary>Bloqué ?</summary>

`if not lines:` est vrai quand la liste est vide.

</details>

## Étape 4 · Favoris (40 min)

<p class="refs" markdown="1">**Notion :** [GET et POST](notion-get-post.html), [Sessions et cookies](notion-sessions.html) · **Recette :** [Mémoriser une liste avec une session](recipe-session-list.html)</p>

**GET** demande une page. **POST** envoie des données qui modifient quelque chose. Une **session** mémorise des données pour un visiteur d'une page à l'autre, dans un **cookie** (petit texte conservé par le navigateur).

### 4A · Lire le gabarit

**À vous.** Ouvrez `templates/favourites.html`. Notez la `method` du formulaire, le `name` du champ et le nom du trou `{{ ... }}`.

### 4B · La route

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```python
@app.route("/basket", methods=["GET", "POST"])
def basket():
    if request.method == "POST":
        item = request.form.get("item", "").strip().upper()   # form, not args
        print("received", item)                              # look in the terminal
    return render_template("basket.html", items="nothing yet")
```

**À vous.** Écrivez `/favourites` de la même façon : lisez `country`, affichez-le avec `print`, montrez `none` pour l'instant.

### 4C · Mémoriser

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```python
items = session.get("basket", [])          # the list, empty the first time
if request.method == "POST":
    ...
    if item and item not in items:
        items = items + [item]              # a NEW list
        session["basket"] = items           # saved
text = ", ".join(items) if items else "none"
```

**À vous.** Faites de même avec `session["favourites"]` et transmettez le texte au gabarit sous le nom `favourites`.

**Vérification.** Ajoutez `FR`, allez sur une autre page, revenez : il est toujours là. `4B`, `4C` `[OK]`.

## Étape 5 · Vérifier la saisie (15 min)

<p class="refs" markdown="1">**Notion :** [Contrôle des saisies et échappement](notion-safety.html) · **Recette :** [Mémoriser une liste avec une session](recipe-session-list.html)</p>

Un visiteur peut saisir n'importe quoi. Vérifiez toujours.

### 5A · Codes connus seulement

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```python
known = any(book["author"] == author for book in BOOKS)   # True if at least one
```

**À vous.** N'ajoutez le pays que s'il existe dans `DATA`.

**Vérification.** `ZZ` n'est pas ajouté ; six `[OK]`. Dans la recherche, saisissez `<b>` : il s'affiche comme du texte, pas en gras.

## Quand ça ne marche pas

| Vous voyez | Regardez |
|---|---|
| `app.py cannot be loaded` | la **dernière** ligne du message : la ligne du fichier et le type d'erreur |
| `Not Found` (404) | l'orthographe de l'adresse dans `@app.route` |
| `Method Not Allowed` (405) | `methods=[...]` dans la route |
| `Internal Server Error` (500) | le terminal où tourne `app.py` : lisez la dernière ligne |

## Pour aller plus loin (facultatif)

### Vider la liste

Ajoutez ce second formulaire à `favourites.html`. Le `name` et la `value` d'un bouton sont envoyés quand on clique.

```html
<form action="/favourites" method="post">
  <button type="submit" name="action" value="clear">Empty the list</button>
</form>
```

Dans la route, si `request.form.get("action")` vaut `"clear"`, la liste devient vide et est enregistrée dans la session.

### Travailler les gabarits

1. Ajoutez un champ `year` au formulaire de `search.html`, avec son `{{ year }}`, et filtrez avec.
2. Reconstruisez vous-même `search.html` à partir de `base.html`.

### Et aussi

1. Affichez la moyenne des résultats.
2. Après un POST, redirigez avec `redirect`.
