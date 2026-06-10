def aprire_file(file):
    with open(file, encoding='utf-8') as f: # Errore windows
        linee = f.readlines()
    return linee

def prendere_dati(contenuto):
    mails = []
    for riga in contenuto[1:]:
        lista = riga.split(",")
        nome = lista[0]
        mail = lista[-5]
        if mail != '' and mail not in mails:
            if '@' in mail:
                mails.append(mail)
        #print(nome, mail)
    
    print(len(mails))
    
    for mail in mails:
        print(mail)
        
def main():
    indirizzo = 'generation/file/trentino.txt'
    linee = aprire_file(indirizzo)
    prendere_dati(linee)

main()