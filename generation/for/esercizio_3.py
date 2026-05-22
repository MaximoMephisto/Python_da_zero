#  Leggere in input 7 numeri e calcolarne la media.
fine = 7
somma = 0
for i in range(fine):
    if i == fine-1:
        num = int(input(f"Inserisci ultimo numero: "))
    elif i == 0:
        num = int(input(f"Inserisci primo numero: "))
    else:
        num = int(input(f"Inserisci numero {i+1}: "))
    
    somma = somma + num
media = round(somma / fine, 2)
print(media)
    