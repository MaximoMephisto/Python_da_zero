ciclo = True
cont = 0
num_min = 99999999999
while ciclo == True:
    cont += 1
    num = int(input("Inserisci un numero: "))
    
    if cont == 5:
        ciclo = False
    else:
        if num < num_min:
            num_min = num
        
print(num_min)