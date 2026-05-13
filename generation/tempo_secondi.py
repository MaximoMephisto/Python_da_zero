# Input ore, minuti e secondi
ore = int(input("Scrivi il numero di ore: "))
minuti = int(input("Scrivi il numero di minuti: "))
secondi = int(input("Scrivi il numero di secondi: "))
# Calcolare il tempo totale in secondi
# 1 ora = 3600 secondi, 1 minuto = 60 secondi    
tempo_totale_secondi = ore * 3600 + minuti * 60 + secondi
# Output
print(f"{ore} ore, {minuti} minuti e {secondi} secondi sono {tempo_totale_secondi} secondi.")
