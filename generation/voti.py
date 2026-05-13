# Input di tre voti
voto_1 = float(input("Inserisci il primo voto: "))
voto_2 = float(input("Inserisci il secondo voto: "))
voto_3 = float(input("Inserisci il terzo voto: "))
# Output dei voti inseriti
print(f"I voti inseriti sono: {voto_1}, {voto_2}, {voto_3}")
# Calcolo della media dei voti
media_voti = (voto_1 + voto_2 + voto_3) / 3
# Output della media dei voti
print(f"La media dei voti è: {media_voti}")