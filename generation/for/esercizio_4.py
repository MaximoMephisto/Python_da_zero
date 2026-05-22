# Scrivere i primi 11 multipli di un numero inserito da tastiera.
num = int(input("Inserisci numero: "))

for i in range(1, 11+1):
    mult = num * i
    print(f"{num} * {i} = {mult}")