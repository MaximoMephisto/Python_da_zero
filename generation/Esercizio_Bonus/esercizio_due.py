print("=================================")
print("Benvenuti al servizio di noleggio")
print("=================================")

nome_cliente = input("Inserisci il tuo nome: ")


print("0) Noleggio di bassa stagione.")
print("1) Noleggio di alta stagione.")
stagione = int(input("Inserisci il periodo di noleggio (Es. 0): "))
if stagione < 0 or stagione > 1:
    print("Error. Scegliere opzione giusta.")
else:

    print("1) Bicicletta di città.")
    print("2) Mountain Bike.")
    print("3) Bicicletta elettrica.")

    opt = int(input("Sceglie una opzione (Es. 2): "))
    if opt <= 0 or opt > 3:
        print("Error. Scegliere una opzione giusta.")
    elif opt == 1:
        nome_bici = "Bicicletta di città"
        prezzo_bici = 3
    elif opt == 2:
        nome_bici = "Mountain Bike"
        prezzo_bici = 5
    elif opt == 3:
        nome_bici = "Bicicletta elettrica"
        prezzo_bici = 8

    if opt == 1 or opt == 2 or opt == 3:
        orario = input("Quante ore vuole noleggiare? (Es. 1:30): ")
        ore, minuti = orario.split(":")
        ore = int(ore)
        minuti = int(minuti)

        if ore < 0 or ore > 23:
            print("Errore, ora non giusta.")
        elif minuti < 0 or minuti > 59:
            print("Errore, minuti non giusti.")
        else:
            minuti_a_ora = minuti / 60
            tot_orario = minuti_a_ora + ore
            
            opt_1 = input("Desidera aggiungere dei caschi? (Es. S/n): ")
            if opt_1.lower() == "s" or opt_1.lower() == "si":
                caschi = int(input("Inserisci il numero di caschi: "))
                if caschi < 0:
                    print("Error, inserire numero valido.")
                else:
                    accessori = caschi * 2
            elif opt_1.lower() == "n" or opt_1.lower == "no":
                caschi = 0
                accessori = 0
            else :
                print("Errore, caratteri non accetatti.")

            if (opt_1 == "s" or opt_1 == "si" or opt_1 == "n" or opt_1 == "no") and (caschi >= 0):
                tot_noleggio = (prezzo_bici * tot_orario) + accessori

                print("=================")
                print("= Noleggio Bici =")
                print(f"Tipo: {nome_bici}")
                print(f"Tempo di noleggio: {ore}:{minuti}h")
                print(f"Accesori aggiunti: {caschi}")
                if stagione == 1:
                    percentuale = (round(tot_noleggio) / 100) * 30
                    tot_noleggio = tot_noleggio + percentuale
                    print("Aumento del 30% per alta stagione.")
                if tot_orario > 8:
                    percentuale = (round(tot_noleggio) / 100) * 15
                    tot_noleggio = tot_noleggio - percentuale
                    print("Sconto applicato del 15% per durata del noleggio.")
                if tot_orario > 6 and opt == 3:
                    print("VERIFICARE LA CARICA DELLA BATTERIA")
                if tot_orario < 2:
                    supplemento = 4
                    tot_noleggio = tot_noleggio + supplemento
                    print("4£ di supplemento fisso per gestione e durata del noleggio..")
                print(f"Prezzo totale del noleggio: {round(tot_noleggio, 2)}£")