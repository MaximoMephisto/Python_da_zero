# Scrivi una funzione stampa_parole(lista) che stampa ogni parola della lista.
# La funzione NON deve restituire nulla.

def stampa_parole(lista):
    for parola in lista:
        print(parola)

stampa_parole(['ciao', 'mondo'])

# Scrivi una funzione somma(a, b) che ritorna la somma dei due numeri.
def somma(a, b):
    ris = a + b
    return ris

print(somma(3, 5))

# Scrivi una funzione conta_elementi(lista) che ritorna la lunghezza della lista.
def conta_elementi(lista):
    return len(lista)

print(conta_elementi([1, 2, 3]))

# Scrivi una funzione in_maiuscolo(testo) che ritorna il testo tutto in maiuscolo.
def in_maiuscolo(testo):
    return testo.upper()

print(in_maiuscolo('ciao'))

# Scrivi una funzione rimuovi_spazi(testo) che ritorna la stringa senza spazi all'inizio e alla fine.
def rimuovi_spazi(testo):
    testo = testo.strip()
    while "  " in testo:
        testo = testo.replace("  ", " ")
    return testo
print(rimuovi_spazi("  Ciao     Mondo! "))

# Scrivi una funzione parola_lunga(lista) che ritorna la parola con più lettere.
def parola_lunga(lista):
    parola = ""
    for parole in lista:
        parole = parole.split()
        for elem in parole:
            if len(elem) > len(parola):
                parola = elem
    return parola

print(parola_lunga(['casa', 'elefante', 'sole']))

# Scrivi una funzione conta_vocali(testo) che ritorna il numero di vocali presenti.
def conta_vocali(testo):
    vocali = ["a", "e", "i", "o", "u"]
    cont = 0
    for lettere in testo:
        if lettere in vocali:
            cont += 1
    return cont

print(conta_vocali('ciao mondo'))

# Scrivi una funzione contiene(lista, parola) che ritorna True se la parola è nella lista.
def contiene(lista, parola):
    if parola in lista:
        return True

print(contiene(['ciao', 'mondo'], 'mondo'))

# Scrivi una funzione stampa_primi_tre(lista) che stampa i primi tre elementi. NON deve restituire nulla.
def stampa_primi_tre(lista):
    print(lista[:3])

stampa_primi_tre([1, 2, 3, 4, 5])

# Scrivi una funzione converti(lista) che ritorna una lista di stringhe partendo da una lista di numeri.
def converti(lista):
    lista_string = []
    for elem in lista:
        lista_string.append(str(elem))
        
    return lista_string

print(converti([1, 2, 3]))

# Scrivi una funzione unisci(a, b) che ritorna le due stringhe unite da uno spazio
def unisci(a, b):
    return(f"{a} {b}")

print(unisci('ciao', 'mondo'))

# Scrivi una funzione ordina(lista) che ritorna la lista ordinata.
def ordina(lista):
    return sorted(lista)

print(ordina([3, 1, 2]))

# Scrivi una funzione stampa_lettere(parola) che stampa ogni lettera su una riga. NON deve restituire nulla.
def stampa_lettere(parola):
    for lettere in parola:
        print(f"- {lettere}")

stampa_lettere('ciao')

# Scrivi una funzione parole_lunghe(lista) che ritorna quante parole hanno più di 3 lettere.
def parole_lunghe(lista):
    parole_trovate = []
    for parole in lista:
        if len(parole) > 3:
            parole_trovate.append(parole)
            
    return parole_trovate

print(parole_lunghe(['casa', 'di', 'sole']))

# Scrivi una funzione ultima_parola(lista) che ritorna l'ultima parola della lista.
def ultima_parola(lista):
    return lista[-1]

print(ultima_parola(['ciao', 'mondo', 'python']))