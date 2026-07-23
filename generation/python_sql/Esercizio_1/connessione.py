import mysql.connector

def conn_db():
    conn = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '1234',
        database = 'cinema'
    )
    # print(conn)
    return conn