# Le tre righe di partenza del tuo esercizio
parola = " Data Engineer "
numeri = [5, 3, 9, 1]
listino = {"mouse": 25.0, "tastiera": 45.0}

print(type(parola))
print(type(numeri))
print(type(listino))
print(parola.strip())
print(parola.strip().upper())
print(parola.count('a'))
print(sorted(numeri))
print(list(listino.keys()))
print(listino["mouse"])

"""
1. Nella riga parola.strip() : qual è l'oggetto e qual è il metodo?
RISPOSTA: L'oggetto è 'parola' e il metodo è 'strip()'.

2. Dopo aver eseguito parola.strip() , la variabile parola contiene ancora gli spazi oppure no?
RISPOSTA: Sì, contiene ancora gli spazi. Le stringhe in Python sono immutabili. Il metodo .strip() non modifica la variabile originale, ma restituisce un valore nuovo che abbiamo stampato al volo. Se stampassimo di nuovo 'parola', gli spazi sarebbero ancora lì.

3. Per ordinare la lista hai usato un metodo di numeri oppure una funzione che riceve numeri? Che differenza c'è fra le due scritture?
RISPOSTA: Ho usato la funzione sorted(numeri), che riceve la lista come argomento. 
La differenza è che la funzione sorted(...) crea e restituisce una nuova lista ordinata senza modificare quella originale (ideale per essere stampata direttamente dentro print). Il metodo numeri.sort() invece modifica la lista originale sul posto e restituisce None, quindi non si può stampare direttamente.
"""

