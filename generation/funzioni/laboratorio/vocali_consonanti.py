# Scrivi una funzione conta_vocali_consonanti(s) che ritorna due numeri: 
# uno per le vocali, uno per le consonanti.

# Nota: gli spazi non contano come consonanti.
def conta_vocali_consonanti(s):
    cont_vocali = 0
    cont_consonanti = 0
    vocali = ["a", "e", "i", "o", "u"]
    for lettere in s.lower():
        if lettere.isalpha():
            if lettere in vocali:
                cont_vocali += 1
            else:
                cont_consonanti += 1
            
    return cont_vocali, cont_consonanti

vocali, consonanti = conta_vocali_consonanti('ciao mondo')
print('vocali =', vocali, '| consonanti =', consonanti)
# atteso: vocali = 5 | consonanti = 4