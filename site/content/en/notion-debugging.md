title: Debugging
---
**Debugging** means finding and fixing a mistake. Reproduce it, read the message (the last line first), decide where it happens (browser or server), change **one** thing, test, write down the cause.

## Example

```text
Traceback (most recent call last):
  File "app.py", line 12, in about      <- where
NameError: name 'jsonfy' is not defined   <- what: read this first
```

## Common mistakes

- Changing several things at once.
- Forgetting to save the file before testing.

## Go further

- Lecture: [CM8](cm8.html)
- Labs using it: [TD7](td7.html), [TD9](td9.html), [TD10](td10.html)
- [All notions](notions.html)
