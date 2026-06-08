# Controllo esistenza utente/libro prima delle operazioni
# Prima di aggiungere o rimuovere un libro, il programma verifica che l’utente esista e che il libro non sia già presente (o sia presente, nel caso di rimozione).
#import time

prestiti = {
    "Marco": [
        "Il Signore degli Anelli", "Se questo è un uomo", "Il fu Mattia Pascal",
        "La Boutique del Mistero", "1984", "Il Nome della Rosa"
    ],
    "Luca": [
        "Harry Potter e la Pietra Filosofale", "Il Padrino",
        "Shining", "Dracula", "Dune"
    ],
    "Sara": [
        "Harry Potter e la Camera dei Segreti", "Orgoglio e Pregiudizio",
        "Se questo è un uomo", "Geronimo Stilton",
        "Piccole Donne", "Jane Eyre", "Emma"
    ],
    "Giulia": [
        "1984", "La Fattoria degli Animali", "Fahrenheit 451",
        "Brave New World", "Il Processo"
    ],
    "Andrea": [
        "Dune", "Fondazione", "Neuromante",
        "Hyperion", "Snow Crash", "Ready Player One"
    ],
    "Chiara": [
        "Orgoglio e Pregiudizio", "Persuasione", "Emma",
        "Ragione e Sentimento", "Jane Eyre", "Cime Tempestose"
    ],
    "Matteo": [
        "Moby Dick", "Ventimila Leghe sotto i Mari",
        "L'Isola del Tesoro", "Robinson Crusoe", "Il Vecchio e il Mare"
    ],
    "Elena": [
        "Il Nome della Rosa", "Baudolino", "Il Pendolo di Foucault",
        "Siddharta", "Lo Straniero", "Delitto e Castigo"
    ],
    "Davide": [
        "Shining", "It", "Misery",
        "Carrie", "Pet Sematary", "Doctor Sleep"
    ],
    "Francesca": [
        "Anna Karenina", "Guerra e Pace", "Madame Bovary",
        "I Miserabili", "Don Chisciotte", "Ulisse", "Lolita"
    ]
}

while True:
    print("===================================================")
    print("1) Visualizza tutti i prestiti")
    print("2) Visualizza i libri di un utente")     #chiedere quindi di quale utente
    print("3) Aggiungi libro ad un utente")         #chiedere quindi di quale utente
    print("4) Rimuovi libro ad un utente")          #chiedere quindi di quale utente
    print("5) Aggiungi un nuovo utente")            #Nuova voce di menu per inserire un nuovo nome utente e inizializzare i suoi prestiti (lista vuota).
    print("6) Rimuovere un utente")
    print("7) Cerca un libro e mostra chi lo ha")   #Inserendo il titolo di un libro, il programma dice quali utenti hanno in prestito quel libro.
    print("8) Conta quanti libri ha in prestito un utente")  #Data la scelta di un utente, mostra il numero totale di libri che ha.
    print("9) Stampare l'utente che ha più libri in prestito")  #difficile
    print("10) Elenco di tutti i libri senza duplicati")   #Voce di menu che mostra l’elenco di tutti i titoli presenti nei prestiti, senza ripetizioni.
    print("11) Libro più prestato")                    #MOLTO DIFFICILE calcola quale libro compare più volte complessivamente tra tutti gli utenti.
    print("0) Esci")
    print("===================================================")

    scelta = input("Scelta: ")
    if scelta.isnumeric():
        scelta = int(scelta)
        if scelta == 1:
            for nome, libri in prestiti.items():
                print(nome, libri)
                
        elif scelta == 2:
            while True:
                utente = input("Inserisci nome del utente: ")
                utente = utente.title()
                if utente not in prestiti:
                    print("Utente non trovato. Riprova.")    
                else:
                    print(prestiti[utente])
                    break
        elif scelta == 3:
            while True:
                utente = input("Inserisci nome del utente: ")
                utente = utente.title()
                if utente not in prestiti:
                    print("Utente non trovato. Riprova.")    
                else:
                    nuovo_libro = input("Inserisci nuovo libro: ")
                    prestiti[utente].append(nuovo_libro)
                    
                    print(f"{prestiti[utente]} -> {nuovo_libro}")
                    break
        elif scelta == 4:
            while True:
                utente = input("Inserisci nome del utente: ")
                utente = utente.title()
                if utente not in prestiti:
                    print("Utente non trovato. Riprova.")    
                else:
                    while True:
                        libro_del = input("Inserisci libro da rimuovere: ")
                        if libro_del not in prestiti[utente]:
                            print("Libro non trovato.")
                        else:
                            prestiti[utente].remove(libro_del)
                            break
                    
                    print(f"Il libro \"{libro_del}\" dal utente \"{utente}\" è stato rimoso corretamente.")
                    break
        elif scelta == 5:
            while True:
                utente = input("Inserire nuovo utente: ")
                utente = utente.title()
                if utente in prestiti.keys():
                    print("Utente esistente.")
                else:
                    prestiti[utente] = []
                    while True:
                        opt = input("Vuole inserire libri al nuovo utente?(S/n): ")
                        opt = opt.lower()
                        
                        if opt == "n":
                            break
                        elif "s":
                            nuovo_libro = input("Inserisci nuovo libro: ")
                            prestiti[utente].append(nuovo_libro)
                            break
                        else:
                            print("Valore non valido.")
                    break
            print(f"Nuovo utente \"{utente}\" con \"{nuovo_libro}\" inserito corretamente.")
        elif scelta == 6:
            while True:
                utente_re =  input("Inserire utente da eliminare: ")
                utente_re = utente_re.title()
                if utente_re  not in prestiti:
                    print("Utente non trovato.")
                else:
                    del prestiti[utente_re]
                    break
            print(f"Utente \"{utente_re}\" eliminato corretamente.")
        elif scelta == 7:
            while True:
                libro_cercato = input("Inserisci il libro da cercare: ")
                for utente, libro in prestiti.items():
                    if libro_cercato in libro:
                        print(f"{utente} ha preso il libro \"{libro_cercato}\"")
                break
        elif scelta == 8:
            while True:
                utente = input("Inserisci utente per contare i suoi libri: ")
                utente = utente.title()
                if utente not in prestiti.keys():
                    print("Utente non trovato.")
                else:
                    for nome, libri in prestiti.items():
                        if utente == nome:
                            qta_libri = len(libri)
                            print(f"{utente} ha preso un totale di {qta_libri} libri.")
                            break 
                    break
        elif scelta == 9:
            utenti_piu_prestiti = []
            for utente, libri in prestiti.items():
                piu_libri = 0
                utente_piu_libri = ""
                qta_piu_libri = len(libri)
                
                if piu_libri < qta_piu_libri:
                    utente_piu_libri = utente
                    piu_libri = qta_piu_libri
                    utenti_piu_prestiti.append([utente_piu_libri, piu_libri])
                
            print(f"Il utente {utente_piu_libri} ha un totale di \"{qta_piu_libri}\" libri in prestito.")
            for prestiti in utenti_piu_prestiti:
                if piu_libri in prestiti:
                    print(f"Riepilogo di utenti con piu prestiti: {prestiti}")
                    
        elif scelta == 10:
            libri_senza_duplicati = []
            cont = 0
            for libri in prestiti.values():
                for libro in libri:
                    if libro not in libri_senza_duplicati:
                        libri_senza_duplicati.append(libro)
                        
            print("Riepilogo di libri:")
            for libri in libri_senza_duplicati:
                cont += 1
                print(f"{cont}) {libri}")
        elif scelta == 11:
            tutti_libri_prestati = []
            qta_volte_prestato = 0
            libro_piu_ripetuto = ""
            for libri in prestiti.values():
                for libro in libri:
                    tutti_libri_prestati.append(libro)
            for libro in tutti_libri_prestati:
                if tutti_libri_prestati.count(libro) > qta_volte_prestato:
                    libro_piu_ripetuto = libro
                    qta_volte_prestato = tutti_libri_prestati.count(libro)
            print(f"Il libro piu prestato è \"{libro_piu_ripetuto}\", prestato {qta_volte_prestato} volte.")
                    
        elif scelta == 0:
            print("Alla prossima!")
            break
    else:
        print("Errore. Devi inserire un valore numerico.")
    #time.sleep(3)