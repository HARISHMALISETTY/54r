import mysql.connector
from db import info

try:
    conn=mysql.connector.connect(**info)
    print('connection successfull')
except:
    print('not able to connect')
cursor=conn.cursor()

def insertManyRecords(data):
    try:        
        insertquery="""insert into students(name,email,course,joined_date) 
        values(%s,%s,%s,%s)"""
        cursor.executemany(insertquery,data)
        print('data inserted successfully')
    except:
        print('something went wrong')
def insertRecords(data):
    try:        
        insertquery="""insert into students(name,email,course,joined_date) 
        values(%s,%s,%s,%s)"""
        cursor.execute(insertquery,data)
        print('data inserted successfully')
    except:
        print('something went wrong')