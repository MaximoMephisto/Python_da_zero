class CartaFedelta:
    PUNTI_PER_EURO = 2
    SFOGLIA_PREMIO = 100
    carte_emesse = 0
    
    def __init__(self, intestatario, punti=0):
        self.intestatario = intestatario
        self.punti = punti
        CartaFedelta.carte_emesse += 1
    
    def acquista(self, euro):
        punti_guadagnati = int(euro) * self.PUNTI_PER_EURO
        self.punti += punti_guadagnati
        return punti_guadagnati
    
    
    def punti_mancanti(self):
        if self.punti < self.SFOGLIA_PREMIO:
            return self.SFOGLIA_PREMIO - self.punti
        return 0
    
    
    def usa_premio(self):
        if self.punti_mancanti() == 0: 
            self.punti -= self.SFOGLIA_PREMIO  
            return True
        return False
    
    
    def __str__(self):
        return f"{self.intestatario}: {self.punti} punti."
    
    
    def __repr__(self):
        return f"CartaFedelta('{self.intestatario}', {self.punti})"


anna = CartaFedelta("Anna Rossi")
luca = CartaFedelta("Luca Bianchi")
print(anna)
print(luca)
print("carte emesse:", CartaFedelta.carte_emesse)
print("Anna spende 30 euro e guadagna", anna.acquista(30), "punti")
print("le mancano", anna.punti_mancanti(), "punti al premio")
print("puo' usare il premio?", anna.usa_premio())
print("Anna spende altri 25 euro e guadagna", anna.acquista(25), "punti")
print(anna)
print("le mancano", anna.punti_mancanti(), "punti al premio")
print("puo' usare il premio?", anna.usa_premio())
print(anna)
print("la carta di Luca e' rimasta a", luca.punti, "punti")
print([anna, luca])
