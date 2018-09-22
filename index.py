import mysql.connector
import pymssql

mydb=mysql.connector.connect(user="root", password="root123", port="3306", host="localhost", database="test")

if mydb.is_connected():
    mycursor = mydb.cursor()
    mycursor.execute("select * from sample_users");
    result=mycursor.fetchall()
    for eachresult in result:
        print(eachresult)

mycursor.execute("insert into sample_users values('test1','test1')")
mydb.commit()

