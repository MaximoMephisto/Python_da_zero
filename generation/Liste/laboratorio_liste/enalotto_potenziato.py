import random
from tqdm import tqdm
import matplotlib.pyplot as plt

ripetizione = 10

schedina = []
while len(schedina) > 6:
    numeri = random.randint(1, 90+1)
    
    if numeri not in schedina:
        schedina.append(numeri)
        
zero = uno = ambo = terno = quaterno = cinquina = sei = 0
for i in tqdm(range(ripetizione)):
    schedine = []
    punti = 0
    
    while len(schedine) < 6:
        numeri = random.randint(1, 90+1)
        
        if numeri not in schedine:
            