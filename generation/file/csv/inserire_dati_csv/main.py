import csv

abitanti = {
    "Roma": 2748000,
    "Bologna": 392000,
    "Torino": 841000,
    "Palermo": 630000,
    "Firenze": 366000,
    "Milano": 1372000,
    "Napoli": 909000,
    "Genova": 558000,
    "Bari": 316000,
    "Foggia": 144000,
}
                                                                                        # ogni linea nuova no ci sara un salto 
                                                                                        # linea senno uno spazio vuoto
with open("generation/file/csv/inserire_dati_csv/popolazione.csv", "w", encoding="utf-8", newline='') as f:
    scrittore_csv = csv.writer(f)
    
    for elem in abitanti.items():
        scrittore_csv.writerow(elem)
    