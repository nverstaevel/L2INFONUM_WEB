title: Page et tableaux lisibles
---
**Quand l'utiliser :** Une feuille de style simple pour toute page.

## Fichiers

`style.css`

```css
body { margin: 0; font-family: system-ui, Arial, sans-serif; line-height: 1.5; color: #14213d; }
main { max-width: 50rem; margin: 0 auto; padding: 1rem; }
img { max-width: 100%; height: auto; }
table { width: 100%; border-collapse: collapse; }
th, td { border: 1px solid #cbd5e1; padding: 0.5rem; text-align: left; }
th { background: #eef2f7; }
```

## Lancer

```text
# in the head of the page:
<link rel="stylesheet" href="style.css">
```

**Vous devez voir :** Le contenu est centré et le tableau a des bordures simples.

## À adapter

Choisissez vos couleurs et largeurs.

- Notions : [Règles et sélecteurs CSS](notion-css-rules.html) · [Modèle de boîte](notion-css-box.html)
- [Toutes les recettes](recipes.html)
