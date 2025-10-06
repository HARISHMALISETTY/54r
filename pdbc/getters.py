import mysql.connector
from db import info

try:
    conn=mysql.connector.connect(**info)
    print('connection successfull')
except:
    print('not able to connect')
cursor=conn.cursor()



def getRecordsByCourse(course_name):
    try:
        cursor.execute("use 54r_batch")
        query='select * from students where course = %s'
        cursor.execute(query,(course_name,))
        results=cursor.fetchall()
        for x in results:
            print(x)
    except:
        print('something went wrong')

def getRecords():
    try:
        cursor.execute("use 54r_batch")
        query='select * from students'
        cursor.execute(query)
        results=cursor.fetchall()
        # print(results)
        for x in results:
            print(x)
    except:
        print('something went wrong')