import mysql.connector
from mysql.connector import errorcode
mydb = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '1234',
  database="cinema_esempio"
)
mycursor = mydb.cursor()
try: 
    query = """
        CREATE TRIGGER trigger_utenti
        BEFORE INSERT ON utenti
        FOR EACH ROW
        BEGIN 
            IF CHAR_LENGTH(NEW.passwd) < 6 THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Errore: La password deve contenere almeno 6 caratteri.';
            END IF;
            
            SET NEW.passwd = SHA2(NEW.passwd, 256);   
        END
    """
    mycursor.execute(query)
    
    print("Fatto, bravi")
except:
    print("Errore")
