# Leggere una lista di interi di 10 elementi e verificare se è palindroma (ovvero se non cambia ad 
# essere letto dalla prima cella all’ultima o viceversa).
numeri = []

for i in range(10):
    num = int(input("Inserire numeri: "))
    numeri.append(num)

numeri_al_contrario = numeri[::-1]

if numeri == numeri_al_contrario:
    print("La lista è palindroma.")
else:
    print("La lista non è palindroma.")