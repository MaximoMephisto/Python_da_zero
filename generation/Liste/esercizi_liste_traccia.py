# Esercizio 1 — Stampa elementi uno per riga
nomi = ["Anna", "Bruno", "Carla", "Dario"]
for nome in nomi:
    print(nome)

# Esercizio 2 — Primo, ultimo e centrale
n = [10, 20, 30, 40, 50, 60, 70]
print(f"Primo: {n[0]}")
print(f"Ultimo: {n[-1]}")
centrale = len(n) // 2
print(f"Centrale: { n[centrale] }")

# Esercizio 3 — Somma e media
voti = [6, 7, 8, 5, 9, 10, 4]
print(f"Suma: {sum(voti)}")
print(f"Media: {sum(voti) / len(voti)}")

# Esercizio 4 — Conta pari e dispari
n = [3, 8, 12, 5, 7, 4, 9, 10, 1, 6]

pari = 0
dispari = 0

for i in n:
    if i % 2 == 0:
        pari += 1
    else:
        dispari += 1

print(f"Ci sono {pari} pari e {dispari} dispari.")

# Esercizio 5 — Massimo e minimo senza max() e min()
n = [42, 7, 19, 88, 3, 55, 21, 64]

n_max = n[0]
n_min = n[0]

for elem in n:
    if elem > n_max:
        n_max = elem
    if elem < n_min:
        n_min = elem
        
print(n_max)
print(n_min)

# Esercizio 6 — Conta le occorrenze (senza .count())
lettere = ['a', 'b', 'a', 'c', 'd', 'a', 'b', 'a']
cercato = 'a'
count = 0

for lettera in lettere:
    if lettera == cercato:
        count += 1
        
print(f"La lettera 'a' si trova {count} volte.")

# Esercizio 7 — Trova la posizione (senza .index())
n = [10, 20, 30, 40, 50, 30, 60]
cercato = 30
count = -1
posizione = []

for i in n:
    count += 1
    if i == cercato:
        posizione.append(count)

if cercato not in n:
    print(-1)
else:
    print(posizione)
    
# Esercizio 9 — Filtra i numeri positivi
n = [-3, 5, 0, -1, 8, -7, 2, 4, -9, 6]
n_positivi = []
for i in n:
    if i > 0:
        n_positivi.append(i)
print(n_positivi)

# Esercizio 10 — Rimuovi i duplicati mantenendo l'ordine
l = [1, 3, 2, 3, 4, 1, 5, 2, 6, 4]
l_ordinata = []

for i in l:
    if i not in l_ordinata:
        l_ordinata.append(i)
print(l_ordinata)

# Esercizio 11 — Somma di due liste posizione per posizione
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]
c = []
count = -1
for n in a:
    count += 1
    nuovo_num = a[count] + b[count]
    c.append(nuovo_num)
print(c)

# Esercizio 12 — Verifica se è ordinata in modo crescente
a = [1, 3, 5, 7, 9]
if a == sorted(a):
    print("True")
else:
    print("False")
    
b = [1, 3, 2, 7, 9]
if b == sorted(b):
    print("True")
else:
    print("False")
