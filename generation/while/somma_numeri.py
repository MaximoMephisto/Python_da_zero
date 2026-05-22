num = int(input("Inserire numero: "))
num_riserva = 0

while num != -1: # ciclo
    num_riserva += num  # Contatore
    num = int(input("Inserire numero: ")) # iterazione: Un giro del ciclo
print(num_riserva)