import mysql.connector
from datetime import datetime
import os
import Tamu
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="tamu"
)

class Satpam:
    def __init__(self, username,password):
        self.username = username
        self.password = password
        
    def show_list(db):
        print("=== APLIKASI DATABASE BUKU TAMU ===")
        print("1. Insert Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Cari Data")
        print("5. Cekout")
        print("0. Keluar")
        print("------------------")
        menu = input("Pilih menu> ")

        # clear screen
        os.system("clear")

        if menu == "1":
            Tamu.insert()
        elif menu == "2":
            Tamu.show()
        elif menu == "3":
            Tamu.delete()
        elif menu == "4":
            Tamu.cari()
        elif menu == "5":
            Tamu.update()
        elif menu == "0":
            exit()
        else:
            print("Menu salah!")
            
if __name__ == "__main__":
    while (True):
        show_list(db)
    
def otentikasi():
    username=input("Username: ")
    import getpass
    password = getpass.getpass()
    if password == '123' and username == 'abc':
        Satpam.show_list(db)
    else:
        print("Username atau Password Anda Salah")
      
