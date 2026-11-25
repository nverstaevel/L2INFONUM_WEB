title: Gabarits et fichiers statiques
---
Un **gabarit** est un fichier HTML dans `templates/` avec des trous `{{ nom }}` remplis par `render_template`. Dans ce cours : ni boucle ni condition dans les gabarits, Python prépare le texte. CSS, JavaScript et images vont dans `static/`.

## Exemple

```python
# app.py
return render_template("shop.html", city="Toulouse")

# templates/shop.html
# <link rel="stylesheet" href="/static/style.css">
# <h1>Shops in {{ city }}</h1>
```

## Ce que vous voyez

```text
<link rel="stylesheet" href="/static/style.css">
<h1>Shops in Toulouse</h1>
```

## Erreurs fréquentes

- `TemplateNotFound` : le dossier ne s'appelle pas exactement `templates`.
- Valeur non transmise à `render_template` : le trou reste vide.

## Pour aller plus loin

- Cours : [CM5](cm5.html)
- Recettes : [Une application Flask avec un gabarit](recipe-flask-app.html)
- TD qui l'utilisent : [TD5](td5.html), [TD6](td6.html), [TD8](td8.html), [TD9](td9.html)
- [Flask et ses résultats](notion-flask-ref.html)
- [Toutes les notions](notions.html)
