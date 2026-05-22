# Obiettivo
# Il giocatore deve indovinare un codice segreto generato casualmente.
# Regole
# -Il programma genera un numero casuale da 100 a 999.
# -Il giocatore ha 10 tentativi massimi.
# Dopo ogni tentativo:
#  se il numero è troppo alto → stampa "Troppo alto"
#  se troppo basso → stampa "Troppo basso"

# Per ogni tentativo il programma mostra:
#  quanti tentativi restano
# Se il giocatore inserisce un numero negativo:
#  il gioco termina subito

# Quando il giocatore indovina:
#  stampa il numero di tentativi usati
#  se supera i 10 tentativi mostrare che ha perso
import random

codice = random.randint(100, 999)

for i in range(10):
    num = int(input("Inserisci un numero: "))
    
    if num < 0:
        print("Non si accetano numeri negativi.")
        break
    
    while num < 100 or num > 999:
        num = int(input("Inserisci un numero tra 100 e 999: "))
        if num < 0:
            print("Non si accetano numeri negativi.")
            break
    if num < 0:
        break
    
    if num < codice:
        print("Il numero è troppo basso")
    elif num > codice:
        print("Il numero è troppo alto")
    else:
        print(f"Hai preso il numero {num} con {i} tentativi.")
        break
if num != codice and num > 0:
    print("Hai perso")
    
    
    