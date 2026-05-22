# Scrivere un programma che lancia 100 monete e dice quante volte è uscita 
# testa e quante volte è uscita croce.
#quindi per esempio, generare numero random da 1 a 2, se è uno per noi 
# vuol dire testa se è due vuol dire croce
import random

testa = 0
croce = 0
for i in range(100):
    moneta = random.randint(1, 2)
    if moneta == 1:
        testa += 1
    else:
        croce += 1
    print(moneta, end=", ")
print(f"Sono uscite {testa} volte testa, e {croce} volte croce")
