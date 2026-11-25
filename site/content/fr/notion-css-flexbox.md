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

## Ce que vous voyez

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · liens inactifs ici</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;nav ul {&#10;  display: flex;&#10;  gap: 1rem;&#10;  flex-wrap: wrap;&#10;  list-style: none;&#10;  padding: 0;&#10;}&#10;&lt;/style&gt;&#10;&lt;nav&gt;&lt;ul&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Home&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Books&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Contact&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/nav&gt;"></iframe></div>

## Erreurs fréquentes

- `display: flex` écrit sur les enfants au lieu du parent.

## Pour aller plus loin

- Cours : [CM3](cm3.html)
- Recettes : [Barre de navigation adaptative](recipe-nav-bar.html)
- TD qui l'utilisent : [TD3](td3.html), [TD9](td9.html)
- [CSS et ses résultats](notion-css-ref.html)
- [Toutes les notions](notions.html)
