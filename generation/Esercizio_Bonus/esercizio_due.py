# Giulia ha aperto da poco un piccolo servizio di noleggio biciclette in una località turistica. 
# Ogni volta che arriva un cliente al banco, deve calcolare a mano il prezzo del noleggio tenendo 
# conto del tipo di bicicletta, della durata, della stagione e di eventuali accessori richiesti. 
# Durante l'alta stagione si formano code lunghissime e Giulia commette spesso errori nei conteggi. 
# Vorrebbe un programma che la aiuti a calcolare in modo rapido e affidabile il prezzo finale del noleggio. 
# Scrivere un programma che:

# Chiede all'utente il nome del cliente.
# Chiede all'utente il tipo di bicicletta noleggiata, indicato tramite un codice numerico: 1 per 
# bicicletta da città, 2 per mountain bike, 3 per bicicletta elettrica.
# Chiede all'utente il numero di ore di noleggio.
# Chiede all'utente il numero di caschi richiesti come accessorio.
# Chiede all'utente se il noleggio avviene in alta stagione, indicato con 1 per sì e 0 per no.
# Conferma all'utente i dati inseriti.

print("=================================")
print("Benvenuti al servizio di noleggio")
print("=================================")

nome_cliente = input("Inserisci il tuo nome: ")

print("1) Bicicletta di città.")
print("2) Mountain Bike.")
print("3) Bicicletta elettrica.")

opt = int(input("Sceglie una opzione (Es. 2): "))
if opt <= 0 or opt > 3:
    print("Error. Scegliere una opzione giusta.")
    exit()
elif opt == 1:
    prezzo_bici = 3
elif opt == 2:
    prezzo_bici = 5
elif opt == 3:
    prezzo_bici = 8

orario = input("Quante ore vuole noleggiare? (Es. 1:30): ")
ore, minuti = orario.split(":")
ore = int(ore)
minuti = int(minuti)
if ore < 0 or ore > 23:
    print("Errore, ora non giusta.")
    exit()
else:
    if minuti < 0 or minuti > 59:
        print("Errore, minuti non giusti.")
        exit()
    else:
        minuti_a_ora = minuti / 60
        tot_orario = minuti_a_ora + ore



# Il programma deve poi calcolare il costo del noleggio sapendo che:

# La bicicletta da città costa 3 € all'ora.
# La mountain bike costa 5 € all'ora.
# La bicicletta elettrica costa 8 € all'ora.
# Se l'utente inserisce un codice di bicicletta diverso da 1, 2 o 3, il programma deve terminare segnalando 
# che il tipo di bicicletta non è disponibile.

# A questo costo va aggiunto il costo degli accessori, pari a 2 € per ogni casco noleggiato.
# Una volta calcolato il costo base del noleggio (bicicletta + accessori), il programma deve applicare 
# eventuali maggiorazioni o sconti secondo questi criteri:

# Se il noleggio avviene in alta stagione, il prezzo viene aumentato del 30%.
# Se la durata del noleggio è superiore a 8 ore, viene applicato uno sconto del 15% sul totale (calcolato dopo 
# l'eventuale maggiorazione stagionale).
# Se la durata del noleggio è inferiore a 2 ore, viene applicato un supplemento fisso di 4 € per la gestione della 
# pratica.