def stampa_menu():
    print("===================================================")
    print("1)  Mostra tutti i giocatori")
    print("2)  Mostra lo storico di un giocatore")
    print("3)  GIOCA  (Indovina il numero)")
    print("4)  Aggiungi un nuovo giocatore")
    print("5)  Rimuovi un giocatore")
    print("6)  Statistiche di un giocatore")
    print("7)  Classifica (per punti totali)")
    print("8)  Record assoluto")
    print("9)  Numeri vinti senza duplicati")
    print("10) Giocatore con più partite")
    print("0)  Esci")
    print("===================================================")
    

def giocatore_esiste(giocatori, nick):
    for utente in giocatori:
        if nick.lower() == utente.lower():
            return True


def calcola_punti(tentativi):
    puntuazione = (6 - tentativi) * 20
    return puntuazione
