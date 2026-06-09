# ====== FUNZIONI DI SUPPORTO (da implementare) ======

# Backend testuale di un'app di streaming. Ogni utente ha una libreria di brani. Ogni brano è una tupla immutabile:

# brano = (titolo, artista, durata_secondi)   # es. ("Imagine", "John Lennon", 183)
# I dati stanno nel dizionario librerie: nome utente → lista dei suoi brani.

# Cosa devi fare
# Il menu e il main sono già pronti e collegati. Devi implementare solo il corpo delle funzioni (ora contengono pass).

# Vincoli tecnici (valutati)
# Tuple: i brani restano tuple immutabili → questo le rende hashable (possono entrare in un set).
# Set: usali davvero per gli artisti unici (voce 10) e i brani in comune (voce 11, intersezione). Niente cicli annidati manuali.
# Stringhe: durata in formato mm:ss (voce 8) e ricerca case-insensitive (voce 7).
# Liste: la libreria di ogni utente è e resta una lista.
# Validazione: nessuna operazione deve far crashare il programma se utente/brano non esiste.

def formatta_durata(secondi):
    minuti = (secondi // 60)
    second = (secondi % 60)
    
    if len(str(second)) == 1:
        formatto = f"{str(minuti)}:0{str(second)}" 
    else:
        formatto = f"{str(minuti)}:{str(second)}" 

    return formatto
    """Converte i secondi in stringa 'mm:ss'. Es: 929 -> '15:29', 65 -> '1:05'."""
    
def utente_esiste(librerie, nome):
    """Restituisce True se l'utente esiste nel dizionario, False altrimenti."""
    pass


# ====== OPERAZIONI DEL MENU (da implementare) ======

def mostra_tutte(librerie):
    print(librerie)


def mostra_utente(librerie, nome):

    if nome in librerie:
        print(librerie[nome])
    else:
        print("Errore, utente non trovato.")
        

def aggiungi_brano(librerie, nome, brano):
    if nome not in librerie:
        print("Utente non trovato.")
    elif brano in librerie[nome]:
        print("Brano esistente.")
    else:
        librerie[nome].append(brano)
    
    """[3] Aggiunge il brano (tupla) alla libreria dell'utente.
    Verifica che l'utente esista e che il brano NON sia già presente."""
    pass


def rimuovi_brano(librerie, nome, titolo):
    verifica = False
    if nome in librerie:
        for brani in librerie[nome]:
            if titolo in brani:
                librerie[nome].remove(brani)
                verifica = True
        if verifica == False:
            print("Brano non trovato.")
        
    """[4] Rimuove dalla libreria dell'utente il brano con quel titolo.
    Verifica che l'utente esista e che il brano sia presente."""


def aggiungi_utente(librerie, nome):
    if nome not in librerie:
        librerie[nome] = []
    """[5] Crea un nuovo utente con libreria vuota. Rifiuta nomi duplicati."""


def rimuovi_utente(librerie, nome):
    if nome in librerie:
        del librerie[nome]
    """[6] Rimuove un utente. Verifica che esista."""


def cerca_brano(librerie, titolo):
    titolo = titolo.lower()
    for nomi in librerie:
        for brano in librerie[nomi]:
            if titolo in brano[0].lower():
                print(nomi)
        
    """[7] Stampa quali utenti possiedono un brano con quel titolo.
    Ricerca CASE-INSENSITIVE ('imagine' deve trovare 'Imagine')."""


def statistiche_utente(librerie, nome):
    
    cont = 0
    durata_tot = 0
    if nome in librerie:
        for elem in librerie[nome]:
            cont += 1
            print(f"{elem[0]} - {elem[1]} - {formatta_durata(elem[2])}")
            durata_tot += elem[2]
            
        print(f"Lunghezza di brani: {cont}")
        print(f"Duara tot: {formatta_durata(durata_tot)}")
    else:
        print("Utente non esistente.")
        
    """[8] Stampa numero di brani e durata totale in formato mm:ss.
    Usa formatta_durata(). Verifica che l'utente esista."""


def utente_con_piu_brani(librerie):
    cont = 0
    utente_max = ""
    for utente in librerie:
        if len(librerie[utente]) > cont:
            cont += len(librerie[utente])
            utente_max = utente
                
    print(utente_max)
            
    """[9] Stampa il nome dell'utente con la libreria più grande."""


def artisti_unici(librerie):
    artisti_non_duplicati = set()
    for utenti, elem in librerie.items():
        for items in elem:
            if items[1] not in artisti_non_duplicati:
                artisti_non_duplicati.add(items[1])
    print(sorted(artisti_non_duplicati))
    
    """[10] Stampa l'elenco degli artisti SENZA duplicati, ordinato alfabeticamente.
    Usa un SET per deduplicare."""


def brani_in_comune(librerie, n1, n2):
    brani_uno = set()
    brani_due = set()
    brani_unici = set()
    if n1 not in librerie:
        print("Utente non trovato.")
    else:
        if n2 not in librerie:
            print("Utente non trovato.")
        else:
            for elem in librerie[n1]:
                brani_uno.add(elem)
            for elem in librerie[n2]:
                brani_due.add(elem)
            for elem in brani_uno:
                if elem in brani_due:
                    brani_unici.add(elem)
            print(brani_unici)
        
    """[11] Stampa i brani presenti in ENTRAMBE le librerie dei due utenti.
    Usa l'INTERSEZIONE di due set. Verifica che entrambi esistano."""


def brano_piu_presente(librerie):
    branis = []
    max_bran = 0
    maxi_bran = []
    max_elem = []
    for utenti, brani in librerie.items():
        for brano in brani:
            branis.append(brano)
    for elem in branis:
        if branis.count(elem) > max_bran:
            max_bran = branis.count(elem)
            if max_bran not in maxi_bran:
                maxi_bran.append(max_bran)
            if elem not in max_elem:
                max_elem.append(elem)
                
    for i in range(len(max_elem)):
        print(f"{max_elem[i]} -> {maxi_bran[i]}")
    """[12] Stampa il brano che compare nel maggior numero di librerie distinte."""


def main():
    # ====== DATI DI PARTENZA ======
    # Un brano è una TUPLA: (titolo, artista, durata_secondi)
    librerie = {
        "Marco": [
            ("Bohemian Rhapsody", "Queen", 355),
            ("Imagine", "John Lennon", 183),
            ("Hotel California", "Eagles", 391),
        ],
        "Luca": [
            ("Imagine", "John Lennon", 183),
            ("Smells Like Teen Spirit", "Nirvana", 301),
        ],
        "Sara": [
            ("Bohemian Rhapsody", "Queen", 355),
            ("Shape of You", "Ed Sheeran", 234),
            ("Imagine", "John Lennon", 183),
        ],
    }

    # ====== MENU PRINCIPALE (già pronto — NON modificare) ======
    # Raccoglie gli input e chiama la funzione giusta.
    # Tu devi solo implementare le funzioni nelle celle sopra.
    import time

    while True:
        print("===================================================")
        print("1)  Mostra tutte le librerie")
        print("2)  Mostra i brani di un utente")
        print("3)  Aggiungi un brano a un utente")
        print("4)  Rimuovi un brano a un utente")
        print("5)  Aggiungi un nuovo utente")
        print("6)  Rimuovi un utente")
        print("7)  Cerca un brano e mostra chi lo possiede")
        print("8)  Statistiche di un utente")
        print("9)  Utente con più brani")
        print("10) Tutti gli artisti senza duplicati")
        print("11) Brani in comune tra due utenti")
        print("12) Brano più presente")
        print("0)  Esci")
        print("===================================================")

        scelta = int(input("Scelta: "))

        if scelta == 1:
            mostra_tutte(librerie)

        elif scelta == 2:
            nome = input("Utente: ")
            
            mostra_utente(librerie, nome)

        elif scelta == 3:
            nome = input("Utente: ")
            titolo = input("Titolo: ")
            artista = input("Artista: ")
            durata = int(input("Durata (secondi): "))
            brano = (titolo, artista, durata)
            aggiungi_brano(librerie, nome, brano)

        elif scelta == 4:
            nome = input("Utente: ")
            titolo = input("Titolo da rimuovere: ")
            rimuovi_brano(librerie, nome, titolo)

        elif scelta == 5:
            nome = input("Nome nuovo utente: ")
            aggiungi_utente(librerie, nome)

        elif scelta == 6:
            nome = input("Utente da rimuovere: ")
            rimuovi_utente(librerie, nome)

        elif scelta == 7:
            titolo = input("Titolo da cercare: ")
            cerca_brano(librerie, titolo)

        elif scelta == 8:
            nome = input("Utente: ")
            statistiche_utente(librerie, nome)

        elif scelta == 9:
            utente_con_piu_brani(librerie)

        elif scelta == 10:
            artisti_unici(librerie)

        elif scelta == 11:
            n1 = input("Primo utente: ")
            n2 = input("Secondo utente: ")
            brani_in_comune(librerie, n1, n2)

        elif scelta == 12:
            brano_piu_presente(librerie)

        elif scelta == 0:
            print("Alla prossima!")
            break

        else:
            print("Scelta non valida.")

        time.sleep(2)


main()