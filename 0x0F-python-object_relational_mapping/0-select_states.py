#!/usr/bin/python3
import MySQLdb
import sys

mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.agrv[3]

connection = MySQLdb.connect(
    host='localhost',
    port=3306,
    user=mysql_user,
    password=mysql_password,
    db=database_name
)

cursor = connection.cursor()

query = "SELECT * FROM states ORDER BY id ASC"
cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()