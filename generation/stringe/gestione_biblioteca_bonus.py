#dati_grezzi = " Il nome della rosa;Umberto Eco;1980;disponibile |1984;George Orwell;1949;prestato| La coscienza di Zeno ;italo svevo;1923;DISPONIBILE|Il deserto dei tartari;Dino Buzzati;1940;prestato |1984;George Orwell;1949;prestato"
libri = []
titoli = []
autori = []
anni = []
stato = []

while True:
    sequenza = 1
    while sequenza == 1:
        dati_grezzi = input("Inserisci libro (titolo;autore;anno;stato): ")
        
        dati_grezzi = dati_grezzi.lower()
        verifica_dati = dati_grezzi.split(';')
        
        if len(verifica_dati) != 4:
            print("Errore, ci devono essere 4 dati inseriti.")
            continue

        if not verifica_dati[2].isdigit():
            print("Errore, l'anno deve essere un numero.")
            continue

        if verifica_dati[3] != "disponibile" and verifica_dati[3] != "prestato":
            print("Errore, inserire uno stato valido.")
            continue
        
        sequenza = 0     
            
    # Pulizia
    dati_grezzi = dati_grezzi.strip().replace("|", ",\n")
    dati_grezzi = dati_grezzi.split(',\n')

    for dati in dati_grezzi:
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
    ########################### asdasdd
    ###########################
    copia_titoli = list(titoli)
    titoli_sistemati = []
    
    for titolo in copia_titoli:
        
        for elem in titolo:  
            minore = ord(titolo[0])
            if elem < minore:
                minore = elem
        
        titoli_sistemati.append(minore)
        copia_titoli.remove(minore)
    
    print(titoli_sistemati)   
    ###########################
    ###########################
        
    print("==========")


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
            
    for libro in libri:
        if libro not in libri_non_duplicati:
            libri_non_duplicati.append(libro)
    print("Nessun duplicato presente")
    print("==========")

    for libro in libri_non_duplicati:
        print(libro)
    print("==========")
        

    # Statistiche sulle stringhe
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
                i = vocali.index(lettera)
                conteggi[i] += 1

    for vocale in vocali:
        coppie = []
        if vocale not in coppie:
            coppie.append(vocale)
            i = vocali.index(vocale)
            for num in conteggi:
                if conteggi.index(num) == i:
                    coppie.append(num)
        
        if coppie not in lista_coppie:
            lista_coppie.append(coppie)
                
    print(lista_coppie)
    print("==========") 

    da_saltare = ["il", "la", "lo", "le", "dei", "del", "di", "e", "della"]
    titolo_pulito = []

    for titolo in titoli_non_duplicati:
        
        titolo = " " + titolo.lower()
        
        for salto in da_saltare:
            if salto in titolo:
                titolo = titolo.replace(f" {salto} " , " ")
            
        titolo_pulito.append(titolo.upper())
            
    print(titolo_pulito)
    print("==========") 

    lettere = []

    for titolo in titolo_pulito:    
        prime_lettere = [lettera[0] for lettera in titolo.split()]
        parola = "".join(prime_lettere)
        lettere.append(parola)

    for titolo in titoli_non_duplicati:
        for elem in lettere:
            if titoli_non_duplicati.index(titolo) == lettere.index(elem):
                print(f"{titolo} -> {elem}")

    print("==========") 

    output = ""

    for i in range(len(titoli_non_duplicati)):
        print(f"{anni[i]} | {titoli_non_duplicati[i]} - {autori[i]} [{stato[i]}]")
        output += f"""
        ----------------------------------------
        {anni[i]} | {titoli_non_duplicati[i]} - {autori[i]} [{stato[i]}]
        """

    print(output)
    
    opt = input("Vuoi aggiungere un altro libro? (S/n): ")
    while opt.lower() != "s" and opt.lower() != "n":
        print("Errore. Option non giusta.")
        opt = input("Vuoi aggiungere un altro libro? (S/n): ")
    
    if opt == "s":
        continue
    if opt == "n":
        break
        

