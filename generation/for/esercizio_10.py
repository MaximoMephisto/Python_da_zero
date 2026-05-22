#chiedere all'utente quale numero di dado sceglie
#simulare il lancio di 100 dadi e stampare quante volte ha vinto
import random

num = int(input("Inserisci numero: "))
while num < 1 or num > 6:
    num = int(input("Errore, Inserisci numero di dado giusto: "))

vincita = 0

for i in range(100):
    facce = random.randint(1, 6)
    if num == facce:
        vincita += 1
print(f"Il giocatore ha vinto {vincita} volte con il numero {num}")