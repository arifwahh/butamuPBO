import mysql.connector
from datetime import datetime
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="tamu"
)

print("SELAMAT DATANG DI APLIKASI BUKU TAMU")
print("Silahkan Login Terlebih Dahulu")

user=input("Username: ")

import getpass

sandi = getpass.getpass()

if sandi == '123' and user == 'abc':

    def insert_data(db):
        nama_tamu = input("Masukan Nama Tamu: ")
        alamat = input("Masukan Alamat: ")
        keperluan = input("Keperluan: ")
        jam_masuk = datetime.now()
        jam_keluar = datetime.now()
        val = (nama_tamu, alamat,keperluan,jam_masuk,jam_keluar)
        cursor = db.cursor()
        sql = "INSERT INTO tamu_masuk (nama_tamu, alamat, keperluan,jam_masuk,jam_keluar) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, val)
        db.commit()
        print("{} data berhasil disimpan".format(cursor.rowcount))


    def show_data(db):
        cursor = db.cursor()
        sql = "SELECT * FROM tamu_masuk"
        cursor.execute(sql)
        results = cursor.fetchall()
        for data in results:
            print(data)

    def delete_data(db):
        cursor = db.cursor()
        show_data(db)
        idtamu = input("pilih id tamu> ")
        sql = "DELETE FROM tamu_masuk WHERE id=%s"
        val = (idtamu,)
        cursor.execute(sql, val)
        db.commit()
        print("{} data berhasil dihapus".format(cursor.rowcount))


    def search_data(db):
        cursor = db.cursor()
        keyword = input("Kata kunci: ")
        sql = "SELECT * FROM tamu_masuk WHERE nama_tamu LIKE %s OR alamat LIKE %s"
        val = ("%{}%".format(keyword), "%{}%".format(keyword))
        cursor.execute(sql, val)
        results = cursor.fetchall()
        for data in results:
            print(data)
    
    def update_data(db):
        idtamu=input("masukan id :")
        jam_keluar=datetime.now()
        val = (jam_keluar,idtamu)
        cursor = db.cursor()
        sql = "UPDATE tamu_masuk SET jam_keluar=%s WHERE id=%s"
        cursor.execute(sql, val)
        db.commit()
        print("{} data berhasil disimpan".format(cursor.rowcount))

    def show_menu(db):
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
            insert_data(db)
        elif menu == "2":
            show_data(db)
        elif menu == "3":
            delete_data(db)
        elif menu == "4":
            search_data(db)
        elif menu == "5":
            update_data(db)
        elif menu == "0":
            exit()
        else:
            print("Menu salah!")

    if __name__ == "__main__":
        while (True):
            show_menu(db)

else:
    print("Username atau Password Anda Salah")

