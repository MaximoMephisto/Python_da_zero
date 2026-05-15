# 4 numeri di fila
# ogni 8 SALTANDO 8 
# partendo da 4


# Come nel riepilogo originale:
num = int(input("Numero: "))
if num >= 4 and (num - 4) % 12 <= 3: # % 12 per non prendere anche i numeri giusti e fare un vero salto di 8, altrimenti se fosse % 8 prenderebbe anche i numeri giusti e sembra un salto a 4.
    print("Numero giusto.")