# Creare e stampare lista
frutte = ["Mela", "Pera", "Arancia"]
print(frutte)

# Accedere agli elementi
colori = ["Rosso", "Bianco", "Rosato", "Verde"]
# Primo elemento
print(colori[0])
# Ultimo elemento con indice negativo
print(colori[-1])
# Terzo elemento
print(colori[2])
print(colori[-2])

# Modificare elemento
spesa = ["Pane", "Latte", "Uova"]
spesa[0] = "Yogurt"
print(spesa)

# Lunghezza di una lista
parole = ["ciao", "mondo", "python", "lista", "esercizio", "facile"]
print(len(parole))

# Iterare con ciclo For
citta = ["Roma", "Milano", "Napoli", "Torino", "Bologna"]
for posto in citta:
    print(posto)

# Iterare usando indice enumerate    
studenti = ["Marco", "Lucia", "Giulia", "Davide"]
for studente in enumerate(studenti):
    print(studente)

# Verificare l'appartenenza con in
lingue = ["python", "java", "rust", "go"]
print("python" in lingue)

# Somma degli elementi
valori = [4, 8, 15, 16, 23, 42]
tot = 0
for x in valori:
    tot += x
    print(f"{tot}")
print(sum(valori))

# Slicing: estrarre sotto-liste
n = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(n[0:3])
print(n[-3:])
print(n[2:7])
print(n[0:9:2])

# Invertire lista
parole = ["uno", "due", "tre", "quattro", "cinque"]
print(parole[::-1])
parole.reverse()
print(parole)

# Min, Max, Media
temperature = [22.5, 19.0, 25.3, 30.1, 28.4, 21.7, 24.0]
print(min(temperature))
print(max(temperature))
print( sum(temperature) / len(temperature), 2 )

# Contare le ocorrenze
voti = [6, 7, 6, 8, 9, 6, 7, 10, 8, 6]

print(voti.count(6))

count = 0
for voto in voti:
    if voto == 8:
        count += 1
print(f"Il numero 8 compare: {count} volte.")

# Ordinare una lista
numeri = [5, 2, 9, 1, 7, 3]
print(sorted(numeri))
numeri.sort(reverse=True)
print(numeri)

        


