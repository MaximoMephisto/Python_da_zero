nomi = ["Marco", "Giulia", "Luca", "Marco", "Sofia", "Alessandro", "Giulia", "Chiara", "Marco", "Martina",
        "Andrea", "Sara", "Luca", "Elena", "Chiara", "Alice", "Marco", "Giulia", "Simone", "Sara",
        "Federico", "Alice", "Tommaso", "Aurora", "Luca", "Sofia", "Marco", "Giulia", "Stefano", "Sara"]

hard_nomi = {}
nomi_non_duplicati = []

cont = 0
for elem in nomi:
    
    if elem in hard_nomi:
        hard_nomi[elem] += 1
    else:
        hard_nomi[elem] = 1
    
    if elem not in nomi_non_duplicati:
        nomi_non_duplicati.append(elem)

print(hard_nomi)
print(nomi_non_duplicati)
#creare nuove lista con:
# HARD: contare ogni nome quante volte appare
# creare lista nomi senza duplicati