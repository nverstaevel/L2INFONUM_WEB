title: Télécharger un fichier
---
**Quand l'utiliser :** Récupérer un fichier de données sur le web avec Python.

## Fichiers

`get_file.py`

```python
from pathlib import Path

import requests

URL = "https://raw.githubusercontent.com/pallets/flask/main/README.md"   # any file address
OUTPUT = Path("data/flask_readme.md")

response = requests.get(URL, timeout=60)
if response.status_code != 200:
    raise SystemExit(f"Failed: status {response.status_code}")
OUTPUT.parent.mkdir(exist_ok=True)
OUTPUT.write_bytes(response.content)
print("Saved", OUTPUT)
```

## Lancer

```text
python get_file.py
```

**Vous devez voir :** Le fichier apparaît dans le dossier `data`.

## À adapter

Changez l'adresse et le nom du fichier. Vérifiez la licence.

- Notions : [HTTP : requêtes, réponses, codes d'état](notion-http.html) · [Lire et écrire des fichiers](notion-python-files.html) · [Données ouvertes et licences](notion-open-data.html)
- [Toutes les recettes](recipes.html)
