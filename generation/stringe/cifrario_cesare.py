# Sposta ogni lettera minuscola (a–z) in avanti di spostamento posizioni, con "ritorno a capo" (dopo z si ricomincia da a). Lascia invariato tutto il resto. Stampa il testo cifrato.
testo = "ciao mondo!"
#print(ord("b"))
#print(chr(98))
#print(chr("b"))
parole_testo = testo.split()
testo_mosso = ""

for parole in parole_testo:
    list_parole = parole.split()
    #print(list_parole)
    parola_mossa = ""
    for parola in list_parole:
        for lettera in parola:
            if lettera.islower():
                codice_n = ord(lettera)
                n_lettera = codice_n + 1
                #print(chr(n_lettera))
            parola_mossa += chr(n_lettera)
    testo_mosso += parola_mossa + " "
    
print(f"{testo} -> {testo_mosso}")
                