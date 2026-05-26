# Creare una lista di interi con 8 elementi e riempirlo con numeri casuali 
# compresi tra 1 e 90 senza ripetizioni.
import random

numeri = []

for i in range(8):
    num_random = random.randint(1, 90)
    
    while num_random in numeri:
        num_random = random.randint(1, 90)
        
    numeri.append(num_random)
        
print(numeri)