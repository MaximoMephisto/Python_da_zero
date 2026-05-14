# Chiede all’utente la larghezza e l’altezza di un rettangolo.
# Conferma all’utente i dati inseriti.
# Se la larghezza è maggiore dell’altezza, stampa che il rettangolo è “Lungo”, altrimenti
# stampa che il rettangolo è “Alto”.

larghezza= float(input("inserisci la larghezza di un rettangolo: "))
lunghezza= float(input("inserisci la lunghezza di un rettangolo: "))

print(f"ti confermo che i dati inseriti sono: {larghezza} {lunghezza}")

if larghezza > lunghezza:
    print("il rettangolo è lungo")
else:
    print("il rettangolo è alto")

operazione1 = 1
operazione2 = 2

operazione = int(input("scegli tra l'operazione 1 o l'operazione 2: "))

# Poi chiede all’utente di scegliere una operazione, scegliendo un codice di operazione
# che può essere 1 o 2:
# ○ Se l’utente sceglie l’operazione 1: Calcola e stampa il valore dell’area del
# rettangolo, pari al prodotto di larghezza con altezza.
# ○ Se l’utente sceglie l’operazione 2: Calcola e stampa il valore del perimetro,
# pari al doppio della somma della larghezza con l’altezza.
# ○ Se l’utente sceglie un differente codice di operazione: Il programma termina
# dicendo all’utente che ha selezionato una operazione non disponibile.

if operazione == operazione1:
    area= larghezza*lunghezza
    print(f"l'aerea del rettangolo è: {area}")
elif operazione==operazione2:
    perimetro= 2*(lunghezza+larghezza)
    print(f"la misura del perimetro è: {perimetro}")
else:
    print("operazione non disponibile, riprova: ")

