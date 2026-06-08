
spese = dict()

while True:
    print('''
        ============
            Menu
        ============
    1) Inserire spesa.
    2) Controllare bilancio.
    3) Modificare spesa.
          ''')
    
    opt = input("scegliere una opzione: ")
    if opt.isnumeric():
        opt = int(opt)
        if opt == 1:
            while True:
                spesa = input("Inserire spesa (Descrizione/importo/categoria): ")
                if "/" not in spesa:
                    print("Errore. I dati devono essere separati per \"/\".")
                else:
                    dati_spesa = spesa.split("/")
                    if len(dati_spesa) != 3:
                        print("Errore, ci devono essere 3 dati della spesa.")
                    else:
                        try:
                            if float(dati_spesa[1]):
                                conferma_importo = True
                        except ValueError:
                            conferma_importo = False
                        
                        if conferma_importo == False:
                            print("Errore, l'importo deve essere un valore numerico.")
                        else:
                            dati_spesa[1] = float(dati_spesa[1])
                            spese[dati_spesa[0]] = dict({'Importo':dati_spesa[1],'Categoria':dati_spesa[2]})
                            break
                    
        elif opt == 2:
            for descrizione, dati in spese.items():
                for dato in dati:
                    print(f"{dato}: {dati[dato]}")
        elif opt == 3:
            pass
        else:
            print("Numero fuori range.")
    else:    
        print("Errore. Scegliere valore numerico.")