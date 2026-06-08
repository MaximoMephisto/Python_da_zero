# Scrivi una funzione sostituisci(frase) che sostituisce ogni 
# 'a' con '@' e ogni 'o' con '0'.
def sostituisci(frase):
    frase = frase.replace('a', '@').replace('o','0')
    return frase

print(sostituisci('ciao'))   # atteso: 'ci@0'