# 1. (return) Scrivi doppio(x) che restituisce x moltiplicato per 2.
# Atteso: doppio(5) → 10, doppio(0) → 0.

def doppio(x):
    return x * 2

# 2. (return) Scrivi area_rettangolo(base, altezza) che restituisce l'area.
# Atteso: area_rettangolo(4, 3) → 12, area_rettangolo(5, 5) → 25.
def area_rettangolo(base, altezza):
    return base * altezza

# 3. (senza return) Scrivi saluta(nome) che stampa Ciao <nome>! (non restituisce niente).
# Atteso: saluta("Fra") stampa Ciao Fra!.
def saluta(nome):
    print(f"Ciao! {nome}")
    
# 4. (return) Scrivi maggiore(a, b) che restituisce il più grande tra due numeri.
# Atteso: maggiore(7, 3) → 7, maggiore(2, 9) → 9.
def maggiore(a, b):
    if a > b:
        return a
    else:
        return b
    
# 5. (senza return) Scrivi stampa_pari(n) che stampa tutti i numeri pari da 0 a n incluso, uno per riga.
# Atteso: stampa_pari(6) stampa 0, 2, 4, 6.
def stampa_pari(n):
    for i in range(n+1):
        if i % 2 == 0:
            print(f"- {i}")
            
# 6. (return) Scrivi conta_vocali(s) che restituisce quante vocali ci sono nella stringa.
# Atteso: conta_vocali("ciao") → 3, conta_vocali("xyz") → 0.
def conta_vocali(s):
    vocali = ["a", "e", "i", "o", "u"]
    cont = 0
    for vocale in vocali:
        if vocale in s:
            cont += 1
    return cont

# 7. (senza return) Scrivi tabellina(n) che stampa la tabellina del numero da 1 a 10 nel formato n x i = risultato.
# Atteso: tabellina(3) stampa 3 x 1 = 3, 3 x 2 = 6, ... 3 x 10 = 30.
def tabellina(n):
    for i in range(10+1):
        print(f"{n} x {i} = {n * i}")
# 8. (return) Scrivi fattoriale(n) che restituisce il fattoriale di n (prodotto da 1 a n).
# Atteso: fattoriale(4) → 24, fattoriale(0) → 1.
import math
def fattoriale(n): 
    return math.factorial(n)

# 9. (return) Scrivi solo_positivi(lista) che restituisce una nuova lista con i soli numeri positivi.
# Atteso: solo_positivi([-2, 3, 0, 5, -1]) → [3, 5].
def solo_positivi(lista):
    numeri_positivi = []
    for numero in lista:
        if numero > 0:
            numeri_positivi.append(numero)
    return numeri_positivi
            
# 10. (senza return) Scrivi fizzbuzz(n) che stampa i numeri da 1 a n, ma sostituisce i 
# multipli di 3 con Fizz, i multipli di 5 con Buzz, e i multipli di entrambi con 
# FizzBuzz.
# Atteso: fizzbuzz(5) stampa 1, 2, Fizz, 4, Buzz.
def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0:
            print(f"Fizz {i}")
        if i % 5 == 0:
            print(f"Buzz {i}")
        if i % 3 == 0 and i % 5 == 0:
            print(f"FizzBuzz {i}")

def print_funcioni(funcione):
    print(funcione)
    
def main():
    print_funcioni(doppio(2))
    print_funcioni(area_rettangolo(2, 5))
    saluta("Maximo")
    print_funcioni(maggiore(4, 7))
    stampa_pari(6)
    print_funcioni(conta_vocali("Lorem ipsum"))
    tabellina(3)
    print_funcioni(fattoriale(4))
    numeri = [-1, -2, -5, 0, 2, 3, 4, 7]
    print_funcioni(solo_positivi(numeri))
    fizzbuzz(40)
    
    
main()