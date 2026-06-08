#fare in modo che stavolta la funzione stampi da inizio a fine, scelta in input dall'utente
#esempio da dove partire? 7, dove arrivare? 15 -> questo stamperà i numeri da 7 a 15 compresi

def stampa_n(n_1, n_2):
    for i in range(n_1, n_2+1):
        print(i)

def main():
    num_1 = int(input("Inserire numero inizio:"))
    num_2 = int(input("Inserire numero fine:"))
    
    stampa_n(num_1, num_2)
    
main()