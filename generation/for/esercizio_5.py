# Scrivere un programma che verifica se un numero è un numero primo (DIFFICILE)

num = int(input("Inserisci un numero: "))
if num <= 1:
    print(f"Il numero {num} non è primo.")
else:
    primo = 0
    for i in range(2, num):
        if num % i == 0:
            primo += 1
            break
    if primo == 0:
        print(f"Il numero {num} è primo.")
    else:
        print(f"Il numero {num} non è primo.")