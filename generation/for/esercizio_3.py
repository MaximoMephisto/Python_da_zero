#  Leggere in input 7 numeri e calcolarne la media.
fine = 7
somma = 0
for i in range(fine):
    num = int(input("Inserisci numero: "))
    somma = somma + num
media = somma / fine
print(media)
    