title: Lire et écrire des fichiers
---
`with open(...) as f:` ouvre un fichier et le referme tout seul. `"r"` lit (par défaut), `"w"` écrit et **remplace** le fichier. `Path` est une autre façon de manipuler les fichiers. Les chemins partent du dossier depuis lequel vous lancez le script.

## Exemple

```python
from pathlib import Path

Path("data").mkdir(exist_ok=True)          # create a folder
with open("data/hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello")
print(Path("data/hello.txt").read_text(encoding="utf-8"))
```

## Erreurs fréquentes

- Ouvrir avec `"w"` un fichier que l'on voulait seulement lire l'efface.

## Pour aller plus loin

- Cours : [CM1](cm1.html)
- Recettes : [Télécharger un fichier](recipe-download.html) · [Filtrer un fichier CSV](recipe-clean-csv.html)
- TD qui l'utilisent : [TD1](td1.html), [TD8](td8.html)
- [Toutes les notions](notions.html)
