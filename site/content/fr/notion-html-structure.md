title: Structure, balises sémantiques, validation
---
`head` contient les informations sur la page, `body` ce qui est affiché. Les balises **sémantiques** disent ce qu'est une partie : `header`, `nav`, `main`, `section`, `footer`. Un seul `h1` par page, puis `h2`, `h3` dans l'ordre. Le [validateur du W3C](https://validator.w3.org/#validate_by_input) trouve les erreurs.

## Exemple

```html
<header><h1>City library</h1></header>
<main>
  <section id="books">
    <h2>Books</h2>
  </section>
</main>
<footer><p>Source: ...</p></footer>
```

## Erreurs fréquentes

- Choisir un titre pour sa taille et non pour son niveau.

## Pour aller plus loin

- Cours : [CM2](cm2.html)
- Recettes : [Une page HTML complète](recipe-page-skeleton.html)
- TD qui l'utilisent : [TD2](td2.html), [TD10](td10.html)
- [Toutes les balises HTML et leur résultat](notion-html-tags.html)
- [Toutes les notions](notions.html)
