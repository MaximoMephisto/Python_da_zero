from connessione import conn_db
import bcrypt

def login(mail, password):
    
    mail = mail.lower()
    
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
        
        
        if bcrypt.checkpw(password.encode('utf-8'), passwd.encode('utf-8')):
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
        
