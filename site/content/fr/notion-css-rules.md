title: Règles et sélecteurs CSS
---
Le **CSS** dit quelle apparence ont les éléments. Une règle = un **sélecteur** + des déclarations `propriété: valeur;`. `p` vise des éléments, `.note` une **classe**, `#about` un **identifiant**, `nav a` les liens dans `nav`. En cas de conflit, le sélecteur le plus précis gagne (**spécificité** : id > classe > élément), puis le dernier.

## Exemple

```css
body { font-family: system-ui, sans-serif; color: #14213d; }
.note { color: darkblue; }
nav a { color: white; }
```

## Ce que vous voyez

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;body { font-family: system-ui, sans-serif; color: #14213d; }&#10;.note { color: darkblue; }&#10;nav a { color: white; }&#10;nav { background: #14213d; padding: 8px; }&#10;&lt;/style&gt;&#10;&lt;nav&gt;&lt;a href=&quot;#&quot;&gt;A link in nav (white)&lt;/a&gt;&lt;/nav&gt;&#10;&lt;p class=&quot;note&quot;&gt;A paragraph with class=&quot;note&quot;.&lt;/p&gt;&#10;&lt;p&gt;A paragraph.&lt;/p&gt;"></iframe></div>

## Erreurs fréquentes

- Un `;` ou une `}` oublié casse les règles suivantes.
- La feuille de style n'est pas liée dans `<head>`.

## Pour aller plus loin

- Cours : [CM3](cm3.html)
- Recettes : [Page et tableaux lisibles](recipe-clean-style.html)
- TD qui l'utilisent : [TD3](td3.html)
- [CSS et ses résultats](notion-css-ref.html)
- [Toutes les notions](notions.html)
