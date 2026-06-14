from utility import giocatore_esiste, calcola_punti

def creazione_dict(file) :
    with open(file, encoding="utf-8") as f:
        dati = f.read()
        lista_dati = dati.split('\n')

    lista = []
    for elem in lista_dati:
        if elem != "":
            giocata_singola = []
            giocata_singola = elem.split(',')
            lista.append(giocata_singola)
        
    keys = []
    riepologo_giocata = []
    
    for elem in lista:
        brano = []
        if elem[0] not in keys:
            keys.append(elem[0])
        brano = elem[:]
        riepologo_giocata.append(tuple(brano))
        
    giocatori = {}
    
    for giocatore in keys: 
        giocatori[giocatore] = []
        
        for brano in riepologo_giocata:
            if giocatore in brano:
                giocatori[giocatore].append(brano[1:])
    
    return giocatori 


def mostra_tutti(giocatori):
    print("I giocatori presenti sono: ")
    for nome in giocatori:
        print(nome)           


def mostra_storico(giocatori, nick):
    if giocatore_esiste(giocatori, nick):
        nick = nick.title()
        for giocatore, giocate in giocatori.items():
            if nick == giocatore:
                print(f"{giocatore} -> {giocate}")
    else:
        print("Giocatore non trovato.")


def dick_a_testo(giocatori):
    testo = ""
    
    for nome in giocatori:
        for giocate in giocatori[nome]:
            testo += f"{nome},{giocate[0]},{giocate[1]},{giocate[2]},{giocate[3]}\n"

    return testo


def gioca(giocatori, nick, file):
    if giocatore_esiste(giocatori, nick):
        nick = nick.title()
        
        import random
        num_segreto = random.randint(1,100)
        
        cont = 0
        numeri_giocati = set()
        vincita = False
        
        while cont < 5:
            cont += 1
            
            num = int(input("Indovina il numero: "))
            print(cont)
            if num in numeri_giocati:
                print("Numero già inserito.")
                cont -= 1 
                continue
            
            if num == num_segreto:
                print("hai vinto")
                numeri_giocati.add(num)
                
                punti = calcola_punti(cont)
                
                brano = ("VINTA", cont, num_segreto, punti)
                
                giocatori[nick].append(brano)
                
                testo = dick_a_testo(giocatori)
                
                with open(file, 'w', encoding="utf-8") as f:
                    f.write(testo)
                                
                vincita = True
                
                break
                
            else:
                print("hai perso")
                numeri_giocati.add(num)
                
                punti = 0
                
                if num < num_segreto:
                    print("Il numero segreto è maggiore.")
                elif num > num_segreto:
                    print("Il numero segreto è minore.")
        
        if not vincita:
            brano = ("PERSA", cont, num_segreto, punti)
                
            giocatori[nick].append(brano)
                
            testo = dick_a_testo(giocatori)
                
            with open(file, 'w', encoding="utf-8") as f:
                f.write(testo)  
    else:
        print("Giocatore non trovato.")


def aggiungi_giocatore(giocatori, nick, file):
    if not giocatore_esiste(giocatori, nick):
        nick = nick.title()
        giocatori[nick] = []
        
        with open(file, 'a', encoding="utf-8") as f:
            f.write(f"\n{nick},")
            
    else:
        print("Giocatore già registrato.")


def rimuovi_giocatore(giocatori, nick, file):
    if giocatore_esiste(giocatori, nick):
        nick = nick.title()
        del giocatori[nick]
        
    with open(file, 'r', encoding="utf-8") as f:
        lineas = f.readlines()
        
    with open(file, 'w', encoding='utf-8') as f:
        for linea in lineas:
            if nick in linea:
                f.write("")
            else:
                f.write(linea)


def statistiche(giocatori, nick):
    qta_vinte = 0
    qta_perse = 0
    punti = 0
    num_giocate = []
        
    if giocatore_esiste(giocatori, nick):
        nick = nick.title()
        
        for giocate in giocatori[nick]:
            if giocate[0] == "VINTA":
                qta_vinte += 1
            else:
                qta_perse += 1
            
            punti += int(giocate[3])
            
            num_giocate.append(int(giocate[1]))
        
        qta_partite = len(giocatori[nick])
        perc_vincita = (qta_vinte / qta_partite) * 100
        perc_vincita = round(float(perc_vincita), 2)
        meno_giocate = min(num_giocate)
     
        print(f"{qta_partite} partite - {qta_vinte} vinte, {qta_perse} persa - {perc_vincita}% - {punti} punti - miglior partita: {meno_giocate} tentativo.")
    
    else:
        print("Giocatore non trovato.")
    

def classifica(giocatori):
    lista_classifica = []
    
    for giocatore in giocatori:
        punti = 0
        for giocate in giocatori[giocatore]:
            punti += int(giocate[3])
            
        if giocatore not in lista_classifica:
            lista_classifica.append([giocatore, punti])
            
    lista_classifica = sorted(lista_classifica, key=lambda x: x[1], reverse=True) #lambda per indicare che indice deve guardare
    
    print(str(lista_classifica).replace('[', '').replace(']', '').replace('\'', ''))    


def record_assoluto(giocatori):
    giocatore_record = ""
    partita = 6
    numero_segreto = 0
    for giocatore, giocate in giocatori.items():
        for partite in giocate:
            if int(partite[1]) < partita:
                partita = int(partite[1])
                giocatore_record = giocatore
                numero_segreto = int(partite[2])
                
    print(f"{giocatore_record} - numero {numero_segreto} in {partita} tentativo.")           


def numeri_vinti(giocatori):
    numeri_vincenti = set()
    for giocate in giocatori.values():
        for partite in giocate:
            if partite[0] == "VINTA":
                numeri_vincenti.add(int(partite[2]))
    numeri_vincenti = list(numeri_vincenti)
    print(numeri_vincenti)
                    

def giocatore_piu_attivo(giocatori):
    max_partite = -1
    piu_giocatore = None

    for giocatore, giocate in giocatori.items():
        if len(giocate) > max_partite:
            max_partite = len(giocate)
            piu_giocatore = giocatore
    
    print(f"{piu_giocatore} ({max_partite} partite).")