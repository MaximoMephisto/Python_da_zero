ora = int(input("Inserire ora: "))
minuti = int(input("Inserire minuti: "))

if (ora < 0 or ora > 23) and (minuti < 0 or minuti > 59):
    print("Ore e minuti non validi.")
elif ora < 0 or ora > 23:
    print("Errore. Ora sbagliata.")
elif minuti < 0 or minuti > 59:
    print("Errore. Minuti sbagliati.")
else:
    ora_in_minuti = ora * 60
    minuti_totali = ora_in_minuti + minuti
    print(f"Sono passati {minuti_totali} dalla mezza notte")

# True AND True = True
# True OR False = True
# Not True = False