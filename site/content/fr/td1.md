title: TD1 · Python, fichiers et données ouvertes
---
**Vendredi 8 janvier 2027 · 3 heures.** Fichiers de départ : dossier `td1` du [dépôt](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td1).

## Objectif

Télécharger un vrai jeu de données Eurostat, le nettoyer et calculer des statistiques simples. **Conservez vos fichiers :** ils servent aux TD suivants.

**Vous avez réussi si** `data/internet_use_clean.csv` a l'en-tête `country,year,value`, ne contient que des pays, et si `data/summary.json` donne la dernière année et l'historique de votre pays.

| Fourni | À vous |
|---|---|
| trois squelettes de scripts, `requirements.txt` | les lignes `TODO` |

Le code et ses commentaires sont en anglais.

## Avant la séance

- [ ] J'ai relu le [CM1](cm1.html).
- [ ] Python et VS Code sont installés ([guide d'installation](setup.html)).

## Étape 1 · Environnement (30 min)

Suivre la partie 3 du [guide d'installation](setup.html) dans le dossier `td1`.

**Point de contrôle :** `(.venv)` s'affiche et `import requests` fonctionne.

<details><summary>Besoin d'aide ?</summary><p>Voir le tableau Dépannage du guide d'installation.</p></details>

## Étape 2 · Télécharger (30 min)

`requests` est un paquet qui envoie des requêtes HTTP depuis Python. Complétez `download.py`. L'adresse est :

```
https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/tin00028?format=SDMX-CSV&compress=false
```

Lancez `python download.py`.

**Point de contrôle :** `data/internet_use.csv` existe et s'ouvre comme du texte.

<details><summary>Indice 1</summary><p>Un <em>code d'état</em> 200 signifie succès. Il est dans <code>response.status_code</code>.</p></details>
<details><summary>Indice 2</summary><p><code>OUTPUT.write_bytes(...)</code> écrit des octets (le contenu brut) dans un fichier.</p></details>

## Étape 3 · Explorer (30 min)

Ouvrez le fichier dans VS Code. Répondez dans `notes.txt` :

1. Quels sont les noms des colonnes ?
2. Que contiennent `geo`, `TIME_PERIOD` et `OBS_VALUE` ?
3. Trouvez un code `geo` qui n'est pas un pays.
4. Toutes les années sont-elles présentes pour tous les pays ?
5. Qui a produit les données, et que faut-il faire pour les réutiliser ? ([notice Eurostat](https://ec.europa.eu/eurostat/fr/help/copyright-notice))

**Point de contrôle :** cinq réponses.

## Étape 4 · Nettoyer (45 min)

Complétez `clean.py`. Gardez les lignes où `indic_is` vaut `I_IU3` (usage d'internet dans les 3 derniers mois), où `geo` est un pays et `OBS_VALUE` non vide.

**Point de contrôle :** le script affiche le nombre de lignes lues et gardées, et le fichier propre ne contient pas `EU27_2020`.

<details><summary>Indice 1</summary><p><code>csv.DictReader</code> donne un dictionnaire par ligne.</p></details>
<details><summary>Indice 2</summary><p><code>continue</code> passe à la ligne suivante d'une boucle.</p></details>
<details><summary>Indice 3</summary><p><code>csv.DictWriter</code> a besoin de <code>fieldnames</code>, puis <code>writeheader()</code> et <code>writerows()</code>.</p></details>

## Étape 5 · Statistiques (45 min)

Complétez `stats.py` : pour la dernière année, la moyenne, la plus petite et la plus grande valeur ; puis l'historique de votre pays. Enregistrez le tout dans `data/summary.json`.

*La moyenne est une moyenne simple entre pays. Ce n'est pas le chiffre de l'UE, qui tient compte de la population.*

**Point de contrôle :** comparez la dernière valeur de votre pays avec le [tableau Eurostat](https://ec.europa.eu/eurostat/databrowser/view/tin00028/default/table?lang=fr).

<details><summary>Indice 1</summary><p><code>max(r["year"] for r in rows)</code> donne la dernière année.</p></details>
<details><summary>Indice 2</summary><p><code>min(rows, key=lambda r: r["value"])</code> renvoie la ligne entière.</p></details>
<details><summary>Indice 3</summary><p><code>json.dump(result, f, indent=2)</code></p></details>

## Extensions

1. Affichez les 5 premiers pays de la dernière année.
2. Pour chaque pays, calculez l'évolution depuis 2015, en gérant les valeurs absentes.
3. Ajoutez un dictionnaire des noms de pays (`"FR": "France"`). La Grèce est codée `EL`.
4. Demandez le code pays avec `input()`.

## Source

Eurostat, jeu `tin00028`. Réutilisation autorisée avec citation de la source. Signalez vos modifications.
