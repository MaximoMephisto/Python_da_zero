# Leggere e memorizzare in una lista sette numeri, dopo averli letti contare quante volte è stato 
# memorizzato lo zero
numeri = []

for i in range(7):
    num = int(input("Inserire numeri: "))
    numeri.append(num)


cont = 0
for elem in numeri:
    if elem == 0:
        cont += 1

print(f"Lo zero si è inserito {cont} volte")