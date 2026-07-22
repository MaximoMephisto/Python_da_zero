import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234",
    database="corsi_formazione"
)

cursor = conn.cursor() 

query = '''
    DELETE FROM studenti WHERE id = %s
'''

dati = (7,)

cursor.execute(query, dati)
conn.commit()

print(f"{cursor.rowcount} record eliminato.")

cursor.close()
conn.close()
