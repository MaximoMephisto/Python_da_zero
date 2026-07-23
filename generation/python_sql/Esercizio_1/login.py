from functions import crittografa
from connessione import conn_db
import bcrypt

def login(mail, password):
    conn = conn_db()
    cursor = conn.cursor()
    
    query = f"""
        SELECT id FROM utenti WHERE email = '{mail}'
    """
    
    cursor.execute(query)
    result = cursor.fetchone()
    
    if not result:
        print("Email non registrato.")
    else:
        id_utente = result[0]
        print(id_utente)
        
        query = f"""
            SELECT passwd FROM utenti WHERE id = {id_utente}
        """
        cursor.execute(query)
        result = cursor.fetchone()
        
        passwd = result[0]
        print(passwd)
        
        pass_encode = crittografa(password)
        
        print(pass_encode)
        
        
        if pass_encode == passwd:
            query = f"""
                SELECT admin FROM utenti WHERE id = {id_utente}
            """
            
            cursor.execute(query)
            result = cursor.fetchone()
            
            admin = result[0]
            
            if admin == 1:
                verifica = True
                return verifica
            elif admin == 0:
                verifica = False
                return verifica
            
        else:
            print("Password errata.")
        
