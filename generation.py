# Calcolo della durata di un corso in giorni e ore #
# Dati di input #
nome = "Maximo"
corso = "Data Science"
durata_settimane = 10
giorni_effetive = 5
# Calcolo della durata del corso #
durata_giorni = durata_settimane * giorni_effetive
ore_di_corso = 8
durata_ore = durata_giorni * ore_di_corso
# Output #
print(f"Il corso di {corso} tenuto da {nome} dura {durata_giorni} giorni e {durata_ore} ore.")

