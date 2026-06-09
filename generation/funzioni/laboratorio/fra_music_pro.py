def formatta_durata(secondi):
    minuti = (secondi // 60)
    second = (secondi % 60)
    
    if len(str(second)) == 1:
        formatto = f"{str(minuti)}:0{str(second)}" 
    else:
        formatto = f"{str(minuti)}:{str(second)}" 

    return formatto
    
def utente_esiste(librerie, nome):
    nome = nome.lower()
    for nom in librerie.keys():
        nom = nom.lower()
        if nome == nom:
            nome = nome.title()
    print(librerie[nome])

def mostra_tutte(librerie):
    print(librerie)

def mostra_utente(librerie, nome):
    utente_esiste(librerie, nome)

def aggiungi_brano(librerie, nome, brano):
    if nome not in librerie:
        print("Utente non trovato.")
    elif brano in librerie[nome]:
        print("Brano esistente.")
    else:
        librerie[nome].append(brano)

def rimuovi_brano(librerie, nome, titolo):
    verifica = False
    if nome in librerie:
        for brani in librerie[nome]:
            if titolo in brani:
                librerie[nome].remove(brani)
                verifica = True
        if verifica == False:
            print("Brano non trovato.")

def aggiungi_utente(librerie, nome):
    if nome not in librerie:
        librerie[nome] = []

def rimuovi_utente(librerie, nome):
    if nome in librerie:
        del librerie[nome]

def cerca_brano(librerie, titolo):
    titolo = titolo.lower()
    for nomi in librerie:
        for brano in librerie[nomi]:
            if titolo in brano[0].lower():
                print(nomi)
        
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

def utente_con_piu_brani(librerie):
    cont = 0
    utente_max = ""
    for utente in librerie:
        if len(librerie[utente]) > cont:
            cont += len(librerie[utente])
            utente_max = utente
                
    print(utente_max)

def artisti_unici(librerie):
    artisti_non_duplicati = set()
    for utenti, elem in librerie.items():
        for items in elem:
            if items[1] not in artisti_non_duplicati:
                artisti_non_duplicati.add(items[1])
    print(sorted(artisti_non_duplicati))

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

def main():
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
    
    for nom in librerie.keys():
        print(nom.lower())
    
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
        
        scelta = input("Scelta: ")
        if scelta.isnumeric():
            scelta = int(scelta)
            
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
                
        else:
            print("Errore, il valore deve essere numerico.")

main()
