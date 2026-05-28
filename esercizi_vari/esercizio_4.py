# Escribe un programa que imprima los 50 primeros números de la sucesión
# de Fibonacci empezando en 0.
# La serie Fibonacci se compone por una sucesión de números en
# la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...

inizio = 1
num_anteriore = 0

for i in range(50):
    if i < inizio:
        num_anteriore = i + inizio
        
    inizio += 1
    print(inizio)
