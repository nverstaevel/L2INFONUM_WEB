title: TD6 · Paramètres, formulaires et sessions
---
**Vendredi 12 février 2027 · 3 heures.** Fichiers de départ : [`td6`](https://github.com/nverstaevel/L2INFONUM_WEB/tree/main/td6).

## Objectif

Construire des pages qui réagissent à la saisie : recherche, filtre et favoris.

**Vous avez réussi si** la recherche par pays et valeur minimale fonctionne, et les favoris persistent d'une page à l'autre.

| Fourni | À vous |
|---|---|
| `app.py` avec le chargement des données, `base.html`, `index.html` | deux gabarits et quatre `TODO` |

## Avant la séance

- [ ] J'ai relu [CM6](cm6.html).
- [ ] Mon CSV nettoyé est dans `data/`.

## Étape 1 · Chaîne de requête (45 min)

Créez `/search`. `request.args.get` lit `?country=FR`. Pas de boucle dans les gabarits : construisez les lignes en Python, assemblez-les et affichez-les dans un bloc `<pre>`, qui conserve les retours à la ligne :

```
results = "\n".join(lines)
# dans le gabarit :
<pre>{{ results }}</pre>
```

**Point de contrôle :** `/search?country=FR` liste les années.

<details><summary>Indice 1</summary><p>`request.args.get("country", "").strip().upper()`</p></details>

## Étape 2 · Formulaire GET et filtre (45 min)

Ajoutez un formulaire `method="get"` pour le pays et une valeur minimale.

**Point de contrôle :** changer le minimum change la liste.

<details><summary>Indice 1</summary><p>`request.args.get("minimum", 0, type=float)`</p></details>
<details><summary>Indice 2</summary><p>Prévoyez le cas sans résultat.</p></details>

## Étape 3 · POST et session (50 min)

Une *session* mémorise des données pour un visiteur dans un *cookie* signé (petit texte conservé par le navigateur). Créez `/favourites` avec `methods=["GET", "POST"]`.

**Point de contrôle :** un pays ajouté est toujours là après une autre page.

<details><summary>Indice 1</summary><p>`request.form.get("country")` lit un champ POST.</p></details>
<details><summary>Indice 2</summary><p>Affectez une nouvelle liste : `session["favourites"] = codes + [code]`.</p></details>
<details><summary>Indice 3</summary><p>Affichez-la avec `", ".join(codes)`.</p></details>

## Étape 4 · Vérifier la saisie (25 min)

N'acceptez que les codes présents dans les données. Ajoutez un bouton pour vider la liste.

**Point de contrôle :** `ZZ` n'est pas ajouté ; chercher `<b>` affiche le texte, pas du gras.

<details><summary>Indice 1</summary><p>Ne désactivez jamais l'échappement : `{{ }}` vous protège.</p></details>

## Extensions

1. Affichez la moyenne des résultats.
2. Conservez les valeurs saisies après envoi.
3. Redirigez après le POST avec `redirect`.
