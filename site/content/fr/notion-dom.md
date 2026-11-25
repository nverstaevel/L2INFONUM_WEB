title: Modifier la page en JavaScript
---
Le navigateur garde la page comme un arbre d'objets (le **DOM**). `document.getElementById` trouve un élément, `textContent` change son texte, `value` lit un champ, `addEventListener` réagit à un clic.

## Exemple

```javascript
const button = document.getElementById("hello");
button.addEventListener("click", () => {
  document.getElementById("message").textContent = "Hello";
});
```

## Ce que vous voyez

<div class="preview"><p><strong>Résultat en direct : le code s'exécute vraiment</strong></p><iframe sandbox="allow-scripts" title="Résultat en direct : le code s'exécute vraiment" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&lt;button id=&quot;hello&quot;&gt;Say hello&lt;/button&gt;&#10;&lt;p id=&quot;message&quot;&gt;...&lt;/p&gt;&#10;&#10;&lt;script&gt;&#10;const button = document.getElementById(&quot;hello&quot;);&#10;button.addEventListener(&quot;click&quot;, () =&gt; {&#10;  document.getElementById(&quot;message&quot;).textContent = &quot;Hello&quot;;&#10;});&#10;&lt;/script&gt;" style="height:100px"></iframe></div>

## Erreurs fréquentes

- L'`id` en JavaScript diffère de celui du HTML : le résultat est `null`.
- Utiliser `textContent`, pas `innerHTML`, pour des données ou une saisie.

## Pour aller plus loin

- Cours : [CM4](cm4.html)
- Recettes : [Une API JSON et son graphique](recipe-api-chart.html)
- TD qui l'utilisent : [TD4](td4.html), [TD7](td7.html)
- [JavaScript et ses résultats](notion-js-ref.html)
- [Toutes les notions](notions.html)
