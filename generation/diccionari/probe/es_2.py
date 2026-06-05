scrivania = {
            'carta':5,
            'matite':2,
            'penne':3
}

while True:
    opt = input("Inserisci 1 per modificare, 2 per cambiare key: ")
    
    if opt.isdigit():
        opt = int(opt)
        if opt == 1:
            while True:
                obj = input("Inserisci cosa vuoi modificare: ")
                if obj not in scrivania:
                    print("Errore, non si trova.")
                    continue
                else:
                    while True:
                        modifica = input("Inserire modifica: ")
                        if modifica.isdigit():
                            break
                        else:
                            print("Modifica sbagliata.")
                    modifica = int(modifica)
                    scrivania[obj] = modifica
                    break
        elif opt == 2:
            while True:
                key = input("Inserisci la key che vuoi modificare: ")

                if key in scrivania:
                    del scrivania[key]
                    nuova_key = input("Inserisci nuova key: ")
                    valore_nuova_key = int(input("Inserire valore key: "))
                    scrivania[nuova_key] = valore_nuova_key
                    break
                else:
                    print("Key non trovata.")
        else:
            print("Inserire opt giusta.")
        print(scrivania)
        uscita = input("Vuoi uscire dal programma? (S/n): ")
        uscita.lower()
        if uscita == "s":
            break
    else:
        print("Inserire opt giusta.")
    
