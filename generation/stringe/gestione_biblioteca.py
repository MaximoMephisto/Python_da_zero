dati_grezzi = " Il nome della rosa;Umberto Eco;1980;disponibile |1984;George Orwell;1949;prestato| La coscienza di Zeno ;italo svevo;1923;DISPONIBILE|Il deserto dei tartari;Dino Buzzati;1940;prestato |1984;George Orwell;1949;prestato"

# Pulizia
dati_grezzi = dati_grezzi.strip().replace("|", ",\n")
dati_grezzi = dati_grezzi.split(',\n')

libri = []

titoli = []
autori = []
anni = []
stato = []

for dati in dati_grezzi:
    dati = dati.strip().split(';')
    titoli.append(dati[0])
    
    dati[1] = dati[1].title()
    autori.append(dati[1])
    
    dati[2] = int(dati[2])
    anni.append(dati[2])
    
    dati[3] = dati[3].lower()
    stato.append(dati[3])
    
    libri.append(dati)

# Interrogazioni di base
qta_libri = len(libri)
print(f"Totale libri: {qta_libri}")

print(sorted(titoli))

for titolo in titoli:
    for anno in anni:
        vecchio = min(anni)
        recente = max(anni)
        if titoli.index(titolo) == anni.index(vecchio):
            print(f"Piu vecchio: {titolo} ({vecchio})")
            break
        if titoli.index(titolo) == anni.index(recente):
            print(f"Piu recente: {titolo} ({recente})")
            break

qta_disponibile = 0
qta_non_disponibile = 0
for elem in stato:
    if elem == "disponibile":
        qta_disponibile += 1
    elif elem == "prestato":
        qta_non_disponibile += 1
            
print(f"Prestato: {qta_non_disponibile}")
print(f"Disponibile: {qta_disponibile}")

# Ricerche e filtri
for libro in libri:
    for dati in libro:
        if "ros" in str(dati).lower():
            print(libro)

titolo_richercatto = "George Orwell"
for libro in libri:
    for dati in libro:
        if titolo_richercatto in str(dati):
            print(libro)

anno_inizio = 1940
anno_fine = 1980

for libro in libri:
    for anno in anni:
        if libri.index(libro) == anni.index(anno):
            if anno >= anno_inizio and anno <= anno_fine:
                print(libro)
                break

# Duplicati e integrità

# Nei dati c'è un libro duplicato (il '1984' compare due volte). Costruisci una nuova
# lista senza duplicati, dove due libri sono duplicati se hanno stesso titolo e stesso autore. Se
# le due copie hanno stato diverso, tieni quella disponibile.