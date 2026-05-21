num_riserva = 0
cont = 0
fine = 7
while True:
    if cont < fine:
        num = int(input("Inserisci numero: "))
        num_riserva += num
        cont += 1
    else:
        break
media = num_riserva / fine
print(media)