num = 0
positivi = negativi = numPari = numDispari = 0
while num != -1:
    num = int(input("Inserisci numero: "))
    
    if num > 0:
        positivi = positivi + 1
    elif num < -1:
        negativi = negativi + 1
        
    if num > 0 and num % 2 == 0:
        numPari = numPari + 1
    if num > 0 and num % 2 != 0:
        numDispari = numDispari + 1
        
print(f"Numeri positivi: {positivi}")
print(f"Numeri negativi: {negativi}")
print(f"Numeri pari: {numPari}")
print(f"Numeri dispari: {numDispari}")
