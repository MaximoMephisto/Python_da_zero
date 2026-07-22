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
CREATE TABLE studenti(
    id INT UNSIGNED PRIMARY KEY,
    nome VARCHAR(50),
    cognome VARCHAR(50),
    matricola INT
);
"""

mycursor.execute(q)

print(mycursor.rowcount, "Record inserted.")