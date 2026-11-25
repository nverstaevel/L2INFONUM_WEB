title: HTTP: requests, responses, status codes
---
**HTTP** is the language between a **client** (browser, script) and a server. The client sends a **request** for an address (**URL**), the server sends a **response** with a **status code** and a content.

## Example

```text
https://example.org/search?country=FR
|       |           |      └ query string (details)
|       |           └ path
|       └ server
└ protocol

200 OK · 404 not found · 405 method not allowed · 500 server error
```

## Common mistakes

- 404: the address is wrong. 500: the program on the server has an error.

## Go further

- Lecture: [CM1](cm1.html)
- Recipes: [Download a file](recipe-download.html)
- Labs using it: [TD1](td1.html), [TD5](td5.html), [TD7](td7.html)
- [Python, with its result](notion-python-ref.html)
- [All notions](notions.html)
