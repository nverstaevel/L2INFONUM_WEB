title: Déboguer
---
**Déboguer**, c'est trouver et corriger une erreur. Reproduire, lire le message (la dernière ligne d'abord), localiser (navigateur ou serveur), changer **une seule** chose, tester, noter la cause.

## Exemple

```text
Traceback (most recent call last):
  File "app.py", line 12, in about      <- where
NameError: name 'jsonfy' is not defined   <- what: read this first
```

## Erreurs fréquentes

- Changer plusieurs choses à la fois.
- Oublier d'enregistrer avant de tester.

## Pour aller plus loin

- Cours : [CM8](cm8.html)
- TD qui l'utilisent : [TD7](td7.html), [TD9](td9.html), [TD10](td10.html)
- [Toutes les notions](notions.html)
