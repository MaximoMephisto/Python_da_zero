# Lista obligatoria
libri = [] 
# Liste di suporto
titoli = []
autori = []
anni = []
stato = []
# Primo ciclo per ripetere richieste di libri
while True:
    # Secondo ciclo per verificare i dati inseriti
    sequenza = 1
    while sequenza == 1:
        dati_grezzi = input("Inserisci libro (titolo;autore;anno;stato): ")
        # lower() per passare tutte a minoscola, split() per separare in una lista dipendendo dal valore dentro (';')
        dati_grezzi = dati_grezzi.lower()
        verifica_dati = dati_grezzi.split(';')
        
        if len(verifica_dati) != 4:
            print("Errore, ci devono essere 4 dati inseriti.")
            # Ricomincia il cilo dal inizio senza continuare alle altre condizioni
            continue

        if not verifica_dati[2].isdigit():
            print("Errore, l'anno deve essere un numero.")
            continue

        if verifica_dati[3] != "disponibile" and verifica_dati[3] != "prestato":
            print("Errore, inserire uno stato valido.")
            continue
        # Stop ciclo
        sequenza = 0     
            
    # Pulizia
    # Separiamo i dati in lista e si remplazano i '|' per una virgola con un salto di linea
    dati_grezzi = dati_grezzi.strip().replace("|", ",\n")
    # Separiamo ogni libro per ogni virgola e salto di linea
    dati_grezzi = dati_grezzi.split(',\n')

    for dati in dati_grezzi:
        # Separiamo ogni dato del libro in una lista e si aggiungono alle liste di suporto
        dati = dati.strip().split(';')
        titoli.append(dati[0])
        
        dati[1] = dati[1].title()
        autori.append(dati[1])
        
        dati[2] = int(dati[2])
        anni.append(dati[2])
        
        dati[3] = dati[3].lower()
        stato.append(dati[3])
        
        libri.append(dati)

    # Interrogazioni di base
    qta_libri = len(libri)
    print(f"Totale libri: {qta_libri}")
    print("==========")

    # print(sorted(titoli))
    ########################### 
    ###########################
    # Facciamo una copia de la lista per non modificare la originale
    copia_titoli = list(titoli)
    
    num = len(copia_titoli)
    for i in range(num):
        cambio = False
        for j in range(0, num - i -1):
            if copia_titoli[j] > copia_titoli[j + 1]: # Se il indice e maggiore al inidice che procede
                #     b                a            ->       a                    b
                copia_titoli[j], copia_titoli[j + 1] = copia_titoli[j + 1], copia_titoli[j] 
                cambio = True # C'e stato cambio quindi continua a verificare
        if not cambio:
            break

    print(f"TITOLI SORT: {copia_titoli}")
    ###########################
    ###########################
        
    print("==========")

    # Prendiamo il anno con valore piu grande (nuovo) e quello con valore piu piccolo (vecchio)
    for titolo in titoli:
        for anno in anni:
            vecchio = min(anni)
            recente = max(anni)
            if titoli.index(titolo) == anni.index(vecchio):
                print(f"Piu vecchio: {titolo} ({vecchio})")
                print("==========")
                
                break
            if titoli.index(titolo) == anni.index(recente):
                print(f"Piu recente: {titolo} ({recente})")
                print("==========")

                break

    # Facciamo un conto di quanti libri sono disponibili e quanti prestati
    qta_disponibile = 0
    qta_non_disponibile = 0
    for elem in stato:
        if elem == "disponibile":
            qta_disponibile += 1
        elif elem == "prestato":
            qta_non_disponibile += 1
                
    print(f"Prestato: {qta_non_disponibile}")
    print("==========")

    print(f"Disponibile: {qta_disponibile}")
    print("==========")


    # Ricerche e filtri
    for libro in libri:
        for dati in libro:
            if "ros" in str(dati).lower():
                print(libro)

    titolo_richercatto = "George Orwell"
    for libro in libri:
        for dati in libro:
            if titolo_richercatto in str(dati):
                print(libro)
    print("==========")
                
    # Facciamo un print dei libri che ci sono tra questi anni (estremi commpresi)
    anno_inizio = 1940
    anno_fine = 1980

    for libro in libri:
        for anno in anni:
            if libri.index(libro) == anni.index(anno):
                if anno >= anno_inizio and anno <= anno_fine:
                    print(libro)                
                    break
    print("==========") 

    # Duplicati e integrità
    libri_non_duplicati = []
    autore_duplicato = ""
    titolo_duplicato = ""

    for autore in autori:
        if autori.count(autore) > 1:
            autore_duplicato = autore
    for titolo in titoli:
        if titoli.count(titolo) > 1:
            titolo_duplicato = titolo

    print(f"Libro duplicato: {titolo_duplicato} di {autore_duplicato}")
    print("==========")
    
    # Facciamo una nuova lista con i libri senza duplicati
    for libro in libri:
        if libro not in libri_non_duplicati:
            libri_non_duplicati.append(libro)
    print("Nessun duplicato presente")
    print("==========")

    for libro in libri_non_duplicati:
        print(libro)
    print("==========")
        

    # Statistiche sulle stringhe
    # Si crea una lista con i titoli senza i duplicati per calcolare la media della lunghezza (carattere) dei titoli
    titoli_non_duplicati = []
    for titolo in titoli:
        if titolo not in titoli_non_duplicati:
            titoli_non_duplicati.append(titolo)

    lunghezza_lista = len(titoli_non_duplicati)
    somma = 0

    for titolo in titoli_non_duplicati:
        somma += len(titolo)

    media = somma / lunghezza_lista
    print(f"lunghezza media titoli: {media}")
    print("==========") 

    # Facciamo print di quello piu lungo
    titolo_piu_lungo = ""
    lunghezza_titolo = 0
    for titolo in titoli_non_duplicati:
        if len(titolo) > len(titolo_piu_lungo):
            titolo_piu_lungo = titolo
            lunghezza_titolo = len(titolo)
    print(f"Piu lungo: {titolo_piu_lungo} ({lunghezza_titolo})")
    print("==========") 


    lista_coppie = []
    vocali = ["a","e","i","o","u"]
    conteggi = [0,0,0,0,0]

    for titolo in titoli_non_duplicati:
        for lettera in titolo:
            if lettera in vocali:
                # per trovare l'indice della vocale trovata nei titoli e sommare allo stesso indice di un altra lista
                i = vocali.index(lettera)
                conteggi[i] += 1

    for vocale in vocali:
        coppie = [] # Dentro il for per ritornare a valore zero una volta inseriti i dati nell altra lista
        if vocale not in coppie:
            coppie.append(vocale)
            i = vocali.index(vocale) # Indice della vocale
            for num in conteggi:
                if conteggi.index(num) == i: # Stesso indice che la vocale
                    coppie.append(num)
        
        # Si salvano i dati nella lista delle coppie senza ripetergli
        if coppie not in lista_coppie:
            lista_coppie.append(coppie)
                
    print(lista_coppie)
    print("==========") 

    da_saltare = ["il", "la", "lo", "le", "dei", "del", "di", "e", "della"]
    titolo_pulito = []

    for titolo in titoli_non_duplicati:
        # Facciamo tutto minoscolo e si aggiungie uno spazio prima del inizio per far stare tutte le parole da saltare nella stessa posizione
        titolo = " " + titolo.lower()
        
        for salto in da_saltare:
            if salto in titolo:
                # Si cambiano le parole per uno spazio vuoto
                titolo = titolo.replace(f" {salto} " , " ")
            
        titolo_pulito.append(titolo.upper())
            
    print(titolo_pulito)
    print("==========") 

    lettere = []
    # Prende l'indice 0 del titolo separato in lista
    for titolo in titolo_pulito:    
        prime_lettere = [lettera[0] for lettera in titolo.split()]
        parola = "".join(prime_lettere) # Definiamo la variabile parola con il valore della prima lettera
        lettere.append(parola) # Si aggiungono queste lettere a la lista

    # Per ogni elemento della lista lettere fare print con lo stesso indice di titoli e lettera
    for titolo in titoli_non_duplicati:
        for elem in lettere:
            if titoli_non_duplicati.index(titolo) == lettere.index(elem):
                print(f"{titolo} -> {elem}")

    print("==========") 

    # Un output sistemato
    output = ""

    for i in range(len(titoli_non_duplicati)):
        print(f"{anni[i]} | {titoli_non_duplicati[i]} - {autori[i]} [{stato[i]}]")
        output += f"""
        ----------------------------------------
        {anni[i]} | {titoli_non_duplicati[i]} - {autori[i]} [{stato[i]}]
        """

    print(output)
    
    # Si chiede se volgiono aggiungere un altro libro alla lista per non far finire il codice con un solo valore
    opt = input("Vuoi aggiungere un altro libro? (S/n): ")
    while opt.lower() != "s" and opt.lower() != "n":
        print("Errore. Option non giusta.")
        opt = input("Vuoi aggiungere un altro libro? (S/n): ")
    
    if opt == "s":
        continue
    if opt == "n":
        break
        

