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

SELECT * FROM corsi;

"""

mycursor.execute(q)

result = mycursor.fetchall() # Recupera tutte le righe dal resultato della query

print(mycursor.rowcount, "Selezione dei dati.")

for righe in result:
    print(righe)

print("---")

for id_corso, nome, costo in result:
    print(f"{id_corso} | {nome} - {costo}$")

print("---")

tot = 0
for id_corso, nome, costo in result:
    costo = float(costo)
    tot += costo
print(f"Tot. prezzo dei corsi: {tot} $")
