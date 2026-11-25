title: Contrôle des saisies et échappement
---
Ne faites jamais confiance à ce qu'envoie un visiteur. **Validez** : type attendu, bornes, valeur connue. L'**échappement** affiche les caractères spéciaux comme du texte : `{{ valeur }}` le fait pour vous. Ne le désactivez pas.

## Exemple

```python
code = request.form.get("code", "").strip().upper()
if code in ["FR", "ES"]:      # known values only
    ...
```

## Ce que vous voyez

```text
accepted: FR
refused:  <B>
```

## Erreurs fréquentes

- Construire du HTML en collant la saisie du visiteur dans un texte.

## Pour aller plus loin

- Cours : [CM6](cm6.html)
- Recettes : [Un formulaire de recherche](recipe-search-form.html) · [Mémoriser une liste avec une session](recipe-session-list.html)
- TD qui l'utilisent : [TD5](td5.html), [TD6](td6.html)
- [Flask et ses résultats](notion-flask-ref.html)
- [Toutes les notions](notions.html)
