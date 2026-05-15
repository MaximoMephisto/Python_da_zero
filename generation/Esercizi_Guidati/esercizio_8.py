n = int(input("Insert a number:"))
if n % 2 == 1:
    print("n is a BLUE number")
if n % 2 == 0:
    print("n is a GREEN number")
if (n//2) % 2 == 0:
    print("n is a PURPLE number")
if ((n // 3) - 3) % 2 == 0:
    print("n is a YELLOW number")
    
# Trovate** almeno 9 differenti numeri BLU
## 5, 7, 9, 11, 13, 15, 17, 19, 21

# Trovate** almeno 9 differenti numeri VERDI
## 2, 4, 6, 8, 10, 12, 14, 16, 18

# Trovate** almeno 9 differenti numeri VIOLA
## 4, 6, 8, 10, 12, 14, 16, 18, 20

# Scrivete i 27 numeri che avete trovato all’interno di un commento.
## 5, 7, 9, 11, 13, 15, 17, 19, 21
## 2, 4, 6, 8, 10, 12, 14, 16, 18
## 4, 6, 8, 10, 12, 14, 16, 18, 20

# Quanti e Quali numeri GIALLI esistono?
## Tanti, parti di questi numeri sono : -3, -2, -1, 0, 1, 2, 9, 10, 11
## Da considerare che per ottenere questi numeri dobbiamo:
## (n // 3) = numero non pare
## -3 per trasformare il numero non pare ottenuto prima ad un numero pare
## n % 2 == 0 per effettivamente verificare che il numero sia pare