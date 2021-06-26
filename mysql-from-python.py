import os
import pymysql
# Get the username from Cloud9 workspace
# (modify this variable if running on another envirnonment)
username = os.getenv("C9_USER")

# Connect to database
connection = pymysql.connect(host = "localhost", user=username, password='', db= 'Chinook')
try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()