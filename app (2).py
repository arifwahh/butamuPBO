import mysql.connector
from datetime import datetime
import os
import Tamu
import Satpam
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="tamu"
)

print("SELAMAT DATANG DI APLIKASI BUKU TAMU")
print("Silahkan Login Terlebih Dahulu")

Satpam.otentikasi()
