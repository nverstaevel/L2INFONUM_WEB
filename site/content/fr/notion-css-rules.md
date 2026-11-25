title: Règles et sélecteurs CSS
---
Le **CSS** dit quelle apparence ont les éléments. Une règle = un **sélecteur** + des déclarations `propriété: valeur;`. `p` vise des éléments, `.note` une **classe**, `#about` un **identifiant**, `nav a` les liens dans `nav`. En cas de conflit, le sélecteur le plus précis gagne (**spécificité** : id > classe > élément), puis le dernier.

## Exemple

```css
body { font-family: system-ui, sans-serif; color: #14213d; }
.note { color: darkblue; }
nav a { color: white; }
```

## Erreurs fréquentes

- Un `;` ou une `}` oublié casse les règles suivantes.
- La feuille de style n'est pas liée dans `<head>`.

## Pour aller plus loin

- Cours : [CM3](cm3.html)
- Recettes : [Page et tableaux lisibles](recipe-clean-style.html)
- TD qui l'utilisent : [TD3](td3.html)
- [Toutes les notions](notions.html)
