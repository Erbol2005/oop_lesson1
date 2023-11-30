# SQL - язык структурировнных запросов
# база данных -
# СУБД - система управление базами данных
# NOsql:SQL
# posgreSQL, mySQL, SQLite

import sqlite3

# CRUD - create, reed, update, delete

db=sqlite3.connect('op_36-3.db')
cursor=db.cursor()

cursor.execute('''CREATE TABLE user(
lastname TEXT,
age  INTEGER,
view INTEGER,
bitday DATE
)''')
for result in cursor:
    print(result)
db.close()