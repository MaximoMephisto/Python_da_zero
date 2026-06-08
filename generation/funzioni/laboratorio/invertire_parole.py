# Scrivi una funzione inverti_parole_lunghe(lista) che inverte solo le parole con più di 4 lettere.
def inverti_parole_lunghe(lista):
    parole_invertite = []
    for parole in lista:
        if len(parole) > 4:
            parole_invertite.append(parole[::-1])
        if len(parole) <= 4:
            parole_invertite.append(parole)
    return parole_invertite

print(inverti_parole_lunghe(['casa', 'elefante', 'sole', 'programma']))