# Scrivere un programma che lancia 10 dadi a 6 facce e se la somma dei 
# risultati è maggiore di 35 dice che il risultato è sopra la media.
import random

facce = random.randint(1, 6)
faccia = 0
for i in range(10):
    faccia += facce
if faccia > 35:
    print(f"Il risultato {faccia} è sopra la media.")
else:
    print(f"Il risultato {faccia} non è sopra la media.")
