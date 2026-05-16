n = int(input("Insert a number:"))

if n < 8 or n > 20:
    print("The number is RED")
elif n>10:
    print("The number is YELLOW")
else:
    print("The number is VERDE")

# Scoprire un numero ROSSO
## n = 21 e n = 7

# Scoprire un numero GIALLO
## n = 11

# Scoprire un numero VERDE
## n = 8 e n = 10

# Quanti numeri VERDI ci sono? Quali?
## Due, 8 e 10 visto che elif non è n >= 10 e if n non è n <= 8
 
# Come funziona l’elemento sintattico or ? Provate a spiegarlo all’interno del codice
## Pensa l'elemento OR proprio come la traduzione e considera 