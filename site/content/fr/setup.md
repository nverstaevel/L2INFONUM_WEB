title: Guide d'installation
---
À faire **avant le TD1** si vous utilisez votre propre ordinateur.

## 1. Installer

1. [Python 3](https://www.python.org/downloads/). Sous Windows, cocher *Add Python to PATH*.
2. [Visual Studio Code](https://code.visualstudio.com/) et son extension *Python*.
3. Un navigateur récent (Firefox ou Chrome) avec ses outils de développement.

## 2. Récupérer les fichiers du cours

Sur le [dépôt du cours](https://github.com/nverstaevel/L2INFONUM_WEB), choisir **Code → Download ZIP** puis décompresser.

## 3. Créer un environnement virtuel

Un *environnement virtuel* est un ensemble de paquets Python propre à un projet. Un *terminal* est une fenêtre où l'on tape des commandes. Dans VS Code, ouvrir le dossier `td1`, puis **Terminal → Nouveau terminal**.

Windows (PowerShell) :

```
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS ou Linux :

```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

**Vérification :** l'invite commence par `(.venv)` et `python -c "import requests; print(requests.__version__)"` affiche un numéro.

À partir du TD5, chaque dossier a son `requirements.txt` (Flask) : refaites la partie 3 dans ce dossier. Plus d'aide : [Dépannage](troubleshooting.html).

## Problèmes fréquents

| Problème | À essayer |
|---|---|
| `python` n'est pas reconnu (Windows) | utiliser `py`, ou réinstaller avec *Add Python to PATH* |
| PowerShell refuse `Activate.ps1` | ouvrir un terminal *Invite de commandes* et lancer `.venv\Scripts\activate.bat` |
| `ModuleNotFoundError: requests` | l'environnement n'est pas activé : l'activer puis réinstaller |
| `FileNotFoundError: data/…` | lancer le script depuis le dossier `td1` |
