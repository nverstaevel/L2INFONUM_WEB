title: Listes, liens, images, accessibilité
---
`ul` / `ol` sont des listes, `li` un élément. `a href` est un lien : vers un autre site, un autre fichier, ou `#id` dans la même page. `img src alt` affiche une image ; `figure` la regroupe avec sa légende, `figcaption`. L'**accessibilité** : tout le monde peut utiliser la page, grâce au texte `alt`, à des liens explicites, à la langue déclarée.

## Exemple

```html
<nav><ul>
  <li><a href="#books">Books</a></li>
  <li><a href="about.html">About us</a></li>
</ul></nav>
<img src="images/library.jpg" alt="Shelves full of books" width="320" height="180">
<figure>
  <img src="images/library.jpg" alt="Shelves full of books" width="320" height="180">
  <figcaption>Our shelves. Drawing: course team.</figcaption>
</figure>
```

## Erreurs fréquentes

- Chemin d'image faux : il part du dossier de la page.
- Un lien qui dit « cliquez ici ».

## Pour aller plus loin

- Cours : [CM2](cm2.html)
- Recettes : [Une page HTML complète](recipe-page-skeleton.html)
- TD qui l'utilisent : [TD2](td2.html)
- [Toutes les balises HTML et leur résultat](notion-html-tags.html)
- [Toutes les notions](notions.html)
