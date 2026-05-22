# Scrivere un programma che legge 10 numeri e dice quanti sono positivi, quanti negativi e quanti nulli.
negativi = 0
positivi = 0
neutro = 0
for i in range(10):
    num = int(input("Inserisci numero: "))
    if num < 0:
        negativi += 1
    elif num > 0:
        positivi += 1
    else:
        neutro += 1
print(f"Ci sono {negativi} numeri negativi.")
print(f"Ci sono {positivi} numeri positivi.")
print(f"Ci sono {neutro} numeri neutro.")