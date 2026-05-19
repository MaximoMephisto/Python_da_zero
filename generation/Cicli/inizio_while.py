tabellina = int(input("Quale tabellina vuoi? "))

inizio = int(input("Da dove vuoi iniziare? "))
while inizio < 0:
    inizio = int(input("Errore, l'inizio deve essere maggiore a zero. Dove vuoi iniziare? "))

stop =  int(input("Dove ti vuoi fermare? "))
while stop < 0 or stop <= inizio:
    stop = int(input("Errore, la fine deve essere maggiore a zero. Dove vuoi fermarti? "))
    
while inizio <= stop:
    print(f"{inizio} x {tabellina} = {inizio*tabellina}")
    inizio += 1