# Estrai solo caratteri alfabetici (niente punteggiatura) e porta tutto in minuscolo, ottenendo una lista parole.
# Crea una lista filtrate che escluda le parole presenti in stopwords (case-insensitive).
# Crea una lista lunghezze con la lunghezza di ogni parola in filtrate (stesso indice).
# Trova la parola più lunga e quante volte compare (lavora solo con liste).
# Ricostruisci una frase che alterni parole “corte” (≤4) e “lunghe” (>4) pescandole in ordine da filtrate. 
# Se una categoria finisce prima, prosegui con l’altra.

testo = "Le liste in Python sono potenti: slicing, comprensioni e molto altro. Le LISTE sono fondamentali."
stopwords = ["e", "in", "le", "sono", "molto"]

testo = testo.lower()

punteggiatura = ". , ! ? ; :"
for simboli in punteggiatura:
    testo = testo.replace(simboli, " ")

parole = testo.split()
parole_filtrate = []

for parola in parole:
    if parola not in stopwords:
        parole_filtrate.append(parola)

lunghezze_parole = []
parola_lunga = ""

for parola in parole_filtrate:
    lunghezze_parole.append(len(parola))
    if len(parola) > len(parola_lunga):
        parola_lunga = parola
        
nuovo_testo = ""
parole_corte = []
parole_lunghe = []

for parola in parole_filtrate:
    if len(parola) <= 4:
        parole_corte.append(parola)
    elif len(parola) >= 4:
        parole_lunghe.append(parola)

for parola in parole_lunghe:
    nuovo_testo += parola + " "

print(f"{parola_lunga}, {parole_filtrate.count(parola_lunga)}")
print(nuovo_testo)
