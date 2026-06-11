def conta_vocali(testo):
    cont = 0
    for lettere in testo:
        if lettere.lower() in "aeiouàéù":
            cont += 1
    
    return cont

test = [
    # Casi base
    ("ciao",        3),    # i, a, o -> 3? NO: c-i-a-o = i,a,o = 3
    ("python",      1),    # o
    ("aeiou",       5),    # tutte
    ("AEIOU",       5),    # maiuscole (case-insensitive)

    # Stringhe senza vocali
    ("",            0),    # stringa vuota
    ("xyz",         0),    # nessuna vocale
    ("bcdfg",       0),    # solo consonanti

    # Maiuscole/minuscole miste
    ("CiAo",        3),    # i, a, o (case-insensitive)? -> i,a,o = 3
    ("Python",      1),    # o

    # Spazi e caratteri speciali (non contano)
    ("a e i o u",   5),    # spazi ignorati
    ("h3ll0!",      0),    # numeri/simboli non sono vocali
    ("ciao, mondo", 5),    # i,a,o + o = 5

    # Vocali ripetute
    ("aaa",         3),
    ("booo",        3),

    # Accenti (con questa versione NON vengono contati)
    ("perché",      2),    # e, e -> "perché": e,e = 2 (la é non conta)
    ("città",       2),    # i (la à non conta)
    ("giù",       2),    # i (la à non conta)
]

passati = 0
falliti = 0

for i, (inp, atteso) in enumerate(test, 1):
    ottenuto = conta_vocali(inp)
    if ottenuto == atteso:
        passati += 1
        print(f"[{i:02d}] ✅ conta_vocali({inp!r}) = {ottenuto}")
    else:
        falliti += 1
        print(f"[{i:02d}] ❌ conta_vocali({inp!r}) = {ottenuto}  (atteso {atteso})")

print("-" * 50)
print(f"Totale: {len(test)}  |  Passati: {passati}  |  Falliti: {falliti}")
print(f"Percentuale successo: {passati / len(test) * 100:.1f}%")