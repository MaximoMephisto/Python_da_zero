import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234",
    database="corsi_formazione"
)

mycursor = mydb.cursor()


q ="""

CREATE TABLE videocorsi (
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50),
    descrizione VARCHAR(100),
    costo DECIMAL(10,2),
    durata INT
);

"""

mycursor.execute(q)


print(mycursor.rowcount, "Tabella creata.")