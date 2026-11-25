title: Mise en page adaptative et media queries
---
Une page **adaptative** s'ajuste à l'écran. Une **media query** applique des règles sous condition. La ligne `viewport` dans `head` est indispensable sur téléphone.

## Exemple

```css
/* in head: <meta name="viewport" content="width=device-width, initial-scale=1"> */
@media (max-width: 600px) {
  nav ul { flex-direction: column; }
}
```

## Erreurs fréquentes

- La media query placée avant la règle normale : c'est alors la règle normale qui gagne.

## Pour aller plus loin

- Cours : [CM3](cm3.html)
- Recettes : [Barre de navigation adaptative](recipe-nav-bar.html)
- TD qui l'utilisent : [TD3](td3.html), [TD10](td10.html)
- [Toutes les notions](notions.html)
