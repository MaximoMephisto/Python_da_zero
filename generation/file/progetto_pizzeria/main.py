from utility import menu
import time

from funzioni import creazione_dict, verifica_opt, creazione_dict_prezzi

def main():
    indirizzo = "generation/file/progetto_pizzeria/dati/ordini.txt"  
    ordini = creazione_dict(indirizzo)
    
    indirizzo_prezzi = "generation/file/progetto_pizzeria/dati/prezzi.txt" 
    prezzi = creazione_dict_prezzi(indirizzo_prezzi)
    
    while True:
        menu()
    
        scelta = input("Opzione: ")
        
        if scelta.isnumeric():
            scelta = int(scelta)
            if scelta == 0:
                print("Addio!")
                break
            
            verifica_opt(scelta, ordini, prezzi, indirizzo)
            
        else:
            print("Errore, il valore deve essere un numero")
        
        time.sleep(2)

main()