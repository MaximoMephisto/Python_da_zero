prodotto1 = {"nome": "Mouse", "prezzo": 25.0, "quantita": 4}
prodotto2 = {"nome": "Tastiera", "prezzo": 45.0, "quantita": 2}
prodotto3 = {"nome": "Monitor", "prezzo": 180.0, "quantita": 0}

def descrivi(p):
    return p["nome"] + " - " + str(p["prezzo"]) + " EUR x " + str(p["quantita"])


def valore_totale(p):
    return p["prezzo"] * p["quantita"]


def disponibile(p):
    return p["quantita"] > 0
    

def vendi(p, quanti):
    if p["quantita"] >= quanti:
        p["quantita"] -= quanti
        return True

    print(f"Non ci sono abbastanza pezzi di {p["nome"]}")
    return False


def valore_magazzino(lista):
    tot = 0
    
    for elem in lista:
        tot += valore_totale(elem)
    
    return tot


magazzino = [prodotto1, prodotto2, prodotto3]
print(descrivi(prodotto1))
print("valore del Mouse:", valore_totale(prodotto1))
print("Monitor disponibile?", disponibile(prodotto3))
print("valore del magazzino:", valore_magazzino(magazzino))
print("vendo 2 Mouse:", vendi(prodotto1, 2))
print(descrivi(prodotto1))
print("vendo 5 Tastiere:", vendi(prodotto2, 5))
print(descrivi(prodotto2))
print("valore del magazzino alla fine:", valore_magazzino(magazzino))