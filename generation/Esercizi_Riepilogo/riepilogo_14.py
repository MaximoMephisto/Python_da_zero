# Scrivere un programma Giudizio che chiede all'utente di inserire 
# un numero intero che rappresenta il voto ricevuto ad un esame universitario 
# (in trentesimi) e procede come segue:

voto = int(input("Inserire voto (in trentesimi): "))
# Se il numero è minore di 0 o maggiore di 30 visualizza il messaggio "Numero Errato"
if voto < 0 and voto > 30:
    print("Numero Errato")
# Se il numero è compreso tra 0 e 17 visualizza il messaggio "Esame non superato"
elif voto >= 0 and voto <= 17:
    print("Esame non superato")
# Se il numero è compreso tra 18 e 24 visualizza il messaggio "Giudizio: Sufficiente"
elif voto >= 18 and voto <= 24:
    print("Giudizio: Sufficiente")
    
    print("1) Registrare il voto.")
    print("0) Non registrare il voto.")
    opt = int(input("Segli una opzione di sopra (Es. 1): "))
    
    if opt == 0:
        print("Voto Rifiutato")
    elif opt == 1:
        print("Voto Accettato")
    else:
        print("Errore di stampa")
    
        
# Se il numero è compreso tra 25 e 30 visualizza il messaggio "Giudizio: Buono"
elif voto >= 25 and voto <= 30:
    print("Giudizio: Buono")
    
    print("1) Registrare il voto.")
    print("0) Non registrare il voto.")
    opt = int(input("Segli una opzione di sopra (Es. 1): "))
    
    if opt == 0:
        print("Voto Rifiutato")
    elif opt == 1:
        print("Voto Accettato")
    else:
        print("Errore di stampa")
    
# Successivamente, se il giudizio è sufficiente oppure buono il programma chiede all'utente 
# se voglia registrare il voto. L'utente può rispondere inserendo 0 per non registrare, oppure 1 per registrare. 
# Nel primo caso il programma stampa "Voto Rifiutato", nel secondo caso stampa "Voto Accettato"
    