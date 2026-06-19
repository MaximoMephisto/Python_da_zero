# partendo dal file csv calcio.csv
# Vogliamo ottenere un nuovo csv chiamato
# calcio_mini.csv

# Che conterrà rispetto l'originale sono:
# nome,ruolo,gol

# Per tutti quei giocatori che hanno fatto piu di 100 gol

import csv

file = "generation/file/csv/progetto/calcio.csv"

with open(file, 'r', encoding='utf-8') as f:
    next(f)
    scrittura_csv = csv.reader(f)
    
    mini_calcio_list = []
    
    for riga in scrittura_csv:
        
        num_gol = riga[6]
        
        if int(num_gol) > 100:
            mini_calcio_list.append((riga[0], riga[2], riga[6]))
           
           
nuovo_file = "generation/file/csv/progetto/mini_calcio.csv" 

with open(nuovo_file, 'w', encoding='utf-8', newline='') as f:
    scrittura_csv = csv.writer(f)
    eders = ["nome", "ruolo", "gol"]
    scrittura_csv.writerow(eders)
    
    mini_calcio_sort = sorted(mini_calcio_list, key=lambda x:x[0])
    
    for elem in mini_calcio_sort:
        scrittura_csv.writerow(elem)