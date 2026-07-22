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

CREATE TABLE corsi (
    id INT UNSIGNED PRIMARY KEY,
    nome VARCHAR(50),
    costo DECIMAL(10,2)
);

"""

mycursor.execute(q)