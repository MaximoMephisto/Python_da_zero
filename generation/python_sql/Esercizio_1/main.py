from login import login
from functions import selezione

def main():
    
    print("-----------------------------")
    print("           Login             ")
    print("-----------------------------")
    
    mail = input("Email:")
    passwd = input("Password:")
    
    verifica = login(mail, passwd)
    
    selezione(verifica)


main()