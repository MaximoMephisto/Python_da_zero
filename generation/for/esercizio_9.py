# Scrivere un programma che chiede un numero all’utente poi estrae 5 
# numeri compresi tra 1 e 90 compresi (tipo la tombola) e dice se è 
# uscito il numero inserito dall’utente.
import random

num = int(input("Inserisci numero: "))

risultato = 0

for i in range(5):
    numeri = random.randint(1, 90)
    if num == numeri:
        risultato = 1
    print(f"I numeri: {numeri}")
    
if risultato == 1:
    print(f"Il numero {num} inserito dal utente è uscito.")
else:
    print(f"Il numero non è uscito.")

