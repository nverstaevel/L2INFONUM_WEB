title: Terminal et environnement virtuel
---
Un **terminal** est une fenêtre où l'on tape des commandes. Un **paquet** est du code écrit par d'autres, que l'on installe. Un **environnement virtuel** (`.venv`) est un ensemble de paquets réservé à un projet, pour que les projets ne se gênent pas. On le crée une fois, on l'**active** dans chaque nouveau terminal.

## Exemple

```text
cd td5                  # go into a folder
.venv\Scripts\Activate.ps1      # activate (Windows)
source .venv/bin/activate       # activate (macOS, Linux)
python app.py                   # run a script
```

## Erreurs fréquentes

- `ModuleNotFoundError` : l'environnement n'est pas activé (pas de `(.venv)` en début de ligne).
- `FileNotFoundError` : le terminal n'est pas dans le bon dossier.

## Pour aller plus loin

- Cours : [CM1](cm1.html)
- Recettes : [Installer un projet](recipe-venv.html)
- TD qui l'utilisent : [TD1](td1.html), [TD5](td5.html)
- [Toutes les notions](notions.html)
