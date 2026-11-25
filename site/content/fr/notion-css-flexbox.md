title: Flexbox
---
**Flexbox** place les enfants d'une boîte en ligne ou en colonne. On écrit `display: flex` sur le **parent**. `gap` est l'espace entre les enfants, `justify-content` agit dans le sens de la ligne, `align-items` en travers.

## Exemple

```css
nav ul {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  list-style: none;
  padding: 0;
}
```

## Erreurs fréquentes

- `display: flex` écrit sur les enfants au lieu du parent.

## Pour aller plus loin

- Cours : [CM3](cm3.html)
- Recettes : [Barre de navigation adaptative](recipe-nav-bar.html)
- TD qui l'utilisent : [TD3](td3.html), [TD9](td9.html)
- [Toutes les notions](notions.html)
