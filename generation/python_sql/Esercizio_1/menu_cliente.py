from functions import aggiungi_film, aggiungi_sala, assegna, mostra_film, mostra_sale, panoramica, modificare_film, modificare_sala, eliminare_film, eliminiare_sala, registrare_utente

def menu():
    while True:
    
        print("Benvenuto al cinema. \n Scegli una opzione:")
        
        print("1) Vedi i film")
        print("2) Vedi le sale")
        print("3) Panoramica")
        print("0) Exit") 
        
        opt = input("Opzione: ")
        
        if opt.isnumeric():
            opt = int(opt)
            
            if opt == 0:
                break
                
            elif opt == 1:
                mostra_film()
                
            elif opt == 2:
                mostra_sale()
            
            elif opt == 3:
                panoramica()
            
                
        else:
            print("Errore, il valore deve essere numerico.")
            continue