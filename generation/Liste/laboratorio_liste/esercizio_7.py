# Creare una lista di 5 elementi casuali da 1 a 20 e stampare su la lista è crescente
import random

numeri = []

for i in range(5):
    num = random.randint(1, 20)
    numeri.append(num)
    
if numeri == sorted(numeri):
    print(f"La lista {numeri} è ordinata")
else:
    print(f"La lista {numeri} non è ordinata")