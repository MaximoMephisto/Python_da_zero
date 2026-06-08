def stampa_pari(numeri):
    for pari in numeri:
        if pari % 2 == 0:
            print(f"I numeri pari della lista sono: {pari}")
        

def main():
    lista = [75,43,5,36,32,34,235,23,5,235,23,632]
    stampa_pari(lista)   #la funzione deve stampare solo i numeri pari della lista passata come parametro

main()