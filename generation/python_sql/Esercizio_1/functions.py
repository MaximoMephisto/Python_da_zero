from connessione import conn_db

conn = conn_db()
cursor = conn.cursor()

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


def aggiungi_film():
    dati = dati_db("film")

    sale_esistenti = []

    for elem in dati:
        sale_esistenti.append(elem[1])

    nuovo_film = input("Inserisci nome film: ")
    if nuovo_film in sale_esistenti:
        print("Film gia inserito.")
    
    else:
        query = """
            INSERT INTO film (nome)
            VALUES (%s)
        """
        
        cursor.execute(query, (nuovo_film,))
        conn.commit()
        print(f"Film {nuovo_film} inserito.")
# aggiungi_film()


def aggiungi_sala():
    dati = dati_db("sale")
    
    sale_esistenti = []

    for elem in dati:
        sale_esistenti.append(elem[1])

    nuova_sala = input("Inserisci nome sala: ")
    if nuova_sala in sale_esistenti:
        print("Sala gia inserita.")
    
    else:
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
        if selezione.lower() == film[1]:
            id_film = film[0]
            break
    
    if id_film is not None:
        
        sale = dati_db("sale")
            
        print("Elenco sale: ")
        cont = 0
        
        for sala in sale:
            cont += 1
        print(f"{cont}) {sala}")
        
        
    
    
    
assegna()

def mostra_film():
    pass

def mostra_sale():
    pass

def panoramica():
    pass
