# Normalizza spazi e capitalizzazione in una nuova lista norm: es. "De Luca, Carlo", "Bianchi, Marco".
# Unisci le due rubriche in una lista unica e crea una lista dedupe senza duplicati (stessa persona = stesso cognome+nome dopo normalizzazione).
# Ordina dedupe alfabeticamente per cognome e, a parità, per nome, usando solo operazioni su stringhe e scambi su lista (nessuna struttura extra).
# Crea una lista di liste iniziali in cui ogni elemento è del tipo ["De Luca, Carlo", "D.L.C."] (usa solo liste e stringhe).

rubrica_a = ["Rossi, Anna", "Bianchi, marco", "Verdi, Lucia", "De Luca, Carlo"]
rubrica_b = ["bianchi, Marco", "Neri, Paola", "De  luca,  carlo", "Rossi,  ANNA "]

liste_unite = rubrica_a + rubrica_b

norm = []

for persone in liste_unite:
    persone = persone.capitalize()
    persone = " ".join(persone.split())
    if persone not in norm:
        norm.append(persone)
print(norm)

norm = sorted(norm)
print(norm)
  
lettera_iniziali = ""
for nomi in norm:
    nomi = nomi.split()
    for lettera in nomi:
        lettera_iniziali = lettera_iniziali + lettera[0]
    lettera_iniziali = lettera_iniziali + " "
    lettera_iniziali = lettera_iniziali.upper()

iniziali_punto = []
lettera_iniziali = lettera_iniziali.split()
for lettere in lettera_iniziali:
    lettere = lettere.split()
    for lettera in lettere:
        lettera = list(lettera)
        lettera ='.'.join(lettera)
    iniziali_punto.append(lettera)
print(iniziali_punto)    

iniziali = []

for nomi in norm:
    list_nome_iniziali = []
    for elem in iniziali_punto:
        if norm.index(nomi) == iniziali_punto.index(elem):
            list_nome_iniziali.append(nomi)
            list_nome_iniziali.append(elem)
    iniziali.append(list_nome_iniziali)
print(iniziali)

# Genera un indice per lettera come lista di stringhe (niente dizionari), ad es.:
# ["B: Bianchi, Marco", "D: De Luca, Carlo", "N: Neri, Paola", "R: Rossi, Anna"].

indice_lettera = []
lettera_iniziali = ""
for nomi in norm:
    nomi = nomi.split()
    for lettera in nomi:
        lettera_iniziali = lettera_iniziali + lettera[0]
        print(lettera_iniziali)
        