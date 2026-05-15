import math
# Costruire un esempio dove viene chiesta all’utente un numero intero 
# n. Il programma deve assegnare alla variabile uno o più colori secondo questi criteri:
num = int(input("Inserisci numero: "))

# I numeri pari compresi tra 10 e 20 sono ROSSI
if num >= 10 and num <= 20 and num % 2 == 0:
    print(f"Il numero {num} pare è di colore ROSSO")
# I numeri dispari, positivi e divisibili per 3 sono VERDI
if num % 2 != 0 and num > 0 and num % 3 == 0:
    print(f"Il numero {num} è di colore VERDE")
# I numeri negativi dispari sono BLU
if num < 0 and num % 2 != 0:
    print(f"Il numero {num} è di colore BLU")
# I numeri 4, 6, 10 e 12 sono GIALLI
if num == 4 or num == 6 or num == 10 or num == 12:
    print(f"Il numero {num} è di colore GIALLO")
# I numeri 21,22,23,24,26,27,28,29 sono VIOLA
if num >= 21 and num <= 29:
    print(f"Il numero {num} è di colore VIOLA")
# I numeri divisibili per 10 e minori di 100 sono ARANCIONI
if num % 10 == 0 and num < 100:
    print(f"Il numero {num} è di colore ARANCIONE")
# Se n è il fattoriale (vedi laboratorio A0 esempio 3) di un numero intero compreso tra 1
# e 5 allora è NERO.
if num == math.factorial(1) or num == math.factorial(2) or num == math.factorial(3) or num == math.factorial(4) or num == math.factorial(5):
    print(f"Il numero {num} è di colore NERO")
# I numeri 3,4,5 e poi 9,10,11 e poi 15,16,17 (e così via, cioè i primi 3 numeri ogni 6 partendo da 3) sono BIANCHI.
