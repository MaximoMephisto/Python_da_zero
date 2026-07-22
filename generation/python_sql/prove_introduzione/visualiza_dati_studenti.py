import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234",
    database="corsi_formazione"
)

cursor = conn.cursor(dictionary=True) # Transforma i dati in diccionario e non in tupla

cursor.execute('SELECT * FROM studenti')
risultati = cursor.fetchall() # Prendi tutte le righe

for elem in risultati:
    print(f'[{elem['id']}] {elem['nome']} {elem['cognome']}')


# Questi due comandi servono a liberare le risorse e a chiudere in modo pulito le connessioni aperte verso il database. 
# Quando un programma Python comunica con un database, apre dei canali di comunicazione che consumano memoria sia sul computer locale sia sul server del database.
cursor.close()
conn.close()