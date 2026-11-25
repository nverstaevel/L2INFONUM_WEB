title: TD7 · Une API JSON consommée par un graphique
---
**Vendredi 26 février 2027 · 3 heures.** Fichiers de départ : dossier [`td7`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td7).

## Objectif

Votre application envoie des données filtrées en JSON, et la page les trace sans se recharger. Une **API** est un ensemble d'adresses que des programmes utilisent pour obtenir des données.

**Vous avez réussi si** : choisir un autre pays redessine le graphique, et `check.py` affiche cinq `[OK]`.

| Étape | Vous faites | Durée |
|---|---|---|
| 1 | Installer et observer | 25 min |
| 2 | Filtrer par pays | 30 min |
| 3 | Filtrer par année | 30 min |
| 4 | Gérer les erreurs | 45 min |
| 5 | Déboguer | 30 min |

## Notions mobilisées dans ce TD

Ouvrez-les quand vous en avez besoin : chacune est une page courte. Les liens sont rappelés à l'étape concernée.

- [API JSON](notion-api.html)
- [fetch : demander des données](notion-fetch.html)
- [Outils de développement](notion-devtools.html)
- [Compréhensions, min, max, sorted](notion-list-tools.html)
- [Paramètres d'URL et chaîne de requête](notion-url-parameters.html)
- [HTTP : requêtes, réponses, codes d'état](notion-http.html)
- [Modifier la page en JavaScript](notion-dom.html)
- [Déboguer](notion-debugging.html)
- **[Flask et ses résultats](notion-flask-ref.html)**

**Exemples clés en main :** [Une API JSON et son graphique](recipe-api-chart.html)

## Avant la séance

- [ ] J'ai relu le [CM7](cm7.html).
- [ ] J'ai mon fichier CSV nettoyé du TD1.

## Comment travailler

1. Faites les étapes **dans l'ordre**.
2. Écrivez uniquement là où vous voyez `TODO`. Son numéro est celui de ce sujet.
3. Après chaque partie, **enregistrez** (`Ctrl+S`, ou `Cmd+S` sur Mac) et lancez le vérificateur dans un terminal (**Terminal → New Terminal** dans VS Code) :

```text
python check.py
```

Sur macOS ou Linux, hors environnement virtuel, tapez `python3`. `[OK]` : la partie fonctionne ; `[  ]` : pas encore. Le vérificateur ne remplace pas un coup d'œil à votre page dans le navigateur.

## Étape 1 · Installer et observer (25 min)

<p class="refs" markdown="1">**Notion :** [API JSON](notion-api.html), [fetch : demander des données](notion-fetch.html), [Outils de développement](notion-devtools.html) · **Recette :** [Une API JSON et son graphique](recipe-api-chart.html)</p>

**Raccourci :** vous pouvez réutiliser l'environnement du TD6 au lieu d'en créer un : `..\td6\.venv\Scripts\Activate.ps1` (Windows) ou `source ../td6/.venv/bin/activate` (macOS, Linux). En cas d'échec, créez-en un nouveau comme ci-dessous.

1. Ouvrez le dossier `td7` dans VS Code et un terminal.
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

Dans le navigateur, appuyez sur `F12`, ouvrez l'onglet **Réseau** et rechargez. Cliquez sur la ligne `data?country=FR`, puis **Réponse**. Lisez `static/chart.js` : `fetch` demande une adresse, puis le graphique est tracé avec la réponse.

**Vérification.** Vous savez dire qui envoie cette requête (la page ou Python ?). Le graphique mélange tous les pays : c'est l'étape suivante.

## Étape 2 · Filtrer par pays (30 min)

<p class="refs" markdown="1">**Notion :** [API JSON](notion-api.html), [Compréhensions, min, max, sorted](notion-list-tools.html) · **Recette :** [Une API JSON et son graphique](recipe-api-chart.html)</p>

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```python
author = request.args.get("author", "")
found = [b for b in BOOKS if b["author"] == author]    # keep some items
return jsonify(found)
```

### 2A · Un seul pays

**À vous.** Remplacez `rows = DATA` par les lignes de `country`.

**Vérification.** Saisissez `ES` dans la page et cliquez sur **Show** : le graphique change. Avec le fichier d'exemple (France seule), le graphique est vide : c'est normal. `2A` `[OK]`.

## Étape 3 · Filtrer par année (30 min)

<p class="refs" markdown="1">**Notion :** [Paramètres d'URL et chaîne de requête](notion-url-parameters.html)</p>

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```python
pages = request.args.get("pages", type=int)   # None if absent
if pages is not None:
    found = [b for b in found if b["pages"] == pages]
```

### 3A · Année facultative

**À vous.** Acceptez `year`. S'il manque, gardez toutes les années.

**Vérification.** `/api/data?country=FR&year=2024` montre une seule ligne. `3A` `[OK]`.

## Étape 4 · Gérer les erreurs (45 min)

<p class="refs" markdown="1">**Notion :** [HTTP : requêtes, réponses, codes d'état](notion-http.html), [API JSON](notion-api.html)</p>

### 4A · En Python

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```python
if not found:
    return jsonify(error="No book found"), 404
```

**À vous.** Renvoyez une erreur JSON avec le code 404 quand il n'y a aucune ligne. La clé doit être `error`.

### 4B · En JavaScript

<p class="refs" markdown="1">**Notion :** [Modifier la page en JavaScript](notion-dom.html), [fetch : demander des données](notion-fetch.html) · **Recette :** [Une API JSON et son graphique](recipe-api-chart.html)</p>

**Exemple** (sur un autre sujet : adaptez-le, ne le recopiez pas tel quel).

```javascript
if (books.error) {
  document.getElementById("info").textContent = books.error;
  return;                     // stop here: no chart
}
document.getElementById("info").textContent = "";
```

**À vous.** Sous `TODO 4B` dans `static/chart.js`, faites de même. La réponse s'appelle `rows` et le paragraphe vide de la page est `message`.

**Vérification.** Saisissez `ZZ` : un message apparaît et la console ne montre aucune erreur `Uncaught`. Une ligne 404 est normale. `4A`, `4B` `[OK]`.

<details markdown="1"><summary>Bloqué ?</summary>

Le navigateur peut garder l'ancien JavaScript : rechargez avec `Ctrl+F5` (`Cmd+Shift+R` sur Mac).

</details>

## Étape 5 · Déboguer (30 min)

<p class="refs" markdown="1">**Notion :** [Déboguer](notion-debugging.html), [Outils de développement](notion-devtools.html)</p>

**Déboguer**, c'est trouver et corriger une erreur. Entraînez-vous exprès :

1. Dans `chart.js`, changez `/api/data` en `/api/dat`. Rechargez.
2. Ouvrez la **Console** : quel est le message ?
3. Ouvrez **Réseau** : quelle adresse a échoué, avec quel code ?
4. Réparez.
5. Notez dans `notes.txt` (dossier `td7`) où vous avez regardé et ce que vous avez vu, en 20 mots au moins.

**Vérification.** Le graphique fonctionne à nouveau et cinq `[OK]`.

## Quand ça ne marche pas

| Vous voyez | Regardez |
|---|---|
| `app.py cannot be loaded` | la **dernière** ligne du message : la ligne du fichier et le type d'erreur |
| `Not Found` (404) | l'orthographe de l'adresse dans `@app.route` |
| `Method Not Allowed` (405) | `methods=[...]` dans la route |
| `Internal Server Error` (500) | le terminal où tourne `app.py` : lisez la dernière ligne |

## Si vous avez fini (facultatif)

1. Comparez avec un second pays.
2. Remplacez le champ par une liste `select`.
3. Choisissez le type de graphique dans la page.
4. Une erreur silencieuse : écrivez `row.values` au lieu de `row.value`. Que se passe-t-il, y a-t-il un message ? Réparez.
