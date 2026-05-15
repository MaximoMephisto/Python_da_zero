# Dato un numero in input, verificare se contiene un valore pari o dispari 
# e se è positivo o negativo.

num = int(input("Scrivi un numero: "))
num_pare = num % 2

if num_pare == 0 and num > 0:
    print("Il numero è pari positivo")
elif num_pare == 0 and num < 0:
    print("Il numero è pare negativo")
elif num_pare != 0 and num > 0:
    print("Il numero non è pare ma è positivo")
elif num_pare != 0 and num < 0:
    print("Il numero non è pare ed è negativo")
else:
    print("Errore: Riprovare.")
    
    