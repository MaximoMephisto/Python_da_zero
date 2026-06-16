import csv

with open("generation/file/proba_documento/libri.csv", "r", encoding="utf-8") as f:
    lettore_csv = csv.reader(f)
    libri = set()
    for i, riga in enumerate(lettore_csv):
        #print(riga)
        
        if i != 0:
            anno = riga[3]
            nome = riga[2]
            cont = 0
            
            if 2015 < int(anno):
                cont += 1
                libri.add(f"{nome} -> {anno}")
                
    print(libri)