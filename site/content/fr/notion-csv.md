title: Fichiers CSV
---
Un fichier **CSV** est un tableau écrit en texte : une ligne par ligne du tableau, des valeurs séparées par des virgules, les noms des colonnes sur la première ligne. Le module `csv` de Python lit chaque ligne comme un dictionnaire. **Tout ce qui est lu est du texte** : convertissez les nombres.

## Exemple

```python
import csv

with open("books.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print(rows[0]["title"])
```

## Erreurs fréquentes

- `"10" > "9"` vaut False : les textes ne se comparent pas comme des nombres. Utilisez `int` ou `float`.
- Oublier `newline=""` (lignes vides sous Windows).

## Pour aller plus loin

- Cours : [CM1](cm1.html)
- Recettes : [Filtrer un fichier CSV](recipe-clean-csv.html)
- TD qui l'utilisent : [TD1](td1.html), [TD8](td8.html)
- [Toutes les notions](notions.html)
