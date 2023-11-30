#
#
# as = синоним
import sqlite3 as sql

with sql.connect('op36-3.db') as con:
    cursor = con.cursor()
    #cursor.execute('''DROP TABLE game''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS game (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_user TEXT NOT NULL,
    pol INTEGER DEFAULT 1,
    age INTEGER,
    date_user DATE DEFAULT '2023-11-28',
    score INTEGER
    ) ''')
#insert
    #cursor.execute('''INSERT INTO game (name_user,pol,age,score) VALUES ('BEKA',3,22,500)''')
    #cursor.execute('''INSERT INTO game VALUES (2,'beka',2,18,20-20-20,100)''')

#reed
    #cursor.execute('''SELECT * FROM game LIMIT 2,99''')

    #cursor.execute('''SELECT * FROM game ORDER BY user_id asc''')
    #cursor.execute('''SELECT * FROM game WHERE score>200 ORDER BY score desc LIMIT 3''')

#update
    cursor.execute('''UPDATE game SET score=score+100 WHERE name_user LIKE "beka" ''')
#delete
    cursor.execute('''DELETE FROM game''')
    cursor.execute('''SELECT * FROM game''')
    for result in cursor:
        print(result)

# CRUD



