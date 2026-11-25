title: TD1 · Python, fichiers et données ouvertes
---
**Vendredi 8 janvier 2027 · 3 heures.** Fichiers de départ : dossier `td1` du [dépôt](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td1).

## Objectif

Vous allez télécharger de vraies données d'Eurostat (l'office statistique de l'Union européenne), les nettoyer et calculer quelques chiffres. **Conservez vos fichiers :** les TD suivants les utilisent.

| Étape | Script (un fichier de code Python) | Il produit | Durée |
|---|---|---|---|
| 1 | aucun : installation | un environnement qui marche | 25 min |
| 2 | `download.py` | `data/internet_use.csv` | 25 min |
| 3 | aucun : lire les données | `notes.txt` | 20 min |
| 4 | `clean.py` | `data/internet_use_clean.csv` | 55 min |
| 5 | `stats.py` | `data/summary.json` | 45 min |

## Comment travailler

1. Faites les étapes **dans l'ordre**. Chacune a besoin de la précédente.
2. Écrivez votre code uniquement là où vous voyez `TODO`. Le numéro du `TODO` est celui de ce sujet.
3. Après chaque partie, **enregistrez** le fichier (`Ctrl+S`, ou `Cmd+S` sur Mac) et lancez le vérificateur :
```text
python check.py
```
`[OK]` signifie que la partie fonctionne. `[  ]` signifie pas encore : lisez le message après la flèche. Il est normal d'avoir beaucoup de `[  ]` au début.

## Rappel de cinq minutes

Un tableau de données est une **liste de dictionnaires** : un dictionnaire par ligne, une **clé** par colonne.
```python
rows = [{"city": "Toulouse", "inhabitants": "500000"},
        {"city": "Paris", "inhabitants": "2100000"}]

for row in rows:
    number = int(row["inhabitants"])   # "500000" (text) -> 500000 (number)
    if number > 1000000:
        print(row["city"])             # Paris
```
## Étape 1 · Installation (25 min)

Un **terminal** est une fenêtre où l'on tape des commandes. Un **environnement virtuel** est un ensemble de paquets Python (du code écrit par d'autres) réservé à un projet.

1. Sur le [dépôt du cours](https://github.com/nverstaevel/L2INFONUM_WEB), cliquez sur **Code → Download ZIP**, puis décompressez le fichier.
2. Dans VS Code : **File → Open Folder** (Fichier → Ouvrir le dossier), choisissez le dossier `td1` (pas tout le dossier du cours).
3. **Terminal → New Terminal**.
4. Tapez ces commandes une par une, en validant par Entrée.

Windows:

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

**Vérification.** La ligne de saisie commence par `(.venv)`, et `python check.py` affiche huit lignes `[  ]`.
<details markdown="1"><summary>Bloqué ?</summary>

Voir le tableau des problèmes fréquents du [guide d'installation](setup.html).

</details>

## Étape 2 · Télécharger (25 min)

`requests` est un paquet qui demande une page ou un fichier à un serveur web, comme le fait un navigateur. Ouvrez `download.py`.

### 2A · L’adresse

Placez cette adresse entre les guillemets de `URL = ""` :
```text
https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/tin00028?format=SDMX-CSV&compress=false
```

### 2B · Est-ce que ça a marché ?

Le serveur répond avec un **code d'état**, un nombre : 200 signifie succès.

**Exemple** (sur un autre sujet : ne le recopiez pas tel quel).
```python
import requests

answer = requests.get("https://www.python.org", timeout=60)
print(answer.status_code)          # 200
if answer.status_code != 200:
    raise SystemExit("It failed")  # stops the script
```

**À vous.** Dans `download.py` la réponse s'appelle `response`. Sous `TODO 2B`, arrêtez le script si son code d'état n'est pas 200.
<details markdown="1"><summary>Bloqué ?</summary>

Deux lignes. La première commence par `if response.` et finit par `:`. La seconde est indentée (4 espaces) et commence par `raise SystemExit(`.

</details>

### 2C · Enregistrer le fichier

**Exemple** (sur un autre sujet : ne le recopiez pas tel quel).
```python
from pathlib import Path

Path("hello.txt").write_bytes(b"Hello")   # b"..." is a piece of bytes
print("Done")
```

**À vous.** `OUTPUT` est déjà un `Path`, et `content` contient déjà les octets. Écrivez `content` dans `OUTPUT` (une ligne), puis affichez un message (une ligne). Lancez :
```text
python download.py
python check.py
```

**Vérification.** `Step 2` affiche `[OK]` et vous pouvez ouvrir `data/internet_use.csv`.
<details markdown="1"><summary>Bloqué ?</summary>

`OUTPUT.write_bytes(...)` : que mettre entre les parenthèses ? Si le message parle de connexion, vérifiez l'adresse et votre accès à Internet.

</details>

## Étape 3 · Lire les données (20 min)

Un fichier **CSV** est un tableau écrit en texte : une ligne du tableau par ligne, les colonnes séparées par des virgules. La première ligne donne les noms des colonnes. Ouvrez `data/internet_use.csv` dans VS Code, créez un fichier `notes.txt` et répondez :

1. Recopiez la première ligne. Combien y a-t-il de colonnes ?
2. Trouvez une ligne de la France (`FR`). Quelle colonne contient l'année ? Laquelle contient le chiffre ?
3. Cherchez (`Ctrl+F`) `EU27`. Est-ce un pays ?
4. Regardez la colonne `indic_is`. Voyez-vous plusieurs valeurs différentes ? Nous ne gardons que `I_IU3` : les personnes ayant utilisé Internet dans les 3 derniers mois.
5. Lisez la [notice de réutilisation d'Eurostat](https://ec.europa.eu/eurostat/fr/help/copyright-notice). Que faut-il écrire quand on réutilise les données ?

## Étape 4 · Nettoyer (55 min)

**Nettoyer**, c'est ne garder que ce qui est utile, avec les bons types. Ouvrez `clean.py`. Il contient trois **fonctions** (des blocs de code qui ont un nom). Une fonction rend son résultat avec `return`.

### 4A · Lire le fichier · `load_rows`

**Exemple** (sur un autre sujet : ne le recopiez pas tel quel).
```python
import csv

with open("cities.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print(rows[0])    # {'city': 'Toulouse', 'inhabitants': '500000'}
```

**À vous.** Écrivez la même chose dans `load_rows`, mais ouvrez le fichier donné par `path` et renvoyez la liste avec `return`. `python check.py` → `Step 4A` `[OK]`.
<details markdown="1"><summary>Bloqué ?</summary>

Dans la fonction : `with open(path, ...) as f:`, puis, indenté, `return list(...)`. Gardez `newline=""` et `encoding="utf-8"`.

</details>

### 4B · Filtrer les lignes · `clean_rows`

**Exemple** (sur un autre sujet : ne le recopiez pas tel quel).
```python
result = []
for row in rows:
    if row["city"] == "Paris":      # != means "is different from"
        continue                    # go directly to the next row
    result.append({"name": row["city"],
                   "people": int(row["inhabitants"])})
```

Écrivez dans la boucle `for`, **un test à la fois** :

| TODO | Sauter la ligne si… | Mots à utiliser |
|---|---|---|
| 4B-1 | la colonne `indic_is` est différente de `INDICATOR` | `!=`, `continue` |
| 4B-2 | `geo` n'a pas 2 lettres, **ou** est dans la liste `AGGREGATES` | `len(...)`, `or`, `in` |
| 4B-3 | `OBS_VALUE` est le texte vide `""` | `==` |
| 4B-4 | (on ne saute pas) ajouter un dictionnaire avec les clés `country`, `year`, `value` | `append`, `int`, `float` |

`country` vient de la colonne `geo`, `year` de `TIME_PERIOD` (un entier), `value` de `OBS_VALUE` (un nombre à virgule). Supprimez la ligne `pass`.

**Vérification.** `Step 4B` `[OK]`.
<details markdown="1"><summary>Bloqué ? 4B-1</summary>

`if row["indic_is"] ... INDICATOR:` puis, indenté, `continue`.

</details>

<details markdown="1"><summary>Bloqué ? 4B-2</summary>

`if len(row["geo"]) != 2 or row["geo"] in ...:`

</details>

<details markdown="1"><summary>Bloqué ? 4B-4</summary>

`cleaned.append({"country": row[...], "year": int(row[...]), "value": ...})`

</details>

### 4C · Écrire le fichier propre · `save_rows`

**Exemple** (sur un autre sujet : ne le recopiez pas tel quel).
```python
with open("copy.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "people"])
    writer.writeheader()      # first line: name,people
    writer.writerows(result)  # one line per dictionary
```

**À vous.** Faites de même dans `save_rows` : le fichier est `path`, les trois colonnes sont `country`, `year`, `value`, et les données sont `rows`. Puis lancez :
```text
python clean.py
python check.py
```

**Vérification.** `clean.py` affiche le nombre de lignes lues et gardées. `data/internet_use_clean.csv` commence par `country,year,value` et ne contient pas `EU27_2020`.
<details markdown="1"><summary>Bloqué ?</summary>

`0 rows kept` ? Vérifiez l'orthographe des colonnes et l'indentation : `append` doit être dans la boucle `for`, et `return cleaned` en dehors.

</details>

## Étape 5 · Statistiques (45 min)

Ouvrez `stats.py`.

### 5A · Lire le fichier propre · `load_clean`

Comme en 4A, mais un CSV ne contient que du texte : convertissez `year` en `int` et `value` en `float`. Cette écriture courte construit une liste d'un coup (une **liste en compréhension**) :
```python
rows = [{"name": r["name"], "people": int(r["people"])}
        for r in csv.DictReader(f)]      # inside a "with open(...) as f:" block
```

**À vous.** Les dictionnaires doivent avoir les clés `country`, `year`, `value`. **Vérification :** `Step 5A` `[OK]`.

### 5B · Dernière année · `summarise`

**Exemple** (sur un autre sujet : ne le recopiez pas tel quel).
```python
cities = [{"name": "A", "people": 10}, {"name": "B", "people": 30}]

biggest = max(c["people"] for c in cities)                # 30
only_big = [c for c in cities if c["people"] == biggest]  # [{'name': 'B', ...}]
smallest = min(cities, key=lambda c: c["people"])         # the whole dictionary of A
average = sum(c["people"] for c in cities) / len(cities)  # 20.0
round(3.14159, 2)                                         # 3.14
```

**À vous**, dans cet ordre. Affichez chaque variable pour la vérifier avant de continuer.

1. `latest` : la plus grande année de `rows`.
2. `current` : seulement les lignes de cette année.
3. `lowest` et `highest` : les lignes de `current` ayant la plus petite et la plus grande `value`.
4. `average` : la moyenne des `value` de `current`.
5. Renvoyez un dictionnaire avec les clés `year`, `countries` (nombre de lignes de `current`), `average` (2 décimales), `lowest`, `highest`.
<details markdown="1"><summary>Bloqué ?</summary>

Remplacez `c` par `r`, `cities` par `rows` ou `current`, et `"people"` par `"year"` ou `"value"`. Pour `highest`, `max` s'utilise comme `min`. La dernière ligne commence par `return {"year": latest, "countries": len(current),`.

</details>

*C'est une moyenne simple entre pays. Ce n'est pas le chiffre de l'UE, qui tient compte de la population.*

### 5C · Un pays au fil du temps · `history`

**Exemple** (sur un autre sujet : ne le recopiez pas tel quel).
```python
points = [{"year": c["year"], "people": c["people"]}
          for c in rows if c["name"] == "A"]
points = sorted(points, key=lambda p: p["year"])   # oldest first
```

**À vous.** Renvoyez la liste des `{"year", "value"}` des lignes dont `country` vaut `country`, de la plus ancienne à la plus récente. En haut du fichier, vous pouvez changer `MY_COUNTRY` (France `FR`, Espagne `ES`, Italie `IT`, Allemagne `DE`).
<details markdown="1"><summary>Bloqué ?</summary>

`if r["country"] == country`, puis `return sorted(points, key=...)`.

</details>

### 5D · Enregistrer en JSON

**JSON** est un format texte pour les listes et dictionnaires, très utilisé sur le web.

**Exemple** (sur un autre sujet : ne le recopiez pas tel quel).
```python
import json

with open("city.json", "w", encoding="utf-8") as f:
    json.dump({"name": "A", "people": 10}, f, indent=2)
```

**À vous.** Sous `TODO 5D`, écrivez `result` dans le fichier `OUTPUT`. Puis lancez :
```text
python stats.py
python check.py
```

**Vérification.** Huit `[OK]`. Comparez la dernière valeur de votre pays avec le [tableau Eurostat](https://ec.europa.eu/eurostat/databrowser/view/tin00028/default/table?lang=fr).

## Si vous avez fini (facultatif)

1. Affichez les 5 pays ayant la plus forte valeur la dernière année. Partez de `sorted(current, key=..., reverse=True)`, puis gardez `[:5]`.
2. Demandez le code pays avec `input()` à la place de `MY_COUNTRY`.
3. Ajoutez un dictionnaire des noms de pays (`{"FR": "France"}`) et affichez le nom. La Grèce est codée `EL`.

## Source

Eurostat, jeu `tin00028`. Réutilisation autorisée avec citation de la source. Signalez vos modifications.
