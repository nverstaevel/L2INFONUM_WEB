title: fetch : demander des données
---
`fetch` envoie une requête depuis la page sans la recharger. La réponse arrive plus tard : chaque `then` dit quoi faire à son arrivée. Un 404 n'arrête pas `fetch` : testez le contenu.

## Exemple

```javascript
fetch("data/books.json")
  .then(response => response.json())
  .then(books => {
    console.log(books);
  });
```

## Ce que vous voyez

<div class="preview"><p><strong>Résultat en direct : le code s'exécute vraiment</strong></p><iframe sandbox="allow-scripts" title="Résultat en direct : le code s'exécute vraiment" srcdoc="&lt;!DOCTYPE html&gt;&lt;meta charset=&quot;utf-8&quot;&gt;&lt;style&gt;body{font-family:system-ui,sans-serif;color:#222}&lt;/style&gt;&#10;&#10;&#10;&lt;script&gt;&#10;const FILES = {&quot;data/books.json&quot;: &quot;[{\&quot;title\&quot;: \&quot;Emma\&quot;}]&quot;};&#10;window.fetch = url =&gt; Promise.resolve(new Response(FILES[url] || &#x27;Not found&#x27;, {status: url in FILES ? 200 : 404}));&#10;console.log = value =&gt; { document.body.textContent = &#x27;console: &#x27; + JSON.stringify(value); };&#10;fetch(&quot;data/books.json&quot;)&#10;  .then(response =&gt; response.json())&#10;  .then(books =&gt; {&#10;    console.log(books);&#10;  });&#10;&lt;/script&gt;" style="height:60px"></iframe></div>

## Erreurs fréquentes

- Utiliser les données hors du `then` : elles ne sont pas encore arrivées.
- Page ouverte par double-clic : `fetch` est bloqué.

## Pour aller plus loin

- Cours : [CM4](cm4.html)
- Recettes : [Un graphique à partir d'un fichier JSON](recipe-chart-from-json.html) · [Une API JSON et son graphique](recipe-api-chart.html)
- TD qui l'utilisent : [TD4](td4.html), [TD7](td7.html), [TD9](td9.html)
- [JavaScript et ses résultats](notion-js-ref.html)
- [Toutes les notions](notions.html)
