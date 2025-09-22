import mysql.connector
from db import info

try:
    conn=mysql.connector.connect(**info)
    print('connection successfull')
except:
    print('not able to connect')
cursor=conn.cursor()
#create database
def createDatabase():
    try:
        query="create database if not exists 54r_batch" #sql query
        cursor.execute(query) #executes that query using execute method in cursor
        print('database created successfully')
    except:
        print('something went wrong')
# createDatabase()

cursor.execute("use 54r_batch")

# create_table="""create table students (id int auto_increment primary key,
#                 name varchar(100),email varchar(100),course varchar(100),
#                 joined_date date)"""
# cursor.execute(create_table)

#insert single record
def insertRecords(data):
    try:        
        insertquery="""insert into students(name,email,course,joined_date) 
        values(%s,%s,%s,%s)"""
        cursor.execute(insertquery,data)
        print('data inserted successfully')
    except:
        print('something went wrong')

# insertRecords(('Nandu','Nandu@gmail.com','PFS','2025-06-08'))
# insertRecords(('Akhil','akhil@gmail.com','DS','2025-05-09'))

#insert multiple records
def insertManyRecords(data):
    try:        
        insertquery="""insert into students(name,email,course,joined_date) 
        values(%s,%s,%s,%s)"""
        cursor.executemany(insertquery,data)
        print('data inserted successfully')
    except:
        print('something went wrong')
# insertManyRecords([('john','john@gmail.com','JFS','2025-04-05'),
#                    ('suman','suman@gmail.com','JFS','2025-05-05'),
#                    ('Rakesh','rakesh@gmail.com','DS','2025-02-06')])


# def getRecords():
#     try:
#         query='select * from students'
#         cursor.execute(query)
#         results=cursor.fetchall()
#         # print(results)
#         for x in results:
#             print(x)
#     except:
#         print('something went wrong')

# getRecords()



def getRecordsByCourse(course_name):
    try:
        query='select * from students where course = %s'
        cursor.execute(query,(course_name,))
        results=cursor.fetchall()
        for x in results:
            print(x)
    except:
        print('something went wrong')

getRecordsByCourse('DS')


conn.commit() 
cursor.close()
conn.close()


