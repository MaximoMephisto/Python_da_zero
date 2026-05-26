# Data una lista di 5 numeri casuali, crea una nuova lista con i quadrati degli 
# elementi
# Esempio: lista_casuale = [3,8,2,5,6]  -> lista_nuova = [9, 64, 4, 25, 36]
import random
numeri = []
numeri_cuadrado = []

for i in range(5):
    num = random.randint(1, 10)
    numeri.append(num)

for elem in numeri:
    numeri_cuadrado.append(elem**2)

print(numeri)
print(numeri_cuadrado)