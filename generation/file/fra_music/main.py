import time 

from funzioni import brano_piu_presente, classifica_artisti, creazione_dict, ordina_libreria, output, sposta_brano
from funzioni import mostra_tutte
from funzioni import mostra_utente
from funzioni import aggiungi_brano
from funzioni import rimuovi_brano
from funzioni import aggiungi_utente
from funzioni import rimuovi_utente
from funzioni import aggiungi_brano
from funzioni import cerca_brano
from funzioni import statistiche_utente
from funzioni import utente_con_piu_brani
from funzioni import artisti_unici
from funzioni import brani_in_comune

from utility import stampa_menu

def main():
        
    indirizzo = 'generation/file/fra_music/dati/librerie.txt'
    librerie = creazione_dict(indirizzo)
    
    while True:
        
        stampa_menu()
        
        scelta = input("Scelta: ")
        if scelta.isnumeric():
            scelta = int(scelta)
            
            if scelta == 1:
                mostra_tutte(librerie)

            elif scelta == 2:
                nome = input("Utente: ")
                mostra_utente(librerie, nome)

            elif scelta == 3:
                nome = input("Utente: ")
                titolo = input("Titolo: ")
                artista = input("Artista: ")
                durata = input("Durata (secondi): ")
                brano = (titolo, artista, durata)
                aggiungi_brano(librerie, nome, brano, indirizzo)

            elif scelta == 4:
                nome = input("Utente: ")
                titolo = input("Titolo da rimuovere: ")
                rimuovi_brano(librerie, nome, titolo, indirizzo)

            elif scelta == 5:
                nome = input("Nome nuovo utente: ")
                aggiungi_utente(librerie, nome, indirizzo)

            elif scelta == 6:
                nome = input("Utente da rimuovere: ")
                rimuovi_utente(librerie, nome, indirizzo)

            elif scelta == 7:
                titolo = input("Titolo da cercare: ")
                cerca_brano(librerie, titolo)

            elif scelta == 8:
                nome = input("Utente: ")
                statistiche_utente(librerie, nome)

            elif scelta == 9:
                utente_con_piu_brani(librerie)

            elif scelta == 10:
                artisti_unici(librerie)

            elif scelta == 11:
                n1 = input("Primo utente: ")
                n2 = input("Secondo utente: ")
                brani_in_comune(librerie, n1, n2)

            elif scelta == 12:
                brano_piu_presente(librerie)
                
            elif scelta == 13:
                output(librerie)
                
            elif scelta == 14:
                origine = input("Utente di origine: ")
                destinazione = input("Utente di destinazione: ")
                titolo = input("Titolo del brano da spostare: ")
                sposta_brano(librerie, origine, destinazione, titolo, indirizzo)

            elif scelta == 15:
                nome = input("Utente: ")
                criterio = input("Ordina per (titolo/artista/durata): ")
                ordina_libreria(librerie, nome, criterio)

            elif scelta == 16:
                classifica_artisti(librerie)
                
            elif scelta == 0:
                print("Alla prossima!")
                break

            else:
                print("Scelta non valida.")
                
        else:
            print("Errore, il valore deve essere numerico.")

        time.sleep(5)
        
main()
