# Proiect Display cu 7 Segmente – ESP8266

Acest proiect controlează un display cu 7 segmente folosind un microcontroller **ESP8266**.
Afișează cifrele de la 0 la 9 în buclă continuă.

\---

## Schema Display-ului cu 7 Segmente

```
 — a —
|     |
f     b
| — g — |
e     c
|     |
 — d —
```

Fiecare literă (a–g) reprezintă un segment al display-ului:

|Segment|Poziție|
|-|-|
|a|Sus|
|b|Dreapta sus|
|c|Dreapta jos|
|d|Jos|
|e|Stânga jos|
|f|Stânga sus|
|g|Mijloc|

\---

## Secvența de Afișare

Sistemul afișează cifrele în ordine:

```
0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 0 → ...
```

După cifra **9**, sistemul revine automat la **0** și ciclul continuă.

### Cum funcționează

* ESP8266 trimite semnale către display-ul cu 7 segmente
* Fiecare cifră activează anumite segmente:

  * Cifra **1** → segmentele **b** și **c**
  * Cifra **8** → **toate** segmentele

### Tabelul secvenței

|Pas|Cifra afișată|
|-|-|
|1|0|
|2|1|
|3|2|
|4|3|
|5|4|
|6|5|
|7|6|
|8|7|
|9|8|
|10|9|
|11|Revine la 0|

\---

## Tabelul de Adevăr – Segmente Active per Cifră

**Convenție:**

* `1` = segment **aprins**
* `0` = segment **stins**

|Cifră|a|b|c|d|e|f|g|
|-|-|-|-|-|-|-|-|
|0|1|1|1|1|1|1|0|
|1|0|1|1|0|0|0|0|
|2|1|1|0|1|1|0|1|
|3|1|1|1|1|0|0|1|
|4|0|1|1|0|0|1|1|
|5|1|0|1|1|0|1|1|
|6|1|0|1|1|1|1|1|
|7|1|1|1|0|0|0|0|
|8|1|1|1|1|1|1|1|
|9|1|1|1|1|0|1|1|

\---




