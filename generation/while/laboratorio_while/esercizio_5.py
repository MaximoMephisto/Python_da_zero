cont = 0

while True:
    
    num = int(input("Inserisci un numero: "))
    if cont == 0:
        num_min = num
    
    cont += 1
    
    if cont == 5:
        break
    else:
        if num < num_min:
            num_min = num
        
print(num_min)