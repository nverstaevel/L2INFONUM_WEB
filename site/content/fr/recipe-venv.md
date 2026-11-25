title: Installer un projet
---
**Quand l'utiliser :** Démarrer un projet Python.

## Fichiers

`requirements.txt`

```text
flask
requests
```

## Lancer

```text
# Windows
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

**Vous devez voir :** La ligne commence par `(.venv)`.

## À adapter

Ne gardez que les paquets utiles.

- Notions : [Terminal et environnement virtuel](notion-terminal-venv.html)
- [Toutes les recettes](recipes.html)
