class Libro:
    def __init__(self, titolo, autore, anno):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.disponibile = True
        
    def presta(self):
        if self.disponibile:
            self.disponibile = False
            return True
        
        return False
    
    
    def restituisci(self):
        if not self.disponibile:
            self.disponibile = "disponibile"
            return True
        
        return False
    
    
    def eta(self, anno_corrente):
        diferenza = anno_corrente - self.anno
        return diferenza
    
    
    def __str__(self):
        if self.disponibile:
            stato = "disponibile"
        else:
            stato = "in prestito"
            
        return f"{self.titolo} ({self.autore}, {self.anno}) - {stato}"
    

a = Libro("Il nome della rosa", "Umberto Eco", 1980)
b = Libro("La coscienza di Zeno", "Italo Svevo", 1923)
print(a)
print(b)
print("eta del primo libro nel 2026:", a.eta(2026), "anni")
print("presto il primo libro:", a.presta())
print(a)
print("provo a prestarlo di nuovo:", a.presta())
print("lo restituisco:", a.restituisci())
print(a)
print("il secondo libro e' ancora disponibile?", b.disponibile)
