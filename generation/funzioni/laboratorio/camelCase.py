# Scrivi una funzione camel_case(frase) che ritorna la frase con ogni 
# parola — tranne la prima — 
# che inizia con la lettera maiuscola, e senza spazi.
def camel_case(frase):
    frase = frase.split()
    frase_camel = ""
    for parole in frase:
        if parole == frase[0]:
            frase_camel += parole
        else:
            frase_camel += parole.title()
    return frase_camel

print(camel_case('ciao mondo bello'))   # atteso: 'ciaoMondoBello'