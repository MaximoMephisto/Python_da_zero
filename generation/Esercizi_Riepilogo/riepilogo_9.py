# Chiede all’utente un orario, espresso in ore e minuti

# Conferma all’utente i dati inseriti se le ore sono comprese tra 0 e 23 e i minuti tra 0 e
# 59. Altrimenti, scrive che i dati inseriti non sono corretti.

ora = int(input("Inserire ora: ")) 

if ora >= 0 and ora <= 23:
    print("Ora corretta.")
    ora_in_minuti = ora * 60
else: 
    print("Errore. Ora sbagliata")
    exit()
    
minuti = int(input("Inserire minuti: "))

if minuti >= 0 and minuti <= 59:
    print("Minuti corretti.")
else: 
    print("Errore. Minuti sbagliati")
    exit()

# Calcola e stampa il numero di minuti che sono passati dalla mezzanotte, ma solo nel
# caso in cui i dati siano corretti.
minuti_totali = ora_in_minuti + minuti
print(f"Sono passati {minuti_totali} dalla mezza notte")