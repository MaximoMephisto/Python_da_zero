while True:
    n = int(input("inserire numeri (inserisci 0 per uscire): "))
    i = 2 # parte dal 2 
    primo = 1

    if n < 2:
        primo = 0

    while i < n:
        if n % i == 0:
            primo = 0
        i = i + 1
    
    if primo == 0:
        print( n, "non è un numero primo")
    else:
        print(n, "è un numero primo")
    
    if n == 0:
        break

