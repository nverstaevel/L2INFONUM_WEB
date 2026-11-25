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

## Ce que vous voyez

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;body { margin: 0; font-family: system-ui, Arial, sans-serif; line-height: 1.5; color: #14213d; }&#10;main { max-width: 50rem; margin: 0 auto; padding: 1rem; }&#10;img { max-width: 100%; height: auto; }&#10;table { width: 100%; border-collapse: collapse; }&#10;th, td { border: 1px solid #cbd5e1; padding: 0.5rem; text-align: left; }&#10;th { background: #eef2f7; }&#10;&#10;&lt;/style&gt;&#10;&lt;main&gt;&#10;&lt;h1&gt;City library&lt;/h1&gt;&#10;&lt;table&gt;&lt;tr&gt;&lt;th&gt;Title&lt;/th&gt;&lt;th&gt;Loans&lt;/th&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Emma&lt;/td&gt;&lt;td&gt;12&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;&#10;&lt;/main&gt;"></iframe></div>

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
