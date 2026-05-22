somma = 0
cont = 0
fine = 7
while True:
    if cont < fine:
        num = int(input("Inserisci numero: "))
        somma += num
        cont += 1
    else:
        break
media = somma / fine
print(media)