import random

giochi = 1_000
point = 0
cont = 0
vincite = 0
perse = 0

craps = [2, 3, 12]
        
for i in range(giochi):
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    
    somma = dado_1 + dado_2
    
    if somma == 7 or somma == 11:
        print(f"Hai vinto. \n Il tuo numero: {somma}")
        vincite += 1
        continue
    elif somma in craps:
        print(f"Hai perso. \n Il tuo numero: {somma}")
        perse += 1
        continue
        
    else:
        while True:
            point = somma
        
            dado_1 = random.randint(1, 6)
            dado_2 = random.randint(1, 6)
            
            somma = dado_1 + dado_2

            if somma == point:
                print(f"Hai vinto. \n I tuoi numeri: {somma} e {point}")
                vincite += 1
                break
            elif somma == 7:
                print(f"Hai perso. \n Numero tuo: {point}, numero uscito: {somma}")
                perse += 1
                break
            
print(f"Qta. vincite: {vincite}")
print(f"Qta. perse: {perse}")
        
    