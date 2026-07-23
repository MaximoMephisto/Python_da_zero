# a) si aggancia al db
from connessione import conn_db

conn = conn_db()
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS sale")
cursor.execute("DROP TABLE IF EXISTS film")
cursor.execute("DROP TABLE IF EXISTS utenti")

# b) crea tabella film
query = """
    CREATE TABLE film (
        id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(30) UNIQUE
    )
"""

try:
    cursor.execute(query)
    
    verifica = """
        SHOW TABLES
    """

    cursor.execute(verifica)
    tabella = cursor.fetchall()
    
    print(f"Tabella creata: {tabella}")
    
except:
    print("Errore al cercare di creare tabella.")
    

# c) crea tabella sale
query_due = """
    CREATE TABLE sale (
        id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(20) UNIQUE,
        capienza INT,
        formato_schermo ENUM("HD", "FULL HD", "4K") DEFAULT "HD",
        film_id INT UNSIGNED,
        FOREIGN KEY (film_id) REFERENCES film(id) ON DELETE SET NULL
    )
"""

try:
    cursor.execute(query_due)
    
    verifica = """
            SHOW TABLES
    """

    cursor.execute(verifica)
    tabella = cursor.fetchall()
    
    print(f"Tabella creata: {tabella}")

except:
    print("Errore al cercare di creare tabella.")
    

query_tre = """
    CREATE TABLE utenti (
        id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(100) NOT NULL,
        cognome VARCHAR(100) NOT NULL,
        email VARCHAR(150) UNIQUE NOT NULL,
        telefono VARCHAR(20),
        data_registrazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        passwd VARCHAR(255) NOT NULL,
        admin BOOLEAN
    )
"""
try:
    cursor.execute(query_tre)
    
    verifica = """
        SHOW TABLES
    """

    cursor.execute(verifica)
    tabella = cursor.fetchall()
    
    print(f"Tabella creata: {tabella}")

except:
    print("Errore al cercare di creare tabella.")


# query_quattro = """
#     CREATE TABLE prenotazioni (
#         id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
#         sala_id INT NOT NULL,
#         film_id INT NOT NULL,
        
#     )
# """

cursor.close()
conn.close()