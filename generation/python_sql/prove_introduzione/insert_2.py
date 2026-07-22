import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234",
    database="corsi_formazione"
)

mycursor = mydb.cursor()

videocorsi = [
    ("Python dall'inizio", 'Corso "base" per chi parte da zero con l\'informatica', 49.99, 320),
    ("SQL: l'arte delle query", 'Impara a "interrogare" i database senza l\'ansia', 59.90, 280),
    ("JavaScript per l'estate", "Un corso 'leggero' ma completo sull'ES6", 39.50, 210),
    ('HTML & CSS: il "web" moderno', "Costruisci siti con l'attenzione ai dettagli", 29.99, 180),
    ("Git: versioni senza l'incubo", 'Gestisci il codice come un "pro" senza perderti', 44.00, 150),
    ("L'algebra dell'algoritmo", 'Teoria e pratica sugli algoritmi "classici"', 69.99, 400),
    ('Data science: dai dati all\'"insight"', "Analizza dati reali con l'aiuto di Pandas", 79.90, 360),
    ("Docker: l'ambiente perfetto", 'Container, immagini e l\'arte del "deploy"', 54.50, 240),
]

for elem in videocorsi:
    # %s = placeholder
    q = f"""

    INSERT INTO videocorsi (nome, descrizione, costo, durata)
    VALUES (%s, %s, %s, %s)

    """
    
    # Al mycursor.execute() si allega anche una tupla con i valori sostitotivi delle placeholder
    values = (elem[0], elem[1], elem[2], elem[3])

    mycursor.execute(q, values)

mydb.commit()
print(mycursor.rowcount, "Record inserted.")