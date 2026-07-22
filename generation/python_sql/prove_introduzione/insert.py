import mysql.connector
 
mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234",
    database="corsi_formazione"
)

mycursor = mydb.cursor()

q = """

INSERT INTO corsi(id, nome, costo)
VALUES 
    (100, "Data Engineer", 1800),
    (200, "Ciber Sicurity", 2900),
    (300, "Excel Avanzato", 1300);

"""

mycursor.execute(q)

mydb.commit() # Per confermare l'inserimento dei dati, come con le transazioni

print(mycursor.rowcount, "Record inserted.")