# Pro version: Creare una lista di 5 elementi casuali da 1 a 20 finché 
# la lista non è crescentee stampare dopo quanti tentativi è stata creata crescente
import random

numeri = []
cont = 0

while True:
    cont += 1
    
    for i in range(5):
        num = random.randint(1, 20)
        numeri.append(num)
        
    if numeri == sorted(numeri):
        break
    else:
        numeri = []

print(f"Per avere la lista {numeri} crescente ci sono voluti {cont} tentativi.")