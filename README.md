KataLog
=======

Scratches which itch?

När jag letar katas för ett team, blir det hela tiden till att googla.
Ofta hamnar jag på Emilys Github, eller går dit, för jag vet ungefär
var en kata ligger. Och därefter kollar jag upp vilka språk katan
är definierad för, genom att se efter vilka "språkmappar" som ligger
i roten.

Istället hade jag velat kunna skriva så här:

```
katalog

  Tennis
  Starter
  MRU
  FSM
  osv.

katalog tennis

  Kata Tennis:
  Full repo name: Tennis Refactoring Kata
  URL: https://github.com/emilybache/...
  Languages: C, C++, JavaScript

katalog add-kata <URL>
Full repo name: ...
Looking up languages... Found Java, JavaScript, Clojure
```

"Databasen" kan vara en enkel katalog.json-fil (som gitignoras).

M.V.P

- implementera add-kata mha click
