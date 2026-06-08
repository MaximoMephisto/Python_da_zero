# Scrivi una funzione filtra_stringa(s) che:

# separa le parole
# tiene solo quelle con almeno 4 lettere
# le restituisce ordinate
def filtra_stringa(s):
    parole_lunghe = []
    s = s.split()
    for elem in s:
        if len(elem) >= 4:
            parole_lunghe.append(elem)
    return sorted(parole_lunghe)

print(filtra_stringa('il sole splende forte'))
# atteso: ['forte', 'sole', 'splende']