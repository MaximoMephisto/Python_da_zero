from connessione import conn_db
from login import login
from menu_admin import menu_admin
from menu_cliente import menu

def main():
    
    print("-----")
    print("Login")
    print("-----")
    mail = input("Inserire mail: ")
    passwd = input("Inserire password: ")
    
    mail = mail.lower()
    passwd = passwd
    
    verifica = login(mail, passwd)
    if verifica is True:
        menu_admin()
    elif verifica is False:
        menu()
    else:
        print("Non si puo accedere, credenziale non valide.")

main()

# bcrypt per cryptare le password

# DELIMITER $$

# CREATE PROCEDURE elenco_film()
# BEGIN
#     SELECT * FROM film;
# END$$

# DELIMITER ;