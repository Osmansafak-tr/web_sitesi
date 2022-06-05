import mysql.connector
import sys
 
mysqldb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="django_websitesi2"
)
cursor = mysqldb.cursor()



a = sys.argv[1]

cursor.execute(" select * from tezler_tez where ogrenci1_no = '{}' OR ogrenci2_no = '{}' OR ogrenci3_no = '{}'".format(a,a,a))
data = cursor.fetchall()
for satir  in data:
    print("'{:<7}','{:<7}','{:<7}','{:<7}','{:<7}','{:<7}',{:<7},'{:<7}','{:<7}','{:<7}','{:<7}','{:<7}','{:<7}'".format(satir[0],satir[1],satir[2],satir[3],satir[4],satir[5],satir[6],satir[7],satir[8],satir[9],satir[12],satir[13],satir[14]))