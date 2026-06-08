# Scrivi una funzione sigla(frase) che 
# ritorna l'iniziale maiuscola di ogni parola.
def sigla(frase):
    sigle = ""
    for parole in frase.split():
        sigle += parole[0].upper()
    return sigle

print(sigla('corso di programmazione'))   # atteso: 'CDP'