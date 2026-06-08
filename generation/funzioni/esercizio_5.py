#dati questi nomi
# nomi = ["Marco", "Giulia", "Alessandro", "Francesca", "Luca", "Chiara",
#         "Matteo", "Sara", "Andrea", "Valentina", "Davide", "Martina",
#         "Simone", "Elena", "Federico", "Alice", "Lorenzo", "Giorgia",
#         "Riccardo", "Beatrice"]
#creare una funzione iniziali() che prende la lista come parametro e RESTITUISCE la 
# lista con le solo iniziali di ciascuna stringa

def iniziali(lista):
    iniziali_nomi = []
    for nomi in lista:
        iniziali_nomi.append(nomi[0])
    return iniziali_nomi        

def main():
    nomi = ["Marco", "Giulia", "Alessandro", "Francesca", "Luca", "Chiara",
        "Matteo", "Sara", "Andrea", "Valentina", "Davide", "Martina",
        "Simone", "Elena", "Federico", "Alice", "Lorenzo", "Giorgia",
        "Riccardo", "Beatrice"]
    lista_iniziali = iniziali(nomi)
    print(lista_iniziali)
    
main()