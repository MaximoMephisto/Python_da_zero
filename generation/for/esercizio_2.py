# Es 3. Leggere un numero naturale n e scrivere in output un numero n di ‘+’.
# (Ad esempio se leggo 5 l’output sarà: +++++ )
num = int(input("Scrivere un numero: "))
for i in range(num):
    print(f"+", end = "")