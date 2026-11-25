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

## Ce que vous voyez

<div class="preview"><p><strong>Résultat dans le navigateur</strong> · pleine largeur (plus de 600px sur ordinateur)</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;nav ul { display: flex; gap: 1rem; list-style: none; padding: 0; }&#10;/* in head: &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt; */&#10;@media (max-width: 600px) {&#10;  nav ul { flex-direction: column; }&#10;}&#10;&lt;/style&gt;&#10;&lt;nav&gt;&lt;ul&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Home&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Books&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Contact&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/nav&gt;"></iframe></div><div class="preview"><p><strong>Résultat dans le navigateur</strong> · 320px de large, comme un téléphone</p><iframe sandbox="allow-same-origin" title="Résultat dans le navigateur" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;base target=&quot;_blank&quot;&gt;&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;&#10;&lt;style&gt;&#10;nav ul { display: flex; gap: 1rem; list-style: none; padding: 0; }&#10;/* in head: &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt; */&#10;@media (max-width: 600px) {&#10;  nav ul { flex-direction: column; }&#10;}&#10;&lt;/style&gt;&#10;&lt;nav&gt;&lt;ul&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Home&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Books&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;#&quot;&gt;Contact&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/nav&gt;" style="width:320px;max-width:100%"></iframe></div>

## Erreurs fréquentes

- La media query placée avant la règle normale : c'est alors la règle normale qui gagne.

## Pour aller plus loin

- Cours : [CM3](cm3.html)
- Recettes : [Barre de navigation adaptative](recipe-nav-bar.html)
- TD qui l'utilisent : [TD3](td3.html), [TD10](td10.html)
- [CSS et ses résultats](notion-css-ref.html)
- [Toutes les notions](notions.html)
