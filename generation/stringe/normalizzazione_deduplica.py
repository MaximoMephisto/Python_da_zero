# Crea una nuova lista puliti con elementi normalizzati (spazi rimossi ai lati, tutto minuscolo).
# Crea una lista unici che contenga ogni prodotto una sola volta
# Crea due liste parallele (difficile):
# voci (gli elementi unici, in ordine)
# conteggi (quanti volte compare ogni elemento in puliti, stesso indice di voci)
# Stampare la lista unici ordinata`.

prodotti = ["  Mela", "pera", "BANANA", "mela ", " Pera ", "kiwi", "banana", "Ananas", "ananas  ", "PESCA", "pesca"]

prodotti_puliti = []

for prodotto in prodotti:
    prodotto = prodotto.lower()
    prodotto = prodotto.replace(" ", "")
    prodotti_puliti.append(prodotto)

prodotti_unici = []
conteggio = []

for prodotto in prodotti_puliti:
    conto = prodotti_puliti.count(prodotto)
    if prodotto not in prodotti_unici:
        prodotti_unici.append(prodotto)
        conteggio.append(conto)
        
print(f"Puliti -> {prodotti_puliti}")
print(f"Unici / Voci -> {prodotti_unici}")
print("-------------------------")
print(f"Voci -> {prodotti_unici}")
print(f"Conteggi - > {conteggio}")
print("-------------------------")
