title: GET et POST
---
**GET** demande une information ; les données sont dans l'adresse. **POST** envoie des données qui modifient quelque chose sur le serveur ; elles sont dans le corps de la requête. Flask lit GET avec `request.args`, POST avec `request.form`.

## Exemple

```python
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        item = request.form.get("item", "")
    return render_template("add.html")
```

## Ce que vous voyez

```text
GET /add  ->  200
<p>Add an item</p>

POST /add  data={'item': 'apple'}  ->  200
<p>Add an item</p>

DELETE /add  ->  405
```

## Erreurs fréquentes

- Erreur 405 : `methods` manque.
- `request.args` utilisé pour un formulaire POST.

## Pour aller plus loin

- Cours : [CM6](cm6.html)
- Recettes : [Mémoriser une liste avec une session](recipe-session-list.html)
- TD qui l'utilisent : [TD6](td6.html)
- [Flask et ses résultats](notion-flask-ref.html)
- [Toutes les notions](notions.html)
