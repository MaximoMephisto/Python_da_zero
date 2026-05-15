n = int(input("Insert a number:"))
if n < 0 or n > 20:
    print("The number is YELLOW")
elif 10 >= n > 5:
    print("The number is GREEN")
elif n >= 15:
    print("The number is WHITE")
elif n == 12:
    print("The number is BLUE")
else:
    print("The number is RED")  

# Scoprite l’elenco completo dei numeri ROSSI.
## 0, 1, 2, 3, 4, 5, 11