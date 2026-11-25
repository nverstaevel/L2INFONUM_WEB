title: HTTP : requêtes, réponses, codes d'état
---
**HTTP** est le langage entre un **client** (navigateur, script) et un serveur. Le client envoie une **requête** vers une adresse (**URL**), le serveur renvoie une **réponse** avec un **code d'état** et un contenu.

## Exemple

```text
https://example.org/search?country=FR
|       |           |      └ query string (details)
|       |           └ path
|       └ server
└ protocol

200 OK · 404 not found · 405 method not allowed · 500 server error
```

## Erreurs fréquentes

- 404 : l'adresse est fausse. 500 : le programme du serveur a une erreur.

## Pour aller plus loin

- Cours : [CM1](cm1.html)
- Recettes : [Télécharger un fichier](recipe-download.html)
- TD qui l'utilisent : [TD1](td1.html), [TD5](td5.html), [TD7](td7.html)
- [Python et ses résultats](notion-python-ref.html)
- [Toutes les notions](notions.html)
