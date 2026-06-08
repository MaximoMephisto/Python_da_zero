# Scrivi una funzione conta_uniche(lista) che ritorna quante parole 
# compaiono una sola volta.

# Vincolo: niente dizionari.

def conta_uniche(lista):
    parole_una_volta = 0
    for parola in lista:
        if lista.count(parola) == 1:
            parole_una_volta += 1
    return parole_una_volta
            

print(conta_uniche(['ciao', 'ciao', 'mondo']))   # atteso: 1