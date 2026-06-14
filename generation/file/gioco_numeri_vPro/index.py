import customtkinter as ctk
import sys
import os
from funzioni import (
    creazione_dict, mostra_tutti, mostra_storico, 
    aggiungi_giocatore, rimuovi_giocatore, statistiche, 
    classifica, record_assoluto, numeri_vinti, giocatore_piu_attivo
)

# Configuración de apariencia
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue") 

class InterfazPrograma(ctk.CTk):
    def __init__(self):
        super().__init__()

        # indirizzo = "generation/file/gioco_numeri/dati/record.txt"
        self.indirizzo = os.path.join("generation/file/gioco_numeri_vPro/dati", "record.txt")

        # giocatori = creazione_dict(indirizzo)
        self.giocatori = creazione_dict(self.indirizzo)

        self.title("GIOCO - Indovina numero By MAx") # Schermo app
        self.geometry("700(x)600".replace('(x)', 'x')) # Dimensioni e botoni (AI)
        self.resizable(False, False) # Non cambia dimensioni di schermo

        # 2. Titolo (AI)
        self.label_titulo = ctk.CTkLabel(self, text="Pannello di Controllo Giocatori", font=("Arial", 22, "bold"))
        self.label_titulo.pack(pady=15)

        # 3. INPUT generale per tutte le opzioni
        self.label_input = ctk.CTkLabel(self, text="Inserisci giocatore:", font=("Arial", 12))
        self.label_input.pack(pady=2)
        self.input_datos = ctk.CTkEntry(self, placeholder_text="Nome giocatore..", width=450, height=35)
        self.input_datos.pack(pady=5)

        # 4. Botoni con dimensione per schermo (AI)
        self.frame_botones = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botones.pack(pady=10)

        # col-12 col-md-3
        ctk.CTkButton(self.frame_botones, text="Mostra Tutti", width=140, command=self.btn_mostra_tutti).grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkButton(self.frame_botones, text="Storico Giocatore", width=140, command=self.btn_storico).grid(row=0, column=1, padx=5, pady=5)
        ctk.CTkButton(self.frame_botones, text="Aggiungi Giocatore", width=140, command=self.btn_aggiungi).grid(row=0, column=2, padx=5, pady=5)
        ctk.CTkButton(self.frame_botones, text="Rimuovi Giocatore", width=140, command=self.btn_rimuovi).grid(row=0, column=3, padx=5, pady=5)

        # col-12 col-md-3
        ctk.CTkButton(self.frame_botones, text="Statistiche", width=140, command=self.btn_statistiche).grid(row=1, column=0, padx=5, pady=5)
        ctk.CTkButton(self.frame_botones, text="Classifica", width=140, command=self.btn_classifica).grid(row=1, column=1, padx=5, pady=5)
        ctk.CTkButton(self.frame_botones, text="Record Assoluto", width=140, command=self.btn_record).grid(row=1, column=2, padx=5, pady=5)
        ctk.CTkButton(self.frame_botones, text="Giocatore Attivo", width=140, command=self.btn_attivo).grid(row=1, column=3, padx=5, pady=5)

        # col-12
        ctk.CTkButton(self.frame_botones, text="Numeri Vincenti", width=140, command=self.btn_numeri_vinti).grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        # Terminal
        self.label_consola = ctk.CTkLabel(self, text="Output gioco:", font=("Arial", 12, "bold"))
        self.label_consola.pack(pady=(10, 5), anchor="w", padx=125)

        self.scatola_texto = ctk.CTkTextbox(self, width=450, height=220, activate_scrollbars=True, font=("Courier New", 12))
        self.scatola_texto.pack(pady=5)
                      # opt  # nostre def
    def print_funzioni(self, funzione, *args):
        # Rimuove i output
        self.scatola_texto.delete("0.0", "end")
        
        # Print nel nostro terminal
        class RedirectorConsola:
            def __init__(self, scatola):
                self.scatola = scatola
            def write(self, texto):
                self.scatola.insert("end", texto)
            def flush(self):
                pass

        consola_original = sys.stdout
        sys.stdout = RedirectorConsola(self.scatola_texto)
        
        try:
            funzione(*args)
        finally:
            sys.stdout = consola_original
            # Aggiorna dict
            self.giocatori = creazione_dict(self.indirizzo)

    def btn_mostra_tutti(self):
        self.print_funzioni(mostra_tutti, self.giocatori)

    def btn_storico(self):
        nick = self.input_datos.get().strip()
        if not nick:
            self.scatola_texto.delete("0.0", "end")
            self.scatola_texto.insert("0.0", "Errore: Inserisci un nickname nell'input in alto.")
            return
        self.print_funzioni(mostra_storico, self.giocatori, nick)

    def btn_aggiungi(self):
        nick = self.input_datos.get().strip()
        if not nick:
            self.scatola_texto.delete("0.0", "end")
            self.scatola_texto.insert("0.0", "Errore: Inserisci il giocatore da aggiungere.")
            return
        self.print_funzioni(aggiungi_giocatore, self.giocatori, nick, self.indirizzo)
        self.input_datos.delete(0, 'end')

    def btn_rimuovi(self):
        nick = self.input_datos.get().strip()
        if not nick:
            self.scatola_texto.delete("0.0", "end")
            self.scatola_texto.insert("0.0", "Errore: Inserisci il giocatore da rimuovere.")
            return
        self.print_funzioni(rimuovi_giocatore, self.giocatori, nick, self.indirizzo)
        self.input_datos.delete(0, 'end')

    def btn_statistiche(self):
        nick = self.input_datos.get().strip()
        if not nick:
            self.scatola_texto.delete("0.0", "end")
            self.scatola_texto.insert("0.0", "Errore: Inserisci un giocatore.")
            return
        self.print_funzioni(statistiche, self.giocatori, nick)

    def btn_classifica(self):
        self.print_funzioni(classifica, self.giocatori)

    def btn_record(self):
        self.print_funzioni(record_assoluto, self.giocatori)

    def btn_attivo(self):
        self.print_funzioni(giocatore_piu_attivo, self.giocatori)

    def btn_numeri_vinti(self):
        self.print_funzioni(numeri_vinti, self.giocatori)


if __name__ == "__main__":
    app = InterfazPrograma()
    app.mainloop()