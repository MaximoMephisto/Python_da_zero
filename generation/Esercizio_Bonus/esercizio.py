ricetta = input("Nome della ricetta: ")

print("################")
print("# Info Ricetta #")
print("################")
farina = float(input("Quantità di farina in grammi (Es. 200): "))
zucchero = float(input("Quantità di zucchero in grammi (Es. 150): "))
burro = float(input("Quantità di burro in grammi (Es. 20): "))
uova = int(input("Quantità di uova: "))

opt_1 = input("Ci vuole piu di una ora per la preparazione? (Es. S/n): ")
if opt_1.lower() == "s" or opt_1.lower == "si":
    ora = int(input("Inserisci ora di lavorazione: "))
    if ora < 0 or ora > 24:
        print("Errore, ora sbagliata.")
        exit()
elif opt_1.lower() == "n" or opt_1.lower() == "no":
    ora = 0
else:
    print("Errore.")
    
opt = input("Ci vuole anche qualche minuto? (Es. S/n): ")
if opt.lower() == "s" or opt.lower() == "si":
    minuti = int(input("Inserisci minuti di lavorazione: "))
    if minuti < 0 or minuti > 59:
        print("Errore, minuti sbagliati.")
        exit()
elif opt.lower() == "n" or opt.lower() == "no":
    minuti = 0   

print("########  Info Ricetta  ########")
print(f"Nome: {ricetta}")
print(f"Ore di preparazione: {ora}:{minuti}h")
print(f"Qta Farina: {farina}")
print(f"Qta Zucchero: {zucchero}")
print(f"Qta Burro: {burro}")
print(f"Qta Uova: {uova}")

farina_kg = farina / 1000
prezzo_farina = round(farina_kg * 0.90, 2)

zucchero_kg = zucchero / 1000
prezzo_zucchero = round(zucchero_kg * 1.90, 2)

burro_kg = burro / 1000
prezzo_burro = round(burro_kg * 8.50, 2)

prezzo_uovo = round(uova * 0.35, 2)

minuto_a_ora = minuti / 60
mano_opera = 15 * (ora+minuto_a_ora)

print("########   Info Costi   ########")
print(f"Prezzo della farina: {prezzo_farina} euros.")
print(f"Prezzo dello zucchero: {prezzo_zucchero} euros.")
print(f"Prezzo dell burro: {prezzo_burro} euros.")
print(f"Prezzo dell uovo: {prezzo_uovo} euros.")
print(f"Manodopera: {mano_opera}")
tot_prodotti = round(prezzo_farina + prezzo_burro + prezzo_uovo + prezzo_zucchero, 2)
tot_costi = tot_prodotti + mano_opera
print(f"Il totale dei costi dei prodotti sono {tot_prodotti} euros. Piu la manodopera {tot_costi} euros.")

# Se il costo totale è inferiore a 5 €, il prezzo di vendita è il triplo del costo.
if tot_costi < 5:
    prezzo_vendita = tot_costi * 3
    print(f"Prezzo finale: {prezzo_vendita}")
# Se il costo totale è compreso tra 5 € e 20 € (inclusi), il prezzo di vendita è il doppio e mezzo del costo.
elif tot_costi >= 5 and tot_costi <= 20:
    meta_costi = tot_costi / 2
    prezzo_vendita = (tot_costi * 2) + meta_costi
    print(f"Prezzo finale: {prezzo_vendita}")
# Se il costo totale è superiore a 20 €, il prezzo di vendita è il doppio del costo.
elif tot_costi > 20:
    prezzo_vendita = tot_costi * 2
    print(f"Prezzo finale: {prezzo_vendita}")
else:
    print("Errore")

if prezzo_vendita > 50:
    print(f"================================= Ricetta PREMIUM ================================ \n")
else:
    print(f"================================= Ricetta NORMALE ================================ \n")

print(f"Ricetta: {ricetta}€                         Ore di preparazione: {ora}:{minuti}")
print(f"Costo ingredienti: {tot_prodotti}€              Costo manodopera: {mano_opera}€")
print(f"Costo totale: {tot_costi}€             Prezzo V. Consigliato: {prezzo_vendita}€")###

if burro > 300:
    print(f"ATTENZIONE: Ricetta molto calorica.")
if uova >= 6:
    print("Ricetta RICCA.")
