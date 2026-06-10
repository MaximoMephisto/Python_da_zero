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

def aggiungi_brano(librerie, nome, brano, file):
    if nome not in librerie:
        print("Utente non trovato.")
    elif brano in librerie[nome]:
        print("Brano esistente.")
    else:
        librerie[nome].append(brano)
                    
        testo_nuovo = diz_testo(librerie)

        with open(file, "w", encoding="utf-8") as f:
            f.write(testo_nuovo)

def rimuovi_brano(librerie, nome, titolo, file):
    verifica = False
    if nome in librerie:
        for brani in librerie[nome]:
            if titolo in brani:
                librerie[nome].remove(brani)
                verifica = True

        if verifica == False:
            print("Brano non trovato.")
    
    testo_nuovo = diz_testo(librerie)
    
    with open(file, 'w') as f:
        f.write(testo_nuovo)
        

def aggiungi_utente(librerie, nome, file):

    if nome not in librerie:
       librerie[nome] = []
       print(nome)
       with open(file, 'a') as f:
           f.write("\n" + nome + ", ")
        
    
def rimuovi_utente(librerie, nome, file):
    if nome in librerie:
        del librerie[nome]
        
    with open(file, 'r') as f:
        lineas = f.readlines()
        
    with open(file, 'w') as f:
        for linea in lineas:
            if nome not in linea:
                f.write(linea)
            else:
                f.write("")

def diz_testo(dict):
    
    testo = ""
    for elem in dict:
        for brano in dict[elem]:
            testo += elem + ", " + brano[0] + ", " + brano[1] + ", " + brano[2] + "\n"

    return testo
    
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

def output(librerie):
    for nome in librerie:
        for titolo, artista, durata in librerie[nome]:
            print(f"{nome}, {titolo}, {artista}, {durata}")

def creazione_dict(file):
    with open(file) as f:
        contenuto = f.read()
    l = contenuto.split('\n')
    
    lista = []
    for elem in l:
        if elem != "":
            l2 = []
            l2 = elem.split(", ")
            lista.append(l2)
            
        keys = []
        dati = []
        for elem in lista:
            brano = []
            if elem[0] not in keys:
                keys.append(elem[0])
            brano = [elem[0], elem[1], elem[2], elem[3]]
            dati.append(tuple(brano))
    
    librerie = dict()
    
    for utenti in keys:
        librerie[utenti] = []
    
    for brano in dati:
        brano_list = list(brano)
        for utenti in keys:
            if utenti in brano_list:
                brano_tuple = tuple(brano_list[1:])
                librerie[utenti].append(brano_tuple)

    return librerie

def sposta_brano(dicz, primo_nome, secondo_nome, brano, ind):
    if primo_nome in dicz:
        for brani in dicz[primo_nome]:
            if brano in brani:
                verifica = True
                aggiungi_brano(dicz, secondo_nome, brani, ind)
                #rimuovi_brano(dicz, primo_nome, brano, ind) se vogliamo rimuovere il brano spostato
        if verifica == False:
            print("Brano non trovato.")
            
    else:
        print("Utente non trovato.")
    
    
def ordina_libreria(librerie, nome, criterio):
    pass

def classifica_artisti(librerie):
    branis = []
    max_bran = 0
    max_elem = ""
    for utenti, brani in librerie.items():
        for brano in brani:
            branis.append(brano)
    for elem in branis:
        if branis.count(elem) > max_bran:
            max_bran = branis.count(elem)
            max_elem = elem[0]
                
    print(max_elem)

def main():
    
    indirizzo = 'generation/file/librerie.txt'
    librerie = creazione_dict(indirizzo)
    
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
        print("13) Far vedere tutti")
        print("14) Sposta un brano da un utente a un altro")
        print("15) Ordina la libreria di un utente")
        print("16) Classifica artisti per numero di brani")
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
                durata = input("Durata (secondi): ")
                brano = (titolo, artista, durata)
                aggiungi_brano(librerie, nome, brano, indirizzo)

            elif scelta == 4:
                nome = input("Utente: ")
                titolo = input("Titolo da rimuovere: ")
                rimuovi_brano(librerie, nome, titolo, indirizzo)

            elif scelta == 5:
                nome = input("Nome nuovo utente: ")
                aggiungi_utente(librerie, nome, indirizzo)

            elif scelta == 6:
                nome = input("Utente da rimuovere: ")
                rimuovi_utente(librerie, nome, indirizzo)

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
                
            elif scelta == 13:
                output(librerie)
                
            elif scelta == 14:
                origine = input("Utente di origine: ")
                destinazione = input("Utente di destinazione: ")
                titolo = input("Titolo del brano da spostare: ")
                sposta_brano(librerie, origine, destinazione, titolo, indirizzo)

            elif scelta == 15:
                nome = input("Utente: ")
                criterio = input("Ordina per (titolo/artista/durata): ")
                ordina_libreria(librerie, nome, criterio)

            elif scelta == 16:
                classifica_artisti(librerie)
                
            elif scelta == 0:
                print("Alla prossima!")
                break

            else:
                print("Scelta non valida.")
                
        else:
            print("Errore, il valore deve essere numerico.")

main()
