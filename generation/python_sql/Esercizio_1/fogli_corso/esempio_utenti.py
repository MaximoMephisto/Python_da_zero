import mysql.connector
from mysql.connector import errorcode
import hashlib

#ripartire da criptare psw direttamente lato db

def controlla(s, numeri, caratteri):
    valida_numeri = False
    valida_caratteri = False
    for c in s:
        if c in caratteri:
            valida_caratteri = True
        if c in numeri:
            valida_numeri = True

    if valida_caratteri == True and valida_numeri == True:
        return True
    else:
        return False


def mostra_opt(id):
    print("Seleziona opt")
    print("1) Mostra tutto.")
    print("2) Logout.")
    
    opt = int(input("Seleziona opt: "))
    
    if opt == 1:
        query = """
            SELECT nome_op, tempo FROM storico_operazioni
            WHERE id = %s
        """
        
        mycursor.execute(query, (id,))
        dati = mycursor.fetchall()
        
        print(dati)
        
        return True
        
    elif opt == 2:
        return False
    



mydb = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '1234',
  database="cinema_esempio"
)

mycursor = mydb.cursor()

while True:
    print("1) registra utente")
    print("2) registra utente")
    print("3) registra utente")
    print("4) login")
    print("0) esci")

    scelta = int(input("Cosa vuoi fare?"))

    if scelta == 1:
        nome_utente = input("Inserisci nome utente: ")

        q = "SELECT id from utenti where username = %s"
        val = (nome_utente, )

        mycursor.execute(q, val)

        result = mycursor.fetchall()

        if result == []:
            password = input("Inserisci password: ")

            q = "INSERT INTO utenti (username, passwd) VALUES (%s, %s)"
            val = (nome_utente, password)

            mycursor.execute(q, val)

            mydb.commit()

            print("Utente registrato con successo!")
        else:
            print("Utente già registrato")

    elif scelta == 2:
        nome_utente = input("Inserisci nome utente: ")
        password = input("Inserisci password: ")

        # controllo_numeri = "0123456789"
        # controllo_simboli = "!?_$"

        # if len(password) >= 6 and controlla(password, controllo_numeri, controllo_simboli):
        if len(password) >= 6:
            q = "INSERT INTO utenti (username, passwd) VALUES (%s, %s)"
            val = (nome_utente, password)

            q2 = f"INSERT INTO log_operazioni(operazione) VALUES ('Registrato utente {nome_utente}')"

            try:
                mycursor.execute(q2)
                mycursor.execute(q, val)
                mydb.commit()
                print("Utente registrato con successo!")
            except:
                print("Errore... Contattare l'assistenza")
                mydb.rollback()
        else:
            print("La password deve avere almeno 6 caratteri, un numero, e un carattere speciale !?$_")


    elif scelta == 3:
        nome_utente = input("Inserisci nome utente: ")
        passwd = input("Inserisci password: ")
        
        try:
            query = """
                INSERT INTO utenti (username, passwd) VALUES (%s, %s)
            """
            
            mycursor.execute(query, (nome_utente, passwd))
            mydb.commit()
            print("Registro completato") 
            
        except:
            print("Errore")
            mydb.rollback() 
        
        # try:
            
        #     q = """
        #         INSERT INTO utenti (username, passwd)
        #         VALUES (
        #             %s,
        #             CASE
        #                 WHEN CHAR_LENGTH(%s) >= 6 THEN SHA2(%s, 256)
        #                 ELSE NULL
        #             END
        #         )
        #     """
            
        #     mycursor.execute(q, (nome_utente, passwd, passwd))
        #     mydb.commit()
            
        #     print("Registro completato.")

        # except:
        #     print(f"Errore")
            
            
        #occhio che qui dobbiamo capire come gestire psw < 6 caratteri
        # while True:
        #     password = input("Inserisci password: ")
        #     if len(password) < 6:
        #         print("Errore, la password deve essere di piu caratteri.")
                
        #     else:
        #         break
        # password = hashlib.sha256(password.encode("utf-8")).hexdigest()

        # q = "INSERT INTO utenti (username, passwd) VALUES (%s, %s)"
        # val = (nome_utente, password)

        # q2 = f"INSERT INTO log_operazioni(operazione) VALUES ('Registrato utente {nome_utente}')"

        # try:
        #     mycursor.execute(q2)
        #     mycursor.execute(q, val)
        #     mydb.commit()
        #     print("Utente registrato con successo!")
        # except mysql.connector.Error as err:
        #     if err.errno == 1062:  # 1062
        #         print("Nome utente già esistente.")
        #     elif err.errno == 4025:  # CHECK fallito (MariaDB)
        #         print("Password troppo corta: minimo 6 caratteri.")
        #     else:
        #         print("Errore, contattare l'assistenza")

        #     mydb.rollback()

    elif scelta == 4:
        nome_utente = input("Inserisci nome utente: ")
        passwd = input("Inserisci password: ")

        try:
            q = "SELECT pass_validazione(%s, %s)"
            mycursor.execute(q, (nome_utente, passwd))
            
            risultato = mycursor.fetchone()
            
            if risultato and int(risultato[0]) > 0:
                id_utente_loggato = int(risultato[0])
                print(f"Login completato con successo! Benvenuto.")
                
                login = True
                
                while login:
                    login = mostra_opt(id_utente_loggato)
                
            else:
                print("Errore: Nome utente o password errati.")
                
                login = False

        except Exception as e:
            print(f"Errore durante l'esecuzione del login: {e}")
        
    elif scelta == 0:
        break


        