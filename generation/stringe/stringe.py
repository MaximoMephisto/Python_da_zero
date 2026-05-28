# 11. Data una stringa, stampa ogni carattere in una riga separata.
stringa = "Maximo"
for elem in stringa:
    print(elem)
    
# 12. Concatena due stringhe senza utilizzare l'operatore +.
a = "Hello"
b = "World"
c = f"{a} {b}"
print(c)

# 13. Conta quante volte la lettera 'e' appare in una stringa.
a = "Hello world"
print(a.count('o'))
# Oppure
cont = 0
for elem in a:
    if elem == "o":
        cont += 1
print(cont)

# 14. Data una stringa, stampa la stessa stringa ma ogni lettera alternata in maiuscolo e minuscolo.
a = "stringa"
b = ""
for i, elem in enumerate(a): # range(len(a))

    if i % 2 == 0:
        b += elem.upper()     
    else:
        b += elem.lower()
        
print(b)

# 15. Trova la lunghezza della stringa più lunga in una lista di stringhe.
stringe = ["hello", "my", "name", "generation"]

parola = ""
lunghezza = 0

for elem in stringe:
    cont = 0
    
    for i in elem: 
        cont += 1
        
    if lunghezza < cont:
        parola = elem
        lunghezza = cont
        
print(f"La parola piu lunga è: {parola} con {lunghezza} caratteri")
        
# 16. Data una stringa, controlla se è un palindromo senza utilizzare la funzione [::-1].
a = "i topi non avevano nipoti"
a = a.replace(" ", "")
b=""

for lettere in reversed(a):
    b += lettere
if a == b:
    print("Parola palindroma")
    print(a)
    print(b)
else:
    print("La parola non è un palindromo")

# 17. Crea una nuova stringa ottenuta concatenando le prime e le ultime due lettere di una stringa data.
a = "abcxxx"
b = "xxxefg"
c = ""
for i in range(2):
    c += a[i]
    
cont = -2    
for i in range(2):
    c += b[cont]
    cont += 1

print(c)

# 18. Conta quante parole di una stringa hanno una lunghezza maggiore di 5 caratteri.
stringa = "Conta quante parole di una stringa hanno una lunghezza maggiore di 5 caratteri."
stringa_separata = stringa.split()
parole = []
for parola in stringa_separata:
    if len(parola) > 5:
        parole.append(parola)
print(f"Parole con piu di 5 caratteri: {parole}")

# 19. Crea una lista di stringhe e restituisci una nuova lista contenente solo le stringhe con almeno una
# vocale.
stringa = ["Crea", "una", "lista", "di", "stringhe", "wwww", "hhh"]
vocali = ["a", "e", "i", "o", "u"]
nuova_stringa = []
for parola in stringa:
    for vocale in vocali:
        if vocale in parola:
            nuova_stringa.append(parola)
print(nuova_stringa)

# 20. Data una stringa, sostituisci tutte le vocali con il simbolo '@'.
stringa = "Data una stringa, sostituisci tutte le vocali con il simbolo"
vocali = ["a", "e", "i", "o", "u"]

for vocale in vocali:
    if vocale in stringa:
        stringa = stringa.replace(vocale, "@")

print(stringa)