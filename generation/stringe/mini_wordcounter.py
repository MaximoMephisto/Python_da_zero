# Dato testo, costruisci una lista di coppie [parola, conteggio] 
# ordinata per frequenza decrescente. Devi: ignorare 
# maiuscole/minuscole; togliere la punteggiatura . , ! ? ;; a 
# parità di conteggio ordinare le parole in ordine alfabetico.

testo = "Il cane corre. Il gatto dorme, il cane salta!"
testo = testo.lower()

punteggiatura = ". , ! ? ;"
for simboli in punteggiatura:
    testo = testo.replace(simboli, " ")

frequence = []
ripetute = []
testo = testo.split()
conteggio = 0
for parola in testo: 
    coppie = [] 
    if parola not in coppie:
        if parola not in ripetute:
            conteggio = 1
            coppie.append(parola)
            coppie.append(testo.count(parola))
        elif parola in coppie:
            conteggio += 1
    if coppie not in frequence:
        frequence.append(coppie)

print(frequence)
    