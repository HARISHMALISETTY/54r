import mysql.connector
from db import info

try:
    conn=mysql.connector.connect(**info)
    print('connection successfull')
except:
    print('not able to connect')
cursor=conn.cursor()

def updateNameByEmail(new_name,email):
   try: 
    print(new_name,email)
    
    updateQuery="""update students SET name = hello where email= Nandu@gmail.com """
    print(updateQuery)
    cursor.execute(updateQuery,(new_name,email))
    print("data updated")
   except:
      print("something went wrong")

def updateCourseByEmail(course,email):
    try:
        cursor.execute('use 54r_batch')
        query="""update students set course = %s where email = %s"""
        cursor.execute(query,(course,email))
        print("data updated successfully")
    except:
        print("something went wrong")