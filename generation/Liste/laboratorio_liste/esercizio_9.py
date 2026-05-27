nomi = ["Marco", "Luca", "Giulia", "Sofia", "Alessandro", "Francesca", "Matteo", "Chiara", "Lorenzo", "Martina",
        "Andrea", "Sara", "Davide", "Elena", "Riccardo", "Alice", "Gabriele", "Giorgia", "Simone", "Beatrice",
        "Federico", "Valentina", "Tommaso", "Aurora", "Niccolò", "Camilla", "Edoardo", "Greta", "Stefano", "Ilaria"]

nomi_con_o = []
nomi_lunghi = []

for elem in nomi:
    
    if elem[-1] == "o":
        nomi_con_o.append(elem)
    
    if len(elem) >= 9:
        nomi_lunghi.append(elem)

print(nomi_con_o)
print(nomi_lunghi)
#creare nuove lista con:
# Nomi che terminano con la o (potete cercare su AI solo come si controlla se termina con la o una stringa)
# Nomi piu lunghi di 9 carattteri