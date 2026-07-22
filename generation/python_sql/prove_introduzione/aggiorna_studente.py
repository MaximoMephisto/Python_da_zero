import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='1234',
    database='corsi_formazione'
)

cursor = conn.cursor()

query = '''
    UPDATE studenti SET cognome = %s
    WHERE id = %s
'''

valori = ("Fornazziari", 9)

cursor.execute(query, valori)
conn.commit()

print(f"{cursor.rowcount} record aggiornato.")

cursor.close()
conn.close()


