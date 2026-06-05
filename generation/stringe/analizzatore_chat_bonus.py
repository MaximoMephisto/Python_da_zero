#     Sfida bonus
# 19. Step 19. Cifrario di Cesare. Scrivi un blocco che, data una stringa e un numero k, sposti
# ogni lettera di k posizioni nell'alfabeto (lascia invariati spazi e simboli). Usa ord() e chr().
# Cifra un messaggio con k=3 e poi decifralo con k=-3 per verificare che torni l'originale.
# Esempio con k = 3:
# originale: "ciao a tutti"
# cifrato: "fldr d wxwwl"
# decifrato: "ciao a tutti"
# 20. Step 20. Usa input() per far inserire un nuovo messaggio nel formato ora;utente;testo.
# Validalo: deve avere 3 campi, l'ora nel formato HH:MM (5 caratteri con i due punti in
# posizione 2). Se valido, aggiungilo alla lista e ristampa il report aggiornato.
# Esempio valido:
# 09:45;teo;arrivo anch'io! #lettura -> aggiunto
# Esempi rifiutati:
# ciao a tutti -> errore: servono 3 campi
# 9.45;teo;ciao -> errore: ora non valida
ciclo = 1

while ciclo == 1:
    
    log_grezzo = input("Inserisci messagio (Es. Ora;utente;messagio): ")
    dati_messagio = log_grezzo.split(";")
    while len(dati_messagio) < 3:
        print("Errore, ci devono essere 3 dati.")
        log_grezzo = input("Inserisci messagio (Es. Ora;utente;messagio): ")
        

ore = []
utenti = []
testi = []

tutti_messagi = []

qta_messagi = len(tutti_messagi)
print(f"{qta_messagi} messaggi")
print("----------")

for dati in log_grezzo:
    messagi = []
    
    dati_ora = dati.replace("[", "").split("]")
    dati_ora = dati_ora[0]
    ore.append(dati_ora)
    
    testo = dati.split("]")[1].strip()
    print(testo)
     
    nome_utenti = testo.split(":")
    
    testo = nome_utenti[1]
    testi.append(nome_utenti[1])
    
    nome_utenti = nome_utenti[0]
    utenti.append(nome_utenti)
    
    messagi.append(dati_ora)
    messagi.append(nome_utenti)
    messagi.append(testo.strip())
    
    tutti_messagi.append(messagi)
    
for messagio in tutti_messagi:
    print(messagio) 
print("----------")

print(f"Totale messagi: {len(tutti_messagi)}")
print("----------")

utenti_unici = []

for utente in utenti:
    if utente not in utenti_unici:
        utenti_unici.append(utente)
        
utenti_unici_sistemati = sorted(utenti_unici)
print(utenti_unici_sistemati)
print("----------")

contatori = []
for i in range(len(utenti_unici)):
    contatori.append(0)

for utente in utenti_unici_sistemati:
    qta_utente = utenti.count(utente)
    index_utente = utenti_unici_sistemati.index(utente)
    
    contatori[index_utente] += qta_utente
    
lista_copie = []

for utente, cont in zip(utenti_unici_sistemati, contatori):
    coppie = []
    coppie.append(utente)
    coppie.append(cont)
    lista_copie.append(coppie)

print(lista_copie)
print("----------")

utente_piu_messagi = ""
piu_messagi = 0

for utente, cont in zip(utenti_unici_sistemati, contatori):
    if cont > piu_messagi:
        piu_messagi = cont
        utente_piu_messagi = utente

print(f"Utente con piu messagi: {utente_piu_messagi} con {piu_messagi} messagi.")
    
# Step 7. Estrai tutte le menzioni: scorri le parole di ogni testo (con .split()) e tieni quelle
# che iniziano con @, togliendo l'@. Attenzione alla punteggiatura attaccata (usa
# .strip("!?.,")).

#punteggiatura = "! ? . ,"
localiza_menzione = "@"
menzioni = []
conto_menzioni = []
lista_menzioni = []
for testo in testi:
    # for simboli in punteggiatura:
    #     testo = testo.replace(simboli, " ")
    #     testo = " ".join(testo.split()) # Sistemazione spazi
    testo = testo.strip("!?.,")
    parole = testo.split()
    for elem in parole:
        if localiza_menzione in elem:
            elem = elem.replace("@", "")
            menzioni.append(elem)
            

for i in range(len(menzioni)):
    conto_menzioni.append(0) 

for utente in menzioni:
    index_utente = menzioni.index(utente)
    conto_utente = menzioni.count(utente)
    conto_menzioni[index_utente] = conto_utente


for cont, utente in zip(conto_menzioni, menzioni):
    
    coppie_menzioni = []
    
    if cont == 0:
        continue
    else:
        coppie_menzioni.append(utente)
        coppie_menzioni.append(cont)
        
    lista_menzioni.append([utente, cont])

print(f"Lista menzioni: {lista_menzioni}")
print("----------")

commenti = []

for testo in testi:
    parole = testo.split()
    for elem in parole:
        if "#" in elem:
            commenti.append(elem)          

commenti_no_duplicati = []
for commento in commenti:
    if commento not in commenti_no_duplicati:
        commenti_no_duplicati.append(commento)
        
print(commenti_no_duplicati)
print("----------")


print(f"Hashtag piu usato: {max(commenti)} ({commenti.count(max(commenti))} volte)")
print("----------")

qta_parole = []
tot_parole = 0
for testo in testi:
    parole = testo.split()
    qta_parole.append(len(parole))
    
tot_parole += sum(qta_parole)
print(f"Parole totali: {tot_parole}")
print("----------")

max_parole = 0
utente_max_parole = ""

for utente, testo in zip(utenti, testi):
    piu_parole = len(testo)
    if piu_parole > max_parole:
        max_parole = piu_parole
        utente_max_parole = utente
print(f"Messagio piu lungo: {utente_max_parole} ({max_parole} caratteri)")
print("----------")

for messagi in tutti_messagi:
    if "libr" in messagi[2]:
        print(f"{messagi[0]} {messagi[1]} -> {messagi[2].capitalize()}")
print("----------")

censured = "ciao"

for testo in testi:
    if censured in testo.lower():
        testo = testo.lower().replace(censured, "****")
        print(testo)
print("----------")

for utente, testo in zip(utenti, testi):
    if utente == "anna":
        print(testo.upper())
print("----------")

        
qta_testo = 0
tipo_orario = 0
messagi_fascie_oraria = []

for ora in ore:
    if ora[:2] == '09':
        qta_testo += 1
        tipo_orario = ora[:2]
        
messagi_fascie_oraria.append([tipo_orario, qta_testo])

qta_testo = 0
tipo_orario = 0

for ora in ore:
    if ora[:2] == '10':
        qta_testo += 1
        tipo_orario = ora[:2]
        
messagi_fascie_oraria.append([tipo_orario, qta_testo])
        
print(messagi_fascie_oraria)
print("----------")

for ora, utente, testo in zip(ore, utenti, testi):
    print(f"{ora} | {utente.upper()} -> {testo}")