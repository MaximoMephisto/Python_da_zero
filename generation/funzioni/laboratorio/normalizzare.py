# Scrivi una funzione normalizza(frase) che:

# rimuove spazi iniziali e finali
# mette tutto in minuscolo
# sostituisce ogni spazio multiplo con uno solo

def normalizza(frase):
    ris = frase.strip().lower()

    while "  " in ris:
        ris = ris.replace("  ", " ")

    return ris

print(normalizza('   Ciao    MONDO  '))   # atteso: 'ciao mondo'
print(normalizza('   Ciao MONDO  '))   # atteso: 'ciao mondo'
print(normalizza('   Ciao                MONDO'))   # atteso: 'ciao mondo'
