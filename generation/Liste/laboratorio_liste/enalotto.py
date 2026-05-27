import random
import matplotlib.pyplot as plt

ripetizioni_schede = 100

schedina = []
super_enalotto = []

storico = []
estrazioni = []

zero = uno = ambo = terno = quaterno = cinquina = sei = 0

for i in range(6):
    num_schedina = random.randint(1, 90)
    
    if num_schedina not in schedina:
        schedina.append(num_schedina)
    
    
for i in range(ripetizioni_schede):
  
    super_enalotto = []
    punti = 0
    
    while len(super_enalotto) < 6:
        numeri_enalotto = random.randint(1, 90)
            
        if numeri_enalotto not in super_enalotto:
            super_enalotto.append(numeri_enalotto)
            estrazioni.append(numeri_enalotto)
            
    for elem in schedina:
        if elem in super_enalotto:
            punti += 1
        
    if punti == 0:
        zero += 1
    elif punti == 1:
        uno += 1    
    elif punti == 2:
        ambo += 1 
    elif punti == 3:
        terno += 1
    elif punti == 4:
        quaterno += 1
    elif punti == 5:
        cinquina += 1
    elif punti == 6:
        sei += 1

perc_zero = (zero / ripetizioni_schede) * 100
perc_uno = (uno / ripetizioni_schede) * 100
perc_ambo = (ambo / ripetizioni_schede) * 100
perc_terno = (terno / ripetizioni_schede) * 100
perc_quaterno = (quaterno / ripetizioni_schede) * 100
perc_cinquina = (cinquina / ripetizioni_schede) * 100
perc_sei = (sei / ripetizioni_schede) * 100

probabilita_zero = 0.5588 * 100
probabilita_uno = 0.3795 * 100
probabilita_ambo = 0.02985 * 100
probabilita_terno = 0.002747 * 100
probabilita_quaterno = 0.0000958 * 100
probabilita_cinquina = 0.00000135 * 100
probabilita_sei = 0.00000000161 * 100

print("\n ======= \n")
print(f"Schedina: {schedina}")
print(f"Ambo: {ambo} volte, in percentuale: {round(perc_ambo, 2)}%  ")
print(f"terno: {terno} volte, in percentuale: {round(perc_terno, 2)}% ")
print(f"Quaterno: {quaterno} volte, in percentuale: {round(perc_quaterno, 2)}% ")
print(f"Cinquina: {cinquina} volte, in percentuale: {round(perc_cinquina, 2)}% ")
print(f"Sei: {sei} volte, in percentuale: {round(perc_sei, 2)}% ")
print("\n ======= \n")

if perc_zero > probabilita_zero:
    print(f"Abbiamo passato la probabilita per {perc_zero - probabilita_zero}")
else:
    print(f"Stiamo sotto la probabilita per {probabilita_zero - perc_zero}")

if perc_uno > probabilita_uno:
    print(f"Abbiamo passato la probabilita per {perc_uno - probabilita_uno}")
else:
    print(f"Stiamo sotto la probabilita per {probabilita_uno - perc_uno}")

if perc_ambo > probabilita_ambo:
    print(f"Ambo: Abbiamo passato la probabilita per {perc_ambo - probabilita_ambo}")
else:
    print(f"Ambo: Stiamo sotto la probabilita per {probabilita_ambo - perc_ambo}")

if perc_terno > probabilita_terno:
    print(f"Terno: Abbiamo passato la probabilita per {perc_terno - probabilita_terno}")
else:
    print(f"Terno: Stiamo sotto la probabilita per {probabilita_terno - perc_terno}")
    
if perc_quaterno > probabilita_quaterno:
    print(f"Quaterno: Abbiamo passato la probabilita per {round(perc_quaterno - probabilita_quaterno, 2)}")
else:
    print(f"Quaterno: Stiamo sotto la probabilita per {round(probabilita_quaterno - perc_quaterno, 2)}")
    
if perc_cinquina > probabilita_cinquina:
    print(f"Cinquina: Abbiamo passato la probabilita per {round(perc_cinquina - probabilita_cinquina, 2)}")
else:
    print(f"Cinquina: Stiamo sotto la probabilita per {round(probabilita_cinquina - perc_cinquina, 2)}")
    
if perc_sei > probabilita_sei:
    print(f"Sei: Abbiamo passato la probabilita per {round(perc_sei - probabilita_sei, 2)}")
else:
    print(f"Sei: Stiamo sotto la probabilita per {round(probabilita_sei - perc_sei, 2)}")    

print("\n ======= \n")

cont = 0
for elem in estrazioni:
    
    storico.append(elem)
    
    if cont == 7:
        storico.append("Numeri giocati: ")
        cont = 0
    cont += 1
        
cont = 0
for elem in storico:
    print(elem, end=" ")
    cont += 1
    
    if cont % 8 == 0:
        print("\n")


num_piu_estrato = qta_estrato = num_meno_estrato = fortunati = sfortunati = 0
qta_meno_estrato = 1_000_000

num_fortunati = []
num_sfortunati = []

for elem in estrazioni:
    
    cont = 0
    
    for num in estrazioni:
        if num == elem:
            cont += 1
    
    if cont > qta_estrato:
        qta_estrato = cont
        num_piu_estrato = elem
        
    if cont < qta_meno_estrato:
        qta_meno_estrato = cont
        num_meno_estrato = elem
    
for i in range(5):
    qta_estrato = -1
    num_piu_estrato = -1
    
    for elem in estrazioni:
        if elem not in num_fortunati:
            cont = 0
        
            for num in estrazioni:
                if num == elem:
                    cont += 1
            
            if cont > qta_estrato:
                qta_estrato = cont
                num_piu_estrato = elem
            
    if num_piu_estrato not in num_fortunati:
        fortunati = num_piu_estrato
        num_fortunati.append(fortunati)  

for i in range(5):
    qta_meno_estrato = 1_000_000
    
    for elem in estrazioni:
        if elem not in num_sfortunati:
            cont = 0
        
            for num in estrazioni:
                if num == elem:
                    cont += 1
            
            if cont < qta_meno_estrato:
                qta_meno_estrato = cont
                num_meno_estrato = elem
            
    if num_meno_estrato not in num_sfortunati:
        sfortunati = num_meno_estrato
        num_sfortunati.append(sfortunati) 
    
print("\n ======= \n")
print(f"\n Numero piu estrato: {num_piu_estrato} ripetuto {qta_estrato} volte")
print(f"\n Numero meno estrato: {num_meno_estrato} ripetuto {qta_meno_estrato} volte")
print(f"\n I numeri fortunati sono: {num_fortunati}")
print(f"\n I numeri meno fortunati sono: {num_sfortunati}")
print("\n ======= \n")

qta_uscite = []
num_presi = []
cont = 0

for elem in estrazioni:
    if elem not in num_presi:
        
        num_presi.append(elem)
        cont = 0
        
        for num in estrazioni:
            if elem == num:
                cont += 1    
            
        qta_uscite.append("Numero: ")
        qta_uscite.append(elem)
        qta_uscite.append("Qta. uscito: ")
        qta_uscite.append(cont)

cont = 0
for elem in qta_uscite:
    print(elem, end=" ")
    cont += 1
    if cont % 4 == 0:
        print("\n")

categorie = ['0', '1', 'Ambo', 'Terno', 'Quaterno', 'Cinquina', 'Sei']
teoriche = [55.88, 37.95, 2.985, 0.2747, 0.00958, 0.000135, 0.00000016]
simulate = [perc_zero, perc_uno, perc_ambo, perc_terno, perc_quaterno, perc_cinquina, perc_sei]  # le percentuali calcolate dalla simulazione

x = range(len(categorie))
plt.bar([i - 0.2 for i in x], teoriche, width=0.4, label='Teorica')
plt.bar([i + 0.2 for i in x], simulate, width=0.4, label='Simulata')
plt.yscale('log')
plt.xticks(x, categorie)
plt.ylabel('% (scala logaritmica)')
plt.legend()
plt.title('SuperEnalotto: teorico vs simulato (1M estrazioni)')
plt.show()