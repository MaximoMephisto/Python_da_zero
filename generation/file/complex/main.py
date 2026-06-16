from funzioni import (leggere_txt, trova_artista_per_lettera,
                      trova_artista_per_anno)

def main():
    indirizzo = 'generation/file/complex/dati/artisti.txt'

    persone_sistemate = leggere_txt(indirizzo)
    for elem in persone_sistemate:
        print(f"{elem[0]} {elem[1]}, {elem[2]}")
    
    lettera = input("Inserire lettera: ")
    while True:
        if len(lettera) > 1:
            lettera = input("Errore, inserire SOLO una lettera: ")
        else:
            break
    lettera = lettera.lower()
    
    print(trova_artista_per_lettera(persone_sistemate, lettera))
    
    anno = input("Inserire anno: ")
    if not anno.isnumeric():
        while True:
            anno = input("Inserire anno (valore numerico): ")
            if anno.isnumeric():
                break
    else:
        anno = int(anno)
        print(trova_artista_per_anno(persone_sistemate, anno))

main()