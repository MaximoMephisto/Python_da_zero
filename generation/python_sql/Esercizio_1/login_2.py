from connessione import conn_db
from functions import crittografa
# conn = conn_db()
# cursor = conn.cursor()

# mail = input("mail: ")

# cursor.execute(f"Select id from utenti where email = '{mail}'")
# result = cursor.fetchone()

# id = result[0]

# pass_utente = f"""
# SELECT passwd FROM utenti WHERE id = {id}
# """

# cursor.execute(pass_utente)
# result = cursor.fetchone()

# print(result[0])

print(crittografa("123"))
print(crittografa("123"))