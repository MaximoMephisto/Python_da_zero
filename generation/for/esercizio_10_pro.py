#versione PRO, giocare contro la CPU
#chiedere all'utente quale numero di dado sceglie
#la CPU ne sceglie un altro (DIVERSO)
#simulare il lancio di 100 dadi e stampare chi dei due ha vinto indicato i risultati
import random

num = int(input("Inserisci numero: "))
while num < 1 or num > 6:
    num = int(input("Errore, inserisci numero di dado giusto: "))
vincita_utente = 0

num_cpu = random.randint(1, 6)
while num_cpu == num:
    num_cpu = random.randint(1, 6)
vincita_cpu = 0

for i in range(100):
    facce = random.randint(1, 6)
    
    if num == facce:
        vincita_utente += 1
    
    if num_cpu == facce:
        vincita_cpu += 1
    

if vincita_utente > vincita_cpu:
    resto = vincita_utente - vincita_cpu 
    print(f"Il utente ha vinto con il numero {num} per {vincita_utente} volte che è comparso il numero, ha {resto} numeri in piu al CPU.")
elif vincita_utente == vincita_cpu:
    print(f"Il utente con il numero {num} e il CPU con il numero {num_cpu} sono pari.")
else:
    resto = vincita_cpu - vincita_utente 
    print(f"Il CPU ha vinto con il numero {num_cpu} per {vincita_cpu} volte che è comparso il numero, ha {resto} numeri in piu al utente.")
        