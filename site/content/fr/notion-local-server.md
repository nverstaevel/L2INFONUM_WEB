title: Serveur local
---
Un **serveur** est un programme qui attend des requêtes et renvoie des réponses. Un serveur **local** tourne sur votre ordinateur, à l'adresse `localhost` ou `127.0.0.1`. Le nombre après `:` est le **port**, la porte sur laquelle le serveur écoute.

## Exemple

```text
python -m http.server        # serves the files of the folder: http://localhost:8000
python app.py                # Flask server: http://127.0.0.1:5000
Ctrl+C                       # stops the server
```

## Erreurs fréquentes

- Ouvrir le fichier par double-clic au lieu de passer par l'adresse du serveur.
- Lancer le serveur depuis le mauvais dossier (404).

## Pour aller plus loin

- Cours : [CM4](cm4.html)
- Recettes : [Un graphique à partir d'un fichier JSON](recipe-chart-from-json.html)
- TD qui l'utilisent : [TD4](td4.html), [TD5](td5.html)
- [Toutes les notions](notions.html)
