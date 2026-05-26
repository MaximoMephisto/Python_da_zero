# Leggere e memorizzare in una lista, 8 numeri reali, dopo averli memorizzati calcolarne la somma e la media
numeri = []

for i in range(8):
    num = float(input("Inserire numeri reali: "))
    numeri.append(num)

somma = sum(numeri)
media = somma / len(numeri)

print(f"Media: {round(media, 2)}")

