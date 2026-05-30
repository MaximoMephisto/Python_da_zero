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

# Trova e stampa la parola più lunga di frase. A parità di lunghezza, tieni la prima.

parola_piu_lunga = ""

for parole in parole_testo:
    if len(parole) == (len(parola_piu_lunga)):
        parola_piu_lunga = parole_testo[0]
    elif len(parole) > len(parola_piu_lunga):
        parola_piu_lunga = parole

print(f"La parola piu lunga è: {parola_piu_lunga}")

# Rendi maiuscola la prima lettera di ogni parola di frase, lasciando il resto invariato. Non usare .title(). Stampa il risultato.

testo_maiuscule = ""
for parole in parole_testo:
    parola = parole[0].upper() + parole[1:]
    testo_maiuscule += " " + parola
print(testo_maiuscule)

# Tieni solo la prima occorrenza di ogni parola di frase, nell'ordine originale, e stampa la frase ripulita.
testo_pulito = ""
for parole in parole_testo:
    if parole not in testo_pulito:
        testo_pulito += " " + parole
        
print(f"Il testo pulito è: {testo_pulito}")

# Costruisci una lista di coppie [carattere, conteggio] per testo, ordinata dal più frequente al meno frequente. Ignora spazi e maiuscole. Stampala.
frequenza = []

for parole in parole_testo: 
    
    coppie = []
    coppie.append(parole)
    conteggio = testo.count(parole)
    coppie.append(conteggio) 
    
    if coppie not in frequenza:
        frequenza.append(coppie)
    
    
print(frequenza)