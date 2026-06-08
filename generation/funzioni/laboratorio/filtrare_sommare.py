# Scrivi una funzione somma_pari(numeri) che ritorna la somma di tutti i 
# numeri pari della lista.
def somma_pari(numeri):
    somma = 0
    for num in numeri:
        if num % 2 == 0:
            somma += num
    return somma

print(somma_pari([1, 2, 4, 7, 8]))   # atteso: 14