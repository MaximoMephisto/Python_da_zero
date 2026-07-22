import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234"
)

mycursor = mydb.cursor()

mycursor.execute('CREATE DATABASE corsi_formazione')
