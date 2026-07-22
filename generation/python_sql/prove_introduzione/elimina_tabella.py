import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234",
    database="corsi_formazione"
)

cursor = conn.cursor() 

dato = 'videocorsi'
query = f'''
    DROP TABLE IF EXISTS {dato}
'''

cursor.execute(query)
conn.commit()

print(f"Tabella eliminata.")

cursor.close()
conn.close()
