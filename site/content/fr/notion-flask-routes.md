title: Flask et les routes
---
**Flask** est un **framework web** : il reçoit les requêtes et appelle vos fonctions. Une **route** relie une adresse à une fonction avec le **décorateur** `@app.route`. La fonction renvoie la réponse.

## Exemple

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True)     # only on your own computer
```

## Ce que vous voyez

```text
GET /  ->  200
Hello

GET /nothing  ->  404
```

## Erreurs fréquentes

- Deux fonctions portant le même nom.
- Un fichier nommé `flask.py` masque la bibliothèque.
- Une route écrite après `app.run`.

## Pour aller plus loin

- Cours : [CM5](cm5.html)
- Recettes : [Une application Flask avec un gabarit](recipe-flask-app.html)
- TD qui l'utilisent : [TD5](td5.html), [TD8](td8.html)
- [Flask et ses résultats](notion-flask-ref.html)
- [Toutes les notions](notions.html)
