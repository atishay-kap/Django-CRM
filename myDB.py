import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'errorshierrors'
)

# Prepare the cursor object
cursorObject = dataBase.cursor()

# Create the database
cursorObject.execute('CREATE DATABASE elderco')

print('all done!!')