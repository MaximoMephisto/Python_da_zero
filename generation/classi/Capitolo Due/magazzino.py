class Prodotto:
    IVA = 0.22
    prodotti_creati = 0
    
    def __init__(self, nome, prezzo, quantita = 0):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita
        Prodotto.prodotti_creati += 1
        
    def valore_totale(self):
        return self.prezzo * self.quantita


    def prezzo_con_iva(self):
        return round(self.prezzo * (1 + self.IVA), 2)


    def disponibile(self):
        return self.quantita > 0


    def vendi(self, quanti):
        if self.quantita >= quanti:
            self.quantita -= quanti
            return True
        return False


    def rifornisci(self, quanti):
        self.quantita += quanti


    def __str__(self):
        return f"{self.nome} - {self.prezzo} EUR x {self.quantita}"


    def __repr__(self):
        return f"Prodotto('{self.nome}')"

mouse = Prodotto("Mouse", 25.0, 4)
tastiera = Prodotto("Tastiera", 45.0, 2)
monitor = Prodotto("Monitor", 180.0)
magazzino = [mouse, tastiera, monitor]
for p in magazzino:
 print(p)
print("prodotti creati:", Prodotto.prodotti_creati)
print("prezzo del Mouse con IVA:", mouse.prezzo_con_iva())
print("Monitor disponibile?", monitor.disponibile())
print("vendo 2 Mouse:", mouse.vendi(2))
print("vendo 5 Tastiere:", tastiera.vendi(5))
monitor.rifornisci(3)
print("dopo il rifornimento:", monitor)
totale = 0
for p in magazzino:
 totale = totale + p.valore_totale()
print("valore del magazzino:", totale)
print("solo i disponibili:", [p for p in magazzino if p.disponibile()])