import mysql.connector
from faker import Faker

fake = Faker('it_IT')

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234",
    database="corsi_formazione"
)

mycursor = mydb.cursor()

for i in range(1, 1000+1):
    q = f"""

    INSERT INTO studenti(id, nome, cognome, matricola)
    VALUES 
        ({i}, "{fake.first_name()}", "{fake.last_name()}", {120000 + i})
    """

    mycursor.execute(q)

mydb.commit() # Per confermare l'inserimento dei dati, come con le transazioni

print(mycursor.rowcount, "Record inserted.")