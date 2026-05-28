import random

carte = []
scartate = []

for i in range(1, 8+1):
    carta = i
    carte.append(carta)
    if i == carta:
        carte.append(carta)

while True:
    posizione_uno = random.randint(1, 8)
    posizione_due = random.randint(1, 8)
    
    if (posizione_uno not in scartate or posizione_due not in scartate) and (posizione_uno == posizione_due):
        print("Coppie trovate!")
        scartate.append(posizione_uno)
        scartate.append(posizione_due)
    else:
        break

print(scartate)
    