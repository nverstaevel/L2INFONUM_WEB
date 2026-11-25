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

## Ce que vous voyez

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;main {&#10;  max-width: 60rem;     /* never wider */&#10;  margin: 0 auto;       /* centred */&#10;  padding: 1rem;        /* inner space */&#10;}&#10;img { max-width: 100%; height: auto; }&#10;main { background: #eef2f7; }&#10;&lt;/style&gt;&#10;&lt;main&gt;&lt;p&gt;The content of main, never wider than 60rem, centred, with inner space.&lt;/p&gt;&lt;/main&gt;"></iframe></div>

## Erreurs fréquentes

- Utiliser `width` au lieu de `max-width` : la page dépasse sur téléphone.

## Pour aller plus loin

- Cours : [CM3](cm3.html)
- Recettes : [Page et tableaux lisibles](recipe-clean-style.html)
- TD qui l'utilisent : [TD3](td3.html)
- [CSS et ses résultats](notion-css-ref.html)
- [Toutes les notions](notions.html)
