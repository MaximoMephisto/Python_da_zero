ordini = {
    101: "Marco Rossi",
    102: "Anna Bianchi",
    103: "Luca Verdi",
    104: "Sara Neri",
    105: "Paolo Gialli",
}

while True:
    ordine = input("Inserire numero di ordine: ")
    
    if ordine.isdigit(): # isnumeric() considera troppi valori come numero (Es. numeros romanos / fracciones)
        ordine = int(ordine)
        if ordine not in ordini:
            print("Inserire un valore dentro il range ordini.")
            continue
        else:
            print(f"L'ordine {ordine} è stato fatto da {ordini[ordine]}")
            break
    else:
        print("Errore, valore non ammesso.")
        continue