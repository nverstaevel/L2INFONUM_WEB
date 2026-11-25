title: Un README de projet
---
**Quand l'utiliser :** Documenter le mini-projet.

## Fichiers

`README.md`

```text
# Library loans

## Question
How do loans change over the year?

## Data
- Source: (link)
- Producer: City library (invented example)
- Licence: (name of the licence)
- Date of download:
- Changes made: kept two columns

## Run
python -m venv .venv
(activate it)
python -m pip install -r requirements.txt
python app.py

## Routes
| Route | Method | Role |
|---|---|---|
| / | GET | chart page |
| /api/loans?branch=north | GET | JSON data |

## Help received
AI tool used to explain an error message.
```

## Lancer

```text
# nothing to run
```

**Vous devez voir :** Une autre personne peut lancer le projet.

## À adapter

Écrivez vos propres informations, jamais une licence que vous n'avez pas lue.

- Notions : [README et dossier de projet](notion-readme.html) · [Données ouvertes et licences](notion-open-data.html)
- [Toutes les recettes](recipes.html)
