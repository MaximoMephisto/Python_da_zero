import random
from tqdm import tqdm
import matplotlib.pyplot as plt

ripetizioni_schede = 100    # Quantità di volte che si ripete il codice

schedina = []

storico = []
estrazioni = []

liste_schede = []

zero = uno = ambo = terno = quaterno = cinquina = sei = 0   # Tutte le variabile sono uguale a zero

# Se la schedina ha meno di 6 dati, gli inserisci verificando che non si ripetono
while len(schedina) < 6:
    num_schedina = random.randint(1, 90)
    
    if num_schedina not in schedina:
        schedina.append(num_schedina)
    

# Si inizia un ciclo che si repite un tot di volte
for i in tqdm(range(ripetizioni_schede)):
    
    # Si crea una lista con 6 dati un tot di volte
    super_enalotto = [] 
    punti = 0
    
    while len(super_enalotto) < 6:
        numeri_enalotto = random.randint(1, 90)
            
        if numeri_enalotto not in super_enalotto:
            super_enalotto.append(numeri_enalotto)
            estrazioni.append(numeri_enalotto)
    
    liste_schede.append(super_enalotto)
            
    # Se qualcuno degli elementi in schedina si trova anche dentro il super
    # enalotto, somma un punto
    for elem in schedina:
        if elem in super_enalotto:
            punti += 1
    
    # Separa i punti per ogni vincita
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

# Premio vincita
premio_ambo = 5
premio_terno = 25
premio_quaterna = 300
premio_cinquina = 32000
premio_sei = 170800000

# calcola le percentuali delle uscite
perc_zero = (zero / ripetizioni_schede) * 100
perc_uno = (uno / ripetizioni_schede) * 100
perc_ambo = (ambo / ripetizioni_schede) * 100
perc_terno = (terno / ripetizioni_schede) * 100
perc_quaterno = (quaterno / ripetizioni_schede) * 100
perc_cinquina = (cinquina / ripetizioni_schede) * 100
perc_sei = (sei / ripetizioni_schede) * 100

# Prendiamo le possibilità
probabilita_zero = 0.5588 * 100
probabilita_uno = 0.3795 * 100
probabilita_ambo = 0.02985 * 100
probabilita_terno = 0.002747 * 100
probabilita_quaterno = 0.0000958 * 100
probabilita_cinquina = 0.00000135 * 100
probabilita_sei = 0.00000000161 * 100

# Stampa i dati iniziali
print("\n ======= \n")
print(f"Schedina: {schedina}")
print(f"Zero: {zero} volte, in percentuale: {round(perc_zero, 2)}%  ")
print(f"Uno: {uno} volte, in percentuale: {round(perc_uno, 2)}%  ")
print(f"Ambo: {ambo} volte, in percentuale: {round(perc_ambo, 2)}%  ")
print(f"terno: {terno} volte, in percentuale: {round(perc_terno, 2)}% ")
print(f"Quaterno: {quaterno} volte, in percentuale: {round(perc_quaterno, 2)}% ")
print(f"Cinquina: {cinquina} volte, in percentuale: {round(perc_cinquina, 2)}% ")
print(f"Sei: {sei} volte, in percentuale: {round(perc_sei, 2)}% ")
print("\n ======= \n")

tot_ambo = ambo * premio_ambo
tot_terno = terno * premio_terno
tot_quaterno = quaterno * premio_quaterna
tot_cinquina = cinquina * premio_cinquina
tot_sei = sei * premio_sei

tot_vincite = tot_ambo + tot_terno + tot_quaterno + tot_cinquina + tot_sei

if tot_vincite < ripetizioni_schede:
    print(f"Abbiamo pero perso, saldo: {tot_vincite - ripetizioni_schede}£")
    print(f"Soldi preso: {tot_vincite}")
elif ripetizioni_schede < tot_vincite:
    print(f"Abbiamo vinto un totale di: {tot_vincite}£")

print("\n ======= \n")

if perc_zero > probabilita_zero:
    print(f"Abbiamo passato la probabilita per {round(perc_zero - probabilita_zero)}%")
else:
    print(f"Stiamo sotto la probabilita per {round(probabilita_zero - perc_zero)}%")

if perc_uno > probabilita_uno:
    print(f"Abbiamo passato la probabilita per {round(perc_uno - probabilita_uno)}%")
else:
    print(f"Stiamo sotto la probabilita per {round(probabilita_uno - perc_uno)}%")

if perc_ambo > probabilita_ambo:
    print(f"Ambo: Abbiamo passato la probabilita per {round(perc_ambo - probabilita_ambo)}%")
else:
    print(f"Ambo: Stiamo sotto la probabilita per {round(probabilita_ambo - perc_ambo)}%")

if perc_terno > probabilita_terno:
    print(f"Terno: Abbiamo passato la probabilita per {round(perc_terno - probabilita_terno)}%")
else:
    print(f"Terno: Stiamo sotto la probabilita per {round(probabilita_terno - perc_terno)}%")
    
if perc_quaterno > probabilita_quaterno:
    print(f"Quaterno: Abbiamo passato la probabilita per {round(perc_quaterno - probabilita_quaterno, 2)}%")
else:
    print(f"Quaterno: Stiamo sotto la probabilita per {round(probabilita_quaterno - perc_quaterno, 2)}%")
    
if perc_cinquina > probabilita_cinquina:
    print(f"Cinquina: Abbiamo passato la probabilita per {round(perc_cinquina - probabilita_cinquina, 2)}%")
else:
    print(f"Cinquina: Stiamo sotto la probabilita per {round(probabilita_cinquina - perc_cinquina, 2)}%")
    
if perc_sei > probabilita_sei:
    print(f"Sei: Abbiamo passato la probabilita per {round(perc_sei - probabilita_sei, 2)}%")
else:
    print(f"Sei: Stiamo sotto la probabilita per {round(probabilita_sei - perc_sei, 2)}%")    

print("\n ======= \n")

# Nuova maniera di prendere le schede fatte
cont = 0
giorno = 0
for elem in liste_schede:
    giorno += 1
    print(f"Schede giocate il giorno {giorno}: {liste_schede[cont]}")
    cont += 1
    
# Trovare num 3
num_3 = 0
cont = 0
for elem in liste_schede:
    if 3 in liste_schede[cont]:
        num_3 += 1
    cont += 1
print(f"Il numero 3 è uscito: {num_3} volte.")

# # # Facciamo un ciclo che percorre tutti gli elementi estratti dalle schedine giocate
# # # for elem in tqdm(estrazioni):
    
# # #     storico.append(elem) # Gli inseriamo nello storico
    
# # #     # Con cont prendiamo la posizione per separare ogni giocata (composta da sei numeri) 
# # #     if cont == 7:
# # #         storico.append("Numeri giocati: ")
# # #         cont = 0
# # #     cont += 1
        
# Per avere una stampa piu visibile gli definiamo un end agli elementi dentro la lista 
# storico per poi ogni 8 elementi fare un salto linea
cont = 0
for elem in storico:
    print(elem, end=" ")
    cont += 1
    
    if cont % 8 == 0: # Salto linea (riepilogo_11)
        print("\n")

num_piu_estrato = qta_estrato = num_meno_estrato = fortunati = sfortunati = 0   # Tutti valgono 0
# Definiamo questo valore MOLTO alto per essere sicuri di prenderne un numero piu 
# piccolo posteriormente
qta_meno_estrato = 1_000_000

num_fortunati = []
num_sfortunati = []

for elem in tqdm(estrazioni): # Percorre gli elementi estrati
    
    cont = 0
    # Per tutti i numeri estrati, se questi si ripetono aumenta il conto del numero ripetuto
    for num in estrazioni:
        if num == elem:
            cont += 1
    
    if cont > qta_estrato:  # Se il numero ripetuto è maggiore alla qta. Estrato
        qta_estrato = cont  # La qta. Estrato è uguale al valore del cont
        num_piu_estrato = elem  # Il numero piu ripetuto prende il valore del elemento (elem = num)
        
    # Si utilizza la stessa logica pero prendendo soltanto gli elementi che meno si ripetono
    if cont < qta_meno_estrato:
        qta_meno_estrato = cont
        num_meno_estrato = elem

# range(5) perche vogliamo soltanto prendere i 5 numeri piu fortunati (quelli piu usciti)
for i in tqdm(range(5)):
    # Posizione -1 per prendere anche il valore della posizione 0
    qta_estrato = -1
    num_piu_estrato = -1
    
    # Si percorre la lista delle estrazioni e se gli elementi non si trovano dentro
    # la lista di numeri fortunati si prende il numero che piu si ripete
    for elem in estrazioni:
        if elem not in num_fortunati:
            cont = 0
        
            for num in estrazioni:
                if num == elem:
                    cont += 1
            
            if cont > qta_estrato:
                qta_estrato = cont
                num_piu_estrato = elem
    
    # Se il numero piu estratti NON si trova gia dentro la lista dei numeri piu fortunati
    # inseriamo un altro numero fortunato, se si trova passa ad altro
    if num_piu_estrato not in num_fortunati:
        fortunati = num_piu_estrato
        num_fortunati.append(fortunati)  

# Stessa logica per i 5 numeri sfortunati
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
    
# Stampa
print("\n ======= \n")
print(f"\n Numero piu estrato: {num_piu_estrato} ripetuto {qta_estrato} volte")
print(f"\n Numero meno estrato: {num_meno_estrato} ripetuto {qta_meno_estrato} volte")
print(f"\n I numeri fortunati sono: {num_fortunati}")
print(f"\n I numeri meno fortunati sono: {num_sfortunati}")
print("\n ======= \n")

qta_uscite = []
### num_presi = []
cont = 0

conteggio = [0] * 90
for lista in liste_schede:
    for num in lista:
        conteggio[num -1] += 1
        print(lista)   
           
print(conteggio)

###
# Possiamo uttilizzare count()
###

# # # # Percorre tutti gli elementi estrati
# # # for elem in tqdm(estrazioni):
# # #     # Se non si trovano dentro la lista di tutti i numeri presi
# # #     if elem not in num_presi:
        
# # #         num_presi.append(elem)  # Gli inseriamo
# # #         cont = 0
        
# # #         # Si contano le ripetizione dei numeri
# # #         for num in estrazioni:
# # #             if elem == num:
# # #                 cont += 1    
        
# # #         # Inseriamo i dati del numero e quante volte è uscito soltanto se
# # #         # non abbiamo gia controlato il numero prima
# # #         qta_uscite.append("Numero: ")
# # #         qta_uscite.append(elem)
# # #         qta_uscite.append("Qta. uscito: ")
# # #         qta_uscite.append(cont)

# Stampa gli elementi usciti con la quantita di volte che è uscito
# # # cont = 0
# # # for elem in qta_uscite:
# # #     print(elem, end=" ")
# # #     cont += 1
# # #     if cont % 4 == 0:
# # #         print("\n")

# Graffico con le percentuali delle uscite
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