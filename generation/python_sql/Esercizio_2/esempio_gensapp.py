import mysql.connector
from mysql.connector import errorcode

mydb = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '1234',
    database="gensapp"
)

def mostra_utenti():
    q = "SELECT * FROM utenti"

    mycursor.execute(q)

    result = mycursor.fetchall()

    for utente in result:
        print(utente[0], "->", utente[1])

def menu():
    print("1) manda messaggio")
    print("2) leggi messaggi")



mycursor = mydb.cursor()

while True:
    menu()

    scelta = int(input("Scelta: "))

    if scelta == 1:
        mostra_utenti()

        scelta_mittente = int(input("Scegli id mittente: "))
        scelta_destinatario = int(input("Scegli id destinatario: "))
        messaggio = input("Inserisci qui il messaggio: ")
        
        id_ordinati = sorted([scelta_mittente, scelta_destinatario])
        chiave_chat = f"chiave_{id_ordinati[0]}_{id_ordinati[1]}"

        q = "INSERT INTO messaggi(messaggio, mittente_id, destinatario_id) VALUES (AES_ENCRYPT(%s, %s), %s, %s)"
        val = (messaggio, chiave_chat, scelta_mittente, scelta_destinatario)

        mycursor.execute(q, val)
        mydb.commit()

    elif scelta == 2:
        mostra_utenti()

        scelta_mittente = int(input("Scegli id mittente: "))

        scelta_destinatario = int(input("Scegli id destinatario: "))
                
        id_ordinati = sorted([scelta_mittente, scelta_destinatario])
        chiave_chat = f"chiave_{id_ordinati[0]}_{id_ordinati[1]}"


        q = """SELECT messaggi.id, AES_DECRYPT(messaggi.messaggio, %s), u1.username, u2.username, messaggi.ora_invio 
                FROM messaggi
                JOIN utenti u1 on messaggi.mittente_id = u1.id
                JOIN utenti u2 on messaggi.destinatario_id = u2.id
                WHERE destinatario_id IN (%s, %s) AND mittente_id IN (%s, %s)
                order by ora_invio;
        """
        val = (chiave_chat, scelta_mittente, scelta_destinatario,  scelta_mittente, scelta_destinatario)

        mycursor.execute(q, val)

        result = mycursor.fetchall()
        
        for elem in result:
            id_msg, messagio, mittente, destinatario, ora = elem
            print(f"[{ora:%d/%m/%Y %H:%M}]  #{id_msg}  {mittente} → {destinatario}")
            
            if messagio is not None:
                print(f"{messagio.decode('utf-8')}")
            else:
                print("Errore.")


