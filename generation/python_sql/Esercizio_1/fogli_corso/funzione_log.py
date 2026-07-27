import mysql.connector

# 1. Connessione al tuo database
mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='1234',
    database="cinema_esempio"
)

mycursor = mydb.cursor()

try:
    mycursor.execute("DROP FUNCTION IF EXISTS pass_validazione;")
    
    query = """
    CREATE FUNCTION pass_validazione(p_utente VARCHAR(255), p_passwd VARCHAR(255))
    RETURNS INT
    DETERMINISTIC
    RETURN IFNULL((SELECT id FROM utenti WHERE username = p_utente AND passwd = SHA2(p_passwd, 256)), 0)
    """

    mycursor.execute(query)
    print("Funzione 'pass_validazione' creata con successo nel database!")

except mysql.connector.Error as err:
    print(f"Errore MySQL specifico: {err}")
except Exception as e:
    print(f"Errore generico: {e}")
