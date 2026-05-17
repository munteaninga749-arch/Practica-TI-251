# Combinațiile Logice și Verificarea Mapării – Display cu 7 Segmente

## Schema segmentelor

```
 — a —
|     |
f     b
| — g — |
e     c
|     |
 — d —
```

---

## Combinațiile Logice pentru cifrele 0–9

Pentru afișajul cu 7 segmente, fiecare cifră este formată prin aprinderea anumitor segmente.

| Cifră | Segmente aprinse      | Segment stins |
|-------|-----------------------|---------------|
| 0     | a, b, c, d, e, f      | g             |
| 1     | b, c                  | a, d, e, f, g |
| 2     | a, b, d, e, g         | c, f          |
| 3     | a, b, c, d, g         | e, f          |
| 4     | b, c, f, g            | a, d, e       |
| 5     | a, c, d, f, g         | b, e          |
| 6     | a, c, d, e, f, g      | b             |
| 7     | a, b, c               | d, e, f, g    |
| 8     | a, b, c, d, e, f, g   | —             |
| 9     | a, b, c, d, f, g      | e             |

---

## Verificarea Mapării Segmentelor

Maparea segmentelor reprezintă verificarea conexiunii dintre pinii ESP8266 și segmentele display-ului.

### Tabel de mapare

| Segment | Pin ESP8266 |
|---------|-------------|
| a       | D1          |
| b       | D2          |
| c       | D3          |
| d       | D4          |
| e       | D5          |
| f       | D6          |
| g       | D7          |

### Cum se verifică

1. Se aprinde fiecare segment **separat**
2. Se observă dacă segmentul **corect** luminează
3. Se compară cu schema afișajului

**Exemplu:** dacă pinul D1 aprinde segmentul de sus → maparea pentru „a" este corectă.
