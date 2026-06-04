t = ((1,), (-5, 0, 42), (100,(1,2,3), 7), "ciao", (3, 3, 3, 3, "luca", 9, (1,2, (1, -9))),  (-1, 999, 0, 8, -12))

#sommare tutti gli elementi di questa tupla e stampare il risultato
prima_lista = []

for elem in t:

    elem = list(elem)
    for x in elem:
        if not isinstance(x, (tuple)) and not isinstance(x, (str)):
            prima_lista.append(x)
        if isinstance(x, (tuple)):
            x = list(x)
            for e in x:
                if not isinstance(e, tuple):
                    prima_lista.append(e)
            for y in x:
                if isinstance(y, (tuple)):
                    y = list(y)
                    for p in y:
                        prima_lista.append(p)
    
    
print(sum(prima_lista))
