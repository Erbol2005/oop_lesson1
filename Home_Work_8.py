import sqlite3


with sqlite3.connect('op36_3.db') as con:
    cursor = con.cursor()


    cursor.execute('''CREATE TABLE IF NOT EXISTS student (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        birth_year INTEGER,
        hobby TEXT,
        homework_score INTEGER
    )''')

    students = [('Иван', 'Иванов', 1995, 'Футбол', 15),
                ('Анна', 'Абалмасова', 1998, 'Чтение', 8),
                ('Егор', 'Иванов', 1997, 'Игры', 12),
                ('София', 'Петрова', 1996, 'Живопись', 5),
                ('Екатерина', 'Сидорова', 1999, 'Кулинария', 11),
                ('Дмитрий', 'Михайлов', 1994, 'Музыка', 9),
                ('Ольга', 'Козлова', 1993, 'Танцы', 14),
                ('Илья', 'Лебедев', 1992, 'Походы', 7),
                ('Анастасия', 'Абазовская', 1991, 'Пение', 10),
                ('Леонид', 'Павлов', 1990, 'Программирование', 13)]

    cursor.executemany(
        'INSERT INTO student (first_name, last_name, birth_year, hobby, homework_score) VALUES (?, ?, ?, ?, ?)',
        students)


    cursor.execute('SELECT * FROM student WHERE LENGTH(last_name) >= 10')
    long_last_name_students = cursor.fetchall()
    print("Студенты с фамилией длиннее 10 символов:", long_last_name_students, "\n")


    cursor.execute('UPDATE student SET first_name = "genius" WHERE homework_score > 10')


    cursor.execute('SELECT * FROM student WHERE first_name = "genius"')
    genius_students = cursor.fetchall()
    print("Студенты со статусом 'genius':", genius_students, "\n")


    cursor.execute('DELETE FROM student WHERE student_id % 2 = 0')



