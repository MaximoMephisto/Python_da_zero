colori = ["rosso", "verde", "blu", "giallo", "viola", "arancio"]
#chiedere all'utente quale colore della lista vuole modificare, e chiedere con quale colore vuole modificarlo
while True:
    colore_modifica = input("Quale colore vuoi modificare? ")
    if colore_modifica in colori:
        break
    
count = -1
for colore in colori:
    count += 1
    if colore == colore_modifica:
        nuovo_colore = input("Scrivi il nuovo colore: ")
        colori[count] = nuovo_colore
        
print(colori)