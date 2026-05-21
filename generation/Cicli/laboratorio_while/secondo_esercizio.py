# input soldi
# pastina = 1
# panino = 1.5
# Finisce quando finisce i soldi
# calcolare numero giorni
# contare cosa a mangiato quante volte
q_soldi = float(input("Quanti soldi ha Mario?"))
borsellino = q_soldi
pastina = 1
panino = 0
giorni = 0
n_panini = 0
n_pastine = 0

while borsellino >= 0:
    giorni += 1
    code_cibo = int(input("Cosa mangierà Mario? (0=panino;1=pastina)"))

    if code_cibo == 0:
        n_panini += 1
        borsellino -= 1
    elif code_cibo == 1:
        n_pastine += 1
        borsellino -= 1.5
    else:
        print("errore, codice inserito non valido")


print(f"Con {q_soldi} Mario ha mangiato per {giorni} giorni" )
print(f"Mario ha mangiato {n_panini} panini e {n_pastine} pastine")