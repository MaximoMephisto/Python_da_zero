# Una classe è un oggetto, i campi/attributi sono le caratteristiche (cosa ha quel oggetto)
# I metodi (funzioni) sono le funzioni del oggetto, le azioni che il oggetto riesce a fare.

class Prodotto:
    def __init__(self, nome, prezzo, quantita):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita


    def valore_totale(self):
        return self.prezzo * self.quantita


    def descrivi(self):
        print(f"Prodotto: {self.nome} | Prezzo: {self.prezzo}€ | Quantità: {self.quantita}")


    def disponibile(self):
        return self.quantita > 0


    def vendi(self, quanti):
        if self.quantita >= quanti:
            self.quantita -= quanti
            return True
        print(f"Non ci sono abbastanza pezzi di {self.nome}")
        return False

prodotto1 = Prodotto("Mouse", 25.0, 4)
prodotto1.descrivi()
print(prodotto1.disponibile())
prodotto1.vendi(2)
print(prodotto1.quantita)
