from functions import aggiungi_film, aggiungi_sala, assegna, mostra_film, mostra_sale, panoramica, modificare_film, modificare_sala, eliminare_film, eliminiare_sala, registrare_utente, controllo_esistenza, creare_presentazione, crittografa
import time

def menu_admin():
    
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
        print("11) Registrare utente")
        print("12) Creare presentazione")
        print("0) Exit") 
        
        opt = input("Opzione: ")
        
        if opt.isnumeric():
            opt = int(opt)

            if opt == 1:
                nuovo_film = input("Inserisci nome film: ")
                aggiungi_film(nuovo_film) 
                time.sleep(3.0)
                
            elif opt == 2:
                nuova_sala = input("Inserisci nome sala: ") 
                aggiungi_sala(nuova_sala) 
                time.sleep(3.0)
                
            elif opt == 3:
                assegna() 
                time.sleep(3.0)
                
            elif opt == 4:
                mostra_film()
                time.sleep(3.0)
                
            elif opt == 5:
                mostra_sale()
                time.sleep(3.0)
            
            elif opt == 6:
                panoramica()
                time.sleep(3.0)
            
            elif opt == 7:
                mostra_film()
                
                film = input("Seleziona film per nome: ")
                
                modificare_film(film)
                time.sleep(3.0)
            
            elif opt == 8:
                mostra_sale()
                
                sala = input("Seleziona sala per nome: ")
                
                modificare_sala(sala)
                time.sleep(3.0)
            
            elif opt == 9:
                mostra_film()
                
                film = input("Seleziona film per nome: ")
                
                eliminare_film(film)
                time.sleep(3.0)
            
            elif opt == 10:
                mostra_sale()
                
                sala = input("Seleziona sala per nome: ")
                
                eliminiare_sala(sala)
                time.sleep(3.0)
                
            elif opt == 11:
                print("Registrare nuovo utente")
                
                nome = input("Nome: ")
                cognome = input("Cognome: ")
                mail = input("Mail: ")
                telefono = input("Telefono: ")
                password = input("Password: ")
                admin = int(input("Admin (1/0): "))
                
                utente = (nome, cognome, mail, telefono, password, admin)
                
                registrare_utente(utente)
                time.sleep(3.0)
                
            elif opt == 12:
                print("Creare nuova presentazione")
                
                mostra_sale()
                
                sala = input("Seleziona sala per nome: ")
                sala_v = controllo_esistenza("sale", sala)
                
                mostra_film()
                
                film =input("Seleziona film per nome: ")
                film_v = controllo_esistenza("film", film)
                
                giorno = input("Inserisci giorno della presentazione (anno/mese/giorno): ")
                ora = input("Inserisci orario della presentazione (ora:minuti): ")
                
                creare_presentazione("sale", "film", sala_v, film_v, giorno, ora)
                
            elif opt == 0:
                verifica = False
                print("Sessione chiusa.")
                return verifica
            
        else:
            print("Errore, il valore deve essere numerico.")
            time.sleep(3.0)
            
            continue