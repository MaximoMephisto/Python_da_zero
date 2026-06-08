# Scrivi una funzione formatta_numeri(lista) che ritorna una lista di 
# stringhe con i numeri formattati con zfill(5).
def formatta_numeri(lista):
    numeri_formattati = []
    for numeri in lista:
        numeri = str(numeri).zfill(5)
        numeri_formattati.append(numeri)
    return numeri_formattati

print(formatta_numeri([1, 23, 456]))   # atteso: ['00001', '00023', '00456']