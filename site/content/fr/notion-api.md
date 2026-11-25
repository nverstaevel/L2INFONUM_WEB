title: API JSON
---
Une **API** est un ensemble d'adresses que des programmes utilisent pour obtenir des données. `jsonify` renvoie du JSON. Le **back-end** (serveur) sert les données, le **front-end** (navigateur) les affiche. Renvoyez un message d'erreur et un code d'état quand il n'y a rien.

## Exemple

```python
@app.route("/api/books")
def api_books():
    author = request.args.get("author", "")
    found = [b for b in BOOKS if b["author"] == author]
    if not found:
        return jsonify(error="No book found"), 404
    return jsonify(found)
```

## Erreurs fréquentes

- Oublier `, 404` : l'erreur passe pour un succès.

## Pour aller plus loin

- Cours : [CM7](cm7.html)
- Recettes : [Une API JSON et son graphique](recipe-api-chart.html)
- TD qui l'utilisent : [TD5](td5.html), [TD7](td7.html), [TD9](td9.html)
- [Toutes les notions](notions.html)
