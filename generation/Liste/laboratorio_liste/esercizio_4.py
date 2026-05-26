# Dopo aver letto e memorizzato 8 numeri in una lista, calcolare la somma di quelli negativi e memorizzare 
# zero al loro posto

numeri = []

for i in range(8):
    num = int(input("Inserire numeri: "))
    numeri.append(num)

print(numeri)

numeri_negativi = 0
cont = -1
for elem in numeri:
    cont += 1
    if elem < 0:
        numeri_negativi = numeri_negativi + elem
        numeri[cont] = 0
        
print(f"La somma di tutti i numeri negativi è: {numeri_negativi}")
print(numeri)