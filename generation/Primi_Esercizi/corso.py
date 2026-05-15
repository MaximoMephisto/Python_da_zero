# Calcolo della durata di un corso in giorni e ore #

# Dati di input 
nome = input("Scrivi il tuo nome: ")
corso = input("Scrivi il nome del corso: ")
durata_settimane = int(input("Scrivi la durata del corso in settimane: "))
giorni_effetive = int(input("Scrivi il numero di giorni effettivi a settimana: "))

# Calcolo della durata del corso 
durata_giorni = durata_settimane * giorni_effetive
ore_di_corso = 8
durata_ore = durata_giorni * ore_di_corso
# Output 
print(f"Il corso di {corso} tenuto da {nome} dura {durata_giorni} giorni e {durata_ore} ore.")

