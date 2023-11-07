import mysql.connector

DATABASEPWD = ''
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=DATABASEPWD,
)

# Create cursor object
cursorObject = dataBase.cursor()

# Create a database

cursorObject.execute('CREATE DATABASE student_database')
print("SETUP SUCCESSFUL!")
