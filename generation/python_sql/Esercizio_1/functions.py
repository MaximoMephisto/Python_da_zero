from connessione import conn_db
import bcrypt

conn = conn_db()
cursor = conn.cursor()

def crittografa(passwd):
    criptata = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
    return criptata


def dati_db(tabella):
    query = f"""
        SELECT * FROM {tabella}
    """
    
    cursor.execute(query)
    dati = cursor.fetchall()
    
    tabella_list = []
    
    for elem in dati:
        tabella_list.append(elem)
    
    return tabella_list


def aggiungi_film(nuovo_film):
    dati = dati_db("film")
    sequenza = 1

    film_esistenti = []

    for elem in dati:
        film_esistenti.append(elem[1])

    while nuovo_film in film_esistenti:
        opt = input(f"{nuovo_film} è già stato inserito, vuoi riprovare? (S/n): ")
        
        if opt.lower() == "s" or opt.lower() == "si":
            nuovo_film = input("Inserire film: ")
            
        else:
            print("Addio.")
            sequenza = 0
            break
    
    if sequenza == 1:
        query = """
            INSERT INTO film (nome)
            VALUES (%s)
        """
        
        cursor.execute(query, (nuovo_film,))
        conn.commit()
        print(f"Film {nuovo_film} inserito.")     
# aggiungi_film()


def aggiungi_sala(nuova_sala):
    dati = dati_db("sale")
    
    sequenza = 1
    sale_esistenti = []

    for elem in dati:
        sale_esistenti.append(elem[1])
    
    while nuova_sala in sale_esistenti:
        opt = input(f"{nuova_sala} è già stata inserita, vuoi riprovare? (S/n): ")
               
        if opt.lower() == "s" or opt.lower() == "si":
            nuova_sala = input("Inserire sala: ")
                
        else:
            print("Addio.")
            sequenza = 0
            break
    
    if sequenza == 1:
        capienza = int(input("Inserisci capacita di sala: "))
        
        formatto_valido = ["HD", "FULL HD", "4K"]
        formatto = input("Inserire formatto (HD, FULL HD, 4K): ").upper()
        if formatto not in formatto_valido:
            print("Errore, sara impostato HD")
            formatto = "HD"
        
        query = """
            INSERT INTO sale (nome, capienza, formato_schermo)
            VALUES (%s, %s, %s)
        """
        
        cursor.execute(query, (nuova_sala, capienza, formatto))
        conn.commit()
        print(f"Sala {nuova_sala} inserita.")
# aggiungi_sala()


def assegna():
    films = dati_db("film")
    
    print("Elenco films: ")
    cont = 0
    for film in films:
        cont += 1
        print(f"{cont}) {film[1]}")
        
    selezione = input("Seleziona il film per nome: ")
    
    id_film = None
    
    for film in films:
        if selezione.lower() == film[1].lower():
            id_film = film[0]
            break
    
    if id_film is not None:
        sale = dati_db("sale")
            
        print("-----")
        print("Elenco sale: ")
        cont = 0
        
        for sala in sale:
            cont += 1
            print(f"{cont}) {sala[1]}")

        selezione_sala = input("Seleziona sala per nome: ")
        
        id_sala = None
        
        for sala in sale:
            if selezione_sala.lower() == sala[1].lower():
                id_sala = sala[0]
                break
        
        if id_sala is not None:
            query = f"""
                UPDATE sale
                SET film_id = {id_film}
                WHERE id = {id_sala}
            """
            
            cursor.execute(query)
            conn.commit()
            print("Relazione aggiunta con succeso.")
        else:
            print("Sala non trovata.")
    
    else:
        print("Film non trovato.")
#assegna()


def mostra_film():
    print("------------")
    print("Elenco films")
    print("------------") 
    
    films = dati_db("film")
    cont = 0
    
    for film in films:
        cont += 1
        print(f"[{cont}] {film[1]}")
  
    
def mostra_sale():
    print("------------")
    print("Elenco sale")
    print("------------") 
    
    sale = dati_db("sale")
    cont = 0
    
    for sala in sale:
        cont += 1
        print(f"[{cont}] {sala[1]}")


def panoramica():
    mostra_film()
    mostra_sale()
    print("------------") 
    
    query = """
        SELECT 
            s.nome AS Nome,
            s.capienza AS Capienza,
            s.formato_schermo AS Formatto,
            f.nome AS Film
        FROM sale AS s
        LEFT JOIN film AS f ON f.id = s.film_id
    """
    cursor.execute(query)
    panoramica = cursor.fetchall()
    
    for elem in panoramica:
        print(f"""
        Sala: {elem[0]}
        Capienza: {elem[1]}
        Qualità: {elem[2]}
        Film: {elem[3] if elem[3] else "Senza film"}       
        """)
    

def modificare_film(film):
    dati = dati_db("film")

    film_esistenti = []
    id_film = None 
    
    for elem in dati:
        film_esistenti.append(elem[1].lower())
        
    while film.lower() not in film_esistenti:
        print("Errore, film non trovato. Inserisci 'exit' per uscire.")
        film = input("Seleziona film per nome: ")   
        if film == "exit":
            break 
        
    for elem in dati:
        if film.lower() == elem[1].lower():
            id_film = elem[0]
        
    while film.lower() in film_esistenti:
        
        modifica = input("Nuovo nome del film: ")
        
        if modifica.lower() in film_esistenti:
            print("Errore, film già inserito")
            continue
        else:  
            query = f"""
                UPDATE film
                SET nome = "{modifica}"
                where id = {id_film}
            """
            cursor.execute(query)
            conn.commit()
            print("Film modificato con succeso.")
            break
            

def modificare_sala(sala):
    dati = dati_db("sale")

    sale_esistenti = []
    id_sala = None 
    
    for elem in dati:
        sale_esistenti.append(elem[1].lower())
        
    while sala.lower() not in sale_esistenti:
        print("Errore, sala non trovata. Inserisci 'exit' per uscire")
        sala = input("Seleziona sala per nome: ")    
        if sala == "exit":
            break
        
    for elem in dati:
        if sala.lower() == elem[1].lower():
            id_sala = elem[0]
        
    while sala.lower() in sale_esistenti:
        
        modifica = input("Nuovo nome della sala: ")
        
        if modifica.lower() in sale_esistenti:
            print("Errore, sala già inserita")
            continue
        else:  
            capienza = int(input("Inserisci capacita di sala: "))        
            formatto_valido = ["HD", "FULL HD", "4K"]
            formatto = input("Inserire formatto (HD, FULL HD, 4K): ").upper()
            if formatto not in formatto_valido:
                print("Errore, sara impostato HD")
                formatto = "HD"
            
            query = """
                UPDATE sale
                    SET 
                    nome = %s, 
                    capienza = %s, 
                    formato_schermo = %s
                WHERE id = %s
            """
            cursor.execute(query, (modifica, capienza, formatto, id_sala))
            conn.commit()
            print(f"Sala {modifica} inserita.")
            break


def eliminare_film(film):
    dati = dati_db("film")

    film_esistenti = []
    id_film = None 
    
    for elem in dati:
        film_esistenti.append(elem[1].lower())
        
    while film.lower() not in film_esistenti:
        print("Errore, film non trovato.")
        film = input("Seleziona film per nome: ")    
        
    for elem in dati:
        if film.lower() == elem[1].lower():
            id_film = elem[0]
            
    query = """
        DELETE FROM film WHERE id = %s
    """
    
    cursor.execute(query, (id_film,))
    conn.commit()
    print(f"{film} eliminato con successo.")
    

def eliminiare_sala(sala):
    dati = dati_db("sale")

    sale_esistenti = []
    id_sala = None 
    
    for elem in dati:
        sale_esistenti.append(elem[1].lower())
        
    while sala.lower() not in sale_esistenti:
        print("Errore, sala non trovata.")
        sala = input("Seleziona sala per nome: ")    
        
    for elem in dati:
        if sala.lower() == elem[1].lower():
            id_sala = elem[0]
            
    query = """
        DELETE FROM sale WHERE id = %s
    """
    
    cursor.execute(query, (id_sala,))
    conn.commit()
    print(f"{sala} eliminata con successo.")


def registrare_utente(utente):
    dati = dati_db("utenti")
    
    clienti_esistenti = []
    sequenza = 1
    
    for elem in dati:
        clienti_esistenti.append(elem[3].lower())
    
    mail_controllo = utente[2].lower()
    
    while mail_controllo in clienti_esistenti:
        opt = input(f"{utente[2]} è già stato registrato, vuoi riprovare? (S/n): ")
                
        if opt.lower() == "s" or opt.lower() == "si":
            nome = input("Nome: ")
            cognome = input("Cognome: ")
            mail = input("Mail: ")
            telefono = input("Telefono: ")
            password = input("Password: ")
            admin = int(input("Admin: "))
            
            utente = (nome, cognome, mail, telefono, password, admin)
            mail_controllo = mail.lower()
                
        else:
            print("Addio.")
            sequenza = 0
            break
            
    if sequenza == 1:
        utente_list = list(utente)
        utente_list[4] = crittografa(utente_list[4])
        utente = tuple(utente_list)
        
        query = """
            INSERT INTO utenti (nome, cognome, email, telefono, passwd, admin)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, utente)
        conn.commit()
        print(f"utente {utente[0]} registrato.")


def creare_presentazione():
    pass
    
    
# def sale_per_prenotare():
#     query = """
#         SELECT 
#             s.nome AS Sala,
#             f.nome AS Film,
#             s.formatto_schermo AS Qualita
#     """



# def prenotare():
#     pass


# utente = (    
#     'admin',
#     'sdasd',
#     'a@mail.com',
#     '+567567',
#     '123',
#     1)

# registrare_utente(utente)