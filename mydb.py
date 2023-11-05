import mysql.connector


dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Shikhatom@137'
)

# Create cursor object
cursorObject = dataBase.cursor()

# Create a database

cursorObject.execute('CREATE DATABASE student_database')
print("SETUP SUCCESSFUL!")
