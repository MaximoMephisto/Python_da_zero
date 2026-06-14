# ====== MENU PRINCIPALE (già pronto — NON modificare) ======
# Raccoglie gli input e chiama la funzione giusta.
# Tu devi solo implementare le funzioni nelle celle sopra.
import time

from utility import stampa_menu
from funzioni import mostra_tutti, gioca, mostra_storico, creazione_dict, aggiungi_giocatore, rimuovi_giocatore, statistiche, classifica, record_assoluto, numeri_vinti, giocatore_piu_attivo

def main():
    #questi dati messi cosi, sono hardcoded, prendiamoli dal file record.txt
    
    indirizzo = "generation/file/gioco_numeri/dati/record.txt"
    giocatori = creazione_dict(indirizzo)

    while True:
        stampa_menu()

        scelta = input("Scelta: ")

        if scelta.isnumeric():
            scelta = int(scelta)
            if scelta == 1:
                mostra_tutti(giocatori)
                
            elif scelta == 2:
                nick = input("Nickname: ")
                mostra_storico(giocatori, nick)

            elif scelta == 3:
                nick = input("Nickname: ")
                gioca(giocatori, nick, indirizzo)

            elif scelta == 4:
                nick = input("Nickname nuovo giocatore: ")
                aggiungi_giocatore(giocatori, nick, indirizzo)

            elif scelta == 5:
                nick = input("Nickname da rimuovere: ")
                rimuovi_giocatore(giocatori, nick, indirizzo)

            elif scelta == 6:
                nick = input("Nickname: ")
                statistiche(giocatori, nick)

            elif scelta == 7:
                classifica(giocatori)

            elif scelta == 8:
                record_assoluto(giocatori)

            elif scelta == 9:
                numeri_vinti(giocatori)

            elif scelta == 10:
                giocatore_piu_attivo(giocatori)

            elif scelta == 0:
                print("Alla prossima!")
                break

            else:
                print("Scelta non valida.")

        else:
            print("La scelta deve essere numerica.")
            
        time.sleep(2)


main()