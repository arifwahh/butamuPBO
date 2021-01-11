import mysql.connector
from datetime import datetime
import os
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="tamu"
)
class Tamu:
    def __init__(self, nama_tamu, alamat,keperluan,jam_masuk,jam_keluar):
        self.nama_tamu = nama_tamu
        self.alamat = alamat
        self.keperluan = keperluan
        self.jam_masuk = jam_masuk
        self.jam_keluar = jam_keluar
   
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
        Tamu.show_data(db)
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

def insert():
    Tamu.insert_data(db)
def show():
    Tamu.show_data(db)
def delete():
    Tamu.delete_data(db)
def cari():
    Tamu.search_data(db)
def update():
    Tamu.update_data(db)
