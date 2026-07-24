from functions import mostra_film, mostra_sale, panoramica

def menu():
    while True:
    
        print("Benvenuto al cinema. \n Scegli una opzione:")
        
        print("1) Vedi i film")
        print("2) Vedi le sale")
        print("3) Panoramica")
        print("4) Prenotare")
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
            
            elif opt == 4:
                #sale_per_prenotare()
                #prenotare()
                pass
                
        else:
            print("Errore, il valore deve essere numerico.")
            continue