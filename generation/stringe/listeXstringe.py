# Conta quante vocali (a, e, i, o, u) ci sono in testo, ignorando 
# maiuscole/minuscole. Stampa il numero.
testo = input("Ingrese testo: ")
testo = testo.lower()

vocali = ["a", "e", "i", "o", "u"]
cont = 0

for vocale in vocali:
    if vocale in testo:
        cont += 1
print(cont)

# Costruisci una lista con la lunghezza di ogni parola di frase e 
# stampala.
lunghezza_parole = []
parole_testo = testo.split()

cont = 0
for parole in parole_testo:
    lunghezza_parole.append(len(parole))
    
print(lunghezza_parole)

# Stampa frase con le parole in ordine inverso (i caratteri di ogni 
# parola restano uguali).

for parole in parole_testo:
    testo_invertito = parole_testo[::-1]

nuovo_testo = " ".join(testo_invertito)
print(nuovo_testo)

# Stabilisci se testo si legge uguale anche al contrario (ignorando 
# maiuscole e spazi) e stampa True o False.

testo = testo.replace(" ", "")
testo_invertito_due = "".join(reversed(testo))
if testo == testo_invertito_due:
    print("True")
else:
    print("False")
