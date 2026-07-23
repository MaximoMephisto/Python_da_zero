from connessione import conn_db

from functions import aggiungi_film, aggiungi_sala, assegna, mostra_film, mostra_sale, panoramica, modificare_film, modificare_sala, eliminare_film, eliminiare_sala, registrare_cliente

def main():
    
    while True:
        
        print("Benvenuto al cinema. \n Scegli una opzione:")
        
        print("1) Aggiungi film")
        print("2) Aggiungi sala")
        print("3) Assegna sala")
        print("4) Vedi i film")
        print("5) Vedi le sale")
        print("6) Panoramica")
        print("7) Modifica film")
        print("8) Modifica sala")
        print("9) Elimina film")
        print("10) Elimina sala")
        print("11) Registrare cliente")
        print("0) Exit") 
        
        opt = input("Opzione: ")
        
        if opt.isnumeric():
            opt = int(opt)
            
            if opt == 0:
                break
            
            elif opt == 1:
                nuovo_film = input("Inserisci nome film: ")
                aggiungi_film(nuovo_film) 
                
            elif opt == 2:
                nuova_sala = input("Inserisci nome sala: ") 
                aggiungi_sala(nuova_sala) 
                
            elif opt == 3:
                assegna() 
                
            elif opt == 4:
                mostra_film()
                
            elif opt == 5:
                mostra_sale()
            
            elif opt == 6:
                panoramica()
            
            elif opt == 7:
                mostra_film()
                
                film = input("Seleziona film per nome: ")
                
                modificare_film(film)
            
            elif opt == 8:
                mostra_sale()
                
                sala = input("Seleziona sala per nome: ")
                
                modificare_sala(sala)
            
            elif opt == 9:
                mostra_film()
                
                film = input("Seleziona film per nome: ")
                
                eliminare_film(film)
            
            elif opt == 10:
                mostra_sale()
                
                sala = input("Seleziona sala per nome: ")
                
                eliminiare_sala(sala)
                
            elif opt == 11:
                print("Registrare nuovo cliente")
                
                nome = input("Nome: ")
                cognome = input("Cognome: ")
                mail = input("Mail: ")
                telefono = input("Telefono: ")
                password = input("Password: ")
                
                cliente = (nome, cognome, mail, telefono, password)
                
                registrare_cliente(cliente)
                
                
                
        else:
            print("Errore, il valore deve essere numerico.")
            continue
        

main()