import customtkinter as ctk
import sys
import os

from funzioni import (
    mostra_listino, mostra_tutti_ordini, mostra_ordini_cliente,
    nuovo_cliente, aggiungi_pizza, rimuovi_pizza, conto, incasso,
    pizze_non_ordinate, pizza_piu_ordinata, cliente_fisso, creazione_dict,
    creazione_dict_prezzi
)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.indirizzo = os.path.join("generation/file/progetto_pizzeria/dati/ordini.txt")
        self.ordini = creazione_dict(self.indirizzo)
        
        self.indirizzo_prezzi = os.path.join("generation/file/progetto_pizzeria/dati/prezzi.txt")
        self.prezzi = creazione_dict_prezzi(self.indirizzo_prezzi)
        
        # SCHERMO #
        self.title('PIZZERIA - By MAx')
        self.geometry('1000x500')
        self.resizable(False, False)
        
        self.label_input = ctk.CTkLabel(self, text="Inserisci cliente")
        self.label_input.pack(pady=2)
        self.input_dati = ctk.CTkEntry(self, placeholder_text='Nome cliente...')
        self.input_dati.pack(pady=5)
        
        self.frame_button = ctk.CTkFrame(self, fg_color='transparent')
        self.frame_button.pack(pady=10)
        
        ctk.CTkButton(self.frame_button, text='Mostra listino', width=200, command=self.btn_mostra_listino).grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkButton(self.frame_button, text='Mostra ordini', width=200, command=self.btn_mostra_tutti_ordini).grid(row=0, column=1, padx=5, pady=5)
        
        
        self.scatola_testo = ctk.CTkTextbox(self, width=450, height=220, activate_scrollbars=True, font=("Courier New", 12))
        self.scatola_testo.pack(pady=5)
        
    def print_funzioni(self, funzione, *args):
        
        self.scatola_testo.delete("0.0", "end")
    
            # Print nel nostro terminal
        class redirezione:
            def __init__(self, scatola):
                self.scatola = scatola
            def write(self, texto):
                self.scatola.insert("end", texto)
            def flush(self):
                pass

        consola_original = sys.stdout
        sys.stdout = redirezione(self.scatola_testo)
        
        try:
            funzione(*args)
        finally:
            sys.stdout = consola_original
            self.ordini = creazione_dict(self.indirizzo)


    def btn_mostra_listino(self):
        self.print_funzioni(mostra_listino, self.prezzi)
        

    def btn_mostra_tutti_ordini(self):
        self.print_funzioni(mostra_tutti_ordini, self.ordini)
    
    
if __name__ == "__main__":
    app = interface()
    app.mainloop()  