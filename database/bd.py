# Considerare che MySql non è collegato
# Username predeterminato per la BD di MySql è root
# La password si mette al instalare la database
# Nome di host: Nome del 'servidor' o IP dove si usa MySql (Es. LocalHost).
# Nome della database

###########################
# ESEMPIO DI COLLEGAMENTO #
###########################

import mysql.connector # Scaricare mysql.connecttor per python per collegare script python a database
from mysql.connector import Error # Per fare print di error

db = mysql.connet( # fa una connesione alla db
    host = 'localhost',
    user = 'root',
    passwd = 'dbms'
)

print(db) # Print se la conesione e andata bene
# Es. <mysql.connector.connection_cext.CMySQLConnection object at 0x0000020C26A84C50>

mysql.connector.connet() # Per collegare il database

connection.is_connected() # Verifica se siamo collegati
connection.cursos() # Per consulte SQL
cursos.close # chiude le consulte
connection.close() # chiudere la conessione


