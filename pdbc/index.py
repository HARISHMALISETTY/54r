import mysql.connector
from db import info
from getters import getRecords
from getters import getRecordsByCourse
from insert import insertManyRecords
from insert import insertRecords
from update import updateNameByEmail
from update import updateCourseByEmail

try:
    conn=mysql.connector.connect(**info)
    # print('connection successfull')
except:
    print('not able to connect')
cursor=conn.cursor()
cursor.execute('use 54r_batch')
#create database
def createDatabase():
    try:
        query="create database if not exists 54r_batch" #sql query
        cursor.execute(query) #executes that query using execute method in cursor
        print('database created successfully')
    except:
        print('something went wrong')
# createDatabase()
#insert operations
# insertRecords(('Nandu','Nandu@gmail.com','PFS','2025-06-08'))
# insertRecords(('Akhil','akhil@gmail.com','DS','2025-05-09'))

#insert multiple records
# insertManyRecords([('john','john@gmail.com','JFS','2025-04-05'),
#                    ('suman','suman@gmail.com','JFS','2025-05-05'),
#                    ('Rakesh','rakesh@gmail.com','DS','2025-02-06')])

#retrieve operations
# getRecords()
# getRecordsByCourse('DS')
# updateNameByEmail('Nandini','Nandu@gmail.com')
updateCourseByEmail('PFS','Mani@gmail.com')
conn.commit() 
cursor.close()
conn.close()


