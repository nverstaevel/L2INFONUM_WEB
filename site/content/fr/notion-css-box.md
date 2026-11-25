title: Modèle de boîte
---
Chaque élément est une boîte : contenu, **padding** (intérieur), **bordure**, **margin** (extérieur). Par défaut, largeur visible = width + padding + bordure. `box-sizing: border-box` les inclut dans `width`.

## Exemple

```css
main {
  max-width: 60rem;     /* never wider */
  margin: 0 auto;       /* centred */
  padding: 1rem;        /* inner space */
}
img { max-width: 100%; height: auto; }
```

## Erreurs fréquentes

- Utiliser `width` au lieu de `max-width` : la page dépasse sur téléphone.

## Pour aller plus loin

- Cours : [CM3](cm3.html)
- Recettes : [Page et tableaux lisibles](recipe-clean-style.html)
- TD qui l'utilisent : [TD3](td3.html)
- [Toutes les notions](notions.html)
