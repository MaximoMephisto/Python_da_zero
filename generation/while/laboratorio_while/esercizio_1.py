popolazione = int(input("Popolazione: "))
tazzo_propagazione = int(input("Tazzo di propagazione: "))
while tazzo_propagazione <= 1:
    tazzo_propagazione = int(input("Errore, tazzo di propagazione deve essere maggiore 1: "))

infetti = 1
giorni = 0
while infetti <= popolazione/2:
    giorni += 1
    infetti = infetti + infetti * tazzo_propagazione
print(f"La quatita di giorni per arrivare alla meta della popolazione e {giorni}")
    