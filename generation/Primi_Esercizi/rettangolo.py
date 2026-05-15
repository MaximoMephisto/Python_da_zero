# input largezza e altezza di un rettangolo
larghezza_rettangolo = int(input("Scrivi la larghezza del rettangolo: "))
altezza_rettangolo = int(input("Scrivi la altezza del rettangolo: "))
# output larghezza e altezza del rettangolo
print(f"La larghezza del rettangolo è {larghezza_rettangolo} e l'altezza è {altezza_rettangolo}.")
# calcolo area del rettangolo
area_rettangolo = larghezza_rettangolo * altezza_rettangolo
print(f"L'area del rettangolo è {area_rettangolo}.")
# calcolo perimetro del rettangolo
perimetro_rettangolo = 2 * (larghezza_rettangolo + altezza_rettangolo)
print(f"Il perimetro del rettangolo è {perimetro_rettangolo}.")
