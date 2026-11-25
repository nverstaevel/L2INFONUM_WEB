title: Dépannage
---
Lisez la **dernière ligne** d'une erreur Python et la **première ligne rouge** de la console.

| Problème | À essayer |
|---|---|
| `python` introuvable | utiliser `py` (Windows) ou `python3` |
| `ModuleNotFoundError` | activer l'environnement, puis `pip install` |
| `FileNotFoundError: data/…` | lancer depuis le dossier qui contient `data` |
| Graphique vide, erreur CORS | page ouverte par double-clic : lancer `python -m http.server` |
| `TemplateNotFound` | le fichier doit être dans `templates/` |
| CSS non appliqué avec Flask | fichier dans `static/`, lien `/static/style.css` |
| 404 sur ma route | vérifier l'orthographe, enregistrer, relancer |
| 405 Method Not Allowed | ajouter `methods=["GET", "POST"]` |
| `RuntimeError … secret key` | définir `app.secret_key` |
| Port 5000 occupé | arrêter l'autre serveur, ou `app.run(debug=True, port=5001)` |
| Modifications invisibles | recharger avec Ctrl+Maj+R (Cmd+Maj+R) |

Une erreur Python incomprise ? Voir les exemples dans [Lire un message d'erreur](notion-python-ref.html#lire-un-message-derreur).
