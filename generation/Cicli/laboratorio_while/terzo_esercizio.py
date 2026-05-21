sequenza = True
cont_num = 1
num_max = int(input("Inserisci numeri in maniera crescente: "))

while sequenza == True:
    num = int(input("Inserisci numeri in maniera crescente: "))

    if num < num_max:
        sequenza = False
    else:
        cont_num += 1
        num_max = num
    
print(f"Sono stati inseriti {cont_num} senza contare il numero che rompe il ciclo.")