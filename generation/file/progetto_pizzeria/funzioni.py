def verifica_opt(opt, ordini, prezzi, indirizzo):
    if opt == 1:
        mostra_listino(prezzi)
    elif opt == 2:
        mostra_tutti_ordini(ordini)
    elif opt == 3:
        while True:
            print("1) Inserire direttamente nome. ")
            print("2) Vedere lista di clienti e scegliere. ")
            scelta = input("Inserisce opzione: ")
            if scelta.isnumeric():
                scelta = int(scelta)
                if scelta == 1:
                    mostra_ordini_cliente(ordini)
                    break
                elif scelta == 2:
                    mostra_ordini_cliente_opt(ordini)
                    break
                else:
                    print("Scelta non valita.")
    elif opt == 4:
        nuovo_cliente(ordini, indirizzo)
    elif opt == 5:
        aggiungi_pizza(ordini, prezzi, indirizzo)
    elif opt == 6:
        while True:
            print("1) Inserire direttamente nome. ")
            print("2) Vedere lista di clienti e scegliere. ")
            scelta = input("Inserire opzione: ")
            if scelta.isnumeric():
                scelta = int(scelta)
                if scelta == 1:
                    rimuovi_pizza(ordini, prezzi, indirizzo)
                    break
                elif scelta == 2:
                    rimuovi_pizza_opt(ordini, indirizzo)
                    break
                else:
                    print("Scelta non valita.") 
            
    elif opt == 7:
        conto(ordini, prezzi)
    elif opt == 8:
        incasso(ordini, prezzi)
    elif opt == 9:
        list_pizze_ordinate = pizze_ordinate(ordini)
        cont = 0
        for elem in sorted(list_pizze_ordinate):
            cont += 1
            print(f" {cont}) {elem}")
            
    elif opt == 10:
        pizze_non_ordinate(ordini, prezzi)
    elif opt == 11:
        pizza_piu_ordinata(ordini)
    elif opt == 12:
        cliente_fisso(ordini, prezzi)
    else:
        print("Scegliere un numero dentro le opzioni.")


def dict_a_testo(ordini):
    testo = ""
    
    for cliente, ordine in ordini.items():
        for pizza in ordine:
            testo += f"{cliente},{pizza}\n"

    return testo


def creazione_dict(file):
    lista_ordini = []
    clienti = []
    ordini_dict = dict()
    
    with open(file, 'r', encoding='utf-8') as f:
        testo_ordini = f.read()
    
    testo_ordini = testo_ordini.replace(',', ', ').split('\n')
    lista_ordini_testo = testo_ordini
    
    for elem in lista_ordini_testo:
        elem = elem.strip()
        if not elem:
            continue
    
        ordine = elem.split(',')
        if len(ordine) < 2:
            continue
        
        lista_ordini.append(ordine)
    
    for ordine in lista_ordini:
        cliente = ordine[0].strip()
        clienti.append(cliente)
    
    clienti = set(clienti)
    for elem in clienti:
        ordini_dict[elem] = []
        
    for ordine in lista_ordini:
        cliente = ordine[0].strip()
        prodotto = ordine[1].strip()
        
        if cliente in ordini_dict:
            if prodotto:
                ordini_dict[cliente].append(prodotto)
    
    return ordini_dict


def creazione_dict_prezzi(file):
    lista_prezzi = []
    prezzi = dict()
    
    with open(file, 'r', encoding='utf-8') as f:
        testo_prezzi = f.read()
    
    testo_prezzi = testo_prezzi.replace('€', ' ').split('\n')
    lista_testo_prezzi = testo_prezzi
    
    for elem in lista_testo_prezzi:
        info = elem.split(',')
        lista_prezzi.append(info)
    
    for elem in lista_prezzi:
        prezzi[elem[0]] = None

    for elem in lista_prezzi:
        prezzo = elem[1].strip()
        for keys in prezzi:
            if elem[0] == keys:
                prezzi[keys] = float(prezzo)
    
    return prezzi
        
    
def mostra_listino(prezzi):
    for pizza, prezzo in sorted(prezzi.items()):
        prezzo = f"{prezzo:.2f}"
        print(f"{pizza} -> €{prezzo}")
        
        
def mostra_tutti_ordini(ordini):
    for cliente, pizza in ordini.items():
        print(f"{cliente} -> {pizza}")
        

def verifica_cliente(cliente, ordini):
    for nome in ordini:
        if cliente.lower() == nome.lower():
            return True


def mostra_ordini_cliente(ordini):
    while True:
        cliente = input("Inserisci nome del cliente: ")
    
        if verifica_cliente(cliente, ordini):
            cliente = cliente.title()
            cont = 0
            
            print("-----")
            print(cliente)
            for ordine in ordini[cliente]:
                cont += 1
                print(f"Ordine N{cont} -> {ordine}")
                
            break
                
        else:
            print("Cliente non trovato.")   
            
            while True:
                pausa = False
                
                scelta = input("Vuole riprovare? (S/n): ")
                scelta = scelta.lower()
                if scelta == "s":
                    break
                elif scelta == "n":
                    pausa = True
                    break
                else:
                    print("Errore, inserire una opzione valita (s / n)")
                    
            if pausa:
                break     
        
def mostra_ordini_cliente_opt(ordini):
    cont = 0
    print("Sceglie il cliente")
    for clienti in ordini:
        cont += 1
        print(f"{cont}) {clienti}")

    while True:
        continua_sequenza = False
        
        scelta = input("Inserire opzione: ")
        if scelta.isnumeric():
            scelta = int(scelta)
            scelta -= 1
            ciclo = len(ordini.keys())
            
            cliente_trovato = False
            
            for i in range(ciclo):
                lista_clienti = list(ordini.keys())
                if scelta == i:
                    cliente = lista_clienti[scelta]
                    for ordine in ordini[cliente]:
                        print(f"Ordine di {cliente} -> {ordine}")
                        
                    cliente_trovato = True
                    break
                
            if not cliente_trovato:
                print("Errore, scelta fuori range.")
                continua_sequenza = True

            if continua_sequenza:
                continue
            
        else:
            print("Errore, caratteri sbagliati.")
            continue
        break
          
def nuovo_cliente(ordini, file):
    while True:
        cliente = input("Inserire nuovo cliente: ")
    
        if not verifica_cliente(cliente, ordini):
            cliente = cliente.title()
            ordini[cliente] = []
            
            with open(file, 'a', encoding='utf-8') as f:
                f.write(f"\n{cliente},")
                
            break
            
        else:
            print("Cliente già registrato.")
            
            while True:
                pausa = False
                
                scelta = input("Vuole riprovare? (S/n): ")
                scelta = scelta.lower()
                if scelta == "s":
                    break
                elif scelta == "n":
                    pausa = True
                    break
                else:
                    print("Errore, inserire una opzione valita (s / n)")
                    
            if pausa:
                break
        
        
def verifica_pizza(pizza, prezzi):
    for elem in prezzi:
        if pizza.lower() in elem.lower():
            return True
        
                
def aggiungi_pizza(ordini, prezzi, file):
    while True:
        cliente = input("Inserisci il cliente per l'ordine: ")
    
        if verifica_cliente(cliente, ordini):
            cliente = cliente.title()
            
            nuova_pizza = input("Inserisci pizza da ordinare: ")
            if verifica_pizza(nuova_pizza, prezzi):
                nuova_pizza = nuova_pizza.title()
                ordini[cliente].append(nuova_pizza)
                
                nuovo_testo = dict_a_testo(ordini)
                
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(nuovo_testo)
                    
                break
            
            else:
                print("Pizza non disponibile sul menu.")
                while True:
                    pausa = False
                    
                    scelta = input("Vuole riprovare? (S/n): ")
                    scelta = scelta.lower()
                    if scelta == "s":
                        break
                    elif scelta == "n":
                        pausa = True
                        break
                    else:
                        print("Errore, inserire una opzione valita (s / n)")
                        
                if pausa:
                    break 
        
        else:
            print("Cliente non trovato.")
            while True:
                pausa = False
                
                scelta = input("Vuole riprovare? (S/n): ")
                scelta = scelta.lower()
                if scelta == "s":
                    break
                elif scelta == "n":
                    pausa = True
                    break
                else:
                    print("Errore, inserire una opzione valita (s / n)")
                    
            if pausa:
                break 
        
        
def rimuovi_pizza(ordini, prezzi, file):
    while True:
        cliente = input("Inserisci nome del cliente per anullare ordine: ")
    
        if verifica_cliente(cliente, ordini):
            cliente = cliente.title()
            pizza = input("Inserisci ordine da anullare: ")
            
            if verifica_pizza(pizza, prezzi):
                pizza = pizza.title()
                if pizza in ordini[cliente]:
                    ordini[cliente].remove(pizza)
                
                    with open(file, 'w', encoding='utf-8') as f:
                        testo_nuovo = dict_a_testo(ordini)
                        f.write(testo_nuovo)
                
                    break
                
                else:
                    print("Ordine del cliente non trovata")
                    while True:
                        pausa = False
                        
                        scelta = input("Vuole riprovare? (S/n): ")
                        scelta = scelta.lower()
                        if scelta == "s":
                            break
                        elif scelta == "n":
                            pausa = True
                            break
                        else:
                            print("Errore, inserire una opzione valita (s / n)")
                            
                    if pausa:
                        break 
            else:
                print("Ordine non trovata.")
                while True:
                    pausa = False
                    
                    scelta = input("Vuole riprovare? (S/n): ")
                    scelta = scelta.lower()
                    if scelta == "s":
                        break
                    elif scelta == "n":
                        pausa = True
                        break
                    else:
                        print("Errore, inserire una opzione valita (s / n)")
                        
                if pausa:
                    break
                
        else:
            print("Cliente non trovato.")
            while True:
                pausa = False
                
                scelta = input("Vuole riprovare? (S/n): ")
                scelta = scelta.lower()
                if scelta == "s":
                    break
                elif scelta == "n":
                    pausa = True
                    break
                else:
                    print("Errore, inserire una opzione valita (s / n)")
                    
            if pausa:
                break


def rimuovi_pizza_opt(ordini, file):
    cont = 0
    print("Sceglie cliente per rimuovere ordine")
    for clienti in ordini:
        cont += 1
        print(f"{cont}) {clienti}")
    
    while True:
        continua_sequenza = False
        
        scelta = input("Inserire opzione (cliente): ")
        if scelta.isnumeric():
            scelta = int(scelta)
            scelta -= 1
            conto_pizza = 0
            ciclo = len(ordini.keys())
            pizza_da_rimuovere = 0
            
            cliente_trovato = False
            
            for i in range(ciclo):
                lista_clienti = list(ordini.keys())
                if scelta == i:
                    cliente = lista_clienti[scelta]
                    
                    cliente_trovato = True
                    
                    for ordine in ordini[cliente]:
                        conto_pizza += 1
                        print(f"{conto_pizza}) {ordine}")

                    scelta_pizza = input("Scegli una opzione: ")
                    if scelta_pizza.isnumeric():
                        scelta_trovata = False
                        scelta_pizza = int(scelta_pizza)
                        scelta_pizza -= 1
                        ciclo_pizze = len(ordini[cliente])
                        
                        for i in range(ciclo_pizze):
                            list_pizze = list(ordini[cliente])
                            if scelta_pizza == i:
                                scelta_trovata = True
                                
                                pizza_da_rimuovere = scelta_pizza
                                indice_pizza = list_pizze[pizza_da_rimuovere]
                                break
                        
                        if not scelta_trovata:
                            print("Scelta fuori range.")
                            continua_sequenza = True

                        
                    break
        
            if not cliente_trovato:
                print("Errore. Scelta fuori range.")
                continua_sequenza = True
                    
            if continua_sequenza:
                continue
            
            ordini[cliente].remove(indice_pizza)
            with open(file, 'w', encoding='utf-8') as f:
                testo_nuovo = dict_a_testo(ordini)
                f.write(testo_nuovo)
                
            print("Ordine rimossa.")
            
        else:
            print("Errore, caratteri sbagliati.")
            continue
        
        break


def conto(ordini, prezzi):
    while True:
        cliente = input("Inserisci cliente: ")
    
        if verifica_cliente(cliente, ordini):
            cliente = cliente.title()
            totale = 0
            for elem in ordini[cliente]:
                for pizza, prezzo in prezzi.items():
                    if elem == pizza:
                        totale += prezzo
                        
            print(f"Il conto di {cliente} è di {totale:.2f}€")
            
            break
            
        else:
            print("Cliente non trovato.")
            while True:
                pausa = False
                
                scelta = input("Vuole riprovare? (S/n): ")
                scelta = scelta.lower()
                if scelta == "s":
                    break
                elif scelta == "n":
                    pausa = True
                    break
                else:
                    print("Errore, inserire una opzione valita (s / n)")
                    
            if pausa:
                break


def incasso(ordini, prezzi):
    incasso = 0
    
    for pizze in ordini.values():
        for pizza in pizze:
            for tipo, prezzo in prezzi.items():
                if pizza == tipo:
                    incasso += prezzo
    
    print(f"Incasso totale: {incasso:.2f}€")
    

def pizze_ordinate(ordini):
    list_pizze_ordinate = set()
    
    for pizze in ordini.values():
        for pizza in pizze:
            list_pizze_ordinate.add(pizza)
        
    return list_pizze_ordinate       
        
        
def pizze_non_ordinate(ordini, prezzi):
    non_ordinate = []
    
    list_pizze_ordinate = pizze_ordinate(ordini)
    
    for pizza in prezzi:
        if pizza not in list(list_pizze_ordinate):
            non_ordinate.append(pizza)
    
    cont = 0
    if len(non_ordinate) > 0:
        for elem in non_ordinate:
            cont += 1
            print(f"Pizze non ordinate:")
            print(f"{cont}) {elem}")
    else:
        print("Tutte le pizze sono state ordinate.")
        
        
def pizza_piu_ordinata(ordini):
    pizze_uniche = pizze_ordinate(ordini)
    tutte_pizze = []
    
    pizza = ""
    pizza_piu = -1
    
    for pizze in ordini.values():
        for pizza in pizze:
            tutte_pizze.append(pizza)
            
    for elem in tutte_pizze:
        conto = tutte_pizze.count(elem)
        
        if conto > pizza_piu:
            pizza_piu = conto
            pizza = elem
    
    print(f"La pizza {pizza}, ordinata {pizza_piu} volte.")


def cliente_fisso(ordini, prezzo):
    conto_max = 0
    cliente_max = ""
    
    for cliente in ordini:
        conto = 0
        for pizza in prezzo:
            for ordine in ordini[cliente]:
                if ordine == pizza:
                    conto += prezzo[pizza]
        
        if conto > conto_max:
            conto_max = conto
            cliente_max = cliente
        
    print(f"{cliente_max} ha spesso di piu con un totale di {conto_max:.2f}€") 