n = int(input("Insert a number:"))
if 4 < n and n < 6:
    print("The number is PURPLE")
if 3 < n < 6:
    print("The number is VIOLET")
else:
    print("The number is GRAY")
    
# Quanti e Quali numeri VIOLA(Purple) ci sono?
## Uno, il 5

# Quanti e Quali numeri VIOLETTO(Violet) ci sono?
## Due, il 4 e 5

# Quanti e Quali numeri sono sia VIOLA che VIOLETTO?
## Uno, il 5

# Esiste un numero VIOLA e GRIGIO allo stesso tempo?
## No

# Come funziona l’elemento sintattico and? Provate a spiegarlo all’interno del codice
# usando un commento
## A differenza del OR, per garantire che AND sia True deve avere le due condizione giuste e non una delle due (o piu dichiarazioni)