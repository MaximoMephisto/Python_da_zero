# I mesi dell'anno possono essere numerati da 1 a 12.
# Realizzare un programma che dato il numero di un mese 
# (fornito dall'utente con input)
# restituisca il numero dei giorni di quel mese
gennaio = "31" 
febbraio = "28"
marzo = "31"
aprile = "30"
maggio = "31"
giunio = "30"
giuglio = "31"
agosto = "31"
settembre = "30"
ottobre = "31"
novembre = "30"
dicembre = "31"

num_mese = int(input("Scegli il NUMERO del mese (Es. 2): "))
if num_mese == 1:
    print(gennaio)
elif num_mese == 2:
    print(febbraio)
elif num_mese == 3:
    print(marzo)
elif num_mese == 4:
    print(aprile)
elif num_mese == 5:
    print(maggio)
elif num_mese == 6:
    print(giunio)
elif num_mese == 7:
    print(giuglio)
elif num_mese == 8:
    print(agosto)
elif num_mese == 9:
    print(settembre)
elif num_mese == 10:
    print(ottobre)
elif num_mese == 11:
    print(novembre)
elif num_mese == 12:
    print(dicembre)
else:
    print("Errore, mese non riconosciuto.")
    
    
    
        
    
    