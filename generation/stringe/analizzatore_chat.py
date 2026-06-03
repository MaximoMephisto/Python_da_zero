log_grezzo = "[09:15] anna: Ciao a tutti! qualcuno ha letto il libro che ho consigliato? #lettura @marco|[09:17] Marco: Ciao Anna! si lo sto leggendo, bellissimo @anna|[09:20] luca: io no ancora... troppo impegnato col lavoro #lavoro|[09:21] anna: dai @luca trovati cinque minuti! #lettura #consigli|[09:30] marco: secondo me a tutti piacerebbe #lettura @anna @luca|[10:05] giulia: scusate il ritardo!! di cosa parlate? @anna|[10:06] anna: ciao @giulia parlavamo di libri #lettura"

log_grezzo = log_grezzo.lower().split('|')
qta_messagi = len(log_grezzo)

print(f"{qta_messagi} messaggi")
print("----------")

ore = []
utenti = []
testi = []

tutti_messagi = []


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

    coppie_menzioni.append(utente)
    coppie_menzioni.append(cont)

    lista_menzioni.append(coppie_menzioni)
    
    
        
    
print(lista_menzioni)

    